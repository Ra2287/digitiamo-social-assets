# -*- coding: utf-8 -*-
"""Genera gli sfondi editoriali per la direzione B ("Pannello pieno").

Perche' servono: la direzione B vuole un campo pieno senza la fascia cielo, ma
fra gli asset Canva non esiste uno sfondo del genere. `webinar_bg.png` e' quasi
giusto (navy pieno + filigrana a circuito + wordmark incorporato) ma porta
incorporata l'**icona videocamera** del Webinar, che su un carosello editoriale
e' il badge di categoria sbagliato.

Cosa fa questo script, partendo da `bg/webinar_bg.png`:
  1. cancella l'icona videocamera (l'area attorno e' navy piatto #0e0a48,
     verificato a pixel: si ricopre senza artefatti)
  2. incolla al suo posto l'icona-categoria corretta (`logo/icon-news-white.png`)
  3. produce anche la variante blu, rimappando le due tinte navy sulle due
     tinte blu del brand (navy -> blue, navy_tint -> blue_tint)

Restano invariati wordmark e filigrana a circuito: sono gli elementi di brand.
Le due varianti servono ad alternare i fondi fra le slide senza uscire dalla
direzione scelta.

Uso: python3 brand/make_editorial_bg.py
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))

# Regione dell'icona videocamera da cancellare, misurata a pixel su webinar_bg
# (glifo bianco a x 937-1079, y 130-222), con margine di sicurezza.
ICON_BOX = (920, 108, 1100, 246)
# Area del wordmark incorporato in webinar_bg (x 142-375, y 143-209).
WORDMARK_BOX = (128, 128, 392, 224)

LOGO_WORDMARK = "logo/digitiamo-wordmark-white.png"

NAVY = np.array([0x0e, 0x0a, 0x48], dtype=float)
NAVY_TINT = np.array([0x2c, 0x28, 0x5e], dtype=float)
BLUE = np.array([0x4a, 0x3a, 0xff], dtype=float)
BLUE_TINT = np.array([0x60, 0x52, 0xff], dtype=float)


def load(rel):
    return Image.open(os.path.join(HERE, rel))


def strip_icon(im):
    """Ricopre l'icona videocamera col navy di fondo."""
    im = im.copy()
    a = np.array(im.convert("RGB"))
    x0, y0, x1, y1 = ICON_BOX
    a[y0:y1, x0:x1] = NAVY.astype(np.uint8)
    return Image.fromarray(a, "RGB")


def place_icon(im, icon_rel, height=104, right=120, top=126):
    """Incolla l'icona-categoria corretta, allineata a destra come nell'originale."""
    icon = load(icon_rel).convert("RGBA")
    w = round(icon.width * height / icon.height)
    icon = icon.resize((w, height), Image.LANCZOS)
    out = im.convert("RGBA")
    out.alpha_composite(icon, (im.width - right - w, top))
    return out.convert("RGB")


def to_blue(im):
    """Rimappa le tinte navy sulle tinte blu, preservando il bianco.

    L'immagine e' composta da due soli toni navy piu' il bianco del marchio: si
    calcola dove ogni pixel cade fra navy e navy_tint e si interpola fra blue e
    blue_tint. Il bianco (marchio, icona) resta bianco.
    """
    a = np.array(im.convert("RGB")).astype(float)
    white = (a[:, :, 0] > 200) & (a[:, :, 1] > 200) & (a[:, :, 2] > 200)

    d = NAVY_TINT - NAVY
    t = ((a - NAVY) @ d) / float(d @ d)
    t = np.clip(t, 0.0, 1.0)[:, :, None]
    out = BLUE * (1.0 - t) + BLUE_TINT * t
    out[white] = [255.0, 255.0, 255.0]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB")


# ---------------------------------------------------------------------------
# Fondo chiaro + varianti scure del marchio
# ---------------------------------------------------------------------------
# Perche': con il solo wordmark bianco ogni slide deve avere un fondo scuro, ed
# e' da li' che nasce la monotonia di un carosello. Il marchio estratto e' una
# maschera bianca con canale alpha, quindi la forma e' nota: ricolorarla in navy
# o blu e' una derivazione fedele (il marchio e' piatto e monocromatico in tutti
# gli asset Canva). NB: e' una DERIVAZIONE, non la versione ufficiale — se il
# team design ha un originale vettoriale, quello vince.

# Gradiente cielo campionato su newsai_bg.png (colonna x=40, fuori dalla nuvola).
SKY_TOP = np.array([0xc5, 0xeb, 0xff], dtype=float)
SKY_BOTTOM = np.array([0xdb, 0xf3, 0xff], dtype=float)
# Filigrana su fondo chiaro: piu' scura del fondo, non piu' chiara.
SKY_TRACE = np.array([0xb0, 0xe0, 0xfa], dtype=float)


