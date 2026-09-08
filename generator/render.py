# -*- coding: utf-8 -*-
"""Renderer unico: HTML -> PNG/PDF. Sostituisce render_carousel.py,
render_single_images.py e render_pdf.py.

Uso:
  python3 render.py carousel        # 6 PNG + PDF del carosello
  python3 render.py singles         # 4 PNG delle immagini singole
  python3 render.py report          # PDF del report PED interno
  python3 render.py all             # tutto

La data NON e' un argomento: viene da week.py (DATE), unica fonte. Prima era
`sys.argv[2]` con default alla stringa letterale 'YYYY-MM-DD', che produceva in
silenzio file con quel nome — poi committati e serviti a Buffer.

Chromium: si usa quello di Playwright. Negli ambienti dove e' preinstallato,
impostare CHROMIUM_PATH (prima era hardcodato a /opt/pw-browsers/chromium,
percorso esistente solo nel container che ha prodotto il batch 2026-08-31).
"""
import asyncio
import os
import sys

from playwright.async_api import async_playwright

import build_report
import names
import plan
import templates
import week
from brand import tokens

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))

# Soglia di leggibilita'. I figli del contenitore sono in em: il piu' piccolo
# e' ~.24em, quindi con il contenitore a 72px il testo minimo resta ~17px su
# una tela da 1200px — leggibile in un feed. Sotto questa soglia l'auto-fit
# "riesce" ma produce microtesto: e' un contenuto da accorciare, non da scalare.
MIN_CONTAINER_FS = 72
# Tetto per l'ingrandimento e quota del riquadro da riempire. 128px lascia
# respirare i titoli piu' corti senza trasformarli in un cartellone; 0.90 evita
# che il blocco tocchi i bordi del riquadro.
MAX_CONTAINER_FS = 128
FILL_TARGET = 0.90

# Rimpicciolisce i .fit finche' rientrano in data-maxh. Portato dal renderer
# social-ped (renderer/server.js::AUTOFIT_JS), dove risolve il troncamento
# silenzioso dei titoli lunghi — qui con in piu' il limite di leggibilita'.
AUTOFIT_JS = r"""
(cfg) => {
  const problems = [];
  document.querySelectorAll('.fit').forEach((el) => {
    const maxh = parseFloat(el.getAttribute('data-maxh') || '0');
    if (!maxh) return;
    let fs = parseFloat(getComputedStyle(el).fontSize);
    let guard = 0;

    // Rimpicciolisce finche' il blocco rientra nel riquadro.
    while (el.scrollHeight > maxh && fs > 8 && guard < 200) {
      fs -= 1; el.style.fontSize = fs + 'px'; guard++;
    }
    // ...e ingrandisce se avanza spazio: la direzione "pannello pieno" vive di
    // contenuto che riempie il campo. Senza questo, una slide con poco testo
    // resta un blocchetto sospeso in mezzo al vuoto. Il tetto evita che due
    // righe diventino un cartellone.
    guard = 0;
    while (el.scrollHeight < maxh * cfg.fill && fs < cfg.maxFs && guard < 200) {
      fs += 1; el.style.fontSize = fs + 'px'; guard++;
      if (el.scrollHeight > maxh) { fs -= 1; el.style.fontSize = fs + 'px'; break; }
    }

    const slide = (el.closest('.slide') || {}).dataset?.slug || '?';
    const text = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 70);
    const wide = Array.from(el.querySelectorAll('*')).find(
      (d) => d.scrollWidth > d.clientWidth + 1 && d.clientWidth > 0);
    if (el.scrollHeight > maxh) {
      problems.push({ kind: 'overflow', slide, text,
                      detail: el.scrollHeight + 'px > ' + maxh + 'px' });
    } else if (wide) {
      // Un testo `nowrap` piu' largo della propria cella sborda NELLA cella
      // accanto: i due contenuti si accavallano senza che il contenitore
      // cresca, quindi controllare solo il contenitore non basta (verificato:
      // era un no-op). Si controlla ogni discendente.
      problems.push({ kind: 'hoverflow', slide,
                      text: (wide.textContent || '').trim().slice(0, 70),
                      detail: wide.scrollWidth + 'px di contenuto in ' + wide.clientWidth + 'px di cella' });
    } else if (fs < cfg.minFs) {
      problems.push({ kind: 'illegible', slide, text,
                      detail: 'ridotto a ' + fs + 'px (minimo ' + cfg.minFs + 'px)' });
    }
  });
  return problems;
}
"""

