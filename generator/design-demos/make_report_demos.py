# -*- coding: utf-8 -*-
"""Tre direzioni di layout per la pagina "Trend del settore" del report PED.

## I problemi da risolvere (rilevati sul report attuale)

1. **Impaginazione rotta.** `trends_page()` impagina a `per_page = 5` fisso, ma a
   794x1123 ce ne stanno circa 3: 4 pagine su 13 sforano l'A4 (fino a 754px) e
   nel PDF le schede si spezzano a meta' fra le pagine. E' da qui che 13 pagine
   dichiarate diventano 17 pagine stampate.
2. **Card + bordo colorato a sinistra, ovunque.** E' il pattern piu'
   riconoscibile della grafica generata da AI, e qui e' su ogni trend e su ogni
   box "Spunto per Digitiamo".
3. **Gerarchia piatta.** Tutto e' una card con lo stesso raggio e lo stesso
   bordo: un trend, un competitor e un'intuizione hanno lo stesso peso visivo.
4. **"Cosa e' successo" e "Perche' e' rilevante" sono indistinguibili** — sono
   un fatto e un'interpretazione, cioe' due cose editorialmente diverse, ma
   hanno la stessa etichettina blu.
5. **Nessuna traccia del linguaggio visivo del brand** oltre a palette e font:
   niente motivo a circuito, niente marchio, niente badge di categoria.

## Le tre direzioni

A  "Dossier"          Via i contenitori. Filetti, numero grande nel margine,
                      fatto e interpretazione separati dalla tipografia.
B  "Spina a circuito" Il motivo del logo diventa una spina verticale; ogni trend
                      e' un nodo. Codifica la sequenza, massima identita'.
C  "Griglia densa"    Tessere compatte su due colonne con fascia navy di testa.
                      La piu' sfogliabile, la piu' densa.

Tutte e tre impaginano **per misura**, non per costante: si aggiungono elementi
finche' entrano davvero nella pagina.

Uso: python3 design-demos/make_report_demos.py
"""
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.async_api import async_playwright

from brand import tokens
from build_report import trends
from generate_html import esc

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = tokens.FORMATS["a4"]
PAD_X, PAD_TOP = 60, 64

WORDMARK = tokens.data_uri(tokens.LOGO["wordmark_white"])
ICON = tokens.data_uri(tokens.LOGO["icon_news_white"])

BASE = """
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#d7d7e2;}
.page{
  width:%dpx; height:%dpx; background:#fff; position:relative;
  overflow:hidden; margin:0 auto 30px; font-family:var(--font-body);
  color:var(--c-navy);
}
.lbl{position:absolute;left:0;top:0;z-index:9;background:var(--c-navy);color:#fff;
     font:700 11px/1 var(--font-body);padding:7px 11px;letter-spacing:.04em;}
.h-sec{font-family:var(--font-display);font-weight:800;font-size:26px;
       letter-spacing:-.01em;text-transform:uppercase;}
.h-num{color:var(--c-blue);}
.h-sub{font-size:12.5px;color:#5b5f8f;font-weight:400;margin-top:5px;}
.pagefoot{position:absolute;bottom:26px;left:%dpx;right:%dpx;display:flex;
  justify-content:space-between;font-size:10px;color:#9498c4;
  border-top:1px solid var(--c-tint);padding-top:9px;}
""" % (W, H, PAD_X, PAD_X)


def head(title, extra_css):
    return ("""<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>%s</title><style>%s
%s
%s</style></head><body>""" % (title, tokens.build_css(), BASE, extra_css))


def foot(label):
    return ('<div class="pagefoot"><div>PED Digitiamo · 31 ago – 4 set 2026</div>'
            '<div>%s</div></div>' % label)


# ---------------------------------------------------------------------------
# A — "Dossier": nessun contenitore. Filetto + numero nel margine.
# Fatto e interpretazione distinti dalla tipografia, non da due box uguali.
# ---------------------------------------------------------------------------
CSS_A = """
.a-head{position:absolute;left:60px;top:64px;right:60px;}
.a-rule{height:3px;width:44px;background:var(--c-green);margin-top:13px;}
.a-list{position:absolute;left:60px;top:172px;right:60px;}
.a-item{display:grid;grid-template-columns:52px 1fr;gap:16px;
        border-top:1px solid #d9d6ea;padding:18px 0 16px;}
.a-item:first-child{border-top:2px solid var(--c-navy);}
.a-n{font-family:var(--font-display);font-weight:800;font-size:34px;
     line-height:.9;color:#fff;-webkit-text-stroke:1.4px var(--c-blue);}
.a-t{font-family:var(--font-display);font-weight:700;font-size:15.5px;
     line-height:1.24;letter-spacing:-.005em;}
.a-fact{font-size:12.4px;line-height:1.5;margin-top:9px;color:#2a2c52;}
.a-why{font-size:12.4px;line-height:1.5;margin-top:10px;padding-left:13px;
       border-left:2px solid var(--c-green);color:var(--c-blue);font-weight:700;}
.a-src{font-size:10.5px;color:#8286b0;margin-top:9px;letter-spacing:.02em;}
.a-src b{color:var(--c-navy);font-weight:700;}
"""


