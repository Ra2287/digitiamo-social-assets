# -*- coding: utf-8 -*-
"""Tre strade NUOVE per il carosello, con immagini reali. Processo huashu completo.

Non sono varianti del sistema attuale: sono tre linguaggi diversi, ognuno con un
riferimento reale dichiarato. Tutti richiamano il brand (palette, Montserrat/Lato,
marchio, motivo a circuito) ma nessuno assomiglia a quello che abbiamo adesso.

## Le tre logiche di huashu, applicate

A · **Riferimento reale** — Bloomberg Businessweek, pagina dati (era Richard
     Turley, 2010-2014). Contrasto di corpo estremo, titolo che dice la
     conclusione, grafico che esce dal margine. Registro: media, non corporate.

B · **Miglior designer per QUESTO cliente** — Giorgia Lupi, partner Pentagram,
     autrice del manifesto Data Humanism ("i dati sono persone, non numeri").
     Scelta non casuale: e' italiana come il cliente, e il suo metodo — un
     linguaggio di simboli inventato per il contenuto, piu' una legenda
     obbligatoria — combacia con un marchio che E' GIA' un circuito con nodi.
     Il nodo del logo diventa il glifo dei dati.

C · **Ruota dei secondi: 2/20 nella partizione infografica** —
     "Explanation Graphics" di Nigel Holmes (direttore grafico di TIME dal 1978
     al 1994). Metafora pittorica, colori piatti saturi, contorni neri, ironia.

## Materiale fotografico: procurato PRIMA di disegnare (Phase 3.5)

- `brand/photo/nasa-columbia-supercomputer.jpg` — pubblico dominio (NASA).
  Test di onesta' superato: la slide parla di "89 miliardi dal segmento data
  center", e la fotografia rende fisico un segmento contabile astratto.
- `brand/third-party/nvidia-wordmark-*.svg` — logo ufficiale. NON e' decorazione:
  il protocollo asset impone che un prodotto nominato mostri il proprio marchio.

Scartate: schede grafiche di consumo del 2009 (fuorvianti per ricavi data center
2026) e foto CC BY-SA (attribuzione + share-alike su un post commerciale).
Dettagli in `brand/photo/PROVENANCE.md`.

## Vincoli dichiarati

- **Due verdi non convivono.** Il verde Nvidia e' #76b900, quello Digitiamo
  #43ef84. Un logo di terzi non si ricolora, quindi dove appare Nvidia l'accento
  Digitiamo passa al blu.
- **La foto va trattata in duotone** sulla palette Digitiamo: a colori pieni
  porta dentro grigi e arancioni che sfondano il sistema cromatico.
- **Degradazione onesta su C**: l'anima dello stile Holmes e' l'illustrazione
  disegnata a mano. Non ho capacita' di generazione immagini confermata, e
  disegnare finte illustrazioni in SVG e' esattamente cio' che il protocollo
  vieta. Quindi C usa la fotografia reale come elemento pittorico e forme piatte
  contornate per il resto: il registro c'e', il tratto a mano no.

Uso: python3 design-demos/make_explore_demos.py
"""
import asyncio
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from PIL import Image
from playwright.async_api import async_playwright

from brand import tokens

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.join(os.path.dirname(HERE), "brand")
W, H = tokens.FORMATS["portrait"]

NAVY, BLUE, GREEN = "#0e0a48", "#4a3aff", "#43ef84"
# Accento usato in QUESTI caroselli. Non e' il verde: il logo NVIDIA porta il
# suo (#76b900) e due verdi diversi sulla stessa pagina si azzuffano — un logo
# di terzi non si ricolora, quindi cede il campo l'accento nostro. Sul navy si
# usa il cielo, sul chiaro il blu brand.
ACC_DARK = "#a9ecff"   # cielo, su fondi scuri
ACC_LIGHT = BLUE       # blu brand, su fondi chiari
SKY, INK = "#c5ebff", "#0e0a48"


