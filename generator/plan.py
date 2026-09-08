# -*- coding: utf-8 -*-
"""Dal report alle slide: sceglie il template giusto e prepara le grafiche.

## Il problema che risolve

Il flusso del lunedi' e': Claude scrive il report con le idee di post, ne mette
una versione su git e una su Buffer come bozza, e un umano corregge. Finora la
parte grafica richiedeva che qualcuno **scegliesse a mano** il tipo di post e i
layout in `week.py` — e per questo ogni esecuzione finiva per riscrivere l'HTML
da zero, con un design diverso ogni settimana.

Qui il ponte c'e' gia': ogni idea nel report ha un campo `format`. Questo modulo
lo legge e ne deriva il tipo di post e la sequenza di slide, usando i template
esistenti. Il risultato e' una **bozza**: `week.py` puo' sovrascrivere qualunque
pezzo, ed e' il posto dove l'umano corregge.

## Perche' per parole chiave e non per corrispondenza esatta

Le stringhe di `format` cambiano fra un'esecuzione e l'altra. Reali, dai due
report esistenti:

    "Thought leadership — apertura settimana"
    "Thought leadership / grande quadro di settore (nessuna vendita)"
    "Mito da sfatare"
    "Mito da sfatare (stile Talent Garden, senza hashtag di chiusura)"
    "Carosello / documento dati"
    "Carosello/documento LinkedIn (data-point multipli)"

Una tabella di corrispondenze esatte si romperebbe alla prima riformulazione.

## Cosa fa quando non sa

**Si ferma e lo dice.** Un formato non riconosciuto solleva un errore con la
stringa esatta, cosi' chi esegue aggiunge una regola o corregge la dicitura del
report. Indovinare un template produrrebbe un post pubblicato nel formato
sbagliato, che e' peggio di un'esecuzione interrotta.
"""
import re

import templates

# ---------------------------------------------------------------------------
# Formato del report -> tipo di post
# ---------------------------------------------------------------------------
# In ordine: vince la prima che corrisponde. Le espressioni girano sul `format`
# in minuscolo. `carosello` sta in cima perche' un'idea puo' essere descritta
# come "carosello divulgativo": vince il contenitore, non il registro.
FORMAT_RULES = [
    (r"carosell|documento linkedin", "_carousel"),   # risolto sotto per registro
    (r"mito da sfatare|mito:", "myth"),
    (r"thought leadership", "thought_leadership"),
    (r"esperienza diretta|case study", "direct_experience"),
    (r"divulgativ|mini-lezione|mini lezione|datapizza", "mini_lesson"),
    (r"lista|riflession|community|recap|chiusura", "closing_list"),
]

# Quale carosello, in base a cosa parla l'idea. Cerca nel titolo e nel testo.
CAROUSEL_RULES = [
    (r"rassegna|news della settimana|notizie della settimana|roundup|"
     r"tre lanci|piu' lanci|piu lanci", "news_roundup"),
    (r"ai act|normativ|complianc|regolament|gdpr|obblig", "compliance_carousel"),
    (r"cos'è|cosa vuol dire|spiegat|come funziona", "explainer_carousel"),
]
CAROUSEL_DEFAULT = "data_carousel"

# Una cifra in apertura di punto: "89 miliardi...", "76% dei progetti...",
# "+117% anno su anno...". Volutamente strinigente — vedi `_rows_from_points`.
FIGURE_RE = re.compile(
    r"^\s*([+~<>]?\s?[\d][\d.,]*\s*(?:%|mld|mln|mila|miliardi|milioni|punti|€|\$)?)"
    r"\s*[—–:,-]?\s*(.+)$"
)


class PlanError(Exception):
    """Il report non dice abbastanza per scegliere un template."""


def _text_of(idea):
    """Tutto il testo dell'idea, per le regole che guardano il contenuto."""
    parts = [idea.get("title", ""), idea.get("hook", ""), idea.get("news", ""),
             idea.get("myth_body", "") or "", idea.get("closing", "") or ""]
    parts += list(idea.get("points", []) or [])
    return " ".join(parts).lower()