# Verifica che nessuna slide sfori il proprio riquadro: .slide ha overflow:hidden,
# quindi un contenuto troppo alto viene tagliato senza alcun errore.
CLIP_CHECK_JS = r"""
() => {
  const bad = [];
  document.querySelectorAll('.slide').forEach((el) => {
    if (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1) {
      bad.push({
        slide: el.dataset.slug || '?',
        scrollHeight: el.scrollHeight, clientHeight: el.clientHeight,
        scrollWidth: el.scrollWidth, clientWidth: el.clientWidth,
      });
    }
  });
  return bad;
}
"""


def _launch_kwargs():
    kwargs = {}
    path = os.environ.get("CHROMIUM_PATH")
    if path:
        if not os.path.exists(path):
            raise SystemExit(
                "CHROMIUM_PATH=%s non esiste. Rimuovi la variabile per usare "
                "il Chromium di Playwright." % path
            )
        kwargs["executable_path"] = path
    return kwargs


async def _open(browser, html, viewport):
    """Carica l'HTML, ASPETTA I FONT, applica l'auto-fit, verifica il clipping."""
    page = await browser.new_page(viewport=viewport)
    await page.set_content(html, wait_until="load")

    # I font sono incorporati in base64, ma il layout del testo va comunque
    # ricalcolato dopo che sono pronti: screenshottare prima puo' catturare
    # un frame con il font di fallback. Era il difetto degli script precedenti,
    # che facevano goto() e subito screenshot().
    await page.evaluate("document.fonts.ready")

    problems = await page.evaluate(AUTOFIT_JS, {
        "minFs": MIN_CONTAINER_FS, "maxFs": MAX_CONTAINER_FS,
        "fill": FILL_TARGET,
    })
    clipped = await page.evaluate(CLIP_CHECK_JS)

    for p in problems:
        label = {
            "overflow": "testo fuori dal riquadro (in altezza)",
            "hoverflow": "contenuto fuori dal riquadro (in larghezza)",
            "illegible": "testo troppo piccolo per essere leggibile",
        }[p["kind"]]
        print("  ERRORE [%s] %s: %s\n           %r"
              % (p["slide"], label, p["detail"], p["text"]), file=sys.stderr)
    for c in clipped:
        print("  ERRORE [%s] slide tagliata: %sx%s dentro %sx%s"
              % (c["slide"], c["scrollWidth"], c["scrollHeight"],
                 c["clientWidth"], c["clientHeight"]), file=sys.stderr)

    if problems or clipped:
        raise SystemExit(
            "Rendering interrotto: %d problemi di testo. Accorcia i contenuti "
            "in week.py — i limiti di caratteri sono in brand-spec.md §6.\n"
            "L'auto-fit e' una rete di sicurezza per piccoli sforamenti, non un "
            "modo per far stare qualunque quantita' di testo."
            % (len(problems) + len(clipped))
        )
    return page


