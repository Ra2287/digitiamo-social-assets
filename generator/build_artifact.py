# -*- coding: utf-8 -*-
"""Compone l'artifact condivisibile per l'approvazione dei post della settimana.

Perche' un artifact e non la pagina locale: `preview.html` sta sul disco di chi
lo genera. Questo va condiviso con chi approva — ed e' il punto del flusso PED,
dove la pubblicazione richiede sempre un via libera umano, PRIMA che le bozze
arrivino su Buffer (vedi CLAUDE.md, "Revisione e approvazione").

La pagina **ricorda le decisioni**: usa il capability `artifact`, quindi chi
apre dopo vede cosa e' stato approvato e cosa no. Lo stato non sta nel DOM: sta
in un blocco JSON, e ogni azione rigenera il documento e lo ripubblica.

I contenuti NON sono scritti a mano qui: vengono da `plan.content()` (la
stessa fonte del renderer e di `publish_buffer.py`) e dai PNG gia' generati in
`settimane/<data>/`. Questo script non genera ne' modifica nessuna grafica:
mostra solo quello che `render.py` ha gia' prodotto.

Uso: python3 build_artifact.py   -> scrive artifact.html, per la settimana
corrente (week.DATE)
"""
import base64
import io
import json
import os

from PIL import Image

import build_report
import names
import plan
import templates
import week

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "artifact.html")

# Larghezza di revisione: 760px basta per giudicare, e tiene il documento
# leggero — conta, perche' ogni approvazione ripubblica l'intera pagina.
REVIEW_W, REVIEW_H, QUALITY = 760, 950, 90


def _slot_for(index):
    """giorno/ora suggeriti per l'idea N-esima, da build_report.publishing."""
    pubs = getattr(build_report, "publishing", None) or []
    if 1 <= index <= len(pubs):
        p = pubs[index - 1]
        return "%s · %s" % (p.get("day", "—"), p.get("time", "—"))
    return "—"


def gather_posts():
    """Le idee Prioritario della settimana corrente, con i loro asset reali.

    Ogni voce punta ai PNG/PDF che `render.py` ha gia' scritto in
    `settimane/<data>/` (via `names.py`, la stessa fonte del renderer):
    questa pagina non ne genera di nuovi, mostra solo quelli.
    """
    carousels, singles = plan.content()
    by_slug_c = {c["slug"]: c for c in carousels}
    by_slug_s = {s["slug"]: s for s in singles}

    posts = []
    for i, idea in enumerate(build_report.ideas, start=1):
        if idea.get("badge") != "Prioritario":
            continue
        slug = plan._slug(idea, i)
        label = templates.POST_TYPES.get(
            (by_slug_c.get(slug) or by_slug_s.get(slug) or {}).get("post_type"),
            {}).get("label", "—")
        if slug in by_slug_c:
            c = by_slug_c[slug]
            paths = [os.path.join(ROOT, names.carousel_slide(slug, k + 1))
                     for k in range(len(c["slides"]))]
        elif slug in by_slug_s:
            paths = [os.path.join(ROOT, names.single(slug))]
        else:
            # Idea Prioritario che il piano non ha generato (caso anomalo:
            # succede solo se SOSTITUISCE_IL_PIANO ha sostituito l'elenco).
            continue
        posts.append(dict(
            id=slug,
            title=(idea.get("titolo_post") or idea.get("title")
                   or slug).replace("*", ""),
            origin="idea %d del report" % i,
            format=label,
            slot=_slot_for(i),
            note=(idea.get("sottotitolo_post") or idea.get("hook") or
                  idea.get("visual_hook") or ""),
            flag=("Parola barrata: «%s»." % idea["barrato"]
                  if idea.get("barrato") else None),
            paths=paths,
        ))
    return posts


def slide_uris(paths):
    out = []
    for p in paths:
        if not os.path.exists(p):
            continue
        im = Image.open(p).convert("RGB").resize((REVIEW_W, REVIEW_H), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        out.append("data:image/jpeg;base64," +
                    base64.b64encode(buf.getvalue()).decode("ascii"))
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
      '<div class="eyebrow">Piano editoriale · ' + esc(PAY.weekLabel) + '</div>' +
      '<h1>' + PAY.posts.length + ' post da approvare</h1>' +
      '<p class="lede">Contenuti dal report PED, con la sezione di origine ' +
      'indicata su ogni post. Sfoglia le slide, poi segna la tua decisione: ' +
      'resta salvata per chi apre dopo. Le bozze su Buffer si creano solo dopo ' +
      'che ogni post qui sotto è "Approvato" (o le modifiche chieste in nota ' +
      'sono state applicate).</p>' +
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

    h += '<p class="foot">' + (canWrite
        ? 'Le decisioni si salvano nella pagina: chi la apre dopo le vede.'
        : 'Hai accesso in sola lettura: puoi sfogliare e commentare, non cambiare le decisioni.') +
      ' Le slide vengono dalla pipeline del repository (<code>render.py</code>): ' +
      'questa pagina non le genera e non le modifica — per cambiarle, scrivi ' +
      'cosa cambiare nella nota del post.</p>';

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
    posts = gather_posts()
    slides = {p["id"]: slide_uris(p.pop("paths")) for p in posts}
    payload = json.dumps({
        "weekLabel": week.WEEK_LABEL,
        "posts": posts,
        "slides": slides,
    }, ensure_ascii=False)

    return ('<!doctype html>\n<html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Approvazione PED %s</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Montserrat:wght@700;800&family=Lato:wght@400;700&display=swap">'
            '<style id="css">%s</style></head><body>'
            '<div class="wrap"><div id="mount"></div></div>'
            '<dialog id="lb"><img id="lbi" alt=""></dialog>'
            '<script id="payload" type="application/json">%s</script>'
            '<script id="state" type="application/json">{}</script>'
            '<script id="app">%s</script>'
            '</body></html>' % (week.DATE, CSS, payload, APP))


if __name__ == "__main__":
    html = build()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("scritto %s (%.1f MB)" % (OUT, os.path.getsize(OUT) / 1e6))