# ---------------------------------------------------------------------------
# Trattamento della fotografia
# ---------------------------------------------------------------------------
def duotone(src, dark, light, out):
    """Mappa la luminanza della foto su due colori del brand.

    Perche': la foto a colori pieni porta dentro grigi neutri e (nell'altra
    candidata) un murale arancione, che sfondano il sistema cromatico. Il
    duotone conserva la struttura dell'immagine — cioe' l'informazione — e la
    riporta dentro la palette.
    """
    im = Image.open(src).convert("RGB")
    a = np.array(im).astype(float)
    lum = (0.2126 * a[:, :, 0] + 0.7152 * a[:, :, 1] + 0.0722 * a[:, :, 2]) / 255.0
    # leggera curva a S: apre le ombre senza slavare le alte luci
    lum = np.clip(lum ** 0.85, 0, 1)[:, :, None]
    d = np.array([int(dark[i:i + 2], 16) for i in (1, 3, 5)], dtype=float)
    l = np.array([int(light[i:i + 2], 16) for i in (1, 3, 5)], dtype=float)
    out_arr = d * (1.0 - lum) + l * lum
    Image.fromarray(np.clip(out_arr, 0, 255).astype(np.uint8), "RGB").save(out, quality=88)
    return out


def uri(path, mime=None):
    ext = os.path.splitext(path)[1].lower()
    mime = mime or {".jpg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}[ext]
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode("ascii"))


PHOTO_SRC = os.path.join(BRAND, "photo/nasa-columbia-supercomputer.jpg")
PHOTO_NAVY = os.path.join(HERE, "_photo-duo-navy.jpg")
PHOTO_SKY = os.path.join(HERE, "_photo-duo-sky.jpg")

CIRCUIT = tokens.data_uri("logo/circuit-motif-white.png")
GRAIN = uri(os.path.join(BRAND, "photo/grain.png"))

WM_WHITE = tokens.data_uri(tokens.LOGO["wordmark_white"])
WM_NAVY = tokens.data_uri(tokens.LOGO["wordmark_navy"])
NV_DARK = uri(os.path.join(BRAND, "third-party/nvidia-wordmark-dark.svg"))
NV_LIGHT = uri(os.path.join(BRAND, "third-party/nvidia-wordmark-light.svg"))

# ---------------------------------------------------------------------------
# Profondita': da cosa arriva
# ---------------------------------------------------------------------------
# Un campo di colore piatto con del testo sopra resta piatto per quanto bene sia
# composto. Qui la profondita' viene da quattro cose, tutte ancorate al brand e
# nessuna decorativa:
#   1. FOTOGRAFIA a piena pagina (in duotone) come fondo, non come francobollo
#   2. STRATIFICAZIONE: il testo scavalca il bordo dell'immagine, i piani si
#      sovrappongono invece di stare in fasce separate
#   3. MOTIVO A CIRCUITO come strato tonale a grande scala — e' la firma del
#      marchio, quindi usarlo come elemento di profondita' e' legittimo
#   4. GRANA di stampa a bassa opacita': materialita' senza gradienti finti
#
# Il gradiente c'e' solo dove il brand lo ha davvero (il cielo di newsai_bg),
# non come effetto aggiunto.

BASE = """
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#d7d7e2;}
.slide{width:%dpx;height:%dpx;position:relative;overflow:hidden;
       font-family:var(--font-body);}
.lbl{position:absolute;left:0;top:0;z-index:9;background:#fff;color:#0e0a48;
     font:700 19px/1 var(--font-body);padding:9px 15px;}
.bleed{position:absolute;}
.credit{position:absolute;font:400 15px/1.3 var(--font-body);}

/* Grana: uno strato sopra tutto, in multiply, quasi invisibile ma cambia la
   percezione di materia. Non intercetta il testo perche' e' pointer-events:none. */
.grain{position:absolute;inset:0;background-image:url(%s);background-size:160px;
  mix-blend-mode:multiply;opacity:.055;pointer-events:none;z-index:8;}
/* Il circuito del marchio come strato di profondita', non come ornamento. */
.circuit{position:absolute;pointer-events:none;}
""" % (W, H, GRAIN)


