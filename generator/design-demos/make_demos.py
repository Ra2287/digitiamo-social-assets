# -*- coding: utf-8 -*-
"""Tre direzioni di design per il carosello editoriale — bozze reali da far scegliere.

## Il problema da risolvere

`newsai_bg.png` e' nato per i post "News AI", dove la fascia cielo (y 0-628,
il 42% dell'immagine) ospita la FOTO dell'articolo. Il carosello editoriale non
ha foto: quella fascia resta un gradiente vuoto, e il contenuto si schiaccia
nella meta' inferiore. Non e' un bug del codice, e' una decisione di design da
prendere.

## Le tre direzioni

A  "Dato nel cielo"     la fascia cielo diventa la zona del NUMERO (navy su
                        cielo), il pannello blu spiega. Il taglio diagonale
                        separa cifra e significato.
B  "Pannello pieno"     via il cielo: fondo navy pieno (webinar_bg), contenuto
                        centrato in un campo unico. La piu' autorevole.
C  "Attraverso il taglio" il cielo resta, ma un unico blocco tipografico
                        attraversa il confine: navy sopra, bianco sotto. Il
                        vincolo del template diventa la firma.

Tutte e tre usano SOLO asset reali di brand (sfondi, wordmark, font).
Uso: python3 design-demos/make_demos.py
"""
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.async_api import async_playwright

from brand import tokens

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = tokens.FORMATS["portrait"]
SKY_END = 628  # dove inizia il pannello blu, misurato sui pixel

BG_NEWS = tokens.data_uri(tokens.BACKGROUNDS["news"])
BG_NAVY = tokens.data_uri(tokens.BACKGROUNDS["webinar"])
WORDMARK = tokens.data_uri(tokens.LOGO["wordmark_white"])

# Contenuto identico nelle tre direzioni: cambia solo il design.
HOOK = dict(
    eyebrow="Analisi settimanale",
    title="L'AI Act non è più una promessa",
    accent="promessa",
    subtitle="È entrato in vigore il 2 agosto 2026. Ecco cosa cambia davvero "
             "per chi fa software in Italia — in 5 numeri.",
)
DATA = dict(
    eyebrow="Data chiave",
    num="2 agosto",
    num2="2026",
    explain="Il giorno in cui gli obblighi dell'AI Act sono passati dalla "
            "teoria alla pratica in tutta l'Unione Europea.",
    note="Non è più una scadenza futura da tenere d'occhio: da questa data, "
         "le regole si applicano.",
    source="Commissione Europea, Axios",
)

