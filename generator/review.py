# -*- coding: utf-8 -*-
"""Pagina di revisione locale: tutte le grafiche della settimana in un browser.

Serve per guardare i caroselli come li vedrebbe qualcuno che scorre il feed —
in sequenza, non un PNG alla volta. Mostra anche il ritmo di colore di ogni
formato, che e' la cosa che si giudica a occhio e non da codice.

Uso:
  python3 review.py                    legge i PNG dalla cartella superiore
  python3 review.py --dir <cartella>   legge da un'altra cartella (es. una prova)
  python3 review.py --no-open          solo genera, stampa il percorso

NB: la cartella superiore contiene gli asset GIA' PUBBLICATI, che la guardia di
render.py protegge dalla sovrascrittura. Per rivedere una nuova generazione,
renderizzala in una cartella di prova e passala con --dir.
"""
import base64
import os
import subprocess
import sys
import webbrowser

import templates
import week

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, ".."))
if "--dir" in sys.argv:
    OUT_DIR = os.path.abspath(sys.argv[sys.argv.index("--dir") + 1])
OUT = os.path.join(HERE, "review.html")


def uri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def find(name):
    p = os.path.join(OUT_DIR, name)
    return p if os.path.exists(p) else None


CSS = """
:root{
  --ground:#eceaf3; --panel:#fff; --line:#d9d5e8;
  --ink:#16143a; --ink2:#5b5f8f; --brand:#4a3aff; --navy:#0e0a48;
  --green:#43ef84; --sky:#c5ebff;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--ground);color:var(--ink);
     font:400 15px/1.6 'Lato',-apple-system,sans-serif;}
.wrap{max-width:1500px;margin:0 auto;padding:40px 28px 80px;}
h1{font:800 34px/1.1 'Montserrat',sans-serif;letter-spacing:-.02em;}
.sub{color:var(--ink2);margin-top:10px;max-width:70ch;}
section{margin-top:44px;background:var(--panel);border:1px solid var(--line);
        border-radius:14px;padding:26px 28px;}
h2{font:800 21px/1.2 'Montserrat',sans-serif;letter-spacing:-.01em;}
.meta{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:12px;}
.chip{font:700 11px/1 'Montserrat',sans-serif;text-transform:uppercase;
      letter-spacing:.08em;padding:6px 10px;border-radius:6px;
      background:#f0eff7;color:var(--ink2);border:1px solid var(--line);}
.chip b{color:var(--ink);}
/* Il ritmo di colore, reso visibile: e' la cosa da giudicare */
.rhythm{display:flex;gap:4px;align-items:center;margin-top:14px;}
.sw{width:34px;height:22px;border-radius:4px;border:1px solid rgba(0,0,0,.15);}
.sw-navy{background:var(--navy);} .sw-blue{background:var(--brand);}
.sw-sky{background:var(--sky);} .sw-news{background:linear-gradient(#c5ebff 45%,var(--brand) 45%);}
.rl{font:700 11px/1 'Montserrat',sans-serif;color:var(--ink2);
    letter-spacing:.06em;text-transform:uppercase;margin-left:8px;}
.strip{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:22px;}
.strip.singles{grid-template-columns:repeat(4,1fr);}
@media(max-width:1100px){.strip,.strip.singles{grid-template-columns:repeat(3,1fr);}}
@media(max-width:680px){.strip,.strip.singles{grid-template-columns:repeat(2,1fr);}}
figure{margin:0;}
figure img{width:100%;height:auto;display:block;border-radius:8px;
           border:1px solid var(--line);cursor:zoom-in;background:#fff;}
figcaption{font:700 10.5px/1.3 'Montserrat',sans-serif;color:var(--ink2);
           text-transform:uppercase;letter-spacing:.06em;margin-top:7px;
           display:flex;justify-content:space-between;gap:6px;}
figcaption span:last-child{color:var(--brand);}
dialog{border:0;padding:0;background:transparent;max-width:96vw;max-height:96vh;}
dialog::backdrop{background:rgba(8,6,24,.9);}
dialog img{max-width:min(92vw,900px);max-height:92vh;width:auto;border-radius:8px;
           box-shadow:0 30px 80px -20px #000;}
.note{margin-top:22px;padding-top:18px;border-top:1px solid var(--line);
      font-size:13.5px;color:var(--ink2);max-width:80ch;}
code{font:12.5px ui-monospace,Menlo,monospace;background:#f0eff7;
     border:1px solid var(--line);border-radius:4px;padding:1px 5px;}
.xgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:22px;}
@media(max-width:1100px){.xgrid{grid-template-columns:1fr;}}
.xcard{border:1px solid var(--line);border-radius:12px;padding:18px 18px 8px;
       background:#faf9fd;}
.xcard h3{font:800 17px/1.2 'Montserrat',sans-serif;letter-spacing:-.01em;}
.xlogic{font:700 10.5px/1 'Montserrat',sans-serif;text-transform:uppercase;
        letter-spacing:.08em;color:var(--brand);margin-top:7px;}
.xdesc{font-size:13.5px;color:var(--ink2);margin-top:9px;}
.xcard .strip{grid-template-columns:1fr 1fr;}
"""


