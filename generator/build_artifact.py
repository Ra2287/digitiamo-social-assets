# -*- coding: utf-8 -*-
"""Compone l'artifact condivisibile per l'approvazione dei post della settimana.

Perche' un artifact e non la pagina locale: `preview.html` sta sul disco di chi
lo genera. Questo va condiviso con chi approva — ed e' il punto del flusso PED,
dove la pubblicazione richiede sempre un via libera umano.

La pagina **ricorda le decisioni**: usa il capability `artifact`, quindi chi
apre dopo vede cosa e' stato approvato e cosa no. Lo stato non sta nel DOM: sta
in un blocco JSON, e ogni azione rigenera il documento e lo ripubblica.

Uso: python3 build_artifact.py   -> scrive artifact.html
"""
import base64
import io
import json
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DEMOS = os.path.join(HERE, "design-demos")
OUT = os.path.join(HERE, "artifact.html")

# Larghezza di revisione: 760px basta per giudicare, e tiene il documento
# leggero — conta, perche' ogni approvazione ripubblica l'intera pagina.
REVIEW_W, REVIEW_H, QUALITY = 760, 950, 90

POSTS = [
    dict(
        id="newsai",
        prefix="W37-1-newsai",
        title="Rassegna News AI",
        origin="trend 01 + 02 + 04",
        format="Rassegna News AI",
        slot="Lun 7/9 · 7:45",
        note="Sei pagine: copertina, tre notizie, il filo comune, la CTA. Ogni "
             "notizia porta data e testata nell'occhiello e chiude con il "
             "richiamo «cosa significa per te» — è la parte che distingue una "
             "rassegna da un elenco di notizie. I marchi sono quelli ufficiali, "
             "su campo chiaro perché le loro varianti sono a inchiostro scuro.",
        flag="Copertina rifatta nei font del brand: non usa più lo sfondo Canva, "
             "che aveva «News AI» incorporato in un grotesque estraneo al "
             "sistema e non modificabile. Il marchio Zhipu AI, prima dichiarato "
             "non reperibile, ora è quello ufficiale dal CDN di Z.ai.",
    ),
    dict(
        id="fatigue",
        prefix="W37-2-model-fatigue",
        title="Model fatigue",
        origin="trend 03",
        format="Carosello dati",
        slot="Mar 8/9 · 8:00",
        note="Dato che il report non aveva, trovato negli articoli: la cadenza "
             "mediana fra rilasci è passata da 37,5 giorni nel 2023 a 11 nel "
             "2026. La slide 2 lo mostra come densità — 5 tratti contro 17, "
             "stessa finestra di sei mesi. Il «da dieci a cinque» ora è una "
             "citazione attribuita a Suresh Vasudevan, CEO di Clockwork Systems.",
        flag="I tratti sono la cadenza mediana documentata, non i singoli "
             "rilasci: è scritto sulla slide.",
    ),
    dict(
        id="agenti",
        prefix="W37-3-agenti-847",
        title="Agenti AI in produzione",
        origin="trend 07 · riframato",
        format="Carosello dati",
        slot="Mer 9/9 · 12:15",
        note="Il post sta sul meccanismo, non su una percentuale: rotazione "
             "delle credenziali su cicli di ~90 giorni, fallimenti silenziosi, "
             "agenti orfani, CVE reali. È anche l'argomento del Team "
             "Augmentation, cosa che il numero non era.",
        flag="Il «76% su 847 deployment» è stato tolto: la fonte è un post su "
             "Medium che compare con due firme diverse allo stesso URL, e la "
             "paternità accademica attribuita da alcune riprese (Stanford, MIT, "
             "Carnegie Mellon, Nvidia) non è verificabile.",
    ),
    dict(
        id="aiact",
        prefix="W37-4-ai-act",
        title="EU AI Act",
        origin="trend 10 · ricostruito",
        format="Carosello normativa",
        slot="Ven 11/9 · 8:00",
        note="Con le date esatte: Allegato III al 2 dicembre 2027, Allegato I al "
             "2 agosto 2028, sandbox al 2 agosto 2027, watermarking con "
             "tolleranza fino al 2 dicembre 2026. E il punto che ribalta la "
             "lettura corrente: la rilevazione dei bias è stata estesa a tutti i "
             "sistemi AI, nello stesso pacchetto che ha rinviato le scadenze.",
        flag="CTA sull'AI Business Academy e non sul Team Augmentation: è "
             "compliance, non architettura.",
    ),
]


