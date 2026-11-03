# -*- coding: utf-8 -*-
"""Token di brand Digitiamo — UNICA fonte di verita' per colori, font e formati.

I valori vengono dal linguaggio di brand approvato il 2 novembre 2026 (i 12
post di riferimento, vedi ../brand-spec.md per la provenienza di ognuno).
Chi modifica questo file sta modificando il brand — aggiornare anche brand-spec.md.

Consumatori:
  - build_css()  -> CSS inline nei template dei post (nessun artefatto su disco)
  - generate_html.py (solo i font legacy del report PDF interno)
"""
import base64
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# PALETTE — linguaggio di brand approvato il 2 novembre 2026 (brand-spec.md §3)
# ---------------------------------------------------------------------------
# Sostituisce la palette ricavata dagli sfondi Canva (#4a3aff, #0e0a48, il verde
# #43ef84 e il cielo): quella resta solo negli asset gia' pubblicati.
COLORS = {
    "primary": "#3E00EA",    # blu Digitiamo: accento su chiaro, testa del gradiente
    "ink": "#070011",        # quasi nero: testo su chiaro, coda del gradiente
    "night": "#1C073A",      # notte: superfici scure piene (cerchi, riquadri)
    "lavender": "#717FFE",   # accento su scuro, virgolette delle citazioni
    "mist": "#EBEEFC",       # testo secondario e occhielli su scuro
    "paper": "#F4F5FA",      # fondo chiaro, testo principale su scuro
    "green": "#00DC93",      # SOLO segnali positivi (un guadagno) e bottone CTA
    # Grigi di servizio dei mock approvati (Chiaro, Interna): corpo e note su chiaro.
    "body_light": "#3A3550",
    "muted_light": "#5B5670",
}

# L'unico gradiente del sistema, per i post scuri.
GRADIENT = "linear-gradient(180deg,#3E00EA 0%,#070011 100%)"

# ---------------------------------------------------------------------------
# TIPOGRAFIA — Sora sola, 400/600/700
# ---------------------------------------------------------------------------
# I .woff2 vengono da @fontsource/sora 5.2.8 (OFL, licenza in fonts/Sora-OFL.txt)
# e sono incorporati in base64: nessuna dipendenza di rete al momento del
# rendering. Due sottoinsiemi per peso, come li distribuisce Google Fonts:
# `latin` copre l'italiano, `latin-ext` il resto (nomi propri stranieri).
FONTS = {
    "display": "Sora",
    "body": "Sora",
    "display_stack": "'Sora', 'Helvetica Neue', Arial, sans-serif",
    "body_stack": "'Sora', 'Helvetica Neue', Arial, sans-serif",
}

_LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
          "U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,"
          "U+2215,U+FEFF,U+FFFD")
_LATIN_EXT = ("U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,"
              "U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,"
              "U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF")

# (famiglia, peso, file, unicode-range)
FONT_FILES = [
    ("Sora", w, "fonts/sora-%s-%d-normal.woff2" % (sub, w), rng)
    for w in (400, 600, 700)
    for sub, rng in (("latin", _LATIN), ("latin-ext", _LATIN_EXT))
]

# Montserrat + Lato restano SOLO per il report PDF interno (generate_html.py),
# che non e' un post e non e' stato ridisegnato. Non usarli nelle grafiche.
LEGACY_FONT_FILES = [
    ("Montserrat", 800, "fonts/Montserrat-800.woff2", None),
    ("Montserrat", 700, "fonts/Montserrat-700.woff2", None),
    ("Lato", 700, "fonts/Lato-700.woff2", None),
    ("Lato", 400, "fonts/Lato-400.woff2", None),
]
LEGACY_BODY_STACK = "'Lato', 'Helvetica Neue', Arial, sans-serif"

# La palette del sistema precedente (ricavata dagli sfondi Canva), SOLO per il
# report PDF interno, che importa questi nomi da build_report.py. Le grafiche
# dei post non la usano: per loro vale COLORS.
LEGACY_COLORS = {
    "blue": "#4a3aff", "navy": "#0e0a48", "green": "#43ef84", "white": "#ffffff",
    "blue_soft": "#717ffe", "tint": "#ebeefc",
}

