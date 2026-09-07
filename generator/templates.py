# -*- coding: utf-8 -*-
"""LAYOUT delle grafiche social: trasforma i dati di week.py in HTML.

Separazione dei ruoli:
  week.py          contenuto della settimana (nessun HTML, nessun colore)
  brand/tokens.py  brand (palette, font, asset, formati)
  templates.py     questo file — layout e composizione
  render.py        HTML -> PNG/PDF

Ogni slide e' un `<div class="slide" data-slug="...">`: render.py legge lo slug
dal DOM, quindi aggiungere/riordinare slide non richiede di toccare il renderer.

## Geometria: gli sfondi di brand NON sono fondi piatti

Ogni PNG in brand/bg/ e' una composizione con marchio e icona-categoria **gia'
incorporati**, piu' zone non utilizzabili. Misure rilevate a pixel, non stimate:

  editorial_navy.png / editorial_blue.png (1200x1500) — usati dal carosello
    y  108- 246  wordmark (sx) + badge categoria (dx) incorporati
    y  246-1500  campo pieno libero -> zona testo, footer in basso libero

  newsai_bg.png (1200x1500) — post News AI con foto dell'articolo
    y    0- 628  fascia cielo chiara + nuvola  -> testo bianco INVISIBILE
    x 1120-1200  taglio diagonale del pannello (scende fino a y=713)
    y  628-1500  pannello blu -> zona testo (bianco)
    x  980-1091 / y  105- 204  icona-categoria incorporata
    x  452- 706 / y 1344-1415  wordmark incorporato -> il footer lo affianca

Da qui due conseguenze non negoziabili:
  1. NON si disegna il marchio: e' gia' nello sfondo. Aggiungerlo lo duplica.
  2. Il contenuto vive dentro il `box` della sua superficie, mai altrove.

## Auto-fit proporzionale

Il contenitore del contenuto ha `font-size:100px` e i figli sono dimensionati in
`em`. L'auto-fit di render.py riduce il font-size del contenitore, quindi tutto
il blocco si rimpicciolisce in proporzione mantenendo le relazioni tipografiche
— invece di rimpicciolire un solo elemento e rompere la gerarchia.
"""
import html as htmlmod
import re

from brand import tokens

W, H = tokens.FORMATS["portrait"]