def page_a(items):
    rows = "".join(f"""
    <div class="a-item">
      <div class="a-n">{i}</div>
      <div>
        <div class="a-t">{esc(t['title'])}</div>
        <div class="a-fact">{esc(t['what'])}</div>
        <div class="a-why">{esc(t['why'])}</div>
        <div class="a-src">Fonte <b>{esc(t['source'])}</b></div>
      </div>
    </div>""" for i, t in items)
    return f"""
<div class="page">
  <div class="lbl">A · Dossier</div>
  <div class="a-head">
    <div class="h-sec"><span class="h-num">01.</span> Trend del settore</div>
    <div class="h-sub">Gli sviluppi più rilevanti degli ultimi 7 giorni nel mondo AI/software tech</div>
    <div class="a-rule"></div>
  </div>
  <div class="a-list">{rows}</div>
  {foot('Sezione 01')}
</div>"""


# ---------------------------------------------------------------------------
# B — "Spina a circuito": il motivo del logo come spina verticale.
# Ogni trend e' un nodo (cerchio + asta), come lo spillo del marchio.
# ---------------------------------------------------------------------------
CSS_B = """
.b-top{position:absolute;left:0;top:0;width:794px;height:132px;background:var(--c-navy);}
.b-top .wm{position:absolute;left:60px;top:44px;width:132px;}
.b-top .ic{position:absolute;right:60px;top:34px;width:52px;}
.b-h{position:absolute;left:60px;top:158px;right:60px;}
.b-h .h-sec{font-size:24px;}
.b-list{position:absolute;left:60px;top:250px;right:60px;}
.b-item{position:relative;padding:0 0 22px 56px;}
.b-item:last-child{padding-bottom:0;}
.b-spine{position:absolute;left:17px;top:6px;bottom:-6px;width:3px;background:var(--c-tint);}
.b-item:last-child .b-spine{display:none;}
.b-node{position:absolute;left:0;top:0;width:37px;height:37px;border-radius:50%;
        background:#fff;border:3px solid var(--c-blue);
        display:flex;align-items:center;justify-content:center;
        font-family:var(--font-display);font-weight:800;font-size:15px;color:var(--c-blue);}
.b-t{font-family:var(--font-display);font-weight:700;font-size:15.5px;
     line-height:1.24;padding-top:7px;}
.b-fact{font-size:12.3px;line-height:1.5;margin-top:8px;color:#2a2c52;}
.b-why{font-size:12.3px;line-height:1.5;margin-top:9px;background:var(--c-tint);
       border-radius:0 8px 8px 0;padding:11px 14px;color:var(--c-navy);}
.b-why b{color:var(--c-blue);text-transform:uppercase;font-size:9.5px;
         letter-spacing:.08em;display:block;margin-bottom:3px;
         font-family:var(--font-display);}
.b-src{font-size:10.5px;color:#8286b0;margin-top:8px;}
.b-src b{color:var(--c-navy);}
"""


def page_b(items):
    rows = "".join(f"""
    <div class="b-item">
      <div class="b-spine"></div><div class="b-node">{i}</div>
      <div class="b-t">{esc(t['title'])}</div>
      <div class="b-fact">{esc(t['what'])}</div>
      <div class="b-why"><b>Perché è rilevante</b>{esc(t['why'])}</div>
      <div class="b-src">Fonte <b>{esc(t['source'])}</b></div>
    </div>""" for i, t in items)
    return f"""
<div class="page">
  <div class="lbl">B · Spina a circuito</div>
  <div class="b-top">
    <img class="wm" src="{WORDMARK}" alt="Digitiamo">
    <img class="ic" src="{ICON}" alt="">
  </div>
  <div class="b-h">
    <div class="h-sec"><span class="h-num">01.</span> Trend del settore</div>
    <div class="h-sub">Gli sviluppi più rilevanti degli ultimi 7 giorni nel mondo AI/software tech</div>
  </div>
  <div class="b-list">{rows}</div>
  {foot('Sezione 01')}
</div>"""


