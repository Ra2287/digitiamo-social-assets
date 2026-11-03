# -*- coding: utf-8 -*-
"""LAYOUT delle grafiche social: trasforma i dati di plan/week in HTML.

Separazione dei ruoli:
  build_report.py  contenuto (le idee della settimana)
  plan.py          scelte guidate dal contenuto (tipo, layout, barratura,
                   cifra, superficie) — nessun HTML qui dentro
  brand/tokens.py  brand (palette, font, asset, formati)
  templates.py     questo file — layout e composizione
  render.py        HTML -> PNG/PDF

Ogni slide e' un `<div class="slide" data-slug="...">`: render.py legge lo slug
dal DOM, quindi aggiungere/riordinare slide non richiede di toccare il renderer.

## Il linguaggio del 2 novembre 2026

Ricavato dai 12 post di riferimento approvati (brand-spec.md §9). Niente piu'
sfondi Canva con marchio e badge incorporati: il fondo e' CSS (il gradiente
unico, oppure il chiaro #F4F5FA, oppure una foto vera con velatura), e il
layout disegna tutto il resto — occhiello in alto a sinistra, marchio
vettoriale in basso a sinistra, `digitiamo.com` o il contapagine a destra.
Niente badge di categoria, niente filigrana a circuito: tolti di proposito.

Geometria (1200x1500, padding dei mock 104/96/88):
  y  104        occhiello (30px, fisso, fuori dall'auto-fit)
  y  200-1300   zona di contenuto, centrata in verticale (auto-fit)
  y 1348-1412   piede: marchio 230x64 a sinistra, testo a destra

## Auto-fit proporzionale

Il contenitore del contenuto ha `font-size:100px` e i figli sono dimensionati in
`em`. L'auto-fit di render.py scala il font-size del contenitore, quindi tutto
il blocco cambia in proporzione mantenendo la gerarchia tipografica.
"""
import html as htmlmod
import re

from brand import tokens

W, H = tokens.FORMATS["portrait"]
C = tokens.COLORS

# Zona di contenuto standard (x, y, w, h). Fuori restano occhiello e piede.
BOX = (96, 200, 1008, 1100)

# Le superfici. `tone` dice se il fondo e' scuro o chiaro: serve all'alternanza
# (plan.py) e a decidere se il verde e' leggibile (solo su scuro).
SURFACES = {
    "dark": dict(
        tone="dark", bg=tokens.GRADIENT,
        ink=C["paper"], body=C["mist"], muted=C["mist"], eyebrow=C["mist"],
        accent=C["lavender"], data=C["lavender"],
        neutral="rgba(235,238,252,.22)", well="rgba(235,238,252,.08)",
        logo="#FFFFFF", site=C["mist"], site_weight=400,
    ),
    "light": dict(
        tone="light", bg=C["paper"],
        ink=C["ink"], body=C["body_light"], muted=C["muted_light"],
        eyebrow=C["primary"], accent=C["primary"], data=C["primary"],
        neutral="rgba(7,0,17,.14)", well="rgba(62,0,234,.06)",
        logo=C["primary"], site=C["primary"], site_weight=600,
    ),
    # Foto vera + velatura dal blu al quasi nero (mock FotoIrca/FotoIed). La
    # foto la mette `_photo_layer`; qui c'e' il fondo sotto, per i bordi.
    "photo": dict(
        tone="dark", bg=C["ink"],
        ink=C["paper"], body=C["mist"], muted=C["mist"], eyebrow=C["mist"],
        accent=C["lavender"], data=C["lavender"],
        neutral="rgba(235,238,252,.22)", well="rgba(235,238,252,.08)",
        logo="#FFFFFF", site=C["mist"], site_weight=400,
    ),
}

# I nomi delle superfici del sistema precedente, per le correzioni a mano in
# week.py scritte prima del 2 novembre 2026: navy/blu/news erano scuri, il
# cielo era chiaro.
ALIASES = {"navy": "dark", "blue": "dark", "news": "dark", "news_cover": "dark",
           "sky": "light"}


