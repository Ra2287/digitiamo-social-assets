# -*- coding: utf-8 -*-
import html as htmlmod
from build_report import trends, competitors, ideas, publishing, WEEK_LABEL, GENERATED_ON, C

def esc(s):
    return htmlmod.escape(s, quote=False)

def para_multiline(s):
    parts = s.split("\n\n")
    return "".join(f"<p>{esc(p)}</p>" for p in parts)

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Archivo+Black&display=swap');
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family:'Manrope',sans-serif; color:{C['navy']}; font-size:14.5px; line-height:1.55; }}
.page {{ width:794px; min-height:1123px; padding:64px 60px; position:relative; page-break-after:always; }}
.page:last-child {{ page-break-after:auto; }}

/* COVER */
.cover {{ background:{C['navy']}; color:{C['white']}; display:flex; flex-direction:column; justify-content:space-between; }}
.cover .brandmark {{ font-weight:800; font-size:22px; letter-spacing:0.5px; }}
.cover .eyebrow {{ display:inline-block; background:{C['green']}; color:{C['navy']}; font-weight:800; font-size:13px; letter-spacing:1.5px; text-transform:uppercase; padding:8px 18px; border-radius:999px; margin-top:60px; }}
.cover h1 {{ font-family:'Archivo Black',sans-serif; font-size:52px; line-height:1.12; margin:28px 0 0 0; max-width:640px; }}
.cover .accent {{ color:{C['green']}; }}
.cover .sub {{ font-size:19px; font-weight:500; color:{C['secondary']}; margin-top:24px; max-width:560px; }}
.cover .footer {{ display:flex; justify-content:space-between; align-items:flex-end; border-top:1px solid rgba(255,255,255,0.15); padding-top:24px; font-size:13px; color:{C['secondary']}; }}