def page(label, css, inner):
    return ('<div class="slide">%s<div class="lbl">%s</div>%s</div>'
            % ("<style>%s</style>" % css if css else "", label, inner))


# ---------------------------------------------------------------------------
# A — Businessweek: la fotografia E' la pagina
# ---------------------------------------------------------------------------
# Prima: pagina bianca + fascia fotografica in mezzo = due piani separati, piatto.
# Ora: la foto occupa tutta la pagina, il titolo le sta SOPRA e la scavalca, e il
# blocco di testo bianco entra nell'immagine come un inserto tipografico da
# rivista. La profondita' viene dalla sovrapposizione, non da un'ombra.
A_CSS = """
.a{background:%(navy)s;}
.a .ph{position:absolute;inset:0;overflow:hidden;}
.a .ph img{width:100%%;height:100%%;object-fit:cover;display:block;}
/* Sfumatura di leggibilita': serve a far reggere il testo sulla foto, non a
   fare atmosfera. Senza, il titolo bianco su alte luci sparisce. */
.a .veil{position:absolute;inset:0;background:
  linear-gradient(180deg,rgba(14,10,72,.92) 0%%,rgba(14,10,72,.62) 34%%,
  rgba(14,10,72,.30) 52%%,rgba(14,10,72,.86) 84%%,rgba(14,10,72,.97) 100%%);}
.a .kicker{position:absolute;left:70px;top:58px;font:800 19px/1 var(--font-display);
  text-transform:uppercase;letter-spacing:.16em;color:%(acc)s;}
.a .head{position:absolute;left:70px;top:96px;width:1020px;
  font:800 76px/1.1 var(--font-display);letter-spacing:-.035em;color:#fff;}
.a .head em{font-style:normal;color:%(acc)s;}
/* L'inserto: un rettangolo bianco che entra nella fotografia, come nelle
   pagine dati del settimanale. E' il piano piu' avanzato della composizione. */
.a .inset{position:absolute;background:#fff;padding:34px 38px;}
.a .inset .lab{font:800 16px/1 var(--font-display);text-transform:uppercase;
  letter-spacing:.13em;color:%(blue)s;}
.a .inset .txt{margin-top:14px;font:400 25px/1.42 var(--font-body);color:#22244a;}
.a .inset .txt b{font-weight:700;color:%(navy)s;}
.a .huge{position:absolute;font:800 var(--fs)/.86 var(--font-display);
  letter-spacing:-.055em;color:#fff;}
.a .bar{position:absolute;height:26px;display:flex;}
.a .bar .seg{background:%(acc)s;}
.a .bar .rest{background:rgba(255,255,255,.26);}
.a .wm{position:absolute;left:70px;bottom:46px;width:168px;}
.a .fnote{position:absolute;right:70px;bottom:54px;font:700 19px/1 var(--font-body);
  color:rgba(255,255,255,.62);}
.a .cr{position:absolute;left:70px;bottom:96px;font:400 14px/1.3 var(--font-body);
  color:rgba(255,255,255,.5);}
""" % dict(navy=NAVY, blue=BLUE, acc=ACC_DARK)


def a_hook():
    return page("A · Businessweek — apertura", A_CSS, f"""
  <div class="a" style="position:absolute;inset:0;">
    <div class="ph"><img src="{uri(PHOTO_NAVY)}" alt="Sala macchine di un supercalcolatore"></div>
    <div class="veil"></div>
    <div class="kicker">Numeri della settimana</div>
    <div class="head">Il trimestre pi&#249; grande<br>della storia di Nvidia<br>
      <em>&#232; quasi tutto un<br>solo segmento</em></div>
    <img src="{NV_DARK}" style="position:absolute;left:70px;top:452px;height:36px;">
    <div class="inset" style="left:70px;right:150px;bottom:210px;">
      <div class="lab">Il dato in una riga</div>
      <div class="txt">Su <b>96,2 miliardi di dollari</b> di fatturato trimestrale,
        <b>89</b> arrivano dai data center. Non &#232; l'azienda che cresce:
        &#232; l'infrastruttura AI.</div>
    </div>
    <div class="cr">Foto: NASA Advanced Supercomputing Facility &#183; pubblico dominio</div>
    <img class="wm" src="{WM_WHITE}">
    <div class="fnote">01 / 06</div>
    <div class="grain"></div>
  </div>""")


