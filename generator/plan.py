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

## Il layout segue il contenuto (dal 2 novembre 2026)

Il `format` decide il TIPO di post; la FORMA del contenuto decide il layout.
Regole deterministiche, in quest'ordine, e stampate da `python3 plan.py` per
ogni idea (tipo, layout, barratura, cifra, superficie):

1. **Citazione.** Se l'idea ha `citazione`, serve anche `autore` (altrimenti si
   ferma: una citazione senza nome non si pubblica). Singola -> layout `quote`;
   carosello -> una slide `quote` dopo la copertina. Mai inventata: senza il
   campo non c'e' citazione.
2. **Foto.** Se l'idea ha `immagine` (un file locale DENTRO la repo, percorso
   relativo alla radice; niente URL, il render non va in rete) -> foto vera a
   tutta pagina con velatura blu/nero: la singola, o la copertina del
   carosello. File mancante o fuori dalla repo -> si ferma. `credito`
   opzionale. Altrimenti la grafica e' tipografica.
3. **Barratura** (una parola per titolo, la barratura a mano del sito):
   - `barrato` nell'idea: la parola deve stare nel titolo, non puo' contenere
     cifre (non si barra un dato) e non puo' avere l'iniziale maiuscola fuori
     dalla prima parola (sembra un nome proprio: un cliente non si barra). Se
     una condizione non regge, si ferma;
   - senza `barrato` nessuna barratura, nemmeno nei miti: ricavarla dal
     titolo cancellava parole che servono a capirlo. La `*parola*` accentata
     resta un accento di colore. Se c'e' la barratura, l'accento si spegne.
4. **Cifre.** Una cifra "forte" e' una cifra IN APERTURA di un punto (o
   dell'hook): «42% ...», «800.000 — ...». In un carosello dati che non e' un
   mito, la prima diventa la **copertina dati** (cifra gigante); tre o piu'
   delle restanti -> **scorecard**, una o due -> slide **cifra**. Nelle singole
   la cifra non prende il posto del titolo: l'immagine e' una sola, e il
   titolo e' il post.
5. **Segnale positivo (verde).** Solo se `positivo` nell'idea nomina una
   parola o cifra del titolo/dei punti, oppure se una cifra e' riconosciuta come
   guadagno: comincia con «−»/«-» e parla di ore, giorni, costi, tempo,
   risparmio; oppure con «+» e parla di ricavi, fatturato, vendite, margine,
   produttivita'. Mai per default. Il verde vive solo su fondo scuro, quindi
   una slide con un guadagno e' scura.