/* GENERIC HEADINGS */
h2.section-title {{ font-family:'Archivo Black',sans-serif; font-size:28px; color:{C['navy']}; margin:0 0 6px 0; text-transform:uppercase; letter-spacing:0.3px; }}
.section-num {{ color:{C['brand']}; }}
.section-sub {{ font-size:14px; color:#5b5f8f; margin-bottom:30px; font-weight:500; }}
.divider {{ height:4px; width:56px; background:{C['green']}; border-radius:2px; margin:14px 0 28px 0; }}

/* TOC */
.toc-item {{ display:flex; align-items:baseline; gap:14px; padding:14px 0; border-bottom:1px solid {C['tint']}; }}
.toc-num {{ font-family:'Archivo Black',sans-serif; color:{C['brand']}; font-size:20px; min-width:34px; }}
.toc-label {{ font-weight:700; font-size:16px; flex:1; }}
.toc-desc {{ font-size:12.5px; color:#5b5f8f; }}

/* TREND CARDS */
.trend-card {{ background:{C['white']}; border:1px solid {C['tint']}; border-left:5px solid {C['brand']}; border-radius:10px; padding:20px 24px; margin-bottom:16px; }}
.trend-num {{ display:inline-flex; align-items:center; justify-content:center; width:26px; height:26px; border-radius:50%; background:{C['brand']}; color:#fff; font-weight:800; font-size:13px; margin-right:10px; }}
.trend-title {{ font-weight:800; font-size:16px; display:inline; }}
.trend-label {{ font-weight:800; font-size:11px; text-transform:uppercase; color:{C['brand']}; letter-spacing:0.5px; margin-top:10px; }}
.trend-text {{ font-size:13.3px; margin:4px 0 8px 0; }}
.trend-source {{ font-size:12px; color:{C['secondary']}; font-weight:700; }}
.trend-source a {{ color:{C['brand']}; text-decoration:none; }}

/* COMPETITOR CARDS */
.comp-card {{ background:{C['tint']}; border-radius:12px; padding:24px 26px; margin-bottom:18px; page-break-inside:avoid; }}
.comp-name {{ font-family:'Archivo Black',sans-serif; font-size:18px; color:{C['navy']}; margin-bottom:14px; }}
.comp-row {{ display:flex; gap:14px; margin-bottom:10px; }}
.comp-label {{ min-width:110px; font-weight:800; font-size:11px; text-transform:uppercase; color:{C['brand']}; letter-spacing:0.4px; padding-top:2px; }}
.comp-value {{ font-size:13.3px; flex:1; }}
.comp-angle {{ background:{C['white']}; border-radius:8px; padding:12px 16px; margin-top:6px; border-left:4px solid {C['green']}; }}

/* IDEA CARDS */
.idea-card {{ border:1px solid {C['tint']}; border-radius:14px; padding:26px 28px; margin-bottom:22px; page-break-inside:avoid; }}
.idea-header {{ display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; }}
.badge {{ display:inline-block; font-weight:800; font-size:11px; letter-spacing:0.6px; text-transform:uppercase; padding:6px 16px; border-radius:999px; }}
.badge-priority {{ background:{C['green']}; color:{C['navy']}; }}
.badge-reserve {{ background:{C['tint']}; color:{C['navy']}; border:1px solid {C['secondary']}; }}
.idea-meta {{ font-size:12px; color:{C['secondary']}; font-weight:700; margin-top:6px; }}
.idea-format {{ font-size:12px; color:{C['brand']}; font-weight:800; text-transform:uppercase; letter-spacing:0.4px; }}
.idea-title {{ font-family:'Archivo Black',sans-serif; font-size:20px; color:{C['navy']}; margin:14px 0 10px 0; line-height:1.25; }}
.idea-news {{ font-size:12px; color:#5b5f8f; margin-bottom:14px; }}
.idea-news a {{ color:{C['brand']}; text-decoration:none; }}
.idea-hook {{ background:{C['tint']}; border-radius:8px; padding:14px 18px; font-weight:700; font-size:13.6px; margin-bottom:14px; }}
.idea-points {{ margin:0 0 14px 0; padding-left:0; list-style:none; }}
.idea-points li {{ position:relative; padding-left:22px; margin-bottom:8px; font-size:13.3px; }}
.idea-points li:before {{ content:"\\2022"; color:{C['brand']}; font-weight:800; position:absolute; left:0; }}
.myth-points li:before {{ content:"\\1F539"; font-size:11px; }}
.idea-cta {{ font-size:13.3px; font-weight:700; color:{C['navy']}; border-top:1px dashed {C['secondary']}; padding-top:12px; margin-top:12px; }}
.idea-hashtags {{ font-size:12px; color:{C['brand']}; font-weight:700; margin-top:8px; }}
.idea-note {{ font-size:11.5px; color:#8286b0; font-style:italic; margin-top:10px; }}
.template-tag {{ display:inline-block; background:#fff3d6; color:#8a6400; font-size:10.5px; font-weight:800; padding:3px 10px; border-radius:6px; margin-left:8px; text-transform:uppercase; }}

/* PUBLISHING TABLE */
table.pubtable {{ width:100%; border-collapse:collapse; margin-bottom:30px; }}
table.pubtable th {{ background:{C['navy']}; color:#fff; font-size:11.5px; text-transform:uppercase; letter-spacing:0.4px; padding:12px 14px; text-align:left; }}
table.pubtable td {{ padding:12px 14px; font-size:12.5px; border-bottom:1px solid {C['tint']}; vertical-align:top; }}
table.pubtable tr:nth-child(even) td {{ background:{C['tint']}; }}

.freq-box {{ background:{C['navy']}; color:#fff; border-radius:14px; padding:28px 30px; margin-top:10px; page-break-inside:avoid; }}
.freq-box h3 {{ font-family:'Archivo Black',sans-serif; font-size:18px; margin:0 0 12px 0; color:{C['green']}; }}
.freq-box p {{ font-size:13px; margin:0 0 10px 0; color:#dfe1fb; }}
.freq-stats {{ display:flex; gap:20px; margin-top:16px; }}
.freq-stat {{ background:rgba(255,255,255,0.06); border-radius:10px; padding:14px 18px; flex:1; }}
.freq-stat .num {{ font-family:'Archivo Black',sans-serif; font-size:26px; color:{C['green']}; }}
.freq-stat .lbl {{ font-size:11px; color:#c7c9f2; margin-top:4px; }}

.pagefoot {{ position:absolute; bottom:28px; left:60px; right:60px; display:flex; justify-content:space-between; font-size:10.5px; color:#9498c4; border-top:1px solid {C['tint']}; padding-top:10px; }}
"""

def cover_page():
    return f"""
<div class="page cover">
  <div>
    <div class="brandmark">Digitiamo</div>
    <span class="eyebrow">Piano Editoriale Digitale</span>
    <h1>PED Digitiamo<br>Settimana del<br><span class="accent">{esc(WEEK_LABEL)}</span></h1>
    <div class="sub">Analisi del settore AI/software tech, mosse dei competitor e piano contenuti LinkedIn pronto all'uso.</div>
  </div>
  <div class="footer">
    <div>Generato il {esc(GENERATED_ON)}</div>
    <div>Ad uso interno — Digitiamo</div>
  </div>
</div>
"""

def toc_page():
    items = [
        ("01", "Trend del settore", "8-10 sviluppi chiave della settimana, con fonti"),
        ("02", "Analisi competitor", "5 player che si sono mossi in modo significativo"),
        ("03", "Idee di post (PED)", "7 idee: 5 Prioritario + 2 Riserva, arco narrativo settimanale"),
        ("04", "Suggerimenti di pubblicazione", "Calendario, orari e ragionamento sulla frequenza"),
    ]
    rows = "".join(f"""
    <div class="toc-item">
      <div class="toc-num">{n}</div>
      <div class="toc-label">{esc(l)}</div>
      <div class="toc-desc">{esc(d)}</div>
    </div>""" for n, l, d in items)
    return f"""
<div class="page">
  <h2 class="section-title">Sommario</h2>
  <div class="divider"></div>
  {rows}
  <div style="margin-top:40px; background:{C['tint']}; border-radius:12px; padding:22px 24px;">
    <div style="font-weight:800; font-size:13px; color:{C['brand']}; text-transform:uppercase; margin-bottom:8px;">Nota metodologica</div>
    <div style="font-size:13px; color:#3a3d6b;">Le notizie sono state raccolte da fonti dirette (comunicati stampa, testate tech verificate) negli ultimi 7 giorni. Le idee di post sono pensate come un vero piano editoriale settimanale con un arco narrativo, non come una lista di formati intercambiabili — l'ordine e il collegamento tra i post è intenzionale.</div>
  </div>
</div>
"""

def trends_page():
    cards = ""
    for i, t in enumerate(trends, start=1):
        src = f'<a href="{t["url"]}">{esc(t["source"])} →</a>' if t.get("url") else esc(t["source"])
        cards += f"""
    <div class="trend-card">
      <div><span class="trend-num">{i}</span><span class="trend-title">{esc(t['title'])}</span></div>
      <div class="trend-label">Cosa è successo</div>
      <div class="trend-text">{esc(t['what'])}</div>
      <div class="trend-label">Perché è rilevante</div>
      <div class="trend-text">{esc(t['why'])}</div>
      <div class="trend-source">Fonte: {src}</div>
    </div>"""
    # split into two pages roughly
    half = (len(trends) + 1) // 2
    cards_list = []
    running = ""
    count = 0
    pages = []
    per_page = 5
    for i in range(0, len(trends), per_page):
        chunk = trends[i:i+per_page]
        chunk_html = ""
        for j, t in enumerate(chunk, start=i+1):
            src = f'<a href="{t["url"]}">{esc(t["source"])} →</a>' if t.get("url") else esc(t["source"])
            chunk_html += f"""
    <div class="trend-card">
      <div><span class="trend-num">{j}</span><span class="trend-title">{esc(t['title'])}</span></div>
      <div class="trend-label">Cosa è successo</div>
      <div class="trend-text">{esc(t['what'])}</div>
      <div class="trend-label">Perché è rilevante</div>
      <div class="trend-text">{esc(t['why'])}</div>
      <div class="trend-source">Fonte: {src}</div>
    </div>"""
        header = f"""<h2 class="section-title"><span class="section-num">01.</span> Trend del settore</h2>
  <div class="section-sub">Gli sviluppi più rilevanti degli ultimi 7 giorni nel mondo AI/software tech</div>
  <div class="divider"></div>""" if i == 0 else f"""<h2 class="section-title" style="font-size:18px;">Trend del settore (continua)</h2><div class="divider"></div>"""
        pages.append(f"""
<div class="page">
  {header}
  {chunk_html}
</div>""")
    return "".join(pages)

def competitors_page():
    cards = ""
    for c in competitors:
        cards += f"""
    <div class="comp-card">
      <div class="comp-name">{esc(c['name'])}</div>
      <div class="comp-row"><div class="comp-label">Cosa ha fatto</div><div class="comp-value">{esc(c['what'])}</div></div>
      <div class="comp-row"><div class="comp-label">Posizionamento</div><div class="comp-value">{esc(c['positioning'])}</div></div>
      <div class="comp-angle"><b style="color:{C['navy']};">Spunto per Digitiamo:</b> {esc(c['angle'])}</div>
    </div>"""
    return f"""
<div class="page">
  <h2 class="section-title"><span class="section-num">02.</span> Analisi competitor</h2>
  <div class="section-sub">Chi si è mosso in modo significativo questa settimana, e come differenziarsi</div>
  <div class="divider"></div>
  {cards}
</div>
"""

def idea_card_html(idea, index):
    badge_class = "badge-priority" if idea["badge"] == "Prioritario" else "badge-reserve"
    template_tag = '<span class="template-tag">Template da personalizzare</span>' if idea.get("is_template") else ""
    news_link = f'<a href="{idea["news_url"]}">{esc(idea["news"])} →</a>' if idea.get("news_url") else esc(idea["news"])

    if idea.get("is_myth"):
        body = f'<div class="idea-hook">{esc(idea["hook"])}</div>'
        body += para_multiline(idea["myth_body"])
        body += '<ul class="idea-points myth-points">' + "".join(f"<li>{esc(p)}</li>" for p in idea["points"]) + "</ul>"
        body += f"<p>{esc(idea['myth_closing'])}</p>"
    else:
        body = f'<div class="idea-hook">{esc(idea["hook"])}</div>'
        body += '<ul class="idea-points">' + "".join(f"<li>{esc(p)}</li>" for p in idea["points"]) + "</ul>"
        if idea.get("closing"):
            body += f"<p>{esc(idea['closing'])}</p>"

    hashtags_html = "" if idea.get("no_hashtags") else f'<div class="idea-hashtags">{esc(idea["hashtags"])}</div>'
    note_html = f'<div class="idea-note">{esc(idea["carousel_note"])}</div>' if idea.get("carousel_note") else ""
    if idea.get("no_hashtags"):
        note_html += '<div class="idea-note">Formato "mito da sfatare": nessun hashtag di chiusura, per coerenza di stile.</div>'

    return f"""
    <div class="idea-card">
      <div class="idea-header">
        <div>
          <span class="badge {badge_class}">{esc(idea['badge'])}</span>{template_tag}
          <div class="idea-meta">{esc(idea['day'])}</div>
        </div>
        <div class="idea-format">{esc(idea['format'])}</div>
      </div>
      <div class="idea-title">{index}. {esc(idea['title'])}</div>
      <div class="idea-news">Notizia di riferimento: {news_link}</div>
      {body}
      <div class="idea-cta">CTA: {esc(idea['cta'])}</div>
      {hashtags_html}
      {note_html}
    </div>"""

def ideas_pages():
    priority = [i for i in ideas if i["badge"] == "Prioritario"]
    reserve = [i for i in ideas if i["badge"] == "Riserva"]
    pages = []

    intro = f"""<h2 class="section-title"><span class="section-num">03.</span> Idee di post (PED)</h2>
  <div class="section-sub">7 idee — 5 Prioritario (nucleo settimanale) + 2 Riserva (banca contenuti) — organizzate come vero arco narrativo</div>
  <div class="divider"></div>
  <div style="background:{C['tint']}; border-radius:10px; padding:16px 20px; margin-bottom:24px; font-size:12.5px;">
    <b>Arco narrativo della settimana:</b> apertura di autorevolezza (nessuna vendita) → mito da sfatare sul vibe coding → carosello dati su compliance AI Act → esperienza diretta di code review con agenti → mini-lezione divulgativa su RAG. I due contenuti di riserva restano pronti come banca contenuti.
  </div>"""

    idx = 1
    cards_html = ""
    for i in priority:
        cards_html += idea_card_html(i, idx)
        idx += 1

    pages.append(f'<div class="page">{intro}{cards_html[:0]}</div>')  # placeholder, will restructure below

    # Rebuild properly: one idea per chunk, packing 2 per page roughly based on length; simplify: 1-2 per page
    pages = []
    idx = 1
    buf = intro
    count_on_page = 0
    for i in priority + reserve:
        card = idea_card_html(i, idx)
        buf += card
        idx += 1
        count_on_page += 1
        if count_on_page >= 1:
            pages.append(f'<div class="page">{buf}</div>')
            buf = ""
            count_on_page = 0
    if buf:
        pages.append(f'<div class="page">{buf}</div>')
    return "".join(pages)

def publishing_page():
    rows = "".join(f"""
      <tr>
        <td><b>{esc(p['day'])}</b></td>
        <td>{esc(p['time'])}</td>
        <td>{esc(p['format'])}</td>
        <td>{esc(p['reason'])}</td>
      </tr>""" for p in publishing)
    return f"""
<div class="page">
  <h2 class="section-title"><span class="section-num">04.</span> Suggerimenti di pubblicazione</h2>
  <div class="section-sub">Calendario consigliato per la settimana, basato su best practice B2B tech LinkedIn</div>
  <div class="divider"></div>
  <table class="pubtable">
    <tr><th>Giorno</th><th>Orario</th><th>Formato</th><th>Motivazione</th></tr>
    {rows}
  </table>

  <div class="freq-box">
    <h3>Quante volte pubblicare a settimana?</h3>
    <p>I benchmark 2026 (Socialinsider, Buffer, Dataslayer, Gallium) indicano <b>3-5 post/settimana</b> come soglia ottimale per crescere con qualità costante — la modalità "growth mode". Pubblicare tutti i giorni ("authority builder") aumenta ulteriormente le impression solo se si mantiene alto il dwell time su ogni contenuto: altrimenti l'algoritmo penalizza anche i post successivi.</p>
    <p>Per questo lo schema di questa settimana è <b>5 idee Prioritario + 2 di Riserva</b>, non 7 pubblicazioni obbligatorie. Le riserve sono banca contenuti da attivare solo se c'è margine editoriale reale.</p>
    <div class="freq-stats">
      <div class="freq-stat"><div class="num">3-5</div><div class="lbl">post/settimana ottimali (growth mode)</div></div>
      <div class="freq-stat"><div class="num">5</div><div class="lbl">idee Prioritario questa settimana</div></div>
      <div class="freq-stat"><div class="num">2</div><div class="lbl">idee di Riserva, pronte all'uso</div></div>
    </div>
  </div>

  <div style="margin-top:26px; background:{C['tint']}; border-radius:10px; padding:18px 22px; font-size:12.5px;">
    <b>Altre best practice applicate:</b> evitare link esterni nel corpo del post (metterli nel primo commento se necessario), rispondere ai commenti nella prima ora per massimizzare la spinta dell'algoritmo, prediligere martedì-giovedì per il traffico professionale più alto, riservare le finestre 7:30-9:30 e 12:00-13:00 ai contenuti a più alta priorità.
  </div>
</div>
"""

def build_full_html():
    pages = cover_page() + toc_page() + trends_page() + competitors_page() + ideas_pages() + publishing_page()
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<style>{CSS}</style>
</head>
<body>
{pages}
</body>
</html>"""

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(here, "report.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_full_html())
    print("HTML generated:", out_path)