HEAD = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>%s</title><style>
%s
body { background:#e9e9f1; }
.slide { margin:0 auto 40px; }
.lbl { position:absolute; left:0; top:0; background:#0e0a48; color:#fff;
       font:700 20px/1 var(--font-body); padding:10px 16px; z-index:9; }
</style></head><body>
"""


def wordmark(**kw):
    style = ";".join("%s:%s" % (k.replace("_", "-"), v) for k, v in kw.items())
    return '<img src="%s" alt="Digitiamo" style="position:absolute;%s">' % (WORDMARK, style)


def foot(source=None, page=None, total=6, color="rgba(255,255,255,.66)",
         source_color=None, source_top=1352):
    """Fonte e numero pagina affiancano il wordmark INCORPORATO nello sfondo
    (x 452-706 su newsai_bg): mai sopra, mai al suo posto."""
    out = ""
    if source:
        out += ('<div style="position:absolute;left:120px;top:%dpx;width:300px;'
                'font:400 19px/1.25 var(--font-body);color:%s;">Fonte: %s</div>'
                % (source_top, source_color or color, source))
    if page:
        out += ('<div style="position:absolute;right:120px;top:1352px;'
                'font:700 22px/1 var(--font-body);color:%s;">%02d / %02d</div>'
                % (color, page, total))
    return out


# ---------------------------------------------------------------------------
# DIREZIONE A — "Dato nel cielo"
# Il cielo ospita la cifra in navy; il pannello blu porta il significato.
# ---------------------------------------------------------------------------
def dir_a():
    s1 = f"""
<div class="slide" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;">
  <div class="lbl">A · slide 1 — hook</div>
  <img src="{BG_NEWS}" style="position:absolute;inset:0;width:100%;height:100%;">
  <div style="position:absolute;left:120px;top:190px;width:900px;">
    <div style="font:700 26px/1 var(--font-display);text-transform:uppercase;
         letter-spacing:1.5px;color:var(--c-blue);">{HOOK['eyebrow']}</div>
    <div style="margin-top:26px;font:800 92px/1.02 var(--font-display);
         letter-spacing:-1.5px;color:var(--c-navy);">L'AI Act<br>non è più una
      <span style="color:var(--c-blue);">promessa</span></div>
  </div>
  <div style="position:absolute;left:120px;top:760px;width:900px;
       font:400 34px/1.36 var(--font-body);color:var(--c-text-on-blue);">{HOOK['subtitle']}</div>
  {foot(page=1)}
</div>"""
    s2 = f"""
<div class="slide" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;">
  <div class="lbl">A · slide 2 — dato</div>
  <img src="{BG_NEWS}" style="position:absolute;inset:0;width:100%;height:100%;">
  <div style="position:absolute;left:120px;top:170px;width:960px;">
    <div style="font:700 26px/1 var(--font-display);text-transform:uppercase;
         letter-spacing:1.5px;color:var(--c-blue);">{DATA['eyebrow']}</div>
    <div style="margin-top:20px;font:800 128px/.94 var(--font-display);
         letter-spacing:-3px;color:var(--c-navy);text-transform:uppercase;">
      {DATA['num']}<br>{DATA['num2']}</div>
  </div>
  <div style="position:absolute;left:120px;top:730px;width:930px;">
    <div style="font:700 38px/1.26 var(--font-body);color:#fff;">{DATA['explain']}</div>
    <div style="margin-top:28px;font:400 28px/1.34 var(--font-body);
         color:var(--c-text-on-blue);">{DATA['note']}</div>
  </div>
  {foot(source=DATA['source'], page=2, source_color='var(--c-blue)', source_top=560)}
</div>"""
    return s1 + s2


# ---------------------------------------------------------------------------
# DIREZIONE B — "Pannello pieno"
# Niente cielo: campo navy unico, contenuto centrato. Registro piu' autorevole.
# ---------------------------------------------------------------------------
def dir_b():
    def slide(label, inner, **f):
        return f"""
<div class="slide" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;">
  <div class="lbl">{label}</div>
  <img src="{BG_NAVY}" style="position:absolute;inset:0;width:100%;height:100%;">
  <div style="position:absolute;left:120px;top:330px;width:960px;height:940px;
       display:flex;flex-direction:column;justify-content:center;">{inner}</div>
  {foot(color='rgba(185,192,245,.72)', **f)}
</div>"""
    s1 = slide("B · slide 1 — hook", f"""
    <div style="font:700 26px/1 var(--font-display);text-transform:uppercase;
         letter-spacing:1.5px;color:var(--c-text-muted-navy);">{HOOK['eyebrow']}</div>
    <div style="margin-top:34px;font:800 94px/1.03 var(--font-display);
         letter-spacing:-1.5px;color:#fff;">L'AI Act<br>non è più una
      <span style="color:var(--c-green);">promessa</span></div>
    <div style="margin-top:44px;font:400 34px/1.36 var(--font-body);
         color:var(--c-text-muted-soft);">{HOOK['subtitle']}</div>""", page=1)
    s2 = slide("B · slide 2 — dato", f"""
    <div style="font:700 26px/1 var(--font-display);text-transform:uppercase;
         letter-spacing:1.5px;color:var(--c-text-muted-navy);">{DATA['eyebrow']}</div>
    <div style="margin-top:26px;font:800 132px/.94 var(--font-display);
         letter-spacing:-3px;color:var(--c-green);text-transform:uppercase;">
      {DATA['num']}<br>{DATA['num2']}</div>
    <div style="margin-top:38px;font:700 38px/1.26 var(--font-body);color:#fff;">{DATA['explain']}</div>
    <div style="margin-top:26px;font:400 28px/1.34 var(--font-body);
         color:var(--c-text-muted-soft);">{DATA['note']}</div>""",
                source=DATA['source'], page=2)
    return s1 + s2


