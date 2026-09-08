# -*- coding: utf-8 -*-
"""Visualizzatore locale dei caroselli: si sfogliano come su LinkedIn.

La griglia di anteprime serve a controllare la coerenza dell'insieme, ma un
carosello si giudica **scorrendolo**: l'ordine delle slide, il punto in cui
l'attenzione cala, se la CTA arriva troppo presto. Questa pagina lo permette.

Uso:
  python3 preview.py                 i 4 post della settimana 37
  python3 preview.py --no-open       genera e stampa il percorso

Frecce ← → per sfogliare, clic sulla slide per vederla a dimensione piena.
"""
import base64
import os
import subprocess
import sys
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
DEMOS = os.path.join(HERE, "design-demos")
OUT = os.path.join(HERE, "preview.html")

# (prefisso file, titolo, origine nel report, nota)
GROUPS = [
    ("W37-1-newsai", "Rassegna News AI",
     "trend 01 + 02 + 04",
     "Ora con la copertina VERA del template: «News AI» e il sottotitolo sono "
     "incorporati nel PNG, si compila solo il periodo. Prima ne avevo improvvisata una."),
    ("W37-2-model-fatigue", "Model fatigue",
     "trend 03",
     "Stile diverso: «ritratto computazionale» (Fathom / Ben Fry) uscito dalla ruota "
     "di huashu — tratti a capello, la densità nasce dai dati. Dato nuovo dagli "
     "articoli: la cadenza mediana è passata da 37,5 giorni nel 2023 a 11 nel 2026."),
    ("W37-3-agenti-847", "Agenti AI in produzione",
     "trend 07 · riframato",
     "Il «76%» è stato tolto: la fonte è un post su Medium con due firme diverse allo "
     "stesso URL, e la paternità accademica non è verificabile. Il post ora poggia sul "
     "meccanismo, che è documentato: CVE reali, fallimenti silenziosi, agenti orfani."),
    ("W37-4-ai-act", "EU AI Act",
     "trend 10 · ricostruito",
     "La versione precedente non diceva nulla. Ora ci sono le date esatte e il "
     "dettaglio che quasi nessuno nota: la rilevazione dei bias è stata ESTESA a tutti "
     "i sistemi AI, nello stesso pacchetto che ha rinviato le scadenze."),
]


def uri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def slides_for(prefix):
    out = []
    i = 1
    while True:
        p = os.path.join(DEMOS, "%s_%d.png" % (prefix, i))
        if not os.path.exists(p):
            break
        out.append(p)
        i += 1
    return out


CSS = """
:root{
  --ground:#e9e8f0; --panel:#fff; --line:#d8d4e6;
  --ink:#16143a; --ink2:#5d5f8c; --brand:#4a3aff; --navy:#0e0a48;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0c0b1c; --panel:#15132e; --line:#2a2749;
    --ink:#eeedf8; --ink2:#a9a6c8; --brand:#8578ff;
  }
}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--ground);color:var(--ink);
     font:400 15px/1.6 'Lato',-apple-system,BlinkMacSystemFont,sans-serif;}
.wrap{max-width:1180px;margin:0 auto;padding:38px 24px 90px;}
h1{font:800 32px/1.1 'Montserrat',sans-serif;letter-spacing:-.02em;}
.lede{color:var(--ink2);margin-top:10px;max-width:66ch;}
kbd{font:600 12px/1 ui-monospace,Menlo,monospace;background:var(--panel);
    border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;
    padding:3px 6px;color:var(--ink2);}

.post{margin-top:34px;background:var(--panel);border:1px solid var(--line);
      border-radius:16px;overflow:hidden;}
.post__head{padding:22px 26px 18px;border-bottom:1px solid var(--line);}
.post__t{font:800 22px/1.2 'Montserrat',sans-serif;letter-spacing:-.01em;}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;}
.chip{font:700 10.5px/1 'Montserrat',sans-serif;text-transform:uppercase;
      letter-spacing:.08em;padding:6px 10px;border-radius:6px;
      background:var(--ground);color:var(--ink2);border:1px solid var(--line);}
.chip b{color:var(--brand);}
.post__note{margin-top:12px;font-size:14px;color:var(--ink2);max-width:78ch;}

/* Lo sfogliatore: la slide grande piu' la striscia delle miniature. */
.stage{display:grid;grid-template-columns:1fr 168px;gap:0;}
@media(max-width:860px){.stage{grid-template-columns:1fr;}}
.frame{position:relative;background:var(--ground);display:flex;
       align-items:center;justify-content:center;padding:24px;min-height:520px;}
.frame img{max-width:100%;max-height:620px;width:auto;height:auto;display:block;
           border-radius:6px;box-shadow:0 18px 44px -22px rgba(14,10,72,.55);
           cursor:zoom-in;}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:42px;height:42px;
     border-radius:50%;border:1px solid var(--line);background:var(--panel);
     color:var(--ink);font:700 18px/1 sans-serif;cursor:pointer;
     display:flex;align-items:center;justify-content:center;}
.nav:hover{background:var(--brand);color:#fff;border-color:var(--brand);}
.nav:disabled{opacity:.3;cursor:default;}
.nav--prev{left:14px;} .nav--next{right:14px;}
.count{position:absolute;bottom:16px;left:50%;transform:translateX(-50%);
       font:700 12px/1 'Montserrat',sans-serif;letter-spacing:.06em;
       color:var(--ink2);background:var(--panel);border:1px solid var(--line);
       border-radius:999px;padding:7px 14px;}
.thumbs{border-left:1px solid var(--line);padding:14px;display:flex;
        flex-direction:column;gap:10px;overflow-y:auto;max-height:640px;}
@media(max-width:860px){.thumbs{flex-direction:row;border-left:0;
        border-top:1px solid var(--line);max-height:none;}}
.thumbs button{border:2px solid transparent;border-radius:7px;padding:0;
               background:none;cursor:pointer;line-height:0;}
.thumbs button[aria-current="true"]{border-color:var(--brand);}
.thumbs img{width:100%;height:auto;border-radius:5px;display:block;}
@media(max-width:860px){.thumbs img{width:88px;}}

dialog{border:0;padding:0;background:transparent;max-width:96vw;max-height:96vh;}
dialog::backdrop{background:rgba(6,5,20,.92);}
dialog img{max-width:min(94vw,860px);max-height:94vh;width:auto;border-radius:8px;}
.foot{margin-top:36px;padding-top:20px;border-top:1px solid var(--line);
      font-size:13.5px;color:var(--ink2);max-width:80ch;}
code{font:12.5px ui-monospace,Menlo,monospace;background:var(--panel);
     border:1px solid var(--line);border-radius:4px;padding:1px 5px;}
@media (prefers-reduced-motion:reduce){*{transition:none!important;}}
"""