def a_data():
    return page("A · Businessweek — dato", A_CSS, f"""
  <div class="a" style="position:absolute;inset:0;">
    <div class="ph"><img src="{uri(PHOTO_NAVY)}" alt="Sala macchine di un supercalcolatore"></div>
    <div class="veil" style="background:linear-gradient(180deg,rgba(14,10,72,.95) 0%,rgba(14,10,72,.55) 46%,rgba(14,10,72,.93) 78%,rgba(14,10,72,.98) 100%);"></div>
    <div class="kicker">Da dove arriva</div>
    <div class="head" style="font-size:60px;width:900px;">89 miliardi su 96,2<br>
      vengono dai <em>data center</em></div>
    <!-- La cifra scavalca il bordo destro: il taglio suggerisce che continui
         oltre la pagina, ed e' cio' che crea profondita' senza ombre. -->
    <div class="huge" style="--fs:330px;left:52px;top:352px;">92,5<span
        style="font-size:118px;">%</span></div>
    <div class="bar" style="left:70px;right:-60px;top:756px;">
      <div class="seg" style="width:92.5%;"></div><div class="rest" style="flex:1;"></div>
    </div>
    <div style="position:absolute;left:70px;top:794px;font:800 17px/1 var(--font-display);
         letter-spacing:.1em;text-transform:uppercase;color:{ACC_DARK};">Data center</div>
    <div class="inset" style="left:70px;right:150px;bottom:200px;">
      <div class="lab">Cosa significa</div>
      <div class="txt">Il segmento &#232; cresciuto del <b>117% anno su anno</b>.
        Per la maggior parte delle aziende quella capacit&#224; si affitta da cloud
        e partner terzi, non si compra.</div>
    </div>
    <img src="{NV_DARK}" style="position:absolute;right:70px;top:112px;height:32px;">
    <div class="cr">Foto: NASA Advanced Supercomputing Facility &#183; pubblico dominio</div>
    <img class="wm" src="{WM_WHITE}">
    <div class="fnote">04 / 06</div>
    <div class="grain"></div>
  </div>""")