# Per ogni superficie: sfondo, zona di contenuto (x, y, w, h) e colori.
#
# DIREZIONE DI DESIGN: B "Pannello pieno" (scelta 2026-09-07, vedi
# design-demos/direction-approved.md). Campo pieno senza fascia cielo, contenuto
# centrato verticalmente: nessuno spazio morto e un solo layout per ogni tipo di
# slide, elenco compreso.
#
# Le due superfici editoriali NON sono decorative: codificano il registro del
# contenuto. Navy = argomentazione (apertura, tesi, chiusura). Blu = fatto
# verificabile (dati, date, elenchi di obblighi). L'alternanza in week.py segue
# questa regola, non un ritmo estetico.
#
# Geometria (misurata a pixel su editorial_*.png, 1200x1500):
#   y  108- 246  wordmark (sx) + badge categoria (dx) INCORPORATI nello sfondo
#   y  246-1500  campo libero -> zona testo
# Il marchio non si disegna mai: e' gia' nello sfondo (brand-spec.md §7.1).
SURFACES = {
    "navy": dict(
        bg="editorial_navy",
        box=(120, 330, 960, 940),
        footer_y=1400,
        ink="#fff",
        furniture="baked",
        accent="var(--c-green)",
        # Tinta dati misurata su questo fondo: chroma PASS, contrasto PASS >=3:1.
        data="var(--c-green)",
        neutral="rgba(255,255,255,.22)",
        body="var(--c-text-muted-soft)",
        muted="rgba(185,192,245,.72)",
    ),
    "sky": dict(
        bg="editorial_sky",
        box=(120, 340, 960, 940),
        footer_y=1420,
        # Su fondo chiaro il testo e' navy e l'accento e' il blu brand: il verde
        # (#43ef84) su cielo (#c5ebff) sarebbe chiaro su chiaro.
        ink="var(--c-navy)",
        accent="var(--c-blue)",
        # Sul cielo il verde misura 1,2:1 di contrasto: inutilizzabile come
        # tinta dati. Il blu brand misura PASS su chroma e contrasto.
        data="var(--c-blue)",
        neutral="rgba(14,10,72,.16)",
        well="rgba(14,10,72,.07)",
        badge_ink="#fff",   # pallino navy con numero bianco, su fondo chiaro
        body="#3a3d6b",
        muted="rgba(14,10,72,.55)",
        # Questo sfondo NON ha marchio ne' badge incorporati: li mette il layout.
        furniture="overlay",
        wordmark="wordmark_navy",
        icon="icon_news_navy",
    ),
    "blue": dict(
        bg="editorial_blue",
        box=(120, 330, 960, 940),
        footer_y=1400,
        ink="#fff",
        furniture="baked",
        # L'accento di TESTO e' il cielo del brand. Ma il cielo non e' una tinta
        # dati (chroma 0.039, "reads gray"): per i marchi numerici si usa il
        # verde, che su questo fondo misura contrasto PASS >=3:1.
        accent="var(--c-sky-top)",
        data="var(--c-green)",
        neutral="rgba(255,255,255,.22)",
        body="var(--c-text-on-blue)",
        muted="rgba(255,255,255,.66)",
    ),
    # Sfondi originali Canva, per i formati che li usano ancora (es. post News AI
    # con foto dell'articolo nella fascia cielo).
    "news": dict(
        bg="news",
        box=(120, 700, 960, 620),
        footer_y=1352,
        ink="#fff",
        furniture="baked",
        accent="var(--c-sky-top)",
        data="var(--c-green)",
        neutral="rgba(255,255,255,.22)",
        body="var(--c-text-on-blue)",
        muted="rgba(255,255,255,.66)",
    ),
}



# ---------------------------------------------------------------------------
# REGISTRO DEI TIPI DI POST
# ---------------------------------------------------------------------------
# Ogni formato che il PED propone ha esigenze diverse: un carosello dati non si
# disegna come una riflessione di chiusura. Qui vive quella differenza, come
# DATI — aggiungere un formato non richiede di toccare il motore.
#
# `rhythm` e' la sequenza di superfici che il carosello percorre. E' la risposta
# alla monotonia: se tutte le pagine stanno sullo stesso fondo il carosello
# sembra una sola immagine ripetuta. Il ritmo non e' casuale, alterna scuro e
# chiaro per dare respiro allo swipe, e mantiene le regole di brand:
#   navy -> accento verde   (l'unico fondo dove il verde e' ammesso)
#   blue -> accento cielo   (il verde su blu vibrerebbe)
#   sky  -> accento blu     (il verde su cielo sarebbe chiaro su chiaro)
# Se una slide dichiara `surface`, quella vince sul ritmo.
#
# `kinds` documenta i layout che il formato usa davvero: serve a chi scrive i
# contenuti in week.py per sapere cosa ha a disposizione.
POST_TYPES = {
    "data_carousel": dict(
        label="Carosello dati",
        format="carousel",
        # Scuro -> chiaro -> scuro: le due pagine chiare cadono sui momenti di
        # respiro (il dato singolo e la lettura), non sull'apertura o sulla CTA.
        rhythm=["navy", "blue", "sky", "blue", "sky", "navy"],
        kinds=["hook", "scorecard", "figure", "share", "statement", "cta"],
    ),
    "explainer_carousel": dict(
        label="Carosello divulgativo",
        format="carousel",
        # Piu' pacato: nessun dato da urlare, quindi piu' chiaro che scuro.
        rhythm=["navy", "sky", "blue", "sky", "blue", "navy"],
        kinds=["hook", "statement", "checklist", "statement", "data", "cta"],
    ),
    "compliance_carousel": dict(
        label="Carosello normativa/compliance",
        format="carousel",
        # Registro istituzionale: prevale il navy, il chiaro solo per l'elenco
        # degli obblighi, dove la leggibilita' conta piu' dell'impatto.
        rhythm=["navy", "blue", "sky", "blue", "navy", "navy"],
        kinds=["hook", "data", "checklist", "data", "statement", "cta"],
    ),
    "thought_leadership": dict(
        label="Thought leadership",
        format="single",
        rhythm=["navy"],
        kinds=["single"],
    ),
    "myth": dict(
        label="Mito da sfatare",
        format="single",
        rhythm=["blue"],
        kinds=["single"],
    ),
    "direct_experience": dict(
        label="Esperienza diretta",
        format="single",
        rhythm=["navy"],
        kinds=["single"],
    ),
    "mini_lesson": dict(
        label="Mini-lezione divulgativa",
        format="single",
        rhythm=["sky"],
        kinds=["single"],
    ),
}


