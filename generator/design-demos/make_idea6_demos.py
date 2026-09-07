# -*- coding: utf-8 -*-
"""Tre idee di layout per l'IDEA 6 del PED — carosello dati Nvidia.

Dalle 7 idee del PED, la 6 ("96,2 miliardi in un trimestre: cosa ci dicono
davvero i numeri di Nvidia", formato Carosello/documento dati, badge Riserva) e'
l'unica **senza grafiche**. Ed e' interamente numeri, quindi e' il caso in cui il
layout decide se il post funziona.

Le tre idee stanno DENTRO la direzione B "Pannello pieno" (approvata 2026-09-07):
il sistema e' deciso, qui si sceglie come trattare una slide guidata dai dati.
Il layout `_data` attuale (occhiello / numero / spiegazione / nota) va bene per
una data secca come "2 agosto 2026", ma non per una cifra con uno scarto: perde
l'unita' di misura, lo scarto percentuale e la proporzione.

## Procedura seguita (skill dataviz)

1. **Forma prima del colore.**
   A -> nessun grafico: una cifra sola e' un "hero number", non un chart.
   B -> proporzione parte/tutto (89 su 96,2): una barra a segmento singolo.
   C -> tre indicatori affiancati: scorecard di stat tile.

2. **Colore calcolato, non valutato a occhio** (`validate_palette.js`):
   - `#d0f0ff` (cielo brand) **FALLISCE il chroma floor** (0.039, "reads gray"):
     NON e' una tinta dati. Resta un neutro.
   - `#43ef84` (verde brand) da solo: chroma PASS, contrasto PASS >= 3:1 su navy
     e su blu. L'unico FAIL e' la lightness band, che e' un vincolo per palette
     categoriali multi-serie e non governa un accento a tinta singola.
   - Conclusione: **una sola tinta dati (verde) + un neutro**. Nessuna palette
     categoriale, quindi nessun rischio CVD sulle coppie adiacenti.

3. **Conseguenza sul brand.** `brand-spec.md` §3 riserva il verde al campo navy,
   e sul campo blu l'accento e' il cielo — che pero' non e' una tinta dati. Quindi
   **le slide con grafico vanno sul campo navy**, dove il verde e' ammesso e
   funziona. Non e' un'eccezione alla regola: la precisa. Navy = argomentazione
   *e* dato quantificato; blu = affermazione fattuale senza grafico.

4. **Specifiche dei segni**: estremita' arrotondate ancorate alla base, stacco di
   superficie fra i riempimenti, cifre in `tabular-nums`, etichette dirette
   (nessuna legenda: due segmenti etichettati si nominano da soli), assi recessivi.

5. **Nessun layer di hover.** La skill lo vuole di default, ma il mezzo qui e' un
   PNG pubblicato su LinkedIn: non esiste hover. I valori stanno quindi tutti come
   etichette diritte nel grafico, non in un tooltip.

Uso: python3 design-demos/make_idea6_demos.py
"""
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.async_api import async_playwright

from brand import tokens

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = tokens.FORMATS["portrait"]
BG = tokens.data_uri(tokens.BACKGROUNDS["editorial_navy"])

# Dati reali dall'idea 6 (build_report.ideas[5]).
TOTALE = 96.2          # miliardi $, fatturato trimestrale
DATACENTER = 89.0      # miliardi $, di cui dal segmento data center
QUOTA = DATACENTER / TOTALE   # 0.925