# ---------------------------------------------------------------------------
# B — Lupi / Data Humanism: via la strip, dentro il circuito
# ---------------------------------------------------------------------------
# La barra colorata in testa e' stata rimossa: era una fascia che non faceva
# altro che contenere il logo. Il marchio ora sta nella composizione, in basso,
# accanto alla legenda che gli appartiene.
# La profondita' viene dal motivo a circuito a grande scala dietro il grafico —
# lo stesso glifo di cui i nodi sono fatti, quindi il fondo e il primo piano
# sono la stessa forma a due scale. E dal gradiente cielo, che il brand ha
# davvero, invece di un bianco piatto.
B_CSS = """
.b{background:linear-gradient(178deg,#eaf6ff 0%%,#f8fbff 46%%,#eef2ff 100%%);}
/* Il circuito, enorme e appena percettibile: e' il fondo su cui i nodi si
   leggono come dettaglio dello stesso sistema. */
/* Il circuito e' bianco con alpha: per tingerlo del blu del brand si usa una
   maschera CSS, non un filtro. `brightness(0) saturate(0)` lo rendeva grigio
   neutro, cioe' fuori palette: erano macchie, non il motivo del marchio. */
.b .circ{position:absolute;background:%(blue)s;opacity:.12;
  -webkit-mask:url(%(circ)s) no-repeat center/contain;
  mask:url(%(circ)s) no-repeat center/contain;}
.b .t{position:absolute;left:76px;top:120px;width:900px;
  font:800 66px/1.06 var(--font-display);letter-spacing:-.028em;color:%(navy)s;}
.b .t span{color:%(blue)s;}
.b .sub{position:absolute;left:76px;width:800px;font:400 25px/1.44 var(--font-body);
  color:#4a4770;}
.b .plot{position:absolute;left:76px;right:76px;}
.b .stem{position:absolute;width:3px;background:%(blue)s;bottom:0;opacity:.55;}
/* I nodi hanno un rilievo reale: un anello di superficie piu' un'ombra corta.
   Non e' una card con box-shadow: e' un segno che sta sopra il piano. */
.b .node{position:absolute;border-radius:50%%;border:4px solid %(blue)s;
  background:#fbfdff;box-shadow:0 8px 18px -6px rgba(14,10,72,.34);}
.b .node.full{background:%(blue)s;box-shadow:inset 0 0 0 4px #fbfdff,
  0 10px 22px -6px rgba(74,58,255,.55);}
.b .nlab{position:absolute;font:800 29px/1.14 var(--font-display);color:%(navy)s;
  text-align:center;letter-spacing:-.01em;}
.b .nsub{position:absolute;font:700 19px/1.24 var(--font-body);color:#6d6a94;
  text-align:center;}
.b .legend{position:absolute;left:76px;right:76px;background:rgba(255,255,255,.72);
  border:1px solid rgba(14,10,72,.10);border-radius:14px;padding:24px 26px;
  box-shadow:0 14px 34px -18px rgba(14,10,72,.30);}
.b .lg{display:flex;gap:34px;flex-wrap:wrap;}
.b .lgi{display:flex;align-items:center;gap:11px;font:400 20px/1.3 var(--font-body);
  color:#4a4770;}
.b .lgk{font-weight:700;color:%(navy)s;}
.b .wm{position:absolute;left:76px;bottom:48px;width:164px;}
.b .fnote{position:absolute;right:76px;bottom:56px;font:700 19px/1 var(--font-body);
  color:#9d9ac0;}
""" % dict(navy=NAVY, blue=BLUE, circ=CIRCUIT)

B_DATA = [
    ("96,2 mld", "fatturato", "trimestre", 300, True),
    ("89 mld", "data center", "+117% a/a", 340, True),
    ("+9%", "titolo", "una seduta", 150, True),
    ("~440 mld", "capitalizz.", "in un giorno", 260, True),
    ("+70%", "atteso", "FY2028", 120, False),
]


def b_glyphs():
    out = ""
    step = 205
    for i, (val, lab, sub, stem, full) in enumerate(B_DATA):
        x = 26 + i * step
        d = 60 if full else 54
        out += f"""
      <div class="stem" style="left:{x + d // 2 - 1}px;height:{stem}px;"></div>
      <div class="node{' full' if full else ''}" style="left:{x}px;
           bottom:{stem - d // 2}px;width:{d}px;height:{d}px;"></div>
      <div class="nlab" style="left:{x - 62}px;bottom:{stem + d // 2 + 74}px;width:{d + 124}px;">{val}</div>
      <div class="nsub" style="left:{x - 62}px;bottom:{stem + d // 2 + 16}px;width:{d + 124}px;">{lab}<br>{sub}</div>"""
    return out