6. **Chiaro/scuro.** Fra i post della settimana (in ordine di report) si
   alterna scuro e chiaro, cosi' due post vicini non sembrano uguali; i
   caroselli contano come scuri (la copertina lo e' sempre), la foto come
   scura. Dentro un carosello il fondo segue il registro: argomentazione scura,
   fatti/elenchi chiari, prima e ultima pagina scure
   (`templates.surface_for`).
7. **Poco testo.** Ogni testo ha un budget (`BUDGET`). Le slide usano prima i
   campi brevi `titolo_post`, `sottotitolo_post`, `punti_post`. Senza, il
   titolo oltre 60 caratteri FERMA il piano (non si taglia un titolo a caso);
   supporto, sintesi, voci e righe si tagliano al primo confine naturale, mai
   a meta' parola, e le voci in piu' si tolgono. Le citazioni non si tagliano:
   oltre budget si ferma.
"""
import os
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
# "+117% anno su anno...", "−12 ore a settimana". Volutamente stringente —
# vedi `_rows_from_points`. Il segno meno vale sia «−» sia «-».
FIGURE_RE = re.compile(
    r"^\s*([+~<>−-]?\s?\d[\d.,]*\s*"
    r"(?:%|mld|mln|mila|miliardi|milioni|punti|minuti|ore|giorni|h|€|\$)?)"
    r"(?=[\s—–:,]|$)\s*[—–:,-]?\s*(.+)$"
)

# Oltre questa lunghezza non e' una cifra ma una frase che comincia con un
# numero. 16 tiene «16,3 miliardi» e «1,7 milioni»: l'unita' va comunque sotto
# la cifra (`_split_figure`), quindi non serve stare piu' stretti.
MAX_FIGURE = 16

# Il guadagno si riconosce dal segno E dall'argomento, mai dal solo segno:
# «+117% di attacchi» non e' una buona notizia.
GAIN_DOWN = re.compile(r"\bore\b|\bh\b|\bminuti\b|\bgiorni\b|cost|spes[ae]|tempo|risparmi", re.I)
GAIN_UP = re.compile(r"ricav|fatturat|vendit|margin|produttivit", re.I)

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


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
        if m and len(m.group(1).strip()) <= MAX_FIGURE:
            numeric.append((m.group(1).strip(), m.group(2).strip()))
        else:
            prose.append(p)
    return numeric, prose


def is_gain(figure, desc=""):
    """Una cifra e' un guadagno solo se segno e argomento concordano."""
    f = (figure or "").strip()
    if f[:1] == "+":
        return bool(GAIN_UP.search(f + " " + desc))
    if f[:1] in "−-":
        return bool(GAIN_DOWN.search(f + " " + desc))
    return False


# Le emoji vanno bene nelle caption, non sulle slide (brand-spec.md, divieti):
# il report le usa negli hook («🔥 Il mito: ...»), quindi si tolgono qui.
_EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]\\s*")


def _clean(text):
    return _EMOJI.sub("", text or "").strip()


# ---------------------------------------------------------------------------
# Quanto testo sta su una slide (regola di Fabio, 2/11/2026: «non usare troppo
# testo nelle slide»). Caratteri, asterischi dell'accento esclusi.
# ---------------------------------------------------------------------------
BUDGET = dict(
    occhiello=24,   # l'etichetta in alto
    titolo=60,      # il titolo a manifesto: 3-8 parole, come nei mock
    supporto=110,   # la frase di supporto: UNA frase
    corpo=140,      # il testo della slide di sintesi
    voce=80,        # una voce di elenco
    voci=3,         # quante voci per elenco (le altre si tolgono)
    scorecard=60,   # la descrizione di una riga della scorecard
    citazione=140,  # una citazione: non si taglia mai, si ferma
    cta=90,         # la frase sotto il titolo della CTA
)

# Dove si puo' tagliare: fine frase, due punti, punto e virgola, lineetta.
_BOUNDARY = re.compile(r"[.?!](?=\s)|[:;](?=\s)|\s[—–-](?=\s)")


def fit(text, limit, one_sentence=False):
    """Il testo dentro il suo budget: (testo, nota del taglio o "").

    Taglia al primo confine naturale che lascia almeno 20 caratteri e sta nel
    budget; se non ce n'e', all'ultima parola intera, con «…». Mai a meta'
    parola. Il font non si rimpicciolisce: si accorcia il testo.
    """
    t = " ".join(_clean(text).split())
    note = ""
    if one_sentence:
        parts = re.split(r"(?<=[.?!])\s+(?=[A-ZÀ-Ý«\"])", t, maxsplit=1)
        if len(parts) > 1:
            t, note = parts[0], "tagliato a fine frase"
    if len(t) <= limit:
        return t, note
    for m in _BOUNDARY.finditer(t):
        end = m.start() + (1 if t[m.start()] in ".?!" else 0)
        cand = t[:end].rstrip(" ,;:—–-")
        if len(cand) + 1 > limit:
            break
        if len(cand) >= 20:
            # Tagliata ai due punti o a una lineetta, la frase chiude col punto.
            return (cand if cand[-1] in ".?!" else cand + "."), "tagliato a un confine"
    cut = t[:limit - 1]
    cut = cut[:cut.rindex(" ")] if " " in cut else cut
    return cut.rstrip(" ,;:—–-") + "…", "tagliato a parola intera"