def _check_size(path, w, h):
    """Ogni PNG deve avere ESATTAMENTE il formato dichiarato in tokens.FORMATS.

    Il formato canonico e' 1200x1500 (i template Canva reali, vedi
    brand-spec.md). Gli asset del bot fino al 31 agosto sono 1080x1350: stesso
    rapporto 4:5, risoluzione minore senza motivo.

    Il controllo esiste perche' quei file vecchi restano visibili nella repo, e
    la deriva tipica e' "mi adeguo a quello che c'e' gia'". Una dimensione
    diversa non produce alcun errore: LinkedIn riscala e il post esce solo un
    po' piu' sgranato, cioe' il tipo di difetto che nessuno attribuisce mai al
    codice. Meglio fermarsi.
    """
    from PIL import Image
    got = Image.open(path).size
    if got != (w, h):
        os.remove(path)
        raise SystemExit(
            "%s e' %dx%d, ma il formato dichiarato e' %dx%d.\n"
            "Il file e' stato rimosso: un asset fuori formato non va pubblicato.\n"
            "La dimensione viene da brand/tokens.py (FORMATS): non adeguarti agli "
            "asset piu' vecchi nella repo, che sono 1080x1350."
            % (os.path.basename(path), got[0], got[1], w, h))


async def _shoot_slides(browser, html, name_for, viewport):
    """Screenshot di ogni .slide, con nome derivato dal suo data-slug."""
    page = await _open(browser, html, viewport)
    slides = await page.query_selector_all(".slide")
    if not slides:
        raise SystemExit("Nessuna slide trovata nell'HTML.")
    paths = []
    for el in slides:
        slug = await el.get_attribute("data-slug")
        if not slug:
            raise SystemExit("Una slide non ha data-slug: impossibile nominare il file.")
        path = os.path.join(OUT_DIR, name_for(slug))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.exists(path):
            # I nomi file pubblicati non vanno mai riusati: Buffer scarica
            # l'asset dall'URL al momento della pubblicazione effettiva, che
            # puo' avvenire giorni dopo. Vedi brand-spec.md §7.7.
            raise SystemExit(
                "%s esiste gia'.\n"
                "I post gia' generati vengono saltati prima di arrivare qui, "
                "quindi questo e' uno stato incoerente: probabilmente il post "
                "ha solo una parte dei suoi asset. Controlla la cartella, "
                "cancella gli asset NON ancora pubblicati e rigenera.\n"
                "Non sovrascrivere: la bozza Buffer punta a quell'URL e Buffer "
                "scarica l'asset alla pubblicazione, non ora."
                % os.path.basename(path)
            )
        await el.screenshot(path=path)
        _check_size(path, viewport["width"], viewport["height"])
        print("  scritto", os.path.basename(path))
        paths.append(path)
    await page.close()
    return paths


def _to_pdf(png_paths, out_path):
    import img2pdf
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(img2pdf.convert(png_paths))
    print("  scritto", os.path.basename(out_path))
    return out_path


def content():
    """Delega a `plan.content()`: unica fonte, condivisa con publish_buffer."""
    return plan.content()


def _check_overrides_current():
    """Le correzioni a mano in `week.py` devono essere della settimana corrente.

    I contenuti derivati dal report sono sempre allineati per costruzione, quindi
    il rischio di obsolescenza resta solo sulle correzioni: un aggiustamento
    scritto per la settimana scorsa passerebbe inosservato, perche' i nomi dei
    file sarebbero comunque nuovi.
    """
    if not (getattr(week, "CAROUSELS", []) or getattr(week, "SINGLES", [])):
        return
    stale = getattr(week, "OVERRIDES_FOR", week.DATE)
    if stale != week.DATE:
        raise SystemExit(
            "week.py: DATE e' %s ma le correzioni a mano sono della settimana "
            "%s (OVERRIDES_FOR).\n"
            "Aggiornale o svuota CAROUSELS/SINGLES, poi porta OVERRIDES_FOR a %s."
            % (week.DATE, stale, week.DATE)
        )


def _state(paths):
    """Stato degli asset di un post: 'da fare', 'fatto' o 'a meta''."""
    done = [p for p in paths if os.path.exists(p)]
    if not done:
        return "da fare"
    return "fatto" if len(done) == len(paths) else "a meta'"