def surface(key):
    return SURFACES[ALIASES.get(key, key)]


# ---------------------------------------------------------------------------
# REGISTRO: quale superficie per quale tipo di slide
# ---------------------------------------------------------------------------
# Dentro un carosello il fondo segue il REGISTRO del contenuto, non un ritmo
# estetico: l'argomentazione (apertura, tesi, citazione, chiusura) sta sullo
# scuro; i fatti da leggere con calma (cifre, elenchi, notizie) sul chiaro.
# Prima e ultima pagina sono sempre scure. Una slide che porta un segnale
# positivo (verde) e' scura comunque: il verde su chiaro non si legge.
LIGHT_KINDS = {"scorecard", "figure", "checklist", "data", "share", "cadence",
               "news_item"}


def surface_for(slide, index, total):
    """La superficie della slide `index` (da 0) di un carosello di `total`."""
    if slide.get("surface"):
        return ALIASES.get(slide["surface"], slide["surface"])
    if slide.get("photo"):
        return "photo"
    if index == 0 or index == total - 1 or slide.get("gain"):
        return "dark"
    return "light" if slide.get("kind") in LIGHT_KINDS else "dark"


# ---------------------------------------------------------------------------
# REGISTRO DEI TIPI DI POST
# ---------------------------------------------------------------------------
# `label` e' l'occhiello di default; `kinds` documenta i layout che il formato
# usa davvero, per chi scrive correzioni a mano in week.py.
POST_TYPES = {
    "data_carousel": dict(label="Carosello dati", format="carousel",
                          kinds=["data_cover", "hook", "scorecard", "figure",
                                 "share", "statement", "cta"]),
    "explainer_carousel": dict(label="Carosello divulgativo", format="carousel",
                               kinds=["hook", "statement", "checklist", "data", "cta"]),
    "compliance_carousel": dict(label="Normativa", format="carousel",
                                kinds=["hook", "data", "checklist", "statement", "cta"]),
    "thought_leadership": dict(label="Thought leadership", format="single",
                               kinds=["single", "quote"]),
    "myth": dict(label="Mito da sfatare", format="single", kinds=["single"]),
    "direct_experience": dict(label="Esperienza diretta", format="single",
                              kinds=["single", "quote"]),
    "mini_lesson": dict(label="Mini-lezione", format="single", kinds=["single"]),
    "news_roundup": dict(label="News AI della settimana", format="carousel",
                         kinds=["news_cover", "news_item", "checklist", "cta"]),
    "closing_list": dict(label="Riflessione di chiusura", format="carousel",
                         kinds=["hook", "checklist", "statement", "cta"]),
}


def esc(s):
    return htmlmod.escape(str(s or ""), quote=False)


_STRIKE_IMG = None


def _strike_img():
    global _STRIKE_IMG
    if _STRIKE_IMG is None:
        _STRIKE_IMG = '<img src="%s" alt="" aria-hidden="true">' % tokens.data_uri(tokens.STRIKE)
    return _STRIKE_IMG


def _word_re(word):
    # Confini di parola anche per le lettere accentate: \b in Python e' Unicode.
    return re.compile(r"(?<!\w)(%s)(?!\w)" % re.escape(esc(word)), re.I)


def accent(s, color, strike=None, gain=None, gain_ok=True):
    """Il testo di un titolo, con i suoi segni.

    - `*parola*` -> parola in colore accento (convenzione dei report);
    - `strike`   -> la parola barrata a mano (una sola, la prima occorrenza).
      Se c'e' la barratura l'accento di colore si spegne: un solo segno per
      titolo, come nei mock;
    - `gain`     -> la parola o cifra in verde, solo se `gain_ok` (fondo scuro).
    Tutto il resto viene escapato.
    """
    parts = re.split(r"\*([^*]+)\*", str(s or ""))
    out = []
    for i, p in enumerate(parts):
        t = esc(p)
        if i % 2 and not strike:
            t = '<span style="color:%s">%s</span>' % (color, t)
        out.append(t)
    html = "".join(out)
    if strike:
        html = _word_re(strike).sub(
            lambda m: '<span class="strike">%s%s</span>' % (m.group(1), _strike_img()),
            html, count=1)
    if gain and gain_ok:
        html = _word_re(gain).sub(
            lambda m: '<span style="color:%s">%s</span>' % (C["green"], m.group(1)),
            html, count=1)
    return html