def rhythm_for(post_type, index, total):
    """La superficie della slide `index` secondo il ritmo del tipo di post.

    Se il ritmo e' piu' corto del carosello si ripete ciclicamente, cosi'
    aggiungere una slide non richiede di riscrivere il ritmo.
    """
    r = POST_TYPES[post_type]["rhythm"]
    return r[index % len(r)]


def esc(s):
    return htmlmod.escape(str(s or ""), quote=False)


def accent(s, color):
    """Convenzione `*parola*` -> span accentato. Tutto il resto viene escapato."""
    parts = re.split(r"\*([^*]+)\*", str(s or ""))
    return "".join(
        '<span style="color:%s">%s</span>' % (color, esc(p)) if i % 2 else esc(p)
        for i, p in enumerate(parts)
    )


# ---------------------------------------------------------------------------
# Layout per `kind`: rendono SOLO il contenuto interno, in em.
# La cornice (sfondo, footer, contenitore auto-fit) la mette _frame().
# ---------------------------------------------------------------------------

def _eyebrow(s, sf):
    return ('<div class="eyebrow" style="font-size:.26em;color:%s;">%s</div>'
            % (sf["accent"], esc(s["eyebrow"])))


def _hook(s, sf):
    return f"""{_eyebrow(s, sf)}
    <div class="display" style="margin-top:.30em;font-size:.80em;color:{sf['ink']};">{accent(s['title'], sf['accent'])}</div>
    <div class="body" style="margin-top:.44em;font-size:.30em;color:{sf['body']};">{esc(s['subtitle'])}</div>"""


def _data(s, sf):
    return f"""{_eyebrow(s, sf)}
    <div class="display" style="margin-top:.24em;font-size:.92em;text-transform:uppercase;color:{sf['accent']};">{esc(s['datanum'])}</div>
    <div class="body body--bold" style="margin-top:.34em;font-size:.34em;line-height:1.26;color:{sf['ink']};">{esc(s['explain'])}</div>
    <div class="body" style="margin-top:.22em;font-size:.26em;color:{sf['body']};">{esc(s['note'])}</div>"""


def _checklist(s, sf):
    # NB: width/height del pallino NON possono stare sullo stesso elemento che
    # ne imposta il font-size — gli `em` si risolverebbero sul proprio font-size
    # invece che su quello del contenitore, collassando il cerchio.
    items = "".join(f"""
    <div style="display:flex;gap:.20em;align-items:flex-start;margin-bottom:.22em;">
      <div style="flex:0 0 .40em;height:.40em;border-radius:50%;background:{sf['ink']};
           display:flex;align-items:center;justify-content:center;">
        <span style="font-family:var(--font-display);font-weight:800;font-size:.21em;
              color:{sf.get('badge_ink', 'var(--c-blue)')};line-height:1;">{n}</span>
      </div>
      <div class="body body--bold" style="font-size:.27em;line-height:1.30;color:{sf['ink']};">{esc(t)}</div>
    </div>""" for n, t in enumerate(s["items"], start=1))
    return f"""{_eyebrow(s, sf)}
    <div class="display" style="margin-top:.24em;font-size:.62em;color:{sf['ink']};">{accent(s['title'], sf['accent'])}</div>
    <div style="margin-top:.44em;">{items}</div>"""