CSS = """
.slide{width:%dpx;height:%dpx;position:relative;overflow:hidden;
       font-family:var(--font-body);}
.slide img.bg{position:absolute;inset:0;width:100%%;height:100%%;}
.lbl{position:absolute;left:0;top:0;z-index:9;background:#fff;color:var(--c-navy);
     font:700 20px/1 var(--font-body);padding:10px 16px;}
.zone{position:absolute;left:120px;top:330px;width:960px;height:940px;
      display:flex;flex-direction:column;justify-content:center;}
.eyebrow{font-family:var(--font-display);font-weight:700;font-size:26px;
         text-transform:uppercase;letter-spacing:1.5px;color:var(--c-green);}
.fig{font-family:var(--font-display);font-weight:800;
     font-variant-numeric:tabular-nums;letter-spacing:-4px;color:#fff;}
.unit{font-family:var(--font-display);font-weight:700;font-size:34px;
      text-transform:uppercase;letter-spacing:1px;color:var(--c-text-muted-soft);}
.delta{display:inline-flex;align-items:baseline;gap:10px;
       font-family:var(--font-display);font-weight:800;
       font-variant-numeric:tabular-nums;color:var(--c-green);}
.say{font:400 30px/1.36 var(--font-body);color:var(--c-text-muted-soft);}
.say b{color:#fff;font-weight:700;}
.foot{position:absolute;left:120px;top:1400px;width:400px;
      font:400 19px/1.25 var(--font-body);color:rgba(185,192,245,.72);}
.pg{position:absolute;right:120px;top:1400px;
    font:700 22px/1 var(--font-body);color:rgba(185,192,245,.72);}
""" % (W, H)


def frame(label, inner, page, source="Intellectia.ai / US News"):
    return f"""
<div class="slide">
  <div class="lbl">{label}</div>
  <img class="bg" src="{BG}" alt="">
  {inner}
  <div class="foot">Fonte: {source}</div>
  <div class="pg">{page:02d} / 06</div>
</div>"""


# ---------------------------------------------------------------------------
# A — "Cifra e scarto": hero number. Nessun grafico.
# Una cifra sola non e' un chart: e' un titolo che si legge come un numero.
# L'unita' di misura e lo scarto, che il layout attuale perde, sono espliciti.
# ---------------------------------------------------------------------------
def dir_a():
    return frame("A · Cifra e scarto", f"""
  <div class="zone">
    <div class="eyebrow">Trimestre record</div>
    <div style="display:flex;align-items:baseline;gap:24px;margin-top:26px;">
      <div class="fig" style="font-size:250px;line-height:.86;">96,2</div>
      <div class="unit" style="padding-bottom:34px;">miliardi<br>di dollari</div>
    </div>
    <div class="delta" style="margin-top:22px;">
      <span style="font-size:76px;line-height:1;">+106%</span>
      <span style="font-family:var(--font-body);font-weight:700;font-size:28px;
            color:var(--c-text-muted-soft);">anno su anno</span>
    </div>
    <div class="say" style="margin-top:44px;">
      Il fatturato trimestrale di Nvidia. <b>Più che raddoppiato in dodici mesi.</b>
    </div>
  </div>""", 2)


# ---------------------------------------------------------------------------
# B — "Quota": proporzione parte/tutto, 89 su 96,2.
# La forma porta l'informazione: la barra e' quasi tutta verde, e quello E' il
# punto — la crescita e' un solo segmento, non l'azienda intera.
# Una tinta dati (verde) + neutro. Etichette dirette, nessuna legenda.
# ---------------------------------------------------------------------------
def dir_b():
    total_w = 960
    gap = 5                                  # stacco di superficie fra i riempimenti
    seg = round(total_w * QUOTA) - gap
    rest = total_w - seg - gap
    return frame("B · Quota", f"""
  <div class="zone">
    <div class="eyebrow">Da dove arriva</div>
    <div style="display:flex;align-items:baseline;gap:20px;margin-top:24px;">
      <div class="fig" style="font-size:170px;line-height:.9;">89</div>
      <div class="unit" style="padding-bottom:22px;">miliardi<br>su 96,2</div>
    </div>

    <!-- Barra parte/tutto: estremita' arrotondate solo sui bordi esterni, cosi'
         il segmento resta ancorato alla base invece di galleggiare. -->
    <div style="margin-top:40px;display:flex;gap:{gap}px;height:64px;">
      <div style="width:{seg}px;background:var(--c-green);border-radius:10px 0 0 10px;"></div>
      <div style="width:{rest}px;background:rgba(255,255,255,.22);border-radius:0 10px 10px 0;"></div>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:14px;
         font-family:var(--font-display);font-weight:700;font-size:24px;
         font-variant-numeric:tabular-nums;text-transform:uppercase;letter-spacing:.5px;">
      <div style="color:var(--c-green);">Data center · 92,5%</div>
      <div style="color:var(--c-text-muted-soft);">Resto · 7,5%</div>
    </div>

    <div class="say" style="margin-top:46px;">
      Quasi tutto il trimestre è un solo segmento, cresciuto del
      <b>117% anno su anno</b>. Non è Nvidia che cresce: è l'infrastruttura AI.
    </div>
  </div>""", 3)