JS = """
document.querySelectorAll('.post').forEach(function(post){
  var imgs = JSON.parse(post.dataset.slides);
  var main = post.querySelector('.frame img');
  var count = post.querySelector('.count');
  var prev = post.querySelector('.nav--prev');
  var next = post.querySelector('.nav--next');
  var thumbs = Array.prototype.slice.call(post.querySelectorAll('.thumbs button'));
  var i = 0;
  function show(n){
    i = Math.max(0, Math.min(imgs.length - 1, n));
    main.src = imgs[i];
    main.alt = 'Slide ' + (i + 1);
    count.textContent = (i + 1) + ' / ' + imgs.length;
    prev.disabled = (i === 0);
    next.disabled = (i === imgs.length - 1);
    thumbs.forEach(function(b, k){ b.setAttribute('aria-current', k === i ? 'true' : 'false'); });
  }
  prev.addEventListener('click', function(){ show(i - 1); });
  next.addEventListener('click', function(){ show(i + 1); });
  thumbs.forEach(function(b, k){ b.addEventListener('click', function(){ show(k); }); });
  // Le frecce agiscono sul post sotto il puntatore: con quattro caroselli in
  // pagina, una scorciatoia globale sarebbe ambigua.
  post.addEventListener('mouseenter', function(){ post.dataset.hot = '1'; });
  post.addEventListener('mouseleave', function(){ delete post.dataset.hot; });
  document.addEventListener('keydown', function(e){
    if (post.dataset.hot !== '1') return;
    if (e.key === 'ArrowLeft') { show(i - 1); e.preventDefault(); }
    if (e.key === 'ArrowRight') { show(i + 1); e.preventDefault(); }
  });
  main.addEventListener('click', function(){
    var d = document.getElementById('lb');
    document.getElementById('lbi').src = main.src;
    d.showModal();
  });
  show(0);
});
var dlg = document.getElementById('lb');
dlg.addEventListener('click', function(){ dlg.close(); });
"""


def build():
    posts = ""
    total = 0
    for prefix, title, origin, note in GROUPS:
        paths = slides_for(prefix)
        if not paths:
            continue
        total += len(paths)
        uris = [uri(p) for p in paths]
        thumbs = "".join(
            '<button aria-current="false"><img src="%s" alt="Slide %d"></button>'
            % (u, k + 1) for k, u in enumerate(uris))
        import json
        posts += """
<article class="post" data-slides='%s'>
  <div class="post__head">
    <div class="post__t">%s</div>
    <div class="chips"><span class="chip">origine <b>%s</b></span>
      <span class="chip">%d slide</span>
      <span class="chip">1200 × 1500</span></div>
    <p class="post__note">%s</p>
  </div>
  <div class="stage">
    <div class="frame">
      <button class="nav nav--prev" aria-label="Slide precedente">‹</button>
      <img src="%s" alt="Slide 1">
      <button class="nav nav--next" aria-label="Slide successiva">›</button>
      <div class="count">1 / %d</div>
    </div>
    <div class="thumbs">%s</div>
  </div>
</article>""" % (json.dumps(uris).replace("'", "&#39;"), title, origin,
                 len(paths), note, uris[0], len(paths), thumbs)

    return """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prove settimana 7–13 settembre</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Lato:wght@400;700&display=swap">
<style>%s</style></head><body>
<div class="wrap">
  <h1>Prove — settimana 7–13 settembre 2026</h1>
  <p class="lede">Quattro post, %d slide, tutte dai contenuti del report reale.
  Passa il puntatore su un carosello e usa <kbd>←</kbd> <kbd>→</kbd> per sfogliarlo,
  oppure clicca la slide per vederla a dimensione piena.</p>
  %s
  <p class="foot">Un carosello si giudica scorrendolo, non a griglia: l'ordine delle
  slide e il punto in cui l'attenzione cala si vedono solo così. Rigenerabile con
  <code>python3 design-demos/make_week37_demos.py</code> e
  <code>python3 preview.py</code>. Valutazione scritta in
  <code>design-demos/settimana37.md</code>.</p>
</div>
<dialog id="lb"><img id="lbi" alt=""></dialog>
<script>%s</script>
</body></html>""" % (CSS, total, posts, JS)


def main():
    html = build()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("scritto %s (%.1f MB)" % (OUT, os.path.getsize(OUT) / 1e6))
    if "--no-open" in sys.argv:
        return
    url = "file://" + OUT
    if sys.platform == "darwin":
        subprocess.run(["open", url], check=False)
    else:
        webbrowser.open(url)
    print("aperto nel browser")


if __name__ == "__main__":
    main()