def post_type_for(idea):
    """Il tipo di post per un'idea del report. Solleva se non e' deducibile."""
    fmt = (idea.get("format") or "").lower()
    if not fmt:
        raise PlanError("idea senza campo `format`: %r" % idea.get("title"))

    for pattern, target in FORMAT_RULES:
        if re.search(pattern, fmt):
            if target != "_carousel":
                return target
            # Il tema si cerca nel testo dell'idea **e** nella dicitura del
            # formato: "ai act" compare nei contenuti, "rassegna" invece solo
            # nel formato ("Carosello / rassegna news della settimana").
            body = _text_of(idea) + " " + fmt
            for cpat, ctype in CAROUSEL_RULES:
                if re.search(cpat, body):
                    return ctype
            return CAROUSEL_DEFAULT

    raise PlanError(
        "formato non riconosciuto: %r (idea: %r).\n"
        "Aggiungi una regola in plan.FORMAT_RULES oppure allinea la dicitura "
        "nel report. Non tiro a indovinare: un template sbagliato diventa un "
        "post pubblicato sbagliato." % (idea.get("format"), idea.get("title"))
    )


# ---------------------------------------------------------------------------
# Idea -> slide
# ---------------------------------------------------------------------------
def _headline(text, limit=64):
    """Un titolo breve ricavato da un punto del report.

    Taglia su un confine naturale (fine frase, due punti, punto e virgola,
    lineetta) e **mai in mezzo a una parola**: il primo tentativo produceva
    titoli come «la quota che usa almeno una tecnologia AI e' piu' che
    raddopp», con l'accento pure sulla parola troncata.

    Ritorna (titolo, intero) dove `intero` dice se il taglio e' avvenuto su un
    confine vero. Se non lo e', il chiamante evita di accentare: accentare una
    parola tagliata e' peggio che non accentare.
    """
    t = " ".join((text or "").split())
    if not t:
        return "", True
    for sep in (". ", ": ", "; ", " — ", " – "):
        if sep in t:
            first = t.split(sep)[0].strip()
            if 12 <= len(first) <= limit:
                return first, True
    if len(t) <= limit:
        return t.rstrip(" .,;:"), True
    cut = t[:limit]
    if " " in cut:
        cut = cut[:cut.rindex(" ")]
    return cut.rstrip(" .,;:"), False


def _accent(title):
    """Evidenzia l'ultima parola del titolo, se il titolo e' abbastanza lungo.

    E' un default, non una regola tipografica: la convenzione `*parola*` resta
    disponibile in `week.py` per accentare la parola giusta a mano. Sui titoli
    reali dei due report l'ultima parola e' quasi sempre quella che porta il
    senso ("...sta per sparire", "...gli sviluppatori senior?").
    """
    if "*" in title:                     # gia' accentato a mano: non toccare
        return title
    words = title.split()
    if len(words) < 4:
        return title
    return " ".join(words[:-1]) + " *" + words[-1] + "*"


def _slug(idea, index):
    base = re.sub(r"[^a-z0-9]+", "-", (idea.get("title") or "").lower()).strip("-")
    return "idea%d-%s" % (index, "-".join(base.split("-")[:4]) or "post")


def _rows_from_points(points):
    """Separa i punti che aprono con una cifra da quelli in prosa.

    La soglia e' deliberatamente alta: si estrae **solo** la cifra iniziale e il
    resto diventa descrizione. Provare a ricavare anche un qualificatore dalla
    prosa produrrebbe colonne che significano cose diverse riga per riga —
    l'errore che la scorecard esiste per evitare.
    """
    numeric, prose = [], []
    for p in points:
        m = FIGURE_RE.match(p)
        if m and len(m.group(1).strip()) <= 12:
            numeric.append((m.group(1).strip(), m.group(2).strip()))
        else:
            prose.append(p)
    return numeric, prose