# ---------------------------------------------------------------------------
# FORMATI — quelli dei template Canva reali
# ---------------------------------------------------------------------------
FORMATS = {
    "portrait": (1200, 1500),  # 4:5 — LinkedIn/Instagram feed (news, carosello, webinar)
    "square": (1200, 1200),    # 1:1 — hiring
    "a4": (794, 1123),         # report PDF interno @96dpi
}

# ---------------------------------------------------------------------------
# ASSET
# ---------------------------------------------------------------------------
LOGO = {
    # Il marchio VETTORIALE ufficiale (team design, 8 settembre 2026). Dal
    # linguaggio del 2 novembre 2026 e' l'UNICA sorgente del marchio nei post:
    # il layout lo disegna con `wordmark_uri(colore)` — bianco su scuro e foto,
    # blu #3E00EA su chiaro. Gli sfondi non hanno piu' il marchio incorporato.
    #
    # I PNG qui sotto restano per il report PDF interno e per la storia: erano
    # stati ESTRATTI dagli sfondi Canva (sagome sovrapposte al 91,2% col vettore).
    "wordmark_vector": "logo/digitiamo-wordmark.svg",

    "wordmark_white": "logo/digitiamo-wordmark-white.png",  # 245x78, alpha
    "icon_news_white": "logo/icon-news-white.png",          # 200x181, alpha
    "icon_webinar_white": "logo/icon-webinar-white.png",    # 154x104, alpha
    # Varianti scure per i fondi chiari, derivate dall'alpha delle bianche
    # (make_editorial_bg.py). Sono DERIVAZIONI, non versioni ufficiali.
    "wordmark_navy": "logo/digitiamo-wordmark-navy.png",
    "wordmark_blue": "logo/digitiamo-wordmark-blue.png",
    "icon_news_navy": "logo/icon-news-navy.png",
    "icon_news_blue": "logo/icon-news-blue.png",
}

# Marchi di terze parti, per le slide che nominano un prodotto riconoscibile
# (vedi brand/third-party/README.md: il protocollo asset impone che un design
# che nomina un prodotto ne mostri il logo ufficiale). Uso editoriale, mai
# ricolorati: il layout li mostra su una pillola bianca, cosi' reggono il
# contrasto su qualunque superficie invece di essere ridisegnati.
THIRD_PARTY = {
    "openai": "third-party/openai-light.svg",
    "anthropic": "third-party/anthropic-light.svg",
    "gemini": "third-party/gemini-light.svg",
    "meta": "third-party/meta-light.svg",
    "nvidia": "third-party/nvidia-wordmark-light.svg",
    "qwen": "third-party/qwen-light.svg",
    "zhipu": "third-party/zhipu-light.svg",
    "eu": "third-party/eu-flag.svg",
}

# SUPERATI dal linguaggio del 2 novembre 2026: nessun layout li usa piu'.
# Restano nella repo perche' gli asset gia' pubblicati in settimane/ ne
# derivano, e la storia deve restare ricostruibile (make_editorial_bg.py).
BACKGROUNDS = {
    # Asset Canva originali
    "news": "bg/newsai_bg.png",
    "news_cover": "bg/newsai_cover_bg.png",
    "webinar": "bg/webinar_bg.png",
    "hiring": "bg/hiring_bg.png",
    # Campi editoriali pieni, per la direzione B — derivati da webinar_bg
    # (icona videocamera rimossa, badge News AI al suo posto).
    # Rigenerabili con: python3 brand/make_editorial_bg.py
    "editorial_navy": "bg/editorial_navy.png",
    "editorial_blue": "bg/editorial_blue.png",
    # Campo chiaro: gradiente cielo + filigrana a circuito. Non ha marchio ne'
    # badge incorporati (li mette il layout, in variante scura).
    "editorial_sky": "bg/editorial_sky.png",
}