# ---------------------------------------------------------------------------
# DIREZIONE C — "Attraverso il taglio"
# Un blocco tipografico unico attraversa il confine cielo/pannello: le righe
# sopra sono navy, quelle sotto bianche. Il vincolo diventa la firma.
# ---------------------------------------------------------------------------
def dir_c():
    # Il confine cielo/pannello e' a y=628. Il blocco tipografico e' posizionato
    # perche' le righe CADANO davvero a cavallo: quelle sopra il confine sono
    # navy (leggibili sul cielo chiaro), quelle sotto bianche (sul pannello blu).
    # Bianco sul cielo NON si usa mai: il contrasto sarebbe inaccettabile.
    s1 = f"""
<div class="slide" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;">
  <div class="lbl">C · slide 1 — hook</div>
  <img src="{BG_NEWS}" style="position:absolute;inset:0;width:100%;height:100%;">
  <div style="position:absolute;left:120px;top:270px;font:700 26px/1 var(--font-display);
       text-transform:uppercase;letter-spacing:1.5px;color:var(--c-blue);">{HOOK['eyebrow']}</div>
  <div style="position:absolute;left:146px;top:420px;width:960px;
       font:800 104px/1.0 var(--font-display);letter-spacing:-2px;">
    <div style="color:var(--c-navy);">L'AI Act</div>
    <div style="color:var(--c-navy);">non è più una</div>
    <div style="color:#fff;">promessa</div>
  </div>
  <div style="position:absolute;left:120px;top:424px;width:6px;height:312px;
       background:var(--c-blue);"></div>
  <div style="position:absolute;left:146px;top:820px;width:900px;
       font:400 34px/1.36 var(--font-body);color:var(--c-text-on-blue);">{HOOK['subtitle']}</div>
  {foot(page=1)}
</div>"""
    s2 = f"""
<div class="slide" style="width:{W}px;height:{H}px;position:relative;overflow:hidden;">
  <div class="lbl">C · slide 2 — dato</div>
  <img src="{BG_NEWS}" style="position:absolute;inset:0;width:100%;height:100%;">
  <div style="position:absolute;left:120px;top:404px;font:700 26px/1 var(--font-display);
       text-transform:uppercase;letter-spacing:1.5px;color:var(--c-blue);">{DATA['eyebrow']}</div>
  <div style="position:absolute;left:146px;top:490px;width:1000px;
       font:800 150px/.92 var(--font-display);letter-spacing:-4px;text-transform:uppercase;">
    <div style="color:var(--c-navy);">{DATA['num']}</div>
    <div style="color:#fff;">{DATA['num2']}</div>
  </div>
  <div style="position:absolute;left:120px;top:494px;width:6px;height:266px;
       background:var(--c-blue);"></div>
  <div style="position:absolute;left:146px;top:830px;width:930px;">
    <div style="font:700 38px/1.26 var(--font-body);color:#fff;">{DATA['explain']}</div>
    <div style="margin-top:28px;font:400 28px/1.34 var(--font-body);
         color:var(--c-text-on-blue);">{DATA['note']}</div>
  </div>
  {foot(source=DATA['source'], page=2, source_top=1352)}
</div>"""
    return s1 + s2


DIRECTIONS = {
    "A-dato-nel-cielo": dir_a,
    "B-pannello-pieno": dir_b,
    "C-attraverso-il-taglio": dir_c,
}


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, fn in DIRECTIONS.items():
            html = HEAD % (name, tokens.build_css()) + fn() + "</body></html>"
            path = os.path.join(HERE, "%s.html" % name)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            page = await browser.new_page(viewport={"width": W, "height": H})
            await page.set_content(html, wait_until="load")
            await page.evaluate("document.fonts.ready")
            for i, el in enumerate(await page.query_selector_all(".slide"), start=1):
                out = os.path.join(HERE, "%s_%d.png" % (name, i))
                await el.screenshot(path=out)
                print("  ", os.path.basename(out))
            await page.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