# ---------------------------------------------------------------------------
# C — "Scorecard": tre indicatori su una slide.
# Piu' densa: una slide invece di tre. Cifre in colonna con tabular-nums, cosi'
# le unita' si allineano e i valori si confrontano a colpo d'occhio.
# ---------------------------------------------------------------------------
# Colonna 1 = la cifra. Colonna 2 = il suo qualificatore (periodo o scarto),
# sempre lo stesso tipo di informazione. Colonna 3 = cosa significa.
ROWS = [
    ("89 mld", "+117%", "dal segmento data center: il vero motore della crescita"),
    ("+9%", "in una seduta", "il titolo, con circa 440 miliardi di capitalizzazione aggiunta in un giorno"),
    ("+70%", "atteso FY2028", "gli analisti scommettono che la domanda di infrastruttura continui a salire"),
]


def dir_c():
    rows = "".join(f"""
    <div style="display:grid;grid-template-columns:250px 250px 1fr;gap:24px;
         align-items:baseline;padding:26px 0;
         border-top:2px solid rgba(255,255,255,.16);">
      <div class="fig" style="font-size:66px;line-height:1;letter-spacing:-2px;">{a}</div>
      <div class="delta" style="font-size:32px;white-space:nowrap;">{b}</div>
      <div style="font:400 24px/1.34 var(--font-body);color:var(--c-text-muted-soft);">{c}</div>
    </div>""" for a, b, c in ROWS)
    return frame("C · Scorecard", f"""
  <div class="zone">
    <div class="eyebrow">I numeri, in fila</div>
    <div class="fig" style="font-size:104px;line-height:1;margin-top:22px;">96,2 mld <span
         style="font-size:52px;color:var(--c-green);letter-spacing:-1px;">+106%</span></div>
    <div class="unit" style="font-size:26px;margin-top:10px;">fatturato trimestrale, anno su anno</div>
    <div style="margin-top:34px;">{rows}</div>
  </div>""", 4)


DIRECTIONS = {"I6-A-cifra-e-scarto": dir_a, "I6-B-quota": dir_b, "I6-C-scorecard": dir_c}


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": W, "height": H})
        for name, fn in DIRECTIONS.items():
            html = ("<!doctype html><html lang=\"it\"><head><meta charset=\"utf-8\">"
                    "<title>%s</title><style>%s\n%s</style></head><body>%s</body></html>"
                    % (name, tokens.build_css(), CSS, fn()))
            with open(os.path.join(HERE, "%s.html" % name), "w", encoding="utf-8") as f:
                f.write(html)
            await page.set_content(html, wait_until="load")
            await page.evaluate("document.fonts.ready")
            el = await page.query_selector(".slide")
            await el.screenshot(path=os.path.join(HERE, "%s.png" % name))
            # Il grafico va guardato, non solo validato: il validator controlla il
            # colore, non la geometria ne' le collisioni fra etichette.
            over = await page.evaluate(
                """() => {const z=document.querySelector('.zone');
                          return Math.round(z.scrollHeight - z.clientHeight);}""")
            print("  %-22s %s" % (name, "ok" if over <= 0 else "SFORA di %dpx" % over))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