def b_hook():
    return page("B · Lupi / Data Humanism — apertura", B_CSS, f"""
  <div class="b" style="position:absolute;inset:0;">
    <div class="circ" style="right:-150px;top:-40px;width:820px;height:1330px;"></div>
    <div class="circ" style="left:-230px;bottom:-190px;width:620px;height:1005px;
         transform:scaleX(-1);opacity:.07;"></div>
    <div class="t">Cinque numeri,<br>un solo <span>segnale</span></div>
    <div class="sub" style="top:296px;">Il trimestre di Nvidia raccontato con
      l'alfabeto del nostro marchio: ogni nodo &#232; una cifra, ogni asta la
      sua crescita.</div>
    <img src="{NV_LIGHT}" style="position:absolute;right:76px;top:126px;height:32px;">
    <div class="plot" style="top:540px;height:430px;">{b_glyphs()}</div>
    <div class="legend" style="top:1046px;">
      <div class="lg">
        <div class="lgi"><span style="display:inline-block;width:22px;height:22px;
          border-radius:50%;background:{BLUE};box-shadow:inset 0 0 0 3px #fff;"></span>
          <span><span class="lgk">cerchio pieno</span> &#183; ricavo realizzato</span></div>
        <div class="lgi"><span style="display:inline-block;width:22px;height:22px;
          border-radius:50%;border:3px solid {BLUE};"></span>
          <span><span class="lgk">cerchio vuoto</span> &#183; ricavo atteso</span></div>
        <div class="lgi"><span style="display:inline-block;width:3px;height:26px;
          background:{BLUE};"></span>
          <span><span class="lgk">asta</span> &#183; pi&#249; alta = crescita maggiore</span></div>
      </div>
      <div style="margin-top:16px;font:400 18px/1.45 var(--font-body);color:#8b88ad;">
        L'alfabeto &#232; costruito sul nodo del marchio Digitiamo, lo stesso motivo
        che vedi in trasparenza sul fondo. La legenda non &#232; opzionale.</div>
    </div>
    <img class="wm" src="{WM_NAVY}">
    <div class="fnote">01 / 06</div>
    <div class="grain"></div>
  </div>""")


def b_data():
    return page("B · Lupi / Data Humanism — dato", B_CSS, f"""
  <div class="b" style="position:absolute;inset:0;">
    <div class="circ" style="right:-210px;top:250px;width:900px;height:1460px;opacity:.10;"></div>
    <div class="t" style="top:118px;font-size:58px;">Il 92,5% del trimestre<br>
      &#232; <span>un solo segmento</span></div>
    <div class="sub" style="top:284px;width:760px;">Ogni nodo &#232; un miliardo di
      dollari. Quelli pieni sono data center.</div>
    <img src="{NV_LIGHT}" style="position:absolute;right:76px;top:124px;height:30px;">
    <div style="position:absolute;left:76px;top:400px;width:1048px;
         display:grid;grid-template-columns:repeat(16,1fr);gap:11px;">
      {''.join('<div style="width:100%%;aspect-ratio:1;border-radius:50%%;%s"></div>'
               % ('background:%s;box-shadow:0 6px 14px -5px rgba(74,58,255,.5);' % BLUE if i < 89
                  else 'border:3px solid #c3bfe0;') for i in range(96))}
    </div>
    <div class="legend" style="top:900px;">
      <div class="lg">
        <div class="lgi"><span style="display:inline-block;width:20px;height:20px;
          border-radius:50%;background:{BLUE};"></span>
          <span><span class="lgk">89 nodi pieni</span> &#183; data center</span></div>
        <div class="lgi"><span style="display:inline-block;width:20px;height:20px;
          border-radius:50%;border:3px solid #c3bfe0;"></span>
          <span><span class="lgk">7 nodi vuoti</span> &#183; tutto il resto</span></div>
      </div>
      <div style="margin-top:14px;font:400 19px/1.5 var(--font-body);color:#4a4770;
           max-width:840px;">Non &#232; Nvidia che cresce: &#232; l'infrastruttura AI.
        Per la maggior parte delle aziende quell'accesso passer&#224; da cloud e
        partner terzi.</div>
    </div>
    <img class="wm" src="{WM_NAVY}">
    <div class="fnote">04 / 06</div>
    <div class="grain"></div>
  </div>""")