def slide_uris(prefix):
    out = []
    i = 1
    while True:
        p = os.path.join(DEMOS, "%s_%d.png" % (prefix, i))
        if not os.path.exists(p):
            break
        im = Image.open(p).convert("RGB").resize((REVIEW_W, REVIEW_H), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        out.append("data:image/jpeg;base64," +
                   base64.b64encode(buf.getvalue()).decode("ascii"))
        i += 1
    return out


CSS = """
:root{
  --ground:#f3f3f8; --panel:#ffffff; --line:#dedaec; --line-2:#efedf6;
  --ink:#16143a; --ink-2:#5d5f8c; --ink-3:#8b8bb0;
  --brand:#4a3aff; --ok:#157a48; --ok-bg:#e6f5ec; --warn:#91560a; --warn-bg:#fdf1e0;
  --shadow:0 1px 2px rgba(22,20,58,.05), 0 14px 34px -20px rgba(22,20,58,.28);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0b0a1c; --panel:#14122e; --line:#2b2850; --line-2:#221f42;
    --ink:#eeedf8; --ink-2:#a8a5c6; --ink-3:#7f7ca4;
    --brand:#8578ff; --ok:#57cf94; --ok-bg:#12301f; --warn:#e0a55a; --warn-bg:#33240e;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 16px 40px -22px rgba(0,0,0,.75);
  }
}
:root[data-theme="dark"]{
  --ground:#0b0a1c; --panel:#14122e; --line:#2b2850; --line-2:#221f42;
  --ink:#eeedf8; --ink-2:#a8a5c6; --ink-3:#7f7ca4;
  --brand:#8578ff; --ok:#57cf94; --ok-bg:#12301f; --warn:#e0a55a; --warn-bg:#33240e;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 16px 40px -22px rgba(0,0,0,.75);
}

*{box-sizing:border-box;}
body{background:var(--ground);color:var(--ink);
  font:400 15.5px/1.62 'Lato','Helvetica Neue',Arial,sans-serif;
  -webkit-font-smoothing:antialiased;}
.wrap{max-width:1160px;margin:0 auto;padding:44px 24px 96px;}

/* ---- intestazione ---- */
.eyebrow{font:700 11.5px/1 'Montserrat',sans-serif;text-transform:uppercase;
  letter-spacing:.15em;color:var(--brand);}
h1{font:800 clamp(29px,4vw,40px)/1.08 'Montserrat',sans-serif;letter-spacing:-.022em;
  margin:14px 0 0;text-wrap:balance;max-width:26ch;}
.lede{margin:16px 0 0;max-width:64ch;font-size:17.5px;color:var(--ink-2);}
.tally{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px;}
.tally .t{background:var(--panel);border:1px solid var(--line);border-radius:10px;
  padding:12px 16px;min-width:104px;}
.tally .n{font:800 25px/1 'Montserrat',sans-serif;font-variant-numeric:tabular-nums;
  letter-spacing:-.02em;}
.tally .k{font:700 10px/1.2 'Montserrat',sans-serif;text-transform:uppercase;
  letter-spacing:.09em;color:var(--ink-3);margin-top:7px;}
.tally .t--ok .n{color:var(--ok);} .tally .t--warn .n{color:var(--warn);}

/* ---- scheda del post ---- */
.post{margin-top:26px;background:var(--panel);border:1px solid var(--line);
  border-radius:16px;overflow:hidden;box-shadow:var(--shadow);}
.post__head{padding:24px 26px 20px;}
.post__row{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;}
.post__n{font:800 12px/1 'Montserrat',sans-serif;color:var(--brand);
  letter-spacing:.1em;}
.post__t{font:800 23px/1.16 'Montserrat',sans-serif;letter-spacing:-.014em;}
.chips{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px;}
.chip{font:700 10px/1 'Montserrat',sans-serif;text-transform:uppercase;
  letter-spacing:.08em;padding:6px 10px;border-radius:6px;background:var(--line-2);
  color:var(--ink-2);border:1px solid var(--line);}
.chip b{color:var(--ink);}
.post__note{margin-top:14px;font-size:14.5px;color:var(--ink-2);max-width:80ch;}
/* Il riquadro "da sapere" non e' decorativo: porta il limite dichiarato del
   post, cioe' la cosa che chi approva deve vedere prima di dire sì. */
.flag{margin-top:14px;display:flex;gap:11px;align-items:flex-start;
  background:var(--warn-bg);border-radius:9px;padding:13px 15px;max-width:80ch;}
.flag__k{font:700 9.5px/1.5 'Montserrat',sans-serif;text-transform:uppercase;
  letter-spacing:.09em;color:var(--warn);flex:0 0 auto;padding-top:1px;}
.flag__t{font-size:13.8px;color:var(--ink-2);}

/* ---- sfogliatore ---- */
.stage{display:grid;grid-template-columns:1fr 152px;border-top:1px solid var(--line);}
@media(max-width:820px){.stage{grid-template-columns:1fr;}}
.frame{position:relative;background:var(--ground);display:flex;align-items:center;
  justify-content:center;padding:26px;min-height:480px;}
.frame img{max-width:100%;max-height:600px;width:auto;display:block;border-radius:5px;
  box-shadow:0 16px 40px -22px rgba(14,10,72,.6);cursor:zoom-in;}
.nav{position:absolute;top:50%;transform:translateY(-50%);width:40px;height:40px;
  border-radius:50%;border:1px solid var(--line);background:var(--panel);
  color:var(--ink);font:700 17px/1 sans-serif;cursor:pointer;display:flex;
  align-items:center;justify-content:center;}
.nav:hover:not(:disabled){background:var(--brand);color:#fff;border-color:var(--brand);}
.nav:disabled{opacity:.28;cursor:default;}
.nav--p{left:14px;} .nav--n{right:14px;}
.count{position:absolute;bottom:16px;left:50%;transform:translateX(-50%);
  font:700 11.5px/1 'Montserrat',sans-serif;font-variant-numeric:tabular-nums;
  letter-spacing:.06em;color:var(--ink-2);background:var(--panel);
  border:1px solid var(--line);border-radius:999px;padding:7px 13px;}
.rail{border-left:1px solid var(--line);padding:13px;display:flex;
  flex-direction:column;gap:9px;overflow-y:auto;max-height:620px;}
@media(max-width:820px){.rail{flex-direction:row;border-left:0;
  border-top:1px solid var(--line);max-height:none;}}
.rail button{border:2px solid transparent;border-radius:6px;padding:0;background:none;
  cursor:pointer;line-height:0;}
.rail button[aria-current="true"]{border-color:var(--brand);}
.rail img{width:100%;height:auto;border-radius:4px;display:block;}
@media(max-width:820px){.rail img{width:82px;}}

/* ---- decisione ---- */
.decide{border-top:1px solid var(--line);padding:20px 26px 24px;}
.decide__k{font:700 10px/1 'Montserrat',sans-serif;text-transform:uppercase;
  letter-spacing:.1em;color:var(--ink-3);}
.btns{display:flex;gap:9px;flex-wrap:wrap;margin-top:12px;}
.btn{font:700 13px/1 'Montserrat',sans-serif;padding:11px 16px;border-radius:8px;
  border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer;}
.btn:hover:not(:disabled){border-color:var(--brand);color:var(--brand);}
.btn[aria-pressed="true"]{background:var(--ink);color:var(--panel);
  border-color:var(--ink);}
.btn--ok[aria-pressed="true"]{background:var(--ok);border-color:var(--ok);color:#fff;}
.btn--warn[aria-pressed="true"]{background:var(--warn);border-color:var(--warn);color:#fff;}
.btn:disabled{opacity:.45;cursor:default;}
.noterow{margin-top:14px;display:flex;gap:9px;align-items:flex-start;flex-wrap:wrap;}
textarea{flex:1;min-width:260px;min-height:62px;font:400 14.5px/1.5 'Lato',sans-serif;
  color:var(--ink);background:var(--ground);border:1px solid var(--line);
  border-radius:9px;padding:11px 13px;resize:vertical;}
textarea:focus-visible,.btn:focus-visible,.nav:focus-visible,
.rail button:focus-visible{outline:2px solid var(--brand);outline-offset:2px;}
.saved{font:700 11.5px/1.5 'Montserrat',sans-serif;color:var(--ok);
  align-self:center;}
.state{margin-top:13px;font-size:13.5px;color:var(--ink-2);}
.state b{color:var(--ink);}

/* ---- piede ---- */
.open{margin-top:34px;background:var(--panel);border:1px solid var(--line);
  border-radius:14px;padding:24px 26px;}
.open h2{font:800 18px/1.2 'Montserrat',sans-serif;letter-spacing:-.01em;}
.open ul{margin:14px 0 0;padding:0;list-style:none;display:grid;gap:11px;}
.open li{position:relative;padding-left:18px;font-size:14.5px;color:var(--ink-2);
  max-width:82ch;}
.open li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;
  border-radius:2px;background:var(--brand);}
.foot{margin-top:26px;font-size:13px;color:var(--ink-3);max-width:80ch;}
code{font:12.5px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--line-2);
  border:1px solid var(--line);border-radius:4px;padding:1px 5px;}

dialog{border:0;padding:0;background:transparent;max-width:96vw;max-height:96vh;}
dialog::backdrop{background:rgba(6,5,20,.93);}
dialog img{max-width:min(94vw,880px);max-height:94vh;width:auto;border-radius:7px;}
@media (prefers-reduced-motion:reduce){*{transition:none!important;}}
"""

APP = r"""
(function () {
  var PAY = JSON.parse(document.getElementById('payload').textContent);
  var STATE = JSON.parse(document.getElementById('state').textContent);
  var mount = document.getElementById('mount');
  var artifact = null;      // resta null se questa vista non puo' pubblicare
  var canWrite = false;
  var cursor = {};          // slide corrente per post: solo vista, non stato condiviso

  function esc(t) {
    return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c];
    });
  }

  function tally() {
    var ok = 0, mod = 0;
    PAY.posts.forEach(function (p) {
      var d = (STATE[p.id] || {}).decision;
      if (d === 'ok') ok++; else if (d === 'mod') mod++;
    });
    return { ok: ok, mod: mod, todo: PAY.posts.length - ok - mod };
  }

  function render() {
    var t = tally();
    var slides = 0;
    PAY.posts.forEach(function (p) { slides += PAY.slides[p.id].length; });

    var h = '<header>' +
      '<div class="eyebrow">Piano editoriale · settimana 37</div>' +
      '<h1>Quattro post da approvare</h1>' +
      '<p class="lede">Settimana 7–13 settembre 2026. Contenuti dal report PED, ' +
      'con la sezione di origine indicata su ogni post. Sfoglia le slide, poi ' +
      'segna la tua decisione: resta salvata per chi apre dopo.</p>' +
      '<div class="tally">' +
      '<div class="t"><div class="n">' + PAY.posts.length + '</div><div class="k">Post</div></div>' +
      '<div class="t"><div class="n">' + slides + '</div><div class="k">Slide</div></div>' +
      '<div class="t t--ok"><div class="n">' + t.ok + '</div><div class="k">Approvati</div></div>' +
      '<div class="t t--warn"><div class="n">' + t.mod + '</div><div class="k">Da modificare</div></div>' +
      '<div class="t"><div class="n">' + t.todo + '</div><div class="k">Da valutare</div></div>' +
      '</div></header>';

    PAY.posts.forEach(function (p, idx) {
      var imgs = PAY.slides[p.id];
      var st = STATE[p.id] || {};
      var i = Math.min(cursor[p.id] || 0, imgs.length - 1);
      var rail = imgs.map(function (u, k) {
        return '<button data-post="' + p.id + '" data-go="' + k + '" ' +
          'aria-current="' + (k === i ? 'true' : 'false') + '" ' +
          'aria-label="Slide ' + (k + 1) + '"><img src="' + u + '" alt=""></button>';
      }).join('');

      h += '<article class="post" data-post="' + p.id + '">' +
        '<div class="post__head">' +
          '<div class="post__row"><span class="post__n">' +
            ('0' + (idx + 1)).slice(-2) + '</span>' +
            '<span class="post__t">' + esc(p.title) + '</span></div>' +
          '<div class="chips">' +
            '<span class="chip">origine <b>' + esc(p.origin) + '</b></span>' +
            '<span class="chip">' + esc(p.format) + '</span>' +
            '<span class="chip">' + imgs.length + ' slide</span>' +
            '<span class="chip">in calendario <b>' + esc(p.slot) + '</b></span>' +
          '</div>' +
          '<p class="post__note">' + esc(p.note) + '</p>' +
          (p.flag ? '<div class="flag"><span class="flag__k">Da sapere</span>' +
                    '<span class="flag__t">' + esc(p.flag) + '</span></div>' : '') +
        '</div>' +
        '<div class="stage">' +
          '<div class="frame">' +
            '<button class="nav nav--p" data-post="' + p.id + '" data-step="-1" ' +
              'aria-label="Slide precedente"' + (i === 0 ? ' disabled' : '') + '>‹</button>' +
            '<img src="' + imgs[i] + '" alt="' + esc(p.title) + ', slide ' + (i + 1) + '" ' +
              'data-zoom="' + p.id + '">' +
            '<button class="nav nav--n" data-post="' + p.id + '" data-step="1" ' +
              'aria-label="Slide successiva"' + (i === imgs.length - 1 ? ' disabled' : '') + '>›</button>' +
            '<div class="count">' + (i + 1) + ' / ' + imgs.length + '</div>' +
          '</div>' +
          '<div class="rail">' + rail + '</div>' +
        '</div>' +
        '<div class="decide">' +
          '<div class="decide__k">La tua decisione</div>' +
          '<div class="btns">' +
            '<button class="btn btn--ok" data-set="ok" data-post="' + p.id + '" ' +
              'aria-pressed="' + (st.decision === 'ok') + '"' + (canWrite ? '' : ' disabled') +
              '>Approvato</button>' +
            '<button class="btn btn--warn" data-set="mod" data-post="' + p.id + '" ' +
              'aria-pressed="' + (st.decision === 'mod') + '"' + (canWrite ? '' : ' disabled') +
              '>Da modificare</button>' +
            (st.decision ? '<button class="btn" data-set="" data-post="' + p.id + '"' +
              (canWrite ? '' : ' disabled') + '>Azzera</button>' : '') +
          '</div>' +
          '<div class="noterow">' +
            '<textarea data-note="' + p.id + '" placeholder="Cosa cambiare, o perché va bene"' +
              (canWrite ? '' : ' readonly') + '>' + esc(st.note || '') + '</textarea>' +
            '<button class="btn" data-savenote="' + p.id + '"' +
              (canWrite ? '' : ' disabled') + '>Salva nota</button>' +
          '</div>' +
          (st.decision || st.note
            ? '<div class="state">Ultimo aggiornamento: <b>' +
              esc(st.at || '—') + '</b>' +
              (st.decision === 'ok' ? ' · approvato' :
               st.decision === 'mod' ? ' · da modificare' : '') + '</div>'
            : '') +
        '</div>' +
      '</article>';
    });

    h += '<section class="open"><h2>Due cose ancora aperte</h2><ul>' +
      '<li><b>Conflitto di formato.</b> Questi post sono 1200×1500 e usano il ' +
      'sistema di brand ricostruito. Il carosello pubblicato dal bot lunedì è ' +
      '1080×1350 e non lo usa: nello stesso feed convivono male, e il bot ' +
      'continuerà a produrre nel formato vecchio ogni lunedì.</li>' +
      '<li><b>La copertina News AI va rifatta nei font del brand.</b> Il testo ' +
      'incorporato nel PNG («News AI», «Le notizie dal mondo AI») non è ' +
      'Montserrat né Lato: è un grotesque messo da Canva. Per questo il periodo ' +
      'sta in una pill — così la differenza tipografica è una gerarchia voluta ' +
      'e non una stonatura.</li>' +
      '</ul></section>' +
      '<p class="foot">' + (canWrite
        ? 'Le decisioni si salvano nella pagina: chi la apre dopo le vede.'
        : 'Hai accesso in sola lettura: puoi sfogliare e commentare, non cambiare le decisioni.') +
      ' Le slide sono bozze rigenerabili da <code>design-demos/make_week37_demos.py</code>.</p>';

    mount.innerHTML = h;
  }

  // Rigenera il DOCUMENTO (non il DOM vissuto) e lo ripubblica: CSS, script e
  // payload vengono ri-emessi identici, cambia solo il blocco di stato, e il
  // punto di montaggio esce vuoto perche' la pagina si ridisegna al caricamento.
  function documentHtml(state) {
    var css = document.getElementById('css').textContent;
    var app = document.getElementById('app').textContent;
    var pay = document.getElementById('payload').textContent;
    return '<!doctype html>\n<html lang="it"><head><meta charset="utf-8">' +
      '<meta name="viewport" content="width=device-width, initial-scale=1">' +
      '<title>' + document.title + '</title>' +
      '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?' +
      'family=Montserrat:wght@700;800&family=Lato:wght@400;700&display=swap">' +
      '<style id="css">' + css + '</style></head><body>' +
      '<div class="wrap"><div id="mount"></div></div>' +
      '<dialog id="lb"><img id="lbi" alt=""></dialog>' +
      '<script id="payload" type="application/json">' + pay + '<\/script>' +
      '<script id="state" type="application/json">' +
      JSON.stringify(state) + '<\/script>' +
      '<script id="app">' + app + '<\/script>' +
      '</body></html>';
  }

  var busy = false;
  function save(next, btn) {
    if (!artifact || !canWrite || busy) return;
    busy = true;
    var label = btn ? btn.textContent : null;
    if (btn) { btn.textContent = 'Salvo…'; }
    artifact.publish(documentHtml(next)).then(function () {
      STATE = next; render();           // la vista si ricarica sulla versione nuova
    }).catch(function (e) {
      busy = false;
      if (btn && label) btn.textContent = label;
      if (e && (e.code === 'not_granted' || e.code === 'not_writer')) {
        canWrite = false; render();
      } else if (!e || e.code !== 'conflict') {
        // conflict e' routine: ogni vista si ricarica sulla versione vincente
        alert('Non è stato possibile salvare. Riprova.');
      }
    });
  }

  function setDecision(id, d, btn) {
    var next = JSON.parse(JSON.stringify(STATE));
    var cur = next[id] || {};
    if (!d) { delete cur.decision; } else { cur.decision = d; }
    cur.at = new Date().toLocaleString('it-IT',
      { day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' });
    if (!cur.decision && !cur.note) { delete next[id]; } else { next[id] = cur; }
    save(next, btn);
  }

  function setNote(id, text, btn) {
    var next = JSON.parse(JSON.stringify(STATE));
    var cur = next[id] || {};
    cur.note = text;
    cur.at = new Date().toLocaleString('it-IT',
      { day: 'numeric', month: 'long', hour: '2-digit', minute: '2-digit' });
    if (!cur.decision && !cur.note) { delete next[id]; } else { next[id] = cur; }
    save(next, btn);
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest('button, img[data-zoom]');
    if (!b) return;
    if (b.dataset.step) {
      var id = b.dataset.post, n = PAY.slides[id].length;
      cursor[id] = Math.max(0, Math.min(n - 1, (cursor[id] || 0) + (+b.dataset.step)));
      render();
    } else if (b.dataset.go !== undefined) {
      cursor[b.dataset.post] = +b.dataset.go; render();
    } else if (b.dataset.set !== undefined) {
      setDecision(b.dataset.post, b.dataset.set, b);
    } else if (b.dataset.savenote) {
      var ta = document.querySelector('[data-note="' + b.dataset.savenote + '"]');
      setNote(b.dataset.savenote, ta ? ta.value.trim() : '', b);
    } else if (b.dataset.zoom) {
      document.getElementById('lbi').src = b.src;
      document.getElementById('lbi').alt = b.alt;
      document.getElementById('lb').showModal();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    var post = document.activeElement && document.activeElement.closest('.post');
    if (!post) return;
    var id = post.dataset.post, n = PAY.slides[id].length;
    cursor[id] = Math.max(0, Math.min(n - 1,
      (cursor[id] || 0) + (e.key === 'ArrowRight' ? 1 : -1)));
    render();
    var sel = document.querySelector('.post[data-post="' + id + '"] .nav--n');
    if (sel) sel.focus();
    e.preventDefault();
  });

  var dlg = document.getElementById('lb');
  dlg.addEventListener('click', function () { dlg.close(); });

  render();   // la pagina si disegna subito, senza aspettare il capability

  if (window.claude && window.claude.use) {
    window.claude.use('artifact').then(function (a) {
      if (!a) return;                  // vista che non puo' pubblicare: resta in lettura
      artifact = a; canWrite = true; render();
    }).catch(function () {});
  }
})();
"""


def build():
    slides = {p["id"]: slide_uris(p["prefix"]) for p in POSTS}
    payload = json.dumps({
        "posts": [{k: v for k, v in p.items() if k != "prefix"} for p in POSTS],
        "slides": slides,
    }, ensure_ascii=False)

    return ('<!doctype html>\n<html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Approvazione PED settimana 37</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Montserrat:wght@700;800&family=Lato:wght@400;700&display=swap">'
            '<style id="css">%s</style></head><body>'
            '<div class="wrap"><div id="mount"></div></div>'
            '<dialog id="lb"><img id="lbi" alt=""></dialog>'
            '<script id="payload" type="application/json">%s</script>'
            '<script id="state" type="application/json">{}</script>'
            '<script id="app">%s</script>'
            '</body></html>' % (CSS, payload, APP))


if __name__ == "__main__":
    html = build()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("scritto %s (%.1f MB)" % (OUT, os.path.getsize(OUT) / 1e6))