def _statement(s, sf):
    return f"""{_eyebrow(s, sf)}
    <div class="display" style="margin-top:.24em;font-size:.66em;color:{sf['ink']};">{accent(s['title'], sf['accent'])}</div>
    <div class="body" style="margin-top:.36em;font-size:.29em;color:{sf['body']};">{esc(s['body'])}</div>
    <div class="body body--bold" style="margin-top:.20em;font-size:.25em;color:{sf['ink']};">{esc(s['note'])}</div>"""


def _cta(s, sf):
    return f"""
    <div class="display" style="font-size:.70em;color:{sf['ink']};">{accent(s['title'], sf['accent'])}</div>
    <div style="margin-top:.40em;background:#fff;border-radius:.24em;padding:.36em .40em;">
      <div class="display" style="font-size:.46em;color:var(--c-blue);">{esc(s['cta_title'])}</div>
      <div class="body" style="margin-top:.16em;font-size:.24em;color:var(--c-navy);">{esc(s['cta_sub'])}</div>
    </div>"""


def _single(s, sf):
    return f"""{_eyebrow(s, sf)}
    <div class="display" style="margin-top:.30em;font-size:.78em;color:{sf['ink']};">{accent(s['title'], sf['accent'])}</div>
    <div style="margin-top:.46em;border-left:.05em solid {sf['accent']};padding:.22em .28em;
         background:{sf.get('well', 'rgba(255,255,255,.10)')};border-radius:.08em;">
      <div class="body body--bold" style="font-size:.27em;line-height:1.32;color:{sf['ink']};">{esc(s['box'])}</div>
    </div>"""


# --- Slide guidate dai dati (idea 6 e futuri caroselli dati) -----------------
# Non sono tre alternative in concorrenza: sono tre tipi di slide di cui un
# carosello dati ha bisogno tutti. La scelta e' la SEQUENZA, non il layout.
#
# Colore: una sola tinta dati (il verde) piu' un neutro. Verificato con il
# validator della skill dataviz — il cielo brand #d0f0ff fallisce il chroma
# floor (0.039, "reads gray") quindi NON puo' codificare una categoria.
# Per questo le slide con grafico vanno sul campo navy, dove il verde e' ammesso.

def _figure(s, sf):
    """Hero number: una cifra sola non e' un grafico, e' un titolo numerico.
    Rende espliciti unita' e scarto, che `data` perdeva."""
    delta = ""
    if s.get("delta"):
        delta = f"""
    <div style="display:flex;align-items:baseline;gap:.10em;margin-top:.20em;">
      <span class="display" style="font-size:.62em;color:{sf['data']};
            font-variant-numeric:tabular-nums;">{esc(s['delta'])}</span>
      <span class="body body--bold" style="font-size:.24em;color:{sf['body']};">{esc(s.get('delta_note',''))}</span>
    </div>"""
    return f"""{_eyebrow(s, sf)}
    <div style="display:flex;align-items:baseline;gap:.20em;margin-top:.22em;">
      <div class="display" style="font-size:2.05em;line-height:.86;letter-spacing:-.04em;
           color:{sf['ink']};font-variant-numeric:tabular-nums;">{esc(s['figure'])}</div>
      <div class="eyebrow" style="font-size:.28em;color:{sf['body']};
           letter-spacing:1px;padding-bottom:.9em;">{esc(s['unit']).replace(chr(10), '<br>')}</div>
    </div>{delta}
    <div class="body" style="margin-top:.36em;font-size:.26em;color:{sf['body']};">{esc(s['say'])}</div>"""


