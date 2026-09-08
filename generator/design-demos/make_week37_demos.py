# -*- coding: utf-8 -*-
"""Prove v2 per i 4 post della settimana 7-13 settembre 2026.

Rispetto alla v1 sono stati letti **gli articoli**, non i riassunti del report.
Ne sono usciti dati che il report non aveva e una correzione di merito.

  1. Rassegna News AI   trend 01+02+04  copertina VERA del template + 3 notizie
  2. Model fatigue      trend 03        stile "ritratto computazionale" (Fathom)
  3. Agenti AI          trend 07        RIFRAMATO sul meccanismo, non sul 76%
  4. EU AI Act          trend 10        RICOSTRUITO con le date concrete

## 1. La copertina mancava perche' non usavo quella vera

`newsai_cover_bg.png` ha titolo, sottotitolo, icona e wordmark **incorporati nel
PNG** (misurati a pixel: y 169-335, 474-593, 701-913, 1344-1415). L'unico campo
variabile e' il **periodo**. In v1 avevo improvvisato una copertina sullo sfondo
delle notizie: sbagliato, la copertina esisteva gia'.

## 2. Model fatigue: dati nuovi dagli articoli

- **Intervallo mediano fra rilasci major: 37,5 giorni nel 2023 -> 11 nel 2026.**
  E' il dato che rende il fenomeno misurabile, ed era assente dal report.
- Il "da dieci a cinque" ha un autore: **Suresh Vasudevan, CEO di Clockwork
  Systems**, citato da CNBC. Una frase attribuita vale piu' di un numero anonimo.

Stile: ruota dei secondi -> **10/20, "Ritratto computazionale" (Fathom / Ben
Fry)**: tratti a capello, densita' per sovrapposizione, la forma nasce dai dati
e non dal layout, zero decorazione.
**Semplificazione dichiarata**: lo stile chiederebbe l'elenco completo dei
rilasci. Non ce l'ho. I tratti rappresentano la **cadenza mediana documentata**,
non i singoli eventi, ed e' scritto sulla slide. Inventare quaranta date per
fare densita' sarebbe esattamente il falso che il protocollo vieta.

## 3. Agenti AI: il 76% non regge come titolo

Verificando la fonte: il numero 847 viene da **un post su Medium che compare con
due firme diverse allo stesso URL** (`snehal_singh` e `neurominimal`), e la
paternita' accademica che alcune riprese attribuiscono (Stanford, MIT, Carnegie
Mellon, Nvidia, "Elloe AI Research Lab") **non e' verificabile**: quel paper non
si trova. Il 91% sul tool-chaining e' reale ma viene da una ricerca diversa
(STAC, 483 casi).

Il caveat del report era giusto. Ma un post Digitiamo che apre con "76%" poggia
su una fonte che un cliente smonta in trenta secondi — ed e' contro la voce del
brand ("niente sensazionalismo").

Quindi il post e' riframato sul **meccanismo**, documentato in modo solido e
verificabile: CVE reali, modalita' di fallimento silenziose, agenti orfani. Il
numero fragile resta fuori. E il meccanismo *e'* l'argomento del Team
Augmentation, cosa che il 76% non era.

## 4. EU AI Act: la v1 non diceva nulla

"Obblighi in vigore, regole in movimento" e' vero e inutile. Gli articoli danno
le date esatte, e una cosa che quasi nessuno nota: **la rilevazione dei bias e'
stata ESTESA** dai soli sistemi ad alto rischio a tutti i sistemi AI e ai
modelli generalisti. Quindi "hanno rinviato tutto" e' una lettura sbagliata: la
scadenza si e' spostata, il perimetro si e' allargato.

Uso: python3 design-demos/make_week37_demos.py
"""
import asyncio
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from playwright.async_api import async_playwright

import render
import templates
from brand import tokens

HERE = os.path.dirname(os.path.abspath(__file__))
TP = os.path.join(os.path.dirname(HERE), "brand", "third-party")
W, H = tokens.FORMATS["portrait"]


# I quattro post stanno in week.py: sono il CONTENUTO della settimana, non
# delle dimostrazioni. Erano definiti qui e da qui non potevano finire su
# Buffer, perche' `publish_buffer` legge da `plan.content()`.
from week import NEWSAI, FATIGUE, AGENTI, AI_ACT


# ---------------------------------------------------------------------------
# 1. Rassegna News AI — con la copertina vera del template
# ---------------------------------------------------------------------------
PIECES = {
    "W37-1-newsai": NEWSAI,
    "W37-2-model-fatigue": FATIGUE,
    "W37-3-agenti-847": AGENTI,
    "W37-4-ai-act": AI_ACT,
}


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": W, "height": H})

        for name, piece in PIECES.items():
            html = templates.carousel_html(piece)
            with open(os.path.join(HERE, "%s.html" % name), "w", encoding="utf-8") as f:
                f.write(html)
            await page.set_content(html, wait_until="load")
            await page.evaluate("document.fonts.ready")
            probs = await page.evaluate(render.AUTOFIT_JS, {
                "minFs": render.MIN_CONTAINER_FS,
                "maxFs": render.MAX_CONTAINER_FS,
                "fill": render.FILL_TARGET})
            slides = await page.query_selector_all(".slide")
            for i, el in enumerate(slides, start=1):
                await el.screenshot(path=os.path.join(HERE, "%s_%d.png" % (name, i)))
            flag = ("  PROBLEMI: " + "; ".join("%s/%s" % (x["kind"], x["slide"])
                                               for x in probs)) if probs else ""
            print("  %-22s %d slide%s" % (name, len(slides), flag))

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
