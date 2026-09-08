# -*- coding: utf-8 -*-
"""Token di brand Digitiamo — UNICA fonte di verita' per colori, font e formati.

I valori qui NON sono scelte di design fatte a mano: sono estratti dagli asset
Canva reali del brand (vedi ../brand-spec.md per la provenienza di ognuno).
Chi modifica questo file sta modificando il brand — aggiornare anche brand-spec.md.

Consumatori:
  - build_css()  -> CSS inline nei template (nessun artefatto su disco)
  - generate_html.py (palette del report PDF)
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# PALETTE — estratta dai PNG di sfondo Canva (conteggio pixel dominanti)
# ---------------------------------------------------------------------------
COLORS = {
    # Primari
    "blue": "#4a3aff",       # blu brand: 44.8% di newsai_bg, 81.8% di newsai_cover_bg
    "navy": "#0e0a48",       # navy profondo: 85.3% di webinar_bg, 17.3% di hiring_bg
    "green": "#43ef84",      # verde accento: 4.1% di hiring_bg (contesti hiring/energia)
    "white": "#ffffff",
    # Tinte derivate (usate per il motivo circuito e i pannelli)
    "blue_tint": "#6052ff",  # traccia circuito su fondo blu (12.3-12.4%)
    "navy_tint": "#2c285e",  # traccia circuito su fondo navy (13.3%)
    # Gradiente cielo (dall'alto verso il basso) di newsai_bg
    # Azzurro pallido usato come INCHIOSTRO su fondo scuro (accento di testo su
    # navy e blu). NON e' il gradiente del campo cielo: quello vive in
    # brand/make_editorial_bg.py (SKY_TOP/SKY_BOTTOM, campionati da newsai_bg) ed
    # e' cotto dentro editorial_sky.png.
    #
    # Prima questo token si chiamava `sky_top` e ce n'erano altri due, `sky_mid`
    # e `sky_bottom`, mai usati: dichiaravano il gradiente una seconda volta con
    # valori diversi da quelli reali (#d0f0ff invece di #c5ebff). Il PNG e' la
    # verita' — il render usa l'immagine, non i token — quindi le slide erano
    # giuste, ma la discrepanza ha fatto diagnosticare a qualcuno un refuso che
    # non c'era. Un valore duplicato in due file e' un bug che aspetta.
    "sky_ink": "#d0f0ff",
    # Testo — valori tarati sul renderer social-ped (leggibilita' verificata)
    "text_on_blue": "#eef0ff",   # corpo su pannello blu
    "text_muted_navy": "#b9c0f5",  # metadati su navy
    "text_muted_soft": "#c7ccf0",  # ruoli/didascalie su navy
    "accent_ring": "#2e7bf0",      # anello avatar / accento secondario
    # Tint chiare per superfici su bianco (report PDF interno)
    "blue_soft": "#717ffe",  # blu secondario, testo di servizio nel report
    "tint": "#ebeefc",
}

# ---------------------------------------------------------------------------
# TIPOGRAFIA — i font REALI del brand, non sostituti
# ---------------------------------------------------------------------------
# Montserrat = display (titoli, numeri, etichette). Lato = corpo.
# I .woff2 sono in brand/fonts/ e vengono incorporati in base64 nei template:
# nessuna dipendenza di rete al momento del rendering.
FONTS = {
    "display": "Montserrat",
    "body": "Lato",
    "display_stack": "'Montserrat', 'Helvetica Neue', Arial, sans-serif",
    "body_stack": "'Lato', 'Helvetica Neue', Arial, sans-serif",
}

FONT_FILES = {
    ("Montserrat", 800): "fonts/Montserrat-800.woff2",
    ("Montserrat", 700): "fonts/Montserrat-700.woff2",
    ("Lato", 700): "fonts/Lato-700.woff2",
    ("Lato", 400): "fonts/Lato-400.woff2",
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
    # Il marchio VETTORIALE ufficiale, fornito dal team design l'8 settembre
    # 2026. E' la sorgente: un solo file per tutti i colori, perche' il fill si
    # sovrascrive via CSS (la classe `.cls-1`).
    #
    # Non e' ancora usato dal renderer, ed e' voluto: il marchio e' COTTO dentro
    # gli sfondi editoriali (editorial_navy/blue), non disegnato dal layout.
    # Passare al vettore vuol dire rigenerare gli sfondi con
    # make_editorial_bg.py, quindi cambiare l'aspetto di ogni slide — un lavoro
    # deliberato, non un effetto collaterale. Gli asset gia' pubblicati non
    # devono cambiare.
    #
    # Verificato che sia lo stesso marchio dei PNG: ritagliati sull'inchiostro i
    # rapporti sono 3.561 (PNG) e 3.508 (SVG), e le sagome si sovrappongono al
    # 91,2%. Lo scarto e' l'antialiasing del PNG, che era stato ESTRATTO dagli
    # sfondi rasterizzati.
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
    }[ext]
    return "data:%s;base64,%s" % (mime, raw)


def font_face_css():
    """@font-face con i woff2 del brand incorporati — zero richieste di rete."""
    blocks = []
    for (family, weight), rel in FONT_FILES.items():
        blocks.append(
            "@font-face{font-family:'%s';font-style:normal;font-weight:%d;"
            "font-display:block;src:url(%s) format('woff2');}"
            % (family, weight, data_uri(rel))
        )
    return "\n".join(blocks)


def css_variables():
    """La palette come custom properties CSS."""
    lines = [":root{"]
    for name, value in COLORS.items():
        lines.append("  --c-%s: %s;" % (name.replace("_", "-"), value))
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
  /* la dimensione la impone il template: i formati sono due (4:5 e 1:1) */
}
.slide__bg {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  display: block;
  object-fit: cover;
}
.slide__layer { position: relative; width: 100%; height: 100%; }

/* Marchio — SEMPRE l'asset reale, mai testo. Vedi brand-spec.md §Divieti. */
.wordmark { position: absolute; display: block; }
.brand-icon { position: absolute; display: block; }

/* Tipografia */
.display {
  font-family: var(--font-display);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.5px;
}
.display--700 { font-weight: 700; }
.eyebrow {
  font-family: var(--font-display);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.5px;
}
.body {
  font-family: var(--font-body);
  font-weight: 400;
  line-height: 1.34;
}
.body--bold { font-weight: 700; }

/* Auto-fit: gli elementi .fit con data-maxh vengono rimpiccioliti fino a
   rientrare nel box. Portato dal renderer social-ped, dove risolve il
   troncamento silenzioso dei titoli lunghi. */
.fit { display: block; }
"""


if __name__ == "__main__":
    # Utile solo per ispezione manuale: i template chiamano build_css() e la
    # inline-ano, quindi non c'e' nessun .css da tenere sincronizzato su disco.
    print(build_css()[:2000])