# Titoli di chiusura per tipo di post. Il report non ha un campo per questo, e
# "Ne parliamo?" era troppo generico. Sono **default da rileggere**: la CTA e' la
# prima cosa che un umano dovrebbe correggere dopo la generazione.
CTA_TITLES = {
    "news_roundup": "Il modello giusto non e' sempre l'*ultimo* uscito",
    "data_carousel": "I numeri non dicono *cosa farne*",
    "compliance_carousel": "La compliance progressiva costa meno di una *rincorsa*",
    "explainer_carousel": "Capirlo è il primo passo. *Applicarlo* è il mestiere",
    "closing_list": "Nessuno di questi punti richiede un modello *migliore*",
}


def _cta_for(idea, post_type):
    """La chiamata all'azione. L'offerta dipende dal registro del post."""
    compliance = post_type == "compliance_carousel"
    return dict(
        kind="cta",
        title=idea.get("cta_title") or CTA_TITLES.get(
            post_type, "Serve qualcuno che se ne *occupi*"),
        cta_title="Scrivici adesso ↗" if compliance else "Parliamone ↗",
        cta_sub=(
            "AI Business Academy Digitiamo: formazione e progetti mirati sui casi "
            "d'uso reali della tua azienda."
            if compliance else
            "Team Augmentation Digitiamo: AI Engineer e sviluppatori senior che si "
            "integrano nel tuo team."
        ),
    )


def slides_for(idea, post_type):
    """La sequenza di slide per un'idea. Bozza: `week.py` puo' sovrascrivere."""
    spec = templates.POST_TYPES[post_type]
    label = spec["label"]
    source = idea.get("news") or None

    if spec["format"] == "single":
        # Un'immagine sola: titolo grande piu' il fatto che lo sostiene.
        box = idea.get("hook") or (idea.get("points") or [""])[0]
        return [dict(kind="single", eyebrow=label, box=box,
                     title=_accent(idea.get("title", "")))]

    points = list(idea.get("points") or [])
    out = [dict(kind="hook", eyebrow=label,
                title=_accent(idea.get("title", "")),
                subtitle=idea.get("hook", ""))]

    numeric, prose = _rows_from_points(points)

    # Tre o piu' cifre stanno meglio in una scorecard che in tre slide-cifra:
    # si confrontano a colpo d'occhio invece di scorrere.
    if len(numeric) >= 3:
        out.append(dict(kind="scorecard", eyebrow="I numeri",
                        rows=numeric, source=source))
    else:
        for figure, desc in numeric:
            out.append(dict(kind="figure", eyebrow="Il dato", figure=figure,
                            unit="", say=desc, source=source))

    # I punti in prosa vanno in un ELENCO, non in slide con titolo.
    #
    # I `points` del report sono frasi esplicative complete, non coppie
    # titolo+corpo. Il primo tentativo ne ricavava un titolo tagliandole, e
    # produceva frammenti come «Ma il 72% delle grandi aziende ha progetti
    # avanzati contro il». La forma corretta per una frase intera e' una voce
    # di elenco: il layout `checklist` esiste e la regge senza inventare nulla.
    head, _ = _headline(idea.get("title", ""), 58)
    for i in range(0, len(prose), 3):
        chunk = prose[i:i + 3]
        out.append(dict(kind="checklist", eyebrow="I punti",
                        title=_accent(head) if i == 0 else head,
                        items=chunk, source=source))

    # La chiusura: il titolo viene dal titolo dell'IDEA (corto e affidabile),
    # non ricavato tagliando la prosa della chiusura.
    tail = idea.get("closing") or idea.get("myth_closing")
    if tail:
        out.append(dict(kind="statement", eyebrow="In sintesi",
                        title=head, body=tail))

    out.append(_cta_for(idea, post_type))
    return out