def strip(items, singles=False):
    cells = ""
    for label, surface, path in items:
        if not path:
            continue
        # Una sola volta il base64: prima era duplicato in src e data-full, cosa
        # che raddoppiava il peso della pagina (27 MB per 22 immagini).
        # Il lightbox riusa il src della miniatura, che e' gia' a piena risoluzione.
        cells += ('<figure><img src="%s" alt="%s">'
                  '<figcaption><span>%s</span><span>%s</span></figcaption></figure>'
                  % (uri(path), label, label, surface))
    return '<div class="strip%s">%s</div>' % (" singles" if singles else "", cells)


def rhythm_bar(surfaces):
    sw = "".join('<div class="sw sw-%s" title="%s"></div>' % (s, s) for s in surfaces)
    return ('<div class="rhythm">%s<span class="rl">ritmo di colore</span></div>'
            % sw)


EXPLORE = [
    ("X-A-businessweek", "A · Businessweek",
     "Bloomberg Businessweek, pagina dati (era Richard Turley). Contrasto di corpo "
     "estremo, titolo che dice la conclusione, foto a piena larghezza, grafico che "
     "esce dal margine.", "riferimento reale"),
    ("X-B-lupi-datahumanism", "B · Lupi / Data Humanism",
     "Giorgia Lupi, partner Pentagram. Un alfabeto di simboli inventato per questo "
     "contenuto, con legenda obbligatoria. Il glifo è il nodo del marchio Digitiamo: "
     "l'alfabeto nasce dall'identità.", "miglior designer per il cliente"),
    ("X-C-holmes-explanation", "C · Holmes / Explanation Graphics",
     "Nigel Holmes, direttore grafico di TIME 1978-1994. Metafora pittorica, colori "
     "piatti, contorni spessi, ironia. Degradazione dichiarata: manca il tratto "
     "disegnato a mano.", "ruota dei secondi · 2/20"),
]


def explore_section():
    """Le tre strade nuove, con immagini reali. In attesa di scelta."""
    cards = ""
    for slug, title, desc, logic in EXPLORE:
        shots = []
        for i in (1, 2):
            p = os.path.join(HERE, "design-demos", "%s_%d.png" % (slug, i))
            if os.path.exists(p):
                shots.append(("pagina %d" % i, logic, p))
        if not shots:
            continue
        cards += ('<div class="xcard"><h3>%s</h3><p class="xlogic">%s</p>'
                  '<p class="xdesc">%s</p>%s</div>'
                  % (title, logic, desc, strip(shots, singles=True)))
    note = (
        "Ognuna ha un riferimento reale dichiarato e usa la foto "
        "<b>NASA Columbia Supercomputer</b> (pubblico dominio) pi\u00f9 il "
        "<b>logo ufficiale NVIDIA</b> \u2014 obbligatorio, non decorativo: un design "
        "che nomina un prodotto deve mostrarlo. La foto \u00e8 trattata in duotone "
        "sulla palette. Scartate: schede grafiche di consumo del 2009 (fuorvianti "
        "per ricavi data center 2026) e foto CC BY-SA (attribuzione + share-alike "
        "su un post commerciale). Il verde Digitiamo non compare dove c'\u00e8 il "
        "verde NVIDIA: sono due verdi diversi (#43ef84 e #76b900) e un logo di "
        "terzi non si ricolora."
    )
    return (
        '<section><h2>Esplorazione \u00b7 tre strade nuove</h2>'
        '<div class="meta">'
        '<span class="chip">stato <b>in attesa di scelta</b></span>'
        '<span class="chip">con immagini reali</span>'
        '<span class="chip">foto <b>pubblico dominio</b></span></div>'
        '<div class="xgrid">' + cards + '</div>'
        '<p class="note">' + note + '</p></section>'
    )