def _title(s, sf, size, key="title", top="0"):
    return ('<div class="display" style="margin-top:%s;font-size:%s;color:%s;">%s</div>'
            % (top, size, sf["ink"],
               accent(s.get(key), sf["accent"], s.get("strike"), s.get("gain"),
                      sf["tone"] == "dark")))


def _p(top, size, color, text, bold=False):
    """Un paragrafo che sparisce se il testo non c'e'."""
    if not text:
        return ""
    cls = "body body--bold" if bold else "body"
    return ('<div class="%s" style="margin-top:%s;font-size:%s;color:%s;">%s</div>'
            % (cls, top, size, color, esc(text)))


def _num_color(s, sf):
    """Il colore di una cifra: verde SOLO se plan.py l'ha riconosciuta come
    guadagno e il fondo e' scuro; altrimenti l'inchiostro della superficie."""
    return C["green"] if s.get("gain") and sf["tone"] == "dark" else sf["ink"]


def _fig_size(text):
    """Corpo della cifra gigante in base alla lunghezza (mock Dati: 380px)."""
    n = len(str(text or ""))
    return "3.6em" if n <= 3 else "2.8em" if n <= 5 else "2.0em" if n <= 8 else "1.4em"


def _source(s, sf):
    """Fonte in fondo al contenuto, sotto un filetto (mock Interna)."""
    if not s.get("source"):
        return ""
    return ('<div style="margin-top:.40em;height:.06em;width:1.6em;background:%s;"></div>'
            '<div class="body" style="margin-top:.20em;font-size:.26em;color:%s;">Fonte: %s</div>'
            % (sf["accent"], sf["muted"], esc(s["source"])))


def _takeaway(s, sf):
    """Il richiamo «cosa significa per te»: e' cio' che rende una rassegna un
    punto di vista invece di un feed. Opzionale."""
    if not s.get("takeaway"):
        return ""
    return ('<div style="margin-top:.36em;border-left:.05em solid %s;padding-left:.24em;">'
            '<div class="body body--bold" style="font-size:.32em;color:%s;">%s</div></div>'
            % (sf["accent"], sf["ink"], esc(s["takeaway"])))


# ---------------------------------------------------------------------------
# Layout per `kind`: rendono SOLO il contenuto interno, in em.
# Occhiello, marchio e piede li mette _frame().
# ---------------------------------------------------------------------------
def _hook(s, sf):
    return _title(s, sf, "1em") + _p(".36em", ".40em", sf["body"], s.get("subtitle"))


def _data_cover(s, sf):
    """Copertina dati (mock Dati): la cifra gigante, poi cosa misura."""
    return f"""
    <div class="display" style="font-size:{_fig_size(s['figure'])};line-height:.9;letter-spacing:-.04em;
         color:{_num_color(s, sf)};font-variant-numeric:tabular-nums;">{esc(s['figure'])}</div>
    {_p('.10em', '.40em', sf['body'], s.get('unit'), bold=True)}
    {_title(s, sf, '.64em', key='say', top='.24em')}
    {_p('.30em', '.40em', sf['body'], s.get('subtitle'))}"""


def _data(s, sf):
    return f"""
    <div class="display" style="font-size:.92em;color:{_num_color(s, sf)};">{esc(s['datanum'])}</div>
    {_p('.30em', '.40em', sf['ink'], s.get('explain'), bold=True)}
    {_p('.20em', '.30em', sf['body'], s.get('note'))}"""