def _todo(items, paths_for):
    """Tiene solo i post da generare, e spiega cosa succede agli altri.

    Rigenerare tutto ogni volta non e' possibile — un asset pubblicato non si
    sovrascrive — ma nemmeno abortire va bene: nel ciclo human-in-the-loop si
    rifa' **un** post e gli altri sono gia' a posto. Quindi qui si salta il
    lavoro gia' fatto, e `render.py` diventa ripetibile.

    Il caso 'a meta'' resta un errore: un post con solo alcune slide sul disco
    non e' ne' fatto ne' da fare, ed e' quasi sempre un'esecuzione interrotta.
    """
    todo, skipped = [], []
    for item in items:
        state = _state([os.path.join(OUT_DIR, n) for n in paths_for(item)])
        if state == "fatto":
            skipped.append(item["slug"])
        elif state == "da fare":
            todo.append(item)
        else:
            raise SystemExit(
                "Il post %s ha solo una parte dei suoi asset sul disco.\n"
                "E' quasi sempre un'esecuzione interrotta: cancella quelli non "
                "ancora pubblicati e rigenera." % item["slug"]
            )
    for slug in skipped:
        print("  gia' fatto, salto: %s (rev %d)" % (slug, names.revision(slug)))
    if skipped and not todo:
        print("  Per rifarne uno: mettilo in week.REDO con revisione %d."
              % (max(names.revision(s_) for s_ in skipped) + 1))
    return todo


async def do_carousel(browser):
    """Genera TUTTI i caroselli della settimana: il PED puo' proporne piu' di uno
    (questa settimana l'idea 3 AI Act e l'idea 6 Nvidia)."""
    _check_overrides_current()
    carousels, _ = content()
    print("caroselli (%s):" % week.DATE)
    carousels = _todo(carousels, lambda c: (
        [names.carousel_slide(c["slug"], i + 1) for i in range(len(c["slides"]))]
        + [names.carousel_pdf(c["slug"])]))
    for carousel in carousels:
        slug, date = carousel["slug"], week.DATE
        print("  %s:" % slug)
        pngs = await _shoot_slides(
            browser, templates.carousel_html(carousel),
            names.carousel_slide_name(slug),
            {"width": templates.W, "height": templates.H},
        )
        _to_pdf(pngs, os.path.join(OUT_DIR, names.carousel_pdf(slug)))


async def do_singles(browser):
    _check_overrides_current()
    print("immagini singole (%s):" % week.DATE)
    singles = _todo(content()[1], lambda x: [names.single(x["slug"])])
    if not singles:
        return
    await _shoot_slides(
        browser, templates.singles_html(singles),
        names.single,
        {"width": templates.W, "height": templates.H},
    )


async def do_report(browser):
    print("report PED (%s):" % week.DATE)
    import generate_html
    html = generate_html.build_full_html()
    w, h = tokens.FORMATS["a4"]
    page = await browser.new_page()
    await page.set_content(html, wait_until="load")
    await page.evaluate("document.fonts.ready")
    out = os.path.join(OUT_DIR, names.report_pdf())
    os.makedirs(os.path.dirname(out), exist_ok=True)
    await page.pdf(path=out, width="%dpx" % w, height="%dpx" % h,
                   print_background=True,
                   margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
    await page.close()
    print("  scritto", os.path.basename(out))


TASKS = {"carousel": do_carousel, "singles": do_singles, "report": do_report}


async def main():
    what = sys.argv[1] if len(sys.argv) > 1 else ""
    if what == "all":
        todo = ["report", "carousel", "singles"]
    elif what in TASKS:
        todo = [what]
    else:
        raise SystemExit("Uso: python3 render.py {%s|all}" % "|".join(TASKS))

    async with async_playwright() as p:
        browser = await p.chromium.launch(**_launch_kwargs())
        try:
            for t in todo:
                await TASKS[t](browser)
        finally:
            await browser.close()
    print("Fatto. Output in %s" % os.path.join(OUT_DIR, names.week_dir()))


if __name__ == "__main__":
    asyncio.run(main())