def headline_for(idea):
    """Il titolo della slide: `titolo_post` se c'e', altrimenti `title` se sta
    nel budget. Altrimenti si ferma: un titolo non si taglia a caso."""
    t = idea.get("titolo_post") or idea.get("title") or ""
    n = len(t.replace("*", ""))
    if n > BUDGET["titolo"]:
        if idea.get("titolo_post"):
            raise PlanError("titolo_post di %d caratteri (massimo %d): accorcialo. "
                            "Idea: %r" % (n, BUDGET["titolo"], idea.get("title")))
        raise PlanError(
            "il titolo dell'idea ha %d caratteri, troppi per una slide (massimo %d).\n"
            "Aggiungi `titolo_post` all'idea: un titolo a manifesto di 3-8 parole, "
            "fedele all'idea. Non lo taglio da solo: un titolo tagliato a caso "
            "diventa un post pubblicato sbagliato. Idea: %r"
            % (n, BUDGET["titolo"], idea.get("title")))
    return t


def _support_for(idea, fallback):
    """La frase di supporto: `sottotitolo_post`, oppure il testo lungo tagliato."""
    if idea.get("sottotitolo_post"):
        t = idea["sottotitolo_post"]
        if len(t) > BUDGET["supporto"]:
            raise PlanError("sottotitolo_post di %d caratteri (massimo %d). Idea: %r"
                            % (len(t), BUDGET["supporto"], idea.get("title")))
        return t, ""
    return fit(fallback, BUDGET["supporto"], one_sentence=True)


def _log(d, field, text, budget, note=""):
    d.setdefault("texts", []).append((field, text, budget, note))
    return text


def _is_myth(idea, post_type):
    return post_type == "myth" or bool(idea.get("is_myth"))


# Parole che dopo «quindi» non sono il cuore dell'affermazione: se capita una
# di queste la regola non e' univoca e non si barra niente.
def _strikeable(word, title):
    """None se la parola si puo' barrare, altrimenti il motivo per non farlo."""
    if not word or " " in word.strip():
        return "una parola sola"
    if re.search(r"\d", word):
        return "contiene cifre: un dato non si barra"
    clean = title.replace("*", "")
    first = clean.split()[0] if clean.split() else ""
    if word[:1].isupper() and word.lower() != first.lower():
        return "iniziale maiuscola: sembra un nome proprio, e un cliente non si barra"
    if not re.search(r"(?<!\w)%s(?!\w)" % re.escape(word), clean, re.I):
        return "non compare nel titolo"
    return None


def strike_word(idea, post_type):
    """La parola da barrare nel titolo, o None. Solleva se `barrato` e' invalido."""
    title = headline_for(idea)
    if idea.get("barrato"):
        why = _strikeable(idea["barrato"], title)
        if why:
            raise PlanError("barrato=%r non va (%s). Idea: %r"
                            % (idea["barrato"], why, title))
        return idea["barrato"]
    return None


def photo_for(idea):
    """Il data URI della foto dell'idea, o None. Solleva se il file non va."""
    rel = idea.get("immagine")
    if not rel:
        return None
    if re.match(r"^[a-z]+://", rel, re.I):
        raise PlanError("immagine=%r: serve un file locale nella repo, non un URL "
                        "(il render non va in rete). Idea: %r" % (rel, idea.get("title")))
    path = os.path.realpath(os.path.join(REPO, rel))
    if not path.startswith(REPO + os.sep) or not os.path.isfile(path):
        raise PlanError("immagine=%r non esiste dentro la repo (percorso relativo "
                        "alla radice). Idea: %r" % (rel, idea.get("title")))
    from brand import tokens
    return tokens.data_uri(path)   # os.path.join con un assoluto ignora HERE