# ---------------------------------------------------------------------------
# Il piano della settimana
# ---------------------------------------------------------------------------
def build(ideas, only_priority=True):
    """Da `build_report.ideas` a (caroselli, immagini singole).

    Per default lavora solo sulle idee **Prioritario**: le Riserva sono banca
    contenuti e i loro asset non vanno generati finche' non servono — altrimenti
    si occupano nomi file che poi non si possono riusare.
    """
    carousels, singles, report = [], [], []
    for i, idea in enumerate(ideas, start=1):
        if only_priority and idea.get("badge") != "Prioritario":
            report.append((i, idea.get("title"), None, "saltata (Riserva)"))
            continue
        ptype = post_type_for(idea)
        spec = templates.POST_TYPES[ptype]
        slides = slides_for(idea, ptype)
        slug = _slug(idea, i)
        if spec["format"] == "carousel":
            # La caption serve anche ai caroselli: la bozza Buffer e' un post
            # con documento allegato, non un PDF muto.
            carousels.append(dict(slug=slug, post_type=ptype,
                                  caption="CAPTION_%d" % i,
                                  title=idea.get("title") or slug,
                                  category="News AI", slides=slides))
        else:
            singles.append(dict(slug=slug, post_type=ptype,
                                caption="CAPTION_%d" % i, **slides[0]))
        report.append((i, idea.get("title"), ptype,
                       "%s · %d slide" % (spec["format"], len(slides))))
    return carousels, singles, report


def content():
    """I contenuti grafici della settimana: report + correzioni a mano.

    Unica fonte per il renderer **e** per la pubblicazione su Buffer. Prima il
    merge stava in `render.py`, che importa playwright: `publish_buffer.py` non
    poteva usarlo e leggeva `week.SINGLES` per conto suo — cioe' una lista
    vuota, ora che le grafiche vengono dal report. Risultato: zero bozze create,
    e nessun errore.

    `week.py` sovrascrive una voce dichiarandola in `CAROUSELS` o `SINGLES` con
    lo **stesso slug** assegnato dal piano: la versione a mano vince. Uno slug
    che il piano non conosce viene aggiunto.
    """
    import build_report
    import week

    over_c = {c["slug"]: c for c in getattr(week, "CAROUSELS", [])}
    over_s = {x["slug"]: x for x in getattr(week, "SINGLES", [])}

    # `week.SOSTITUISCE_IL_PIANO` = il piano derivato dal report non vale per
    # questa settimana: valgono solo le voci dichiarate a mano.
    #
    # Serve al ciclo con l'umano. Una persona deve poter dire "pubblica questi,
    # non quelli": succede quando i post approvati non corrispondono alle idee
    # del report — per esempio perche' tre trend sono stati fusi in una
    # rassegna, o perche' un'idea e' stata scartata in revisione. Senza questa
    # possibilita' l'unica via d'uscita e' falsificare il report perche' produca
    # l'elenco giusto, che e' peggio.
    if getattr(week, "SOSTITUISCE_IL_PIANO", False):
        if not (over_c or over_s):
            raise SystemExit(
                "week.SOSTITUISCE_IL_PIANO e' attivo ma CAROUSELS e SINGLES "
                "sono vuoti: non ci sarebbe niente da generare.")
        return list(over_c.values()), list(over_s.values())

    carousels, singles, _ = build(build_report.ideas)
    carousels = [over_c.get(c["slug"], c) for c in carousels]
    singles = [over_s.get(x["slug"], x) for x in singles]
    used = {c["slug"] for c in carousels} | {x["slug"] for x in singles}
    return (carousels + [c for s_, c in over_c.items() if s_ not in used],
            singles + [x for s_, x in over_s.items() if s_ not in used])


if __name__ == "__main__":
    import build_report
    print("Piano derivato dal report:\n")
    cs, ss, rep = build(build_report.ideas)
    for i, title, ptype, note in rep:
        print("  %d. %-34s %-20s %s"
              % (i, (title or "")[:34], ptype or "—", note))
    print("\n  caroselli: %d   immagini singole: %d" % (len(cs), len(ss)))
