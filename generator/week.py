# -*- coding: utf-8 -*-
"""Date della settimana e correzioni a mano alle grafiche.

## Cosa NON sta piu' qui

I contenuti delle slide. Vengono **derivati dal report** da `plan.py`: si
scrivono le idee in `build_report.py` e le grafiche seguono, senza che nessuno
scelga i template. Prima erano scritti a mano qui, ed e' il motivo per cui ogni
esecuzione del lunedi' finiva per reinventare il design.

## Cosa sta qui

1. **Le date.** `DATE` finisce nei nomi dei file, quindi e' una scelta
   deliberata e non si ricava da una stringa in prosa del report.
2. **Le correzioni.** Dopo la revisione umana una slide puo' aver bisogno di una
   sistemata: si dichiara qui, con lo **stesso slug** che il piano assegna (lo
   stampa `python3 plan.py`), e la versione a mano vince su quella derivata.

Esempio di correzione:

    CAROUSELS = [
        dict(slug="idea3-l-ai-nelle-aziende", post_type="data_carousel",
             category="News AI", slides=[...]),   # sequenza completa a mano
    ]

Convenzione nei testi: `*parola*` rende la parola in colore accento. Il piano
accenta l'ultima parola del titolo per default; scrivendo gli asterischi a mano
si sceglie la parola giusta.
"""
import base64
import os

# Settimana di pubblicazione. Finisce nei nomi dei file: non riusare mai una
# combinazione data+slug gia' pubblicata (vedi CLAUDE.md).
DATE = "2026-09-21"
WEEK_LABEL = "21 - 27 settembre 2026"

# A quale settimana appartengono le CORREZIONI qui sotto. Controllato solo se ce
# ne sono: serve a non riapplicare a una settimana nuova un aggiustamento
# scritto per quella vecchia, che passerebbe inosservato perche' i nomi dei file
# sarebbero comunque nuovi.
OVERRIDES_FOR = "2026-09-21"

# Rifacimenti: slug del post -> numero di revisione. Ciclo human-in-the-loop.
#
# Vuoto = prima generazione del lunedi'. Se un post va RIFATTO dopo la revisione
# umana, segnalo qui con 1 (poi 2, 3...): i suoi file prendono il suffisso `-r1`,
# quindi stessa settimana e stesso post ma **URL nuovo**. Poi la bozza Buffer va
# rifatta sul nuovo URL, e quella vecchia cancellata.
#
# Gli slug sono quelli stampati da `python3 plan.py`. Esempio:
#   REDO = {"idea2-la-sicurezza-dell-ai": 1}
REDO = {}

# I post approvati NON corrispondono alle idee del report solo in casi
# eccezionali (fusione di trend, idee scartate in revisione). Questa settimana
# le grafiche si derivano dal report (CLAUDE.md, regola 2): resta False.
SOSTITUISCE_IL_PIANO = False

# ---------------------------------------------------------------------------
# Marchi di terzi (disponibili se una settimana futura ne avesse bisogno in
# un carosello dichiarato a mano). Nessuna idea di questa settimana li usa.
# ---------------------------------------------------------------------------
_TP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand", "third-party")


def svg_uri(name):
    with open(os.path.join(_TP, name), "rb") as f:
        return "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")


# Nessuna correzione a mano questa settimana: tutto deriva dal report.
CAROUSELS = []
SINGLES = []