def build():
    blocks = []

    for c in week.CAROUSELS:
        pt = templates.POST_TYPES[c["post_type"]]
        surfaces = [templates.rhythm_for(c["post_type"], i, len(c["slides"]))
                    if not s.get("surface") else s["surface"]
                    for i, s in enumerate(c["slides"])]
        items = []
        for i, (s, surf) in enumerate(zip(c["slides"], surfaces), start=1):
            items.append(("%02d · %s" % (i, s["kind"]), surf,
                          find("carosello_%s_%s_slide%d.png" % (c["slug"], week.DATE, i))))
        pdf = find("carosello_%s_%s.pdf" % (c["slug"], week.DATE))
        blocks.append("""
<section>
  <h2>Carosello · %s</h2>
  <div class="meta">
    <span class="chip">tipo <b>%s</b></span>
    <span class="chip">slug <b>%s</b></span>
    <span class="chip">%d pagine</span>
    %s
  </div>
  %s
  %s
</section>""" % (pt["label"], c["post_type"], c["slug"], len(c["slides"]),
                 '<span class="chip">PDF <b>generato</b></span>' if pdf else "",
                 rhythm_bar(surfaces), strip(items)))

    items = []
    for s in week.SINGLES:
        pt = templates.POST_TYPES[s["post_type"]]
        items.append((pt["label"], pt["rhythm"][0],
                      find("brandstyle_%s_%s.png" % (s["slug"], week.DATE))))
    blocks.append("""
<section>
  <h2>Immagini singole · una per post prioritario</h2>
  <div class="meta"><span class="chip">%d immagini</span>
    <span class="chip">superficie <b>dal tipo di post</b></span></div>
  %s
  %s
</section>""" % (len(week.SINGLES),
                 rhythm_bar([templates.POST_TYPES[s["post_type"]]["rhythm"][0]
                             for s in week.SINGLES]),
                 strip(items, singles=True)))

    blocks.append(explore_section())

    return """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<title>Revisione PED — %s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Lato:wght@400;700&display=swap">
<style>%s</style></head><body>
<div class="wrap">
  <h1>Revisione grafiche PED</h1>
  <p class="sub">Settimana %s · sorgente <code>%s</code>. Ogni formato ha il proprio ritmo di colore, definito in
  <code>templates.POST_TYPES</code>: le pagine cambiano fondo restando dentro le regole
  di brand. Clicca una slide per vederla a dimensione piena.</p>
  %s
  <p class="note">Le superfici sono tre. Il colore del <b>testo</b> e la
  <b>tinta dei dati</b> sono ruoli distinti, e i limiti sono misurati col
  validator, non stimati: <b>navy</b> testo bianco / dati verde (PASS);
  <b>blu</b> testo bianco, accento cielo, dati verde (PASS \u2265 3:1);
  <b>cielo</b> testo navy / dati blu \u2014 sul cielo il verde misura 1,2:1 ed
  \u00e8 inutilizzabile. Il fondo chiaro esiste perch\u00e9 il marchio \u00e8
  stato derivato anche in navy e blu dalla maschera alpha di quello bianco:
  prima, con il solo marchio bianco, ogni pagina era costretta a un fondo scuro.</p>
</div>
<dialog id="lb"><img id="lbi" alt=""></dialog>
<script>
(function(){
  var d=document.getElementById('lb'), i=document.getElementById('lbi');
  document.querySelectorAll('figure img').forEach(function(el){
    el.addEventListener('click',function(){ i.src=el.currentSrc||el.src; i.alt=el.alt; d.showModal(); });
  });
  d.addEventListener('click',function(){ d.close(); });
})();
</script>
</body></html>""" % (week.DATE, CSS, week.WEEK_LABEL, OUT_DIR, "".join(blocks))


def main():
    html = build()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("scritto %s (%.1f MB)" % (OUT, os.path.getsize(OUT) / 1e6))
    if "--no-open" in sys.argv:
        return
    url = "file://" + OUT
    # macOS: `open` e' piu' affidabile di webbrowser quando il default e' Safari
    if sys.platform == "darwin":
        subprocess.run(["open", url], check=False)
    else:
        webbrowser.open(url)
    print("aperto nel browser")


if __name__ == "__main__":
    main()