# ---------------------------------------------------------------------------
# C — Holmes / Explanation Graphics: stampa a registro, non rettangoli piatti
# ---------------------------------------------------------------------------
# La fascia in testa e' stata sostituita da un'etichetta che sta nella
# composizione. La profondita' arriva dall'ombra dura a registro — quella dei
# blocchi tipografici stampati con la lastra leggermente fuori registro — che e'
# esattamente il linguaggio di stampa dell'epoca di Holmes, non un box-shadow
# morbido da interfaccia.
C_CSS = """
.c{background:%(sky)s;}
.c .circ{position:absolute;left:-160px;bottom:-180px;width:680px;opacity:.20;
  filter:brightness(0) saturate(0);}
.c .tag{position:absolute;left:56px;top:52px;background:%(navy)s;color:#fff;
  font:800 24px/1 var(--font-display);text-transform:uppercase;letter-spacing:.09em;
  padding:15px 22px;box-shadow:10px 10px 0 0 %(acc)s;}
.c .t{position:absolute;left:56px;right:56px;
  font:800 64px/1.06 var(--font-display);letter-spacing:-.03em;color:%(navy)s;}
.c .t u{text-decoration:none;border-bottom:10px solid %(acc)s;}
.c .say{position:absolute;left:56px;font:400 25px/1.42 var(--font-body);color:#22244a;}
.c .say b{font-weight:700;color:%(navy)s;}
/* Blocchi con ombra dura a registro: il piano si stacca senza sfumature. */
.c .stack{position:absolute;display:flex;align-items:flex-end;gap:16px;}
.c .blk{border:5px solid %(navy)s;background:%(blue)s;box-shadow:8px 8px 0 0 %(navy)s;}
.c .blk.ghost{background:transparent;box-shadow:8px 8px 0 0 rgba(14,10,72,.22);}
.c .cap{position:absolute;font:800 21px/1.2 var(--font-display);color:%(navy)s;
  text-transform:uppercase;letter-spacing:.05em;}
/* La foto entra come blocco stampato, con lo stesso registro dei blocchi dati. */
.c .photo{position:absolute;overflow:hidden;border:5px solid %(navy)s;
  box-shadow:12px 12px 0 0 %(navy)s;}
.c .photo img{width:100%%;height:100%%;object-fit:cover;display:block;}
.c .wm{position:absolute;left:56px;bottom:44px;width:158px;}
.c .fnote{position:absolute;right:56px;bottom:50px;font:800 21px/1 var(--font-display);
  color:%(navy)s;}
.c .cr{position:absolute;font:400 14px/1.3 var(--font-body);color:#5b5f8f;}
""" % dict(navy=NAVY, blue=BLUE, acc=ACC_LIGHT, sky=SKY)


def c_hook():
    blks = "".join('<div class="blk" style="width:78px;height:%dpx;"></div>' % h
                   for h in (56, 92, 136, 192, 262))
    return page("C · Holmes / Explanation Graphics — apertura", C_CSS, f"""
  <div class="c" style="position:absolute;inset:0;">
    <img class="circ" src="{CIRCUIT}" alt="">
    <div class="tag">Spiegato semplice</div>
    <img src="{NV_LIGHT}" style="position:absolute;right:56px;top:62px;height:36px;">
    <div class="t" style="top:184px;">Nvidia guadagna<br>come una <u>centrale</u>,<br>
      non come un negozio</div>
    <div class="say" style="top:430px;width:620px;">Non vende un pezzo alla volta:
      vende la corrente che fa girare tutto il resto.</div>
    <div class="stack" style="left:56px;top:580px;">{blks}</div>
    <div class="cap" style="left:56px;top:880px;">Cinque trimestri, un solo motore</div>
    <div class="photo" style="left:56px;right:68px;top:930px;height:330px;">
      <img src="{uri(PHOTO_SKY)}" alt="Sala macchine di un supercalcolatore">
    </div>
    <div class="cr" style="left:56px;top:1290px;">Foto: NASA Advanced Supercomputing
      Facility &#183; pubblico dominio</div>
    <img class="wm" src="{WM_NAVY}">
    <div class="fnote">01 / 06</div>
    <div class="grain"></div>
  </div>""")