def data_uri(rel_path):
    """Legge un asset di brand e lo restituisce come data: URI base64.

    Incorporare invece di linkare e' deliberato: il rendering headless non deve
    dipendere dalla rete ne' dalla directory di lavoro corrente.
    """
    path = os.path.join(HERE, rel_path)
    with open(path, "rb") as f:
        raw = base64.b64encode(f.read()).decode("ascii")
    ext = os.path.splitext(rel_path)[1].lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".woff2": "font/woff2",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
    }[ext]
    return "data:%s;base64,%s" % (mime, raw)


def font_face_css(files=None):
    """@font-face con i woff2 incorporati — zero richieste di rete."""
    blocks = []
    for family, weight, rel, rng in (files or FONT_FILES):
        blocks.append(
            "@font-face{font-family:'%s';font-style:normal;font-weight:%d;"
            "font-display:block;src:url(%s) format('woff2');%s}"
            % (family, weight, data_uri(rel),
               "unicode-range:%s;" % rng if rng else ""))
    return "\n".join(blocks)


def wordmark_uri(fill):
    """Il marchio vettoriale in un colore, come data: URI.

    Il fill si scrive come attributo e lo <style> interno si toglie: un SVG
    usato come <img> non eredita il CSS della pagina, quindi la classe `.cls-1`
    non si puo' sovrascrivere da fuori.
    """
    with open(os.path.join(HERE, LOGO["wordmark_vector"]), encoding="utf-8") as f:
        svg = f.read()
    svg = re.sub(r"<defs>.*?</defs>", "", svg, flags=re.S)
    svg = svg.replace('class="cls-1"', 'fill="%s"' % fill)
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("ascii")


# La barratura a mano del sito (digitiamo-site/assets/barratura-manuale-blu.svg,
# tratto #60A5FA), in copia con preserveAspectRatio="none" perche' si stiri
# sulla parola. Il colore vive nel file: non si ridichiara come token.
STRIKE = "strike/barratura.svg"


def css_variables():
    """La palette come custom properties CSS."""
    lines = [":root{"]
    for name, value in COLORS.items():
        lines.append("  --c-%s: %s;" % (name.replace("_", "-"), value))
    lines.append("  --gradient: %s;" % GRADIENT)
    lines.append("  --font-display: %s;" % FONTS["display_stack"])
    lines.append("  --font-body: %s;" % FONTS["body_stack"])
    lines.append("}")
    return "\n".join(lines)


def build_css():
    """CSS di brand completo: @font-face incorporati + variabili + primitive condivise.

    Questo e' l'unico posto dove vivono i token visivi condivisi fra i template.
    Prima erano copia-incollati (e divergenti) fra carousel_slides.html e
    single_images.html.
    """
    return "\n".join([
        "/* Generato da brand/tokens.py — inline, nessun file su disco. */",
        font_face_css(),
        "",
        css_variables(),
        "",
        _PRIMITIVES,
    ])


# Primitive condivise dai template delle slide. Deliberatamente minimali:
# il layout specifico di ogni tipo di slide sta nel suo template, qui c'e'
# solo cio' che DEVE restare identico fra i formati.
_PRIMITIVES = """
* { margin: 0; padding: 0; box-sizing: border-box; }

.slide {
  position: relative;
  overflow: hidden;
  font-family: var(--font-body);
  /* la dimensione la impone il template */
}

/* Tipografia: Sora sola. Titoli 700 a manifesto, interlinea stretta e
   spaziatura negativa; occhielli 600 maiuscoli e spaziati (mock approvati). */
.display {
  font-family: var(--font-display);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.03em;
}
.eyebrow {
  font-family: var(--font-display);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 4px;
}
.body {
  font-family: var(--font-body);
  font-weight: 400;
  line-height: 1.35;
}
.body--bold { font-weight: 600; }

/* La barratura a mano: la parola resta leggibile, il tratto le passa sopra. */
.strike { position: relative; display: inline-block; }
.strike img { position: absolute; left: -4%; top: 30%; width: 108%; height: 50%; }

/* Auto-fit: gli elementi .fit con data-maxh vengono rimpiccioliti fino a
   rientrare nel box (render.py). */
.fit { display: block; }
"""


if __name__ == "__main__":
    print(build_css()[:2000])