def _share(s, sf):
    """Proporzione parte/tutto. Qui la FORMA porta l'informazione: se un segmento
    occupa quasi tutta la barra, quello e' il messaggio.

    Specifiche dei segni: stacco di superficie fra i riempimenti, estremita'
    arrotondate solo sui bordi esterni (il segmento resta ancorato, non
    galleggia), etichette dirette su entrambi i segmenti — nessuna legenda,
    perche' due segmenti etichettati si nominano da soli."""
    quota = float(s["value"]) / float(s["total"])
    pct = quota * 100
    return f"""{_eyebrow(s, sf)}
    <div style="display:flex;align-items:baseline;gap:.18em;margin-top:.20em;">
      <div class="display" style="font-size:1.40em;line-height:.9;letter-spacing:-.03em;
           color:{sf['ink']};font-variant-numeric:tabular-nums;">{esc(s['figure'])}</div>
      <div class="eyebrow" style="font-size:.26em;color:{sf['body']};
           letter-spacing:1px;padding-bottom:.7em;">{esc(s['unit']).replace(chr(10), '<br>')}</div>
    </div>
    <div style="margin-top:.34em;display:flex;gap:.045em;height:.52em;">
      <div style="width:{pct:.2f}%;background:{sf['data']};
           border-radius:.09em 0 0 .09em;"></div>
      <div style="flex:1;background:{sf['neutral']};
           border-radius:0 .09em .09em 0;"></div>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:.12em;">
      <div class="eyebrow" style="font-size:.21em;color:{sf['data']};
           font-variant-numeric:tabular-nums;letter-spacing:.5px;">{esc(s['label'])} · {pct:.1f}%</div>
      <div class="eyebrow" style="font-size:.21em;color:{sf['body']};
           font-variant-numeric:tabular-nums;letter-spacing:.5px;">{esc(s['label_rest'])} · {100-pct:.1f}%</div>
    </div>
    <div class="body" style="margin-top:.38em;font-size:.26em;color:{sf['body']};">{esc(s['say'])}</div>"""


def _scorecard(s, sf):
    """Piu' indicatori su una slide. La colonna centrale significa SEMPRE la
    stessa cosa (il qualificatore del dato): se in una riga fosse una seconda
    cifra assoluta, la griglia mentirebbe sul proprio significato."""
    rows = "".join(f"""
    <div style="display:grid;grid-template-columns:1.9em 2.35em 1fr;gap:.18em;
         align-items:baseline;padding:.15em 0;
         border-top:2px solid {sf['neutral']};">
      <div class="display" style="font-size:.40em;line-height:1;letter-spacing:-.02em;
           color:{sf['ink']};font-variant-numeric:tabular-nums;">{esc(f)}</div>
      <div class="display" style="font-size:.27em;line-height:1;color:{sf['data']};
           white-space:nowrap;font-variant-numeric:tabular-nums;">{esc(q)}</div>
      <div class="body" style="font-size:.20em;color:{sf['body']};">{esc(d)}</div>
    </div>""" for f, q, d in s["rows"])
    head = ""
    if s.get("figure"):
        head = f"""
    <div class="display" style="margin-top:.18em;font-size:.80em;line-height:1;
         color:{sf['ink']};font-variant-numeric:tabular-nums;letter-spacing:-.02em;">{esc(s['figure'])}
      <span style="font-size:.5em;color:{sf['data']};">{esc(s.get('delta',''))}</span></div>
    <div class="eyebrow" style="font-size:.21em;color:{sf['body']};
         margin-top:.06em;letter-spacing:1px;">{esc(s.get('unit',''))}</div>"""
    return f"""{_eyebrow(s, sf)}{head}
    <div style="margin-top:.26em;">{rows}</div>"""


LAYOUTS = {
    "hook": _hook, "data": _data, "checklist": _checklist,
    "statement": _statement, "cta": _cta, "single": _single,
    "figure": _figure, "share": _share, "scorecard": _scorecard,
}



def _furniture(sf, category=None):
    """Marchio e badge di categoria per le superfici che non li hanno
    incorporati nello sfondo. Sulle altre non si disegna nulla: aggiungerlo
    duplicherebbe quello gia' presente (brand-spec.md §7.1)."""
    if sf.get("furniture") != "overlay":
        return ""
    out = ('<img src="%s" alt="Digitiamo" style="position:absolute;left:120px;'
           'top:140px;width:245px;">' % tokens.data_uri(tokens.LOGO[sf["wordmark"]]))
    if category and sf.get("icon"):
        out += ('<img src="%s" alt="" style="position:absolute;right:120px;'
                'top:126px;width:104px;">' % tokens.data_uri(tokens.LOGO[sf["icon"]]))
    return out