def c_data():
    full = "".join('<div class="blk" style="width:58px;height:128px;"></div>' for _ in range(9))
    return page("C · Holmes / Explanation Graphics — dato", C_CSS, f"""
  <div class="c" style="position:absolute;inset:0;">
    <img class="circ" src="{CIRCUIT}" alt="">
    <div class="tag">Il dato, senza giri</div>
    <img src="{NV_LIGHT}" style="position:absolute;right:56px;top:62px;height:36px;">
    <div class="t" style="top:184px;font-size:58px;">Su dieci euro incassati,<br>
      <u>nove sono data center</u></div>
    <div class="stack" style="left:56px;top:400px;">{full}
      <div class="blk ghost" style="width:58px;height:128px;"></div></div>
    <div class="cap" style="left:56px;top:568px;">9 pieni su 10 &nbsp;&#183;&nbsp;
      89 di 96,2 miliardi</div>
    <div class="say" style="top:626px;width:980px;">Il segmento data center &#232;
      cresciuto del <b>117% in un anno</b>. Tutto il resto dell'azienda &#8212;
      gaming, automotive, professionale &#8212; sta in quell'unico blocco vuoto.</div>
    <div class="photo" style="left:56px;right:68px;top:790px;height:340px;">
      <img src="{uri(PHOTO_SKY)}" alt="Sala macchine di un supercalcolatore">
    </div>
    <div class="say" style="top:1170px;width:940px;font-size:23px;">Per la maggior
      parte delle aziende quella capacit&#224; si affitta, non si compra.</div>
    <img class="wm" src="{WM_NAVY}">
    <div class="fnote">04 / 06</div>
    <div class="grain"></div>
  </div>""")


DIRECTIONS = {
    "X-A-businessweek": [a_hook, a_data],
    "X-B-lupi-datahumanism": [b_hook, b_data],
    "X-C-holmes-explanation": [c_hook, c_data],
}


async def main():
    print("trattamento fotografia (duotone sulla palette):")
    duotone(PHOTO_SRC, NAVY, "#dbe6ff", PHOTO_NAVY)
    duotone(PHOTO_SRC, "#123a6b", SKY, PHOTO_SKY)
    print("   _photo-duo-navy.jpg  _photo-duo-sky.jpg")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        pg = await browser.new_page(viewport={"width": W, "height": H})
        for name, fns in DIRECTIONS.items():
            body = "".join(fn() for fn in fns)
            html = ('<!doctype html><html lang="it"><head><meta charset="utf-8">'
                    '<title>%s</title><style>%s\n%s</style></head><body>%s</body></html>'
                    % (name, tokens.build_css(), BASE, body))
            with open(os.path.join(HERE, "%s.html" % name), "w", encoding="utf-8") as f:
                f.write(html)
            await pg.set_content(html, wait_until="load")
            await pg.evaluate("document.fonts.ready")
            for i, el in enumerate(await pg.query_selector_all(".slide"), start=1):
                await el.screenshot(path=os.path.join(HERE, "%s_%d.png" % (name, i)))
            # Gli strati decorativi (circuito, grana) escono dal bordo DI
            # PROPOSITO e sono gia' tagliati da overflow:hidden. Contarli
            # segnalerebbe uno sforamento che non esiste, quindi si misura solo
            # il contenuto: testo, immagini di contenuto, blocchi dati.
            bad = await pg.evaluate("""() => {
              const skip = /circ|grain|veil|\\bph\\b/;
              return Array.from(document.querySelectorAll('.slide')).filter((s) => {
                const top = s.getBoundingClientRect().top;
                return Array.from(s.querySelectorAll('*')).some((e) => {
                  const cn = (e.className && e.className.toString) ? e.className.toString() : '';
                  if (skip.test(cn)) return false;
                  const r = e.getBoundingClientRect();
                  return (r.bottom - top) > s.clientHeight + 1 || r.width > s.clientWidth + 1;
                });
              }).length;
            }""")
            print("  %-26s %d pagine%s" % (name, len(fns), "  SFORA" if bad else ""))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