def _checklist(s, sf):
    items = "".join(f"""
    <div style="display:flex;gap:.28em;align-items:baseline;padding:.18em 0;border-top:2px solid {sf['neutral']};">
      <div class="display" style="flex:0 0 .9em;font-size:.36em;color:{sf['accent']};">{n:02d}</div>
      <div class="body" style="font-size:.32em;color:{sf['ink']};">{esc(t)}</div>
    </div>""" for n, t in enumerate(s["items"], start=1))
    return _title(s, sf, ".64em") + f'<div style="margin-top:.40em;">{items}</div>'


def _statement(s, sf):
    return (_title(s, sf, ".80em")
            + _p(".36em", ".40em", sf["body"], s.get("body"))
            + _p(".24em", ".32em", sf["ink"], s.get("note"), bold=True))


def _cta(s, sf):
    """Chiusura (mock Chiusura): titolo, frase, bottone verde. Il verde del
    bottone e' l'unico uso del verde che non e' un segnale positivo."""
    return f"""{_title(s, sf, '1em')}
    {_p('.40em', '.40em', sf['body'], s.get('cta_sub'))}
    <div style="margin-top:.48em;display:inline-flex;align-items:center;justify-content:center;
         font-size:.38em;line-height:1;padding:.62em 1.1em;border-radius:999px;background:{C['green']};">
      <span class="display" style="font-size:1em;line-height:1;color:{C['ink']};letter-spacing:0;">{esc(s['cta_title'])}</span>
    </div>"""


def _logo_row(names, sf):
    """Marchi di terze parti citati nel post, su pillola chiara: mai ricolorati
    (brand/third-party/README.md), quindi la pillola regge il contrasto."""
    names = [n for n in (names or []) if n in tokens.THIRD_PARTY]
    if not names:
        return ""
    chips = "".join(
        '<div style="display:inline-flex;align-items:center;background:%s;'
        'border-radius:.14em;padding:.10em .22em;">'
        '<img src="%s" style="height:.24em;width:auto;display:block;"></div>'
        % (C["paper"], tokens.data_uri(tokens.THIRD_PARTY[n]))
        for n in names)
    return '<div style="display:flex;gap:.14em;margin-top:.36em;">%s</div>' % chips


def _sandbox_box(label, sf):
    return f"""
    <div style="flex:1;border:.035em dashed {sf['neutral']};border-radius:.16em;
         padding:.30em .10em;text-align:center;">
      <div style="width:.30em;height:.30em;border-radius:50%;background:{sf['data']};margin:0 auto;"></div>
      <div class="eyebrow" style="margin-top:.16em;font-size:.16em;color:{sf['body']};letter-spacing:1px;">{esc(label)}</div>
    </div>"""


def _sandbox_diagram(sf):
    """Due ambienti isolati con un canale nascosto: il meccanismo della notizia
    con forme geometriche, niente illustrazioni di fantasia."""
    return f"""
    <div style="display:flex;align-items:stretch;margin-top:.36em;">
      {_sandbox_box("AGENTE A — VM ISOLATA", sf)}
      <div style="flex:0 0 .78em;display:flex;flex-direction:column;
           align-items:center;justify-content:center;gap:.05em;padding:0 .06em;">
        <div style="width:100%;border-top:.025em dashed {sf['accent']};"></div>
        <div class="eyebrow" style="font-size:.135em;color:{sf['accent']};
             text-align:center;letter-spacing:.5px;line-height:1.3;">CANALE NASCOSTO<br>(CACHE CPU)</div>
        <div style="width:100%;border-top:.025em dashed {sf['accent']};"></div>
      </div>
      {_sandbox_box("AGENTE B — VM ISOLATA", sf)}
    </div>"""


def _single(s, sf):
    """Immagine singola (mock Main/Mito/Chiaro): titolo a manifesto, una frase
    di supporto. `box` e' il nome storico del campo di supporto."""
    diagram = _sandbox_diagram(sf) if s.get("diagram") == "sandbox" else ""
    return (_title(s, sf, "1em") + _logo_row(s.get("logos"), sf) + diagram
            + _p(".36em", ".40em", sf["body"], s.get("box") or s.get("subtitle")))