def quote_for(idea):
    """La citazione dell'idea come slide, o None. Mai senza autore."""
    if not idea.get("citazione"):
        return None
    if not idea.get("autore"):
        raise PlanError("citazione senza autore: non si pubblica una frase senza "
                        "chi l'ha detta. Idea: %r" % idea.get("title"))
    if len(idea["citazione"]) > BUDGET["citazione"]:
        raise PlanError("citazione di %d caratteri (massimo %d): una citazione non "
                        "si taglia, si sceglie piu' corta. Idea: %r"
                        % (len(idea["citazione"]), BUDGET["citazione"], idea.get("title")))
    return dict(kind="quote", quote=idea["citazione"], who=idea["autore"],
                role=idea.get("ruolo"))


def _split_figure(fig):
    """«16,3 miliardi» -> («16,3», «miliardi»): la cifra gigante e' il numero,
    l'unita' va sotto in piccolo, altrimenti non sta nella larghezza."""
    m = re.match(r"^([+~<>−-]?\s?\d[\d.,]*\s*%?)\s*(.*)$", fig)
    return (m.group(1).strip(), m.group(2).strip()) if m else (fig, "")


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
    """La chiamata all'azione. L'offerta dipende dal registro del post.

    Il bottone non ha la freccia «↗»: Sora non ha quel glifo, e un carattere
    di ripiego in un bottone si vede.
    """
    compliance = post_type == "compliance_carousel"
    return dict(
        kind="cta",
        title=idea.get("cta_title") or CTA_TITLES.get(
            post_type, "Serve qualcuno che se ne *occupi*"),
        cta_title="Scrivici su digitiamo.com" if compliance else "Parliamone su digitiamo.com",
        # Entro BUDGET["cta"] (90): verificato in test_pipeline.py.
        cta_sub=(
            "AI Business Academy: formazione sui casi d'uso reali della tua azienda."
            if compliance else
            "Team Augmentation: AI Engineer senior che lavorano nel tuo team."
        ),
    )


def decide(idea, post_type):
    """Le scelte guidate dal contenuto, prima di comporre le slide.

    Ritorna un dizionario leggibile — e' anche cio' che `python3 plan.py`
    stampa, perche' chi rivede capisca il perche' di ogni grafica.
    """
    # `punti_post`: versioni brevi dei punti, per le slide. I `points` lunghi
    # restano per il report e le caption.
    points = list(idea.get("punti_post") or idea.get("points") or [])
    numeric, prose = _rows_from_points(points)
    hook_fig = FIGURE_RE.match(idea.get("hook") or "")
    if hook_fig and len(hook_fig.group(1).strip()) <= MAX_FIGURE:
        numeric = [(hook_fig.group(1).strip(), hook_fig.group(2).strip())] + numeric
    gains = [f for f, d in numeric if is_gain(f, d)]
    positivo = idea.get("positivo")
    if positivo:
        haystack = " ".join([headline_for(idea)] + points)
        if positivo.lower() not in haystack.lower():
            raise PlanError("positivo=%r non compare ne' nel titolo ne' nei punti: "
                            "il verde segna un guadagno che c'e'. Idea: %r"
                            % (positivo, idea.get("title")))
        gains.append(positivo)
    myth = _is_myth(idea, post_type)
    data_cover = (post_type == "data_carousel" and not myth and bool(numeric))
    return dict(
        headline=headline_for(idea),
        strike=strike_word(idea, post_type),
        photo=photo_for(idea),
        quote=quote_for(idea),
        numeric=numeric, prose=prose, gains=gains,
        positivo=positivo,
        myth=myth,
        data_cover=data_cover,
    )