def _footer(sf, source=None, page=None, total=None):
    """Fonte a sinistra, numero pagina a destra.

    Su editorial_* il wordmark e' in alto, quindi la riga bassa e' libera; su
    `news` il wordmark e' incorporato al centro-basso (x 452-706) e questi due
    blocchi lo affiancano senza sovrapporsi.
    """
    y = sf["footer_y"]
    out = []
    if source:
        out.append(
            '<div class="body" style="position:absolute;left:120px;top:%dpx;width:310px;'
            'font-size:19px;line-height:1.25;color:%s;">Fonte: %s</div>'
            % (y, sf["muted"], esc(source))
        )
    if page:
        out.append(
            '<div class="body body--bold" style="position:absolute;right:120px;top:%dpx;'
            'font-size:22px;color:%s;">%02d / %02d</div>'
            % (y, sf["muted"], page, total)
        )
    return "".join(out)


def _frame(slug, surface_key, inner, source=None, page=None, total=None, category=None):
    sf = SURFACES[surface_key]
    x, y, w, h = sf["box"]
    bg = tokens.data_uri(tokens.BACKGROUNDS[sf["bg"]])
    # La zona esterna ha altezza fissa e centra verticalmente; il blocco interno
    # ha font-size:100px con i figli in em, cosi' l'auto-fit lo scala in
    # proporzione. data-maxh e' l'altezza della zona: oltre quella, si rimpicciolisce.
    return f"""
  <div class="slide" data-slug="{esc(slug)}" style="width:{W}px;height:{H}px;">
    <img class="slide__bg" src="{bg}" alt="">
    {_furniture(sf, category)}
    <div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;
         display:flex;flex-direction:column;justify-content:center;">
      <div class="fit content" data-maxh="{h}" style="font-size:100px;">
        {inner}
      </div>
    </div>
    {_footer(sf, source, page, total)}
  </div>"""


def _document(slides_html, title):
    """Un solo documento con tutte le slide impilate: un browser, N screenshot."""
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><title>{esc(title)}</title>
<style>
{tokens.build_css()}
body {{ background:#e9e9f1; }}
.slide {{ margin:0 auto 40px; }}
</style></head>
<body>
{slides_html}
</body></html>"""


def carousel_html(carousel):
    """Le slide del carosello. La superficie di ogni pagina viene dal ritmo del
    tipo di post, a meno che la slide non la dichiari esplicitamente."""
    total = len(carousel["slides"])
    ptype = carousel.get("post_type")
    parts = []
    for i, s in enumerate(carousel["slides"], start=1):
        if s.get("surface"):
            key = s["surface"]
        elif ptype:
            key = rhythm_for(ptype, i - 1, total)
        else:
            key = carousel.get("surface", "navy")
        parts.append(_frame(
            slug="slide%d" % i, surface_key=key,
            inner=LAYOUTS[s["kind"]](s, SURFACES[key]),
            source=s.get("source"), page=i, total=total,
            category=carousel.get("category"),
        ))
    return _document("".join(parts), "Carosello %s" % carousel["slug"])


def singles_html(singles):
    """Le immagini singole. La superficie viene dal tipo di post, cosi' le
    quattro immagini della settimana non finiscono tutte sullo stesso fondo."""
    parts = []
    for s in singles:
        if s.get("surface"):
            key = s["surface"]
        elif s.get("post_type"):
            key = POST_TYPES[s["post_type"]]["rhythm"][0]
        else:
            key = "navy"
        parts.append(_frame(
            slug=s["slug"], surface_key=key,
            inner=LAYOUTS["single"](s, SURFACES[key]),
            category=s.get("category"),
        ))
    return _document("".join(parts), "Immagini singole")