def _figure(s, sf):
    """Una cifra sola: e' un titolo numerico, non un grafico."""
    delta = ""
    if s.get("delta"):
        delta = (f'<div style="display:flex;align-items:baseline;gap:.10em;margin-top:.20em;">'
                 f'<span class="display" style="font-size:.62em;color:{sf["data"]};">{esc(s["delta"])}</span>'
                 f'{_p("0", ".30em", sf["body"], s.get("delta_note"), bold=True)}</div>')
    return f"""
    <div class="display" style="font-size:{_fig_size(s['figure'])};line-height:.9;letter-spacing:-.04em;
         color:{_num_color(s, sf)};font-variant-numeric:tabular-nums;">{esc(s['figure'])}</div>
    {_p('.12em', '.40em', sf['body'], (s.get('unit') or '').replace(chr(10), ' '), bold=True)}{delta}
    {_p('.30em', '.40em', sf['ink'], s.get('say'))}"""


def _share(s, sf):
    """Proporzione parte/tutto: la forma porta l'informazione."""
    pct = float(s["value"]) / float(s["total"]) * 100
    return f"""
    <div class="display" style="font-size:1.6em;line-height:.9;letter-spacing:-.04em;
         color:{_num_color(s, sf)};font-variant-numeric:tabular-nums;">{esc(s['figure'])}</div>
    {_p('.12em', '.32em', sf['body'], (s.get('unit') or '').replace(chr(10), ' '), bold=True)}
    <div style="margin-top:.36em;display:flex;gap:.045em;height:.40em;">
      <div style="width:{pct:.2f}%;background:{sf['data']};border-radius:.09em 0 0 .09em;"></div>
      <div style="flex:1;background:{sf['neutral']};border-radius:0 .09em .09em 0;"></div>
    </div>
    <div style="display:flex;justify-content:space-between;margin-top:.12em;">
      <div class="eyebrow" style="font-size:.22em;color:{sf['data']};letter-spacing:1px;">{esc(s['label'])} · {pct:.1f}%</div>
      <div class="eyebrow" style="font-size:.22em;color:{sf['body']};letter-spacing:1px;">{esc(s['label_rest'])} · {100-pct:.1f}%</div>
    </div>
    {_p('.36em', '.36em', sf['body'], s.get('say'))}"""


def _scorecard(s, sf):
    """Piu' indicatori su una slide. Righe da 2 (cifra, descrizione) o 3
    (cifra, qualificatore, descrizione): la colonna centrale significa sempre
    la stessa cosa, altrimenti la griglia mente."""
    gains = set(s.get("gains") or [])

    def row(r):
        if len(r) == 3:
            figure, qual, desc = r
            mid = ('<div class="body body--bold" style="font-size:.28em;color:%s;white-space:nowrap;">%s</div>'
                   % (sf["data"], esc(qual)))
            cols = "2.3em 2.2em 1fr"
        else:
            figure, desc = r
            color = C["green"] if figure in gains and sf["tone"] == "dark" else sf["ink"]
            # Cifra sopra, descrizione sotto: una cifra con unita' ("1,7 milioni")
            # in colonna stretta andava a capo e si sovrapponeva.
            return f"""
    <div style="padding:.20em 0;border-top:2px solid {sf['neutral']};">
      <div class="display" style="font-size:.68em;line-height:1.05;letter-spacing:-.03em;white-space:nowrap;
           color:{color};font-variant-numeric:tabular-nums;">{esc(figure)}</div>
      <div class="body" style="margin-top:.10em;font-size:.30em;line-height:1.3;color:{sf['body']};">{esc(desc)}</div>
    </div>"""
        color = C["green"] if figure in gains and sf["tone"] == "dark" else sf["ink"]
        return f"""
    <div style="display:grid;grid-template-columns:{cols};gap:.24em;align-items:baseline;
         padding:.18em 0;border-top:2px solid {sf['neutral']};">
      <div class="display" style="font-size:.52em;line-height:1;letter-spacing:-.03em;
           color:{color};font-variant-numeric:tabular-nums;">{esc(figure)}</div>
      {mid}
      <div class="body" style="font-size:.26em;color:{sf['body']};">{esc(desc)}</div>
    </div>"""

    head = ""
    if s.get("title"):
        head = _title(s, sf, ".64em") + '<div style="height:.32em"></div>'
    elif s.get("figure"):
        head = (f'<div class="display" style="font-size:.80em;color:{sf["ink"]};">{esc(s["figure"])} '
                f'<span style="font-size:.5em;color:{sf["data"]};">{esc(s.get("delta", ""))}</span></div>'
                + _p(".06em", ".26em", sf["body"], s.get("unit")))
    return head + "".join(row(r) for r in s["rows"])