def slides_for(idea, post_type, d=None):
    """La sequenza di slide per un'idea. Bozza: `week.py` puo' sovrascrivere."""
    d = d or decide(idea, post_type)
    spec = templates.POST_TYPES[post_type]
    label = spec["label"]
    source = idea.get("news") or None
    head = _log(d, "titolo", d["headline"], BUDGET["titolo"])
    title = _accent(head)
    long_support = idea.get("visual_hook") or idea.get("hook") or (idea.get("points") or [""])[0]

    if spec["format"] == "single":
        # Un'immagine sola. Citazione > titolo; la foto, se c'e', fa da fondo.
        if d["quote"]:
            one = dict(d["quote"], eyebrow=label)
            _log(d, "citazione", d["quote"]["quote"], BUDGET["citazione"])
        else:
            box, note = _support_for(idea, long_support)
            one = dict(kind="single", eyebrow=label,
                       box=_log(d, "supporto", box, BUDGET["supporto"], note), title=title,
                       strike=d["strike"], gain=d["positivo"],
                       logos=idea.get("logos"), diagram=idea.get("diagram"))
        if d["photo"]:
            one.update(photo=d["photo"], photo_alt=idea.get("immagine_alt", ""),
                       credit=idea.get("credito"))
        return [one]

    numeric, prose = list(d["numeric"]), d["prose"]
    sub, note = _support_for(idea, long_support)
    if d["data_cover"]:
        fig, desc = numeric.pop(0)
        num, unit = _split_figure(fig)
        say, snote = fit(desc, BUDGET["supporto"], one_sentence=True)
        cover = dict(kind="data_cover", eyebrow=label, figure=num, unit=unit,
                     say=_log(d, "cifra", say, BUDGET["supporto"], snote),
                     subtitle=head.replace("*", ""), gain=fig in d["gains"])
    else:
        cover = dict(kind="hook", eyebrow=label, title=title,
                     subtitle=_log(d, "supporto", sub, BUDGET["supporto"], note),
                     strike=d["strike"], gain=d["positivo"])
    if d["photo"]:
        cover.update(photo=d["photo"], photo_alt=idea.get("immagine_alt", ""))
    out = [cover]
    if d["quote"]:
        out.append(dict(d["quote"], eyebrow="Chi l'ha detto"))

    # Tre o piu' cifre stanno meglio in una scorecard che in tre slide-cifra:
    # si confrontano a colpo d'occhio invece di scorrere.
    if len(numeric) >= 3:
        gains = [f for f, _ in numeric if f in d["gains"]]
        rows = []
        for f, desc in numeric:
            t, n = fit(desc, BUDGET["scorecard"], one_sentence=True)
            rows.append((f, _log(d, "riga %s" % f, t, BUDGET["scorecard"], n)))
        out.append(dict(kind="scorecard", eyebrow="I numeri", rows=rows,
                        gains=gains, gain=bool(gains), source=source))
    else:
        for figure, desc in numeric:
            num, unit = _split_figure(figure)
            t, n = fit(desc, BUDGET["supporto"], one_sentence=True)
            out.append(dict(kind="figure", eyebrow="Il dato", figure=num,
                            unit=unit, say=_log(d, "cifra %s" % figure, t, BUDGET["supporto"], n),
                            source=source, gain=figure in d["gains"]))

    # I punti in prosa vanno in UN elenco di al massimo BUDGET["voci"] voci,
    # ognuna dentro BUDGET["voce"]: i punti in piu' si tolgono (e lo si dice),
    # il font non si rimpicciolisce. Sono frasi intere, non coppie titolo+corpo:
    # ricavarne un titolo tagliandole produceva frammenti.
    if prose:
        items = []
        for p_ in prose[:BUDGET["voci"]]:
            t, n = fit(p_, BUDGET["voce"], one_sentence=True)
            items.append(_log(d, "voce", t, BUDGET["voce"], n))
        if len(prose) > BUDGET["voci"]:
            _log(d, "elenco", "", BUDGET["voci"],
                 "%d voci tolte (massimo %d)" % (len(prose) - BUDGET["voci"], BUDGET["voci"]))
        out.append(dict(kind="checklist", eyebrow="I punti", title=title,
                        items=items, source=source))

    # La chiusura: di default il titolo e' quello del post (ripetuto dalla
    # copertina), il corpo la chiusura accorciata. Ripetere il titolo va bene
    # quando la copertina e' un hook testuale (il mito), ma su un carosello
    # dati la copertina mostra gia' la cifra gigante e il titolo per esteso
    # come sottotitolo: la slide di chiusura che ripete lo stesso titolo
    # risulta una quasi-copia della copertina. `closing_title` lascia
    # scegliere un titolo diverso per la sintesi; senza, il default resta
    # quello di sempre (nessuna settimana precedente cambia).
    #
    # Il corpo di default e' la chiusura lunga del report, troncata al primo
    # confine entro il budget: su una chiusura lunga il taglio puo' fermarsi
    # a una frase introduttiva, che ripete le stesse parole del titolo
    # (es. "procedura" + "avrebbe potuto") senza aggiungere l'informazione
    # concreta che segue nel report. `closing_body` lascia scrivere una
    # versione breve e autonoma apposta per la slide, che non deve ripetere
    # il titolo; senza, il default resta quello di sempre.
    tail = idea.get("closing") or idea.get("myth_closing")
    if tail:
        body, n = fit(idea.get("closing_body") or tail, BUDGET["corpo"])
        closing_title = idea.get("closing_title") or head.replace("*", "")
        if len(closing_title.replace("*", "")) > BUDGET["titolo"]:
            raise PlanError("closing_title di %d caratteri (massimo %d). Idea: %r"
                            % (len(closing_title.replace("*", "")), BUDGET["titolo"], idea.get("title")))
        out.append(dict(kind="statement", eyebrow="In sintesi",
                        title=closing_title,
                        body=_log(d, "sintesi", body, BUDGET["corpo"], n)))

    # Di default ogni post chiude con la CTA (Team Augmentation o AI Business
    # Academy a seconda del registro). `senza_cta` toglie quella slide per
    # un'idea specifica, quando l'offerta non e' pertinente al contenuto:
    # senza il flag non cambia nulla (nessuna settimana precedente cambia).
    if not idea.get("senza_cta"):
        cta = _cta_for(idea, post_type)
        if len(cta["title"].replace("*", "")) > BUDGET["titolo"]:
            raise PlanError("cta_title di %d caratteri (massimo %d). Idea: %r"
                            % (len(cta["title"].replace("*", "")), BUDGET["titolo"], idea.get("title")))
        out.append(cta)
    for i, sl in enumerate(out):
        sl["surface"] = templates.surface_for(sl, i, len(out))
    return out