def circuit_mask():
    """Estrae la filigrana a circuito da webinar_bg come maschera 0..1.

    La traccia e' navy_tint su navy: si misura quanto ogni pixel si e' spostato
    dal fondo verso la tinta. I pixel bianchi (marchio e icona) vanno esclusi,
    altrimenti finirebbero nella maschera.
    """
    a = np.array(load("bg/webinar_bg.png").convert("RGB")).astype(float)
    d = NAVY_TINT - NAVY
    t = np.clip(((a - NAVY) @ d) / float(d @ d), 0.0, 1.0)
    # Escludere il solo bianco puro non basta: i bordi antialiasati del marchio
    # e dell'icona finiscono nella maschera e ricompaiono come contorno
    # fantasma sul fondo chiaro. Si azzerano anche le loro aree per intero.
    near_white = (a[:, :, 0] > 130) & (a[:, :, 1] > 130) & (a[:, :, 2] > 130)
    t[near_white] = 0.0
    for x0, y0, x1, y1 in (ICON_BOX, WORDMARK_BOX):
        t[y0:y1, x0:x1] = 0.0
    return t


def sky_ground(h, w):
    """Gradiente cielo verticale, dai valori reali del brand."""
    ramp = np.linspace(0.0, 1.0, h)[:, None, None]
    return SKY_TOP * (1.0 - ramp) + SKY_BOTTOM * ramp


def make_sky_bg():
    """Campo chiaro di brand: gradiente cielo + filigrana a circuito."""
    t = circuit_mask()
    h, w = t.shape
    ground = np.repeat(sky_ground(h, w), w, axis=1)
    m = t[:, :, None]
    out = ground * (1.0 - m) + SKY_TRACE * m
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB")


def tint(src_rel, rgb, out_name):
    """Ricolora un asset bianco mantenendo l'alpha (cioe' la forma).

    Vale per il wordmark e per i badge di categoria: sono glifi piatti
    monocromatici, quindi la ricolorazione e' fedele alla forma originale.
    """
    a = np.array(load(src_rel).convert("RGBA"))
    a[:, :, 0], a[:, :, 1], a[:, :, 2] = rgb
    Image.fromarray(a, "RGBA").save(os.path.join(HERE, out_name))
    print("  %s %dx%d" % (out_name, a.shape[1], a.shape[0]))


def export_circuit():
    """Esporta il motivo a circuito come PNG con alpha.

    Perche' serve separato: dentro gli sfondi il circuito e' incollato a una
    tinta fissa. Come maschera alpha diventa un elemento posizionabile e
    ricolorabile — cioe' usabile come strato di profondita' a qualunque scala,
    che e' il modo in cui il marchio smette di essere solo un logo in un angolo.
    """
    t = circuit_mask()
    ys, xs = np.where(t > 0.02)
    crop = t[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    rgba = np.zeros((crop.shape[0], crop.shape[1], 4), dtype=np.uint8)
    rgba[:, :, 0:3] = 255
    rgba[:, :, 3] = (np.clip(crop, 0, 1) * 255).astype(np.uint8)
    out = os.path.join(HERE, "logo/circuit-motif-white.png")
    Image.fromarray(rgba, "RGBA").save(out)
    print("  logo/circuit-motif-white.png %dx%d" % (crop.shape[1], crop.shape[0]))


def export_grain(size=160, seed=7):
    """Grana di stampa piastrellabile.

    Da' materialita' alle superfici piatte senza aggiungere un gradiente
    decorativo. Seed fisso: due esecuzioni devono dare lo stesso file.
    """
    rng = np.random.default_rng(seed)
    noise = rng.normal(128, 26, (size, size)).clip(0, 255).astype(np.uint8)
    g = np.zeros((size, size, 4), dtype=np.uint8)
    g[:, :, 0:3] = noise[:, :, None]
    g[:, :, 3] = 255
    out = os.path.join(HERE, "photo/grain.png")
    Image.fromarray(g, "RGBA").save(out)
    print("  photo/grain.png %dx%d (piastrellabile)" % (size, size))


def main():
    base = strip_icon(load("bg/webinar_bg.png"))
    navy = place_icon(base, "logo/icon-news-white.png")
    navy.save(os.path.join(HERE, "bg/editorial_navy.png"))
    print("  bg/editorial_navy.png", navy.size)

    blue = to_blue(navy)
    blue.save(os.path.join(HERE, "bg/editorial_blue.png"))
    print("  bg/editorial_blue.png", blue.size)

    sky = make_sky_bg()
    # Sul campo chiaro il badge di categoria bianco sparirebbe: si usa la
    # variante navy del marchio e nessun badge incorporato (lo mette il layout).
    sky.save(os.path.join(HERE, "bg/editorial_sky.png"))
    print("  bg/editorial_sky.png", sky.size)

    # Varianti scure per i fondi chiari: senza queste, ogni slide dovrebbe
    # avere un fondo scuro e il carosello sarebbe monotono.
    for rgb, suffix in (((0x0e, 0x0a, 0x48), "navy"), ((0x4a, 0x3a, 0xff), "blue")):
        tint(LOGO_WORDMARK, rgb, "logo/digitiamo-wordmark-%s.png" % suffix)
        tint("logo/icon-news-white.png", rgb, "logo/icon-news-%s.png" % suffix)

    export_circuit()
    export_grain()


if __name__ == "__main__":
    main()