def _news_cover(s, sf):
    return _title(s, sf, "1em") + _p(".36em", ".40em", sf["body"], s.get("subtitle"))


def _news_period(s, sf):
    """Copertina News AI: il periodo come titolo (prima era una pillola sopra
    una copertina Canva con il testo incorporato; ora la copertina e' nostra)."""
    return (f'<div class="display" style="font-size:1em;color:{sf["ink"]};">News AI</div>'
            + _p(".24em", ".44em", sf["body"], s.get("periodo"), bold=True))


def _news_item(s, sf):
    """Una notizia: data e testata, titolo, corpo, e il richiamo «per te»."""
    return f"""
    <div class="eyebrow" style="font-size:.28em;color:{sf['accent']};">{esc(s['categoria'])}</div>
    <div class="display" style="margin-top:.16em;font-size:.64em;color:{sf['ink']};">{esc(s['titolo'])}</div>
    {_p('.24em', '.32em', sf['body'], s.get('corpo'))}
    {_takeaway(s, sf)}"""


def _cadence(s, sf):
    """Due bande di tratti: la densita' rende la cadenza MEDIANA documentata,
    non eventi inventati."""
    def band(days, span):
        return "".join(
            '<div style="position:absolute;top:0;bottom:0;width:2px;left:%.3f%%;'
            'background:%s;"></div>' % ((i * days / span) * 100.0, sf["data"])
            for i in range(int(span / days) + 1))

    span = float(s.get("span", 180))
    rows = "".join(f"""
    <div style="margin-bottom:.26em;">
      <div class="eyebrow" style="font-size:.22em;color:{sf['body']};letter-spacing:1.2px;">{esc(r['label'])}</div>
      <div style="position:relative;height:.92em;margin-top:.10em;
           border-bottom:2px solid {sf['neutral']};">{band(float(r['every']), span)}</div>
    </div>""" for r in s["bands"])
    return (_title(s, sf, ".56em") + f'<div style="margin-top:.30em;">{rows}</div>'
            + _p(".04em", ".26em", sf["body"], s.get("say")))


def _quote(s, sf):
    """Citazione attribuita (mock Citazione). Mai inventata: plan.py la usa
    solo se l'idea porta `citazione` E `autore`."""
    return f"""
    <div class="display" style="font-size:2.6em;line-height:.6;color:{C['lavender']};" aria-hidden="true">“</div>
    <div class="display" style="margin-top:.20em;font-size:.84em;line-height:1.1;color:{sf['ink']};">{esc(s['quote'])}</div>
    {_p('.48em', '.40em', sf['ink'], s.get('who'), bold=True)}
    {_p('.06em', '.32em', sf['body'], s.get('role'))}
    {_p('.30em', '.32em', sf['body'], s.get('say'))}"""


LAYOUTS = {
    "hook": _hook, "data_cover": _data_cover, "data": _data,
    "checklist": _checklist, "statement": _statement, "cta": _cta,
    "single": _single, "figure": _figure, "share": _share,
    "scorecard": _scorecard, "news_cover": _news_cover, "news_item": _news_item,
    "news_period": _news_period, "cadence": _cadence, "quote": _quote,
}