def _tone(surface):
    return templates.SURFACES[surface]["tone"]


def _alternate(items):
    """Chiaro/scuro fra i post della settimana, nell'ordine del report.

    `items` e' una lista di (formato, slide di copertina). I caroselli e le foto
    sono scuri per costruzione; le singole tipografiche prendono il tono
    opposto al post precedente. Una singola con un guadagno resta scura.
    """
    prev = "light"          # cosi' il primo post della settimana e' scuro
    for fmt, cover in items:
        if fmt == "carousel":
            tone = "dark"
        elif cover.get("photo"):
            cover["surface"], tone = "photo", "dark"
        elif cover.get("kind") == "quote" or cover.get("gain"):
            cover["surface"], tone = "dark", "dark"
        else:
            tone = "dark" if prev == "light" else "light"
            cover["surface"] = tone
        prev = tone


def _why(d, slides, fmt):
    """Una riga che spiega le scelte: la legge chi rivede, non il codice."""
    kinds = [s["kind"] for s in slides]
    surf = [s.get("surface", "?") for s in slides]
    fig = d["numeric"][0][0] if d["numeric"] else "—"
    lines = []
    for field, text, budget, note in d.get("texts", []):
        flag = "  <- %s" % note if note else ""
        if text:
            lines.append("  %-14s %3d/%-3d «%s»%s" % (field, len(text.replace("*", "")),
                                                    budget, text, flag))
        else:
            lines.append("  %-14s %s" % (field, note))
    return ("layout %s · barrato %s · cifra %s%s · superficie %s%s%s"
            % (" > ".join(kinds) if fmt == "carousel" else kinds[0],
               repr(d["strike"]) if d["strike"] else "—", fig,
               " (copertina dati)" if d["data_cover"] else
               " (singola: il titolo resta il post)" if fmt == "single" and d["numeric"] else "",
               "/".join(surf),
               " · verde: %s" % ", ".join(d["gains"]) if d["gains"] else "",
               " · foto" if d["photo"] else "")) + "".join("\n     " + x for x in lines)