# ---------------------------------------------------------------------------
# C — "Griglia densa": tessere su due colonne, fascia navy di testa.
# La piu' sfogliabile: piu' trend per pagina, meno pagine totali.
# ---------------------------------------------------------------------------
CSS_C = """
.c-head{position:absolute;left:60px;top:64px;right:60px;
        display:flex;justify-content:space-between;align-items:flex-end;
        border-bottom:2px solid var(--c-navy);padding-bottom:11px;}
.c-count{font-family:var(--font-display);font-weight:800;font-size:11px;
         color:var(--c-blue);letter-spacing:.08em;text-transform:uppercase;}
.c-grid{position:absolute;left:60px;top:144px;right:60px;
        display:grid;grid-template-columns:1fr 1fr;gap:10px;
        align-content:start;}
.c-tile{border:1px solid #dcd9ec;display:flex;flex-direction:column;}
.c-bar{background:var(--c-navy);color:#fff;padding:7px 10px;display:flex;gap:8px;
       align-items:flex-start;}
.c-n{font-family:var(--font-display);font-weight:800;font-size:12px;
     color:var(--c-green);flex:0 0 auto;padding-top:1px;}
.c-t{font-family:var(--font-display);font-weight:700;font-size:11.8px;line-height:1.2;}
.c-body{padding:9px 10px 0;font-size:10.6px;line-height:1.4;color:#2a2c52;flex:1;}
.c-why{margin:8px 10px 0;padding:7px 9px;background:var(--c-tint);
       font-size:10.4px;line-height:1.38;}
.c-why b{display:block;font-family:var(--font-display);font-size:9px;
         text-transform:uppercase;letter-spacing:.07em;color:var(--c-blue);margin-bottom:3px;}
.c-src{padding:6px 10px 9px;font-size:9.4px;color:#8286b0;}
.c-src b{color:var(--c-navy);}
"""


def page_c(items):
    tiles = "".join(f"""
    <div class="c-tile">
      <div class="c-bar"><div class="c-n">{i:02d}</div><div class="c-t">{esc(t['title'])}</div></div>
      <div class="c-body">{esc(t['what'])}</div>
      <div class="c-why"><b>Perché è rilevante</b>{esc(t['why'])}</div>
      <div class="c-src">Fonte <b>{esc(t['source'])}</b></div>
    </div>""" for i, t in items)
    return f"""
<div class="page">
  <div class="lbl">C · Griglia densa</div>
  <div class="c-head">
    <div>
      <div class="h-sec"><span class="h-num">01.</span> Trend del settore</div>
      <div class="h-sub">Gli sviluppi più rilevanti degli ultimi 7 giorni</div>
    </div>
    <div class="c-count">{len(items)} di {len(trends)}</div>
  </div>
  <div class="c-grid">{tiles}</div>
  {foot('Sezione 01')}
</div>"""


DIRECTIONS = {
    "R-A-dossier": (CSS_A, page_a, 4),
    "R-B-spina-circuito": (CSS_B, page_b, 3),
    "R-C-griglia-densa": (CSS_C, page_c, 6),
}

# Quanto spazio verticale puo' occupare il contenuto prima di sforare la pagina.
# Il footer sta a 26px dal fondo, quindi si lascia un margine di sicurezza.
CONTENT_LIMIT = H - 70


async def fit_count(page, css, builder, start):
    """Impagina PER MISURA: parte da `start` trend e toglie finche' entrano.

    E' il punto: il layout attuale usa una costante (5) che non corrisponde a
    quanto entra davvero, e sfora. Qui si misura.
    """
    n = start
    while n > 1:
        items = list(enumerate(trends[:n], start=1))
        await page.set_content(head("fit", css) + builder(items) + "</body></html>",
                               wait_until="load")
        await page.evaluate("document.fonts.ready")
        h = await page.evaluate(
            """() => {const l=document.querySelector('.a-list,.b-list,.c-grid');
                      return Math.round(l.getBoundingClientRect().bottom);}""")
        if h <= CONTENT_LIMIT:
            return n, h
        n -= 1
    return 1, h


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": W, "height": H})
        report = []
        for name, (css, builder, start) in DIRECTIONS.items():
            n, h = await fit_count(page, css, builder, start)
            items = list(enumerate(trends[:n], start=1))
            html = head(name, css) + builder(items) + "</body></html>"
            with open(os.path.join(HERE, "%s.html" % name), "w", encoding="utf-8") as f:
                f.write(html)
            await page.set_content(html, wait_until="load")
            await page.evaluate("document.fonts.ready")
            el = await page.query_selector(".page")
            await el.screenshot(path=os.path.join(HERE, "%s.png" % name))
            pages = -(-len(trends) // n)  # ceil
            report.append((name, n, h, pages))
            print("  %-22s %d trend/pagina  (contenuto fino a y=%d di %d)  -> %d pagine per 10 trend"
                  % (name, n, h, CONTENT_LIMIT, pages))
        await browser.close()
        return report


if __name__ == "__main__":
    asyncio.run(main())