# ---------------------------------------------------------------------------
# Visuali a piena pagina
# ---------------------------------------------------------------------------
def _photo_layer(s):
    """Foto vera a tutta pagina con velatura dal blu al quasi nero (FotoIrca)."""
    return ('<img src="%s" alt="%s" style="position:absolute;left:0;top:0;width:%dpx;'
            'height:%dpx;object-fit:cover;">'
            '<div style="position:absolute;inset:0;background:linear-gradient(180deg,'
            'rgba(62,0,234,.82) 0%%,rgba(62,0,234,.55) 40%%,rgba(7,0,17,.92) 80%%,#070011 100%%);"></div>'
            % (s["photo"], esc(s.get("photo_alt", "")), W, H))


NEWS_BAND = 780   # altezza della fascia visuale delle notizie


def _news_visual(s):
    """La fascia in alto di una notizia: foto (in bianco e nero, moltiplicata
    sul blu e sfumata nel quasi nero, mock News) oppure i marchi ufficiali dei
    prodotti di cui si parla, su carta. Un marchio mancante si dichiara col
    nome: non si ridisegna."""
    if s.get("photo"):
        return ('<div style="position:absolute;left:0;top:0;width:%dpx;height:%dpx;overflow:hidden;">'
                '<img src="%s" alt="%s" style="width:100%%;height:100%%;object-fit:%s;'
                'filter:grayscale(1) contrast(1.1);display:block;">'
                '<div style="position:absolute;inset:0;background:%s;mix-blend-mode:multiply;"></div>'
                '<div style="position:absolute;inset:0;background:linear-gradient(180deg,'
                'rgba(7,0,17,0) 55%%,#070011 100%%);"></div></div>'
                % (W, NEWS_BAND, s["photo"], esc(s.get("photo_alt", "")),
                   s.get("photo_fit", "cover"), C["primary"]))
    items = s.get("marks") or [dict(src=s.get("mark"), label=s.get("mark_alt", ""),
                                    w=s.get("mark_w", 440))]
    cells = []
    for m in items:
        if m.get("src"):
            art = ('<img src="%s" alt="%s" style="width:%dpx;max-width:100%%;height:auto;display:block;">'
                   % (m["src"], esc(m.get("label", "")), m.get("w", 400)))
        else:
            art = ('<div style="font:700 %dpx/1.05 var(--font-display);color:%s;'
                   'letter-spacing:-.02em;text-align:center;">%s</div>'
                   % (m.get("size", 62), C["ink"], esc(m.get("label", ""))))
        note = ('<div style="margin-top:16px;font:400 22px/1.35 var(--font-body);color:%s;'
                'text-align:center;">%s</div>' % (C["muted_light"], esc(m["note"]))
                if m.get("note") else "")
        cells.append('<div style="flex:1;display:flex;flex-direction:column;align-items:center;'
                     'justify-content:center;padding:0 22px;"><div style="height:190px;display:flex;'
                     'align-items:center;justify-content:center;">%s</div>%s</div>' % (art, note))
    sep = '<div style="width:2px;align-self:stretch;margin:150px 0;background:rgba(7,0,17,.13);"></div>'
    return ('<div style="position:absolute;left:0;top:0;width:%dpx;height:%dpx;background:%s;'
            'display:flex;align-items:center;justify-content:center;padding:120px 80px 40px;">%s</div>'
            % (W, NEWS_BAND, C["paper"], sep.join(cells)))