# ---------------------------------------------------------------------------
# Il piano della settimana
# ---------------------------------------------------------------------------
def build(ideas, only_priority=True):
    """Da `build_report.ideas` a (caroselli, immagini singole, resoconto).

    Per default lavora solo sulle idee **Prioritario**: le Riserva sono banca
    contenuti e i loro asset non vanno generati finche' non servono — altrimenti
    si occupano nomi file che poi non si possono riusare.

    Il resoconto ha una riga per idea: (numero, titolo, tipo, nota, perche').
    """
    carousels, singles, report, rows = [], [], [], []
    for i, idea in enumerate(ideas, start=1):
        if only_priority and idea.get("badge") != "Prioritario":
            report.append((i, idea.get("title"), None, "saltata (Riserva)", ""))
            continue
        ptype = post_type_for(idea)
        spec = templates.POST_TYPES[ptype]
        d = decide(idea, ptype)
        slides = slides_for(idea, ptype, d)
        slug = _slug(idea, i)
        single = None
        if spec["format"] == "carousel":
            # La caption serve anche ai caroselli: la bozza Buffer e' un post
            # con documento allegato, non un PDF muto.
            # Convenzione: il testo del post e' `CAPTION_<numero dell'idea nel
            # report>` in captions.py. Legata all'indice e non allo slug perche'
            # chi scrive i testi lavora sul report, dove le idee sono numerate.
            carousels.append(dict(slug=slug, post_type=ptype,
                                  caption="CAPTION_%d" % i,
                                  title=idea.get("title") or slug,
                                  category="News AI", slides=slides))
        else:
            single = dict(slug=slug, post_type=ptype,
                          caption="CAPTION_%d" % i, **slides[0])
            singles.append(single)
        rows.append((spec["format"], slides, d, len(report), single))
        report.append((i, idea.get("title"), ptype,
                       "%s · %d slide" % (spec["format"], len(slides)), ""))

    # L'alternanza si decide sull'intera settimana, poi si riporta sulle singole.
    _alternate([(fmt, single or slides[0]) for fmt, slides, _, _, single in rows])
    for fmt, slides, d, at, single in rows:
        if single:
            slides[0]["surface"] = single["surface"]
        report[at] = report[at][:4] + (_why(d, slides, fmt),)
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
    import week

    print("Piano derivato dal report:\n")
    cs, ss, rep = build(build_report.ideas)
    for i, title, ptype, note, why in rep:
        print("  %d. %-34s %-20s %s"
              % (i, (title or "")[:34], ptype or "—", note))
        if why:
            print("     %s" % why)
    print("\n  caroselli: %d   immagini singole: %d" % (len(cs), len(ss)))

    # In un'esecuzione automatica questo output finisce in un log che nessuno
    # sta guardando: deve dire cosa verra' generato DAVVERO, non il piano
    # teorico. Con l'interruttore attivo le due cose sono diverse.
    if getattr(week, "SOSTITUISCE_IL_PIANO", False):
        vc, vs = content()
        print("\n  ATTENZIONE: week.SOSTITUISCE_IL_PIANO e' attivo, quindi il")
        print("  piano qui sopra NON viene usato. Verranno generati:\n")
        for x in vc:
            print("  - carosello  %-34s %-20s %d slide"
                  % (x["slug"][:34], x.get("post_type") or "—", len(x["slides"])))
        for x in vs:
            print("  - singola    %-34s %s" % (x["slug"][:34], x.get("post_type") or "—"))