# ---------------------------------------------------------------------------
# Cornice
# ---------------------------------------------------------------------------
def _frame(slug, sf_key, inner, eyebrow=None, right=None, visual="",
           box=BOX, align="center", top_logo=False, left_text=None,
           eyebrow_color=None):
    sf = surface(sf_key)
    x, y, w, h = box
    logo = ('<img src="%s" alt="Digitiamo" style="width:%dpx;height:%dpx;object-fit:contain;'
            'object-position:left center;display:block;">')
    top = ""
    if top_logo:
        top = ('<div style="position:absolute;left:96px;top:104px;">%s</div>'
               % (logo % (tokens.wordmark_uri(sf["logo"]), 300, 84)))
    elif eyebrow:
        top = ('<div class="eyebrow" style="position:absolute;left:96px;right:96px;top:104px;'
               'font-size:30px;line-height:1.25;color:%s;">%s</div>'
               % (eyebrow_color or sf["eyebrow"], esc(eyebrow)))
    left = (('<div class="body" style="font-size:30px;color:%s;">%s</div>' % (sf["site"], esc(left_text)))
            if left_text else logo % (tokens.wordmark_uri(sf["logo"]), 230, 64))
    right_html = ('<div class="body" style="font-size:30px;font-weight:%d;color:%s;">%s</div>'
                  % (sf["site_weight"], sf["site"] if right == "digitiamo.com" else sf["muted"],
                     esc(right))) if right else ""
    return f"""
  <div class="slide" data-slug="{esc(slug)}" style="width:{W}px;height:{H}px;background:{sf['bg']};">
    {visual}
    {top}
    <div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;
         display:flex;flex-direction:column;justify-content:{align};">
      <div class="fit content" data-maxh="{h}" style="font-size:100px;">
        {inner}
      </div>
    </div>
    <div style="position:absolute;left:96px;right:96px;bottom:88px;height:64px;
         display:flex;justify-content:space-between;align-items:center;">
      {left}{right_html}
    </div>
  </div>"""


def _slide_frame(slug, s, key, right):
    """Una slide qualunque nella sua cornice: sceglie visuale e geometria."""
    kind = s.get("kind", "single")
    inner = LAYOUTS[kind](s, surface(key)) + _source(s, surface(key))
    kw = {}
    if key == "photo" and s.get("photo") and kind != "news_item":
        kw = dict(visual=_photo_layer(s), box=(96, 520, 1008, 780), align="flex-end")
    elif kind == "news_item" and (s.get("photo") or s.get("mark") or s.get("marks")):
        kw = dict(visual=_news_visual(s), box=(96, NEWS_BAND + 20, 1008, 1300 - NEWS_BAND - 20),
                  align="flex-start",
                  eyebrow_color=None if s.get("photo") else C["primary"])
        if s.get("credit"):
            right = s["credit"]
    return _frame(slug, key, inner, eyebrow=s.get("eyebrow"), right=right,
                  top_logo=(kind == "cta"),
                  left_text="Segui Digitiamo per il prossimo" if kind == "cta" else None,
                  **kw)


def _document(slides_html, title):
    """Un solo documento con tutte le slide impilate: un browser, N screenshot."""
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><title>{esc(title)}</title>
<style>
{tokens.build_css()}
body {{ background:#e9e9f1; }}
.slide {{ margin:0 auto 40px; }}
</style></head>
<body>
{slides_html}
</body></html>"""


def carousel_html(carousel):
    """Le slide del carosello. La superficie di ogni pagina la sceglie plan.py
    (campo `surface`); se manca — correzioni a mano — vale `surface_for`."""
    slides = carousel["slides"]
    total = len(slides)
    parts = []
    for i, s in enumerate(slides, start=1):
        key = surface_for(s, i - 1, total)
        if s.get("photo") and s.get("kind") == "news_item":
            key = "dark"
        parts.append(_slide_frame("slide%d" % i, s, key, "%02d / %02d" % (i, total)))
    return _document("".join(parts), "Carosello %s" % carousel["slug"])


def singles_html(singles):
    """Le immagini singole. La superficie la sceglie plan.py (alternanza della
    settimana); senza, scuro — o foto, se la singola ne porta una."""
    parts = []
    for s in singles:
        key = ALIASES.get(s.get("surface"), s.get("surface")) or ("photo" if s.get("photo") else "dark")
        parts.append(_slide_frame(s["slug"], s, key, "digitiamo.com"))
    return _document("".join(parts), "Immagini singole")
