# -*- coding: utf-8 -*-
"""Date della settimana e correzioni a mano alle grafiche.

## Cosa NON sta piu' qui

I contenuti delle slide. Vengono **derivati dal report** da `plan.py`: si
scrivono le idee in `build_report.py` e le grafiche seguono, senza che nessuno
scelga i template. Prima erano scritti a mano qui, ed e' il motivo per cui ogni
esecuzione del lunedi' finiva per reinventare il design.

## Cosa sta qui

1. **Le date.** `DATE` finisce nei nomi dei file, quindi e' una scelta
   deliberata e non si ricava da una stringa in prosa del report.
2. **Le correzioni.** Dopo la revisione umana una slide puo' aver bisogno di una
   sistemata: si dichiara qui, con lo **stesso slug** che il piano assegna (lo
   stampa `python3 plan.py`), e la versione a mano vince su quella derivata.

Esempio di correzione:

    CAROUSELS = [
        dict(slug="idea3-l-ai-nelle-aziende", post_type="data_carousel",
             category="News AI", slides=[...]),   # sequenza completa a mano
    ]

Convenzione nei testi: `*parola*` rende la parola in colore accento. Il piano
accenta l'ultima parola del titolo per default; scrivendo gli asterischi a mano
si sceglie la parola giusta.
"""
import base64
import os

# Settimana di pubblicazione. Finisce nei nomi dei file: non riusare mai una
# combinazione data+slug gia' pubblicata (vedi CLAUDE.md).
DATE = "2026-09-07"
WEEK_LABEL = "7 - 13 settembre 2026"

# A quale settimana appartengono le CORREZIONI qui sotto. Controllato solo se ce
# ne sono: serve a non riapplicare a una settimana nuova un aggiustamento
# scritto per quella vecchia, che passerebbe inosservato perche' i nomi dei file
# sarebbero comunque nuovi.
OVERRIDES_FOR = "2026-09-07"

# Rifacimenti: slug del post -> numero di revisione. Ciclo human-in-the-loop.
#
# Vuoto = prima generazione del lunedi'. Se un post va RIFATTO dopo la revisione
# umana, segnalo qui con 1 (poi 2, 3...): i suoi file prendono il suffisso `-r1`,
# quindi stessa settimana e stesso post ma **URL nuovo**. Poi la bozza Buffer va
# rifatta sul nuovo URL, e quella vecchia cancellata.
#
# Perche' non sovrascrivere: la bozza esistente punta al vecchio URL e Buffer
# scarica l'asset al momento della pubblicazione effettiva. Sovrascrivere
# cambierebbe in silenzio l'immagine di una bozza gia' vista da una persona.
#
# Perche' per post e non per settimana: se va rifatto un post solo, gli altri
# restano quelli approvati e le loro bozze non vanno toccate.
#
# Gli slug sono quelli stampati da `python3 plan.py`. Esempio:
#   REDO = {"idea2-la-sicurezza-dell-ai": 1}
REDO = {}

# I post approvati NON corrispondono alle idee del report: tre trend sono stati
# fusi in una rassegna, e le idee 3-4-5 del report sono state scartate in
# revisione. Quindi valgono solo le voci dichiarate qui sotto.
#
# Non e' la modalita' normale. Di norma le grafiche si derivano dal report
# (CLAUDE.md, regola 2) e questo resta False.
SOSTITUISCE_IL_PIANO = True

# ---------------------------------------------------------------------------
# Marchi di terzi usati nei post di questa settimana
# ---------------------------------------------------------------------------
# Uso editoriale: dicono di chi parla la notizia. Mai ricolorati, mai accostati
# al marchio Digitiamo in modo che suggerisca una partnership. Provenienza in
# brand/third-party/README.md. Vanno su campo chiaro perche' le varianti
# disponibili sono a inchiostro scuro.
_TP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand", "third-party")


def svg_uri(name):
    with open(os.path.join(_TP, name), "rb") as f:
        return "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")


OPENAI = svg_uri("openai-light.svg")
GOOGLE = svg_uri("google-wordmark.svg")
QWEN = svg_uri("qwen-light.svg")
ZHIPU = svg_uri("zhipu-light.svg")
EUFLAG = svg_uri("eu-flag.svg")

MARK_FIELD = "linear-gradient(160deg,#ffffff,#eef2ff)"


NEWSAI = dict(
    slug="newsai-settimana-37",
    caption="CAPTION_NEWSAI",
    title="Tre lanci in una settimana, tre strategie diverse",
    post_type="news_roundup",
    category="News AI",
    slides=[
        # Copertina tipografica sul campo navy: il marchio vero e' incorporato
        # nello sfondo. Sostituisce lo sfondo Canva `newsai_cover_bg`, che
        # aveva "News AI" scritto in un grotesque fuori brand e non
        # modificabile.
        dict(kind="news_cover",
             eyebrow="News della settimana",
             title="Tre lanci in una settimana. Tre strategie *diverse*",
             subtitle="GPT-6 Astra, Gemini 3.8 Flash e la convergenza "
                      "Zhipu/Alibaba: cosa raccontano questi annunci a chi deve "
                      "scegliere la propria stack tecnologica."),

        # Le pagine di spiegazione. L'occhiello porta data e testata: in una
        # rassegna dire quando e da chi e' informazione, non decorazione.
        dict(
            kind="news_item",
            categoria="3 settembre · OpenAI",
            titolo="GPT-6 Astra: fra «salto generazionale» e rollout confuso",
            corpo="Greg Brockman lo definisce «un salto generazionale». Ma "
                  "l'accesso iniziale resta ai soli clienti del programma "
                  "Daybreak, e Forbes parla di «curioso falso avvio» fra "
                  "annuncio e reale disponibilità.",
            takeaway="Fra hype e prontezza per l'azienda c'è una distanza: "
                     "serve saper distinguere cosa è già utilizzabile da cosa "
                     "è ancora una demo.",
            marks=[dict(src=OPENAI, label="OpenAI", w=430)], mark_bg=MARK_FIELD,
            source="Forbes, CNBC · 3/9/2026",
        ),
        dict(
            kind="news_item",
            categoria="2 settembre · Google",
            titolo="Gemini 3.8 Flash: il quarto Flash in 106 giorni",
            corpo="Google rilascia la quarta versione «Flash» in poco più di "
                  "tre mesi, mentre il modello di punta Gemini 3.5 Pro — "
                  "promesso per giugno — resta assente.",
            takeaway="Un'architettura indipendente dal modello protegge "
                     "dall'instabilità delle roadmap dei vendor: un endpoint da "
                     "aggiornare, non un prodotto da riscrivere.",
            marks=[dict(src=GOOGLE, label="Google", w=400)], mark_bg=MARK_FIELD,
            source="Fortune, 9to5Google · 2–3/9/2026",
        ),
        dict(
            kind="news_item",
            categoria="26–28 agosto · Zhipu e Alibaba",
            titolo="GLM-5.3 e Qwen3.8: due lab, la stessa architettura",
            corpo="Zhipu AI e Alibaba convergono in modo indipendente sulla "
                  "stessa scelta architetturale, con un pricing open-weight "
                  "molto aggressivo.",
            takeaway="Costi più bassi abbassano la barriera per sperimentare, "
                     "ma aprono domande di governance e sovranità del dato per "
                     "le aziende europee.",
            marks=[
                dict(src=ZHIPU, label="Zhipu AI", w=150, note="Zhipu AI · GLM"),
                dict(src=QWEN, label="Alibaba Qwen", w=190, note="Qwen · Alibaba"),
            ],
            mark_bg=MARK_FIELD,
            source="MarkTechPost, OrcaRouter · 26–28/8/2026",
        ),

        # Il filo comune, su cielo: e' il momento di respiro prima della
        # chiusura, e su fondo chiaro un elenco numerato si legge meglio.
        dict(kind="checklist",
             eyebrow="Il filo comune",
             title="Tre strategie diverse. Una sola domanda per chi *sceglie*",
             items=[
                 "OpenAI punta sull'annuncio della svolta, ma la disponibilità "
                 "reale resta limitata.",
                 "Google itera velocissimo su modelli leggeri e rimanda ancora "
                 "il proprio flagship.",
                 "I lab cinesi competono su prezzo e apertura, spostando la "
                 "scelta su governance e compliance.",
             ]),

        dict(kind="cta",
             title="Il modello giusto non è sempre l'*ultimo* uscito",
             cta_title="Scrivici",
             cta_sub="Il Team Augmentation di Digitiamo aiuta a scegliere e "
                     "integrare l'AI adatta al proprio caso d'uso, senza "
                     "rincorrere ogni annuncio."),
    ],
)


# ---------------------------------------------------------------------------
# 2. Model fatigue — dentro il brand, con copertina, testo asciutto
# ---------------------------------------------------------------------------
# Il trapianto integrale dello stile Fathom (fondo nero, tipografia propria) era
# fuori brand e troppo testuale. Resta solo il segno che funzionava — la densita'
# che nasce dai dati — come `kind` dentro i template di brand.
FATIGUE = dict(
    slug="model-fatigue-settimana-37",
    caption="CAPTION_FATIGUE",
    title="Model fatigue: un modello ogni 11 giorni",
    post_type="data_carousel",
    category="News AI",
    slides=[
        # Copertina: solo la tesi. Nient'altro.
        dict(kind="hook", surface="navy",
             eyebrow="Model fatigue",
             title="Nel 2023 un modello ogni 37 giorni. Oggi ogni *11*",
             subtitle="Quattro laboratori hanno rilasciato un modello importante "
                      "nella stessa settimana."),
        dict(kind="cadence", surface="blue",
             eyebrow="La cadenza",
             title="Stessa finestra di sei mesi",
             bands=[
                 dict(label="2023 · un rilascio ogni 37,5 giorni", every=37.5),
                 dict(label="2026 · un rilascio ogni 11 giorni", every=11.0),
             ],
             say="I tratti sono la cadenza mediana documentata, non i singoli rilasci.",
             source="CNBC 6/9/2026"),
        dict(kind="figure", surface="navy",
             eyebrow="Il divario",
             figure="11", unit="giorni\nfra un rilascio\ne il successivo",
             delta="da 37,5", delta_note="nel 2023",
             say="Il ciclo di valutazione di un'azienda non si è accorciato allo "
                 "stesso modo.",
             source="CNBC 6/9/2026"),
        dict(kind="quote", surface="blue",
             eyebrow="Come reagisce chi compra",
             quote="Se una startup vuole valutare dieci modelli AI per un certo "
                   "compito, magari ne prende cinque.",
             who="Suresh Vasudevan",
             role="CEO, Clockwork Systems — citato da CNBC",
             say="Metà delle opzioni non viene guardata. La scelta premia la "
                 "notorietà del fornitore, non il caso d'uso.",
             source="CNBC 6/9/2026"),
        dict(kind="statement", surface="navy",
             eyebrow="Il costo vero",
             title="Chi rincorre ogni rilascio paga la *migrazione*, non il progresso",
             body="Prompt da ritarare, valutazioni da rifare, comportamenti "
                  "diversi sui casi limite.",
             note="Chi ha un'architettura indipendente dal fornitore aggiorna un "
                  "endpoint. Gli altri riscrivono — e lo rifanno undici giorni dopo."),
        dict(kind="cta", surface="navy",
             title="Non serve il modello più nuovo. Serve *poterlo cambiare*",
             cta_title="Parliamone ↗",
             cta_sub="Team Augmentation Digitiamo: AI Engineer e Dev senior che "
                     "progettano l'astrazione fra il prodotto e il fornitore di "
                     "modelli — e la documentano."),
    ],
)


# ---------------------------------------------------------------------------
# 3. Agenti AI — riframato sul meccanismo
# ---------------------------------------------------------------------------
AGENTI = dict(
    slug="agenti-produzione-settimana-37",
    caption="CAPTION_AGENTI",
    title="Perche gli agenti AI smettono di funzionare",
    post_type="data_carousel",
    category="News AI",
    slides=[
        dict(kind="hook", surface="navy",
             eyebrow="Agenti AI in produzione",
             title="Gli agenti non si schiantano. *Derivano*",
             subtitle="Il motivo per cui un agente AI smette di funzionare in "
                      "azienda non è quasi mai «non ha capito». È molto più "
                      "banale — e molto più prevedibile."),
        dict(kind="statement", surface="blue",
             eyebrow="Il fallimento tipico",
             title="Funziona per due mesi. Poi *scade una chiave*",
             body="Un agente entra in produzione e lavora. Dopo 30-60 giorni un "
                  "token di accesso scade o viene revocato: le API ruotano le "
                  "credenziali su cicli di circa novanta giorni.",
             note="Un invalid_grant di Google o un INVALID_SESSION_ID di "
                  "Salesforce da un refresh token scaduto non si recupera "
                  "riprovando. La logica di retry non serve a niente.",
             source="Documentazione tecnica sull'autenticazione degli agenti, 2026"),
        dict(kind="checklist", surface="blue",
             eyebrow="Perché non te ne accorgi",
             title="I fallimenti sono *silenziosi*",
             items=[
                 "Il tool restituisce un risultato vuoto e il modello lo legge "
                 "come «nessun dato», non come errore",
                 "Scritture parziali che corrompono lo stato dei passaggi "
                 "successivi, senza nessun messaggio d'errore",
                 "Percorsi di recupero inventati dal modello, che somigliano a "
                 "progresso e non lo sono",
             ],
             source="Analisi sulle modalità di fallimento degli agenti, 2026"),
        dict(kind="statement", surface="navy",
             eyebrow="Il problema di inventario",
             title="Gli *agenti orfani* sono la norma, non l'eccezione",
             body="Agenti il cui creatore non è più in azienda — account "
                  "disattivato — ma le cui credenziali restano attive. È uno dei "
                  "riscontri più frequenti nelle verifiche degli inventari "
                  "aziendali del 2026.",
             note="Non è una vulnerabilità esotica: è la conseguenza di non aver "
                  "mai deciso chi possiede il ciclo di vita di quelle chiavi.",
             source="Rilievi su inventari di agenti in azienda, 2026"),
        dict(kind="statement", surface="blue",
             eyebrow="E quando è ostile",
             title="Le catene di strumenti sono la *superficie d'attacco*",
             body="Chiamate a strumenti singolarmente innocue, orchestrate in "
                  "sequenza, producono un esito malevolo. La ricerca STAC ha "
                  "misurato tassi di successo oltre il 90% su 483 casi.",
             note="Casi reali documentati nel 2025-2026: una RCE nel protocollo "
                  "MCP (CVE-2025-6514, CVSS 9,6), un'iniezione via hooks in un "
                  "agente di coding (CVE-2025-59536, CVSS 8,7), un pacchetto "
                  "malevolo pubblicato come MCP server.",
             source="STAC (arXiv) · CVE-2025-6514 · CVE-2025-59536"),
        dict(kind="cta", surface="navy",
             title="Il prototipo lo fa l'AI. *La produzione è un mestiere*",
             cta_title="Parliamone ↗",
             cta_sub="Team Augmentation Digitiamo: figure senior che progettano "
                     "rotazione delle credenziali, allarmi sui fallimenti "
                     "silenziosi, inventario degli agenti e fallback controllato. "
                     "La parte che nessuna demo mostra."),
    ],
)


# ---------------------------------------------------------------------------
# 4. EU AI Act — ricostruito con le date concrete
# ---------------------------------------------------------------------------
AI_ACT = dict(
    slug="ai-act-settimana-37",
    caption="CAPTION_AIACT",
    title="AI Act: cosa si applica adesso e cosa e stato rinviato",
    post_type="compliance_carousel",
    category="News AI",
    slides=[
        dict(
            kind="news_item", surface="news",
            categoria="Normativa",
            titolo="AI Act: le scadenze si spostano, il perimetro si allarga",
            corpo="Il pacchetto Omnibus è in vigore dal 27 luglio 2026. Ha "
                  "rinviato gli obblighi sull'alto rischio, ma nello stesso "
                  "testo ha esteso la rilevazione dei bias a tutti i sistemi AI. "
                  "«Hanno rinviato tutto» è una lettura sbagliata.",
            photo=EUFLAG, photo_alt="Bandiera dell'Unione Europea",
            photo_fit="contain", photo_bg="#003399", photo_pad=54,
            credit="Bandiera UE · pubblico dominio",
            source="Regolamento (UE) 2026/1744",
        ),
        dict(kind="checklist", surface="blue",
             eyebrow="Cosa si applica già",
             title="In vigore *adesso*, non rinviabile",
             items=[
                 "Trasparenza (art. 50): dichiarare quando l'utente interagisce "
                 "con un sistema AI — dal 2 agosto 2026",
                 "Watermarking dei contenuti generati: dal 2 agosto 2026, con "
                 "tolleranza per i sistemi preesistenti fino al 2 dicembre 2026",
                 "Divieti sui casi inaccettabili e obblighi sui modelli "
                 "generalisti: già in vigore da febbraio e agosto 2025",
             ],
             source="Regolamento (UE) 2026/1744, art. 50"),
        dict(kind="scorecard", surface="navy",
             eyebrow="Cosa è stato rinviato",
             figure="3", delta="proroghe",
             unit="le nuove scadenze sull'alto rischio",
             rows=[
                 ("2 dic 2027", "Allegato III",
                  "sistemi autonomi: selezione del personale, credito, istruzione, infrastrutture critiche"),
                 ("2 ago 2028", "Allegato I",
                  "AI incorporata in prodotti già regolati: dispositivi medici, macchinari, giocattoli"),
                 ("2 ago 2027", "Sandbox",
                  "gli spazi di sperimentazione regolamentata"),
             ],
             source="Regolamento (UE) 2026/1744"),
        dict(kind="statement", surface="blue",
             eyebrow="Il dettaglio che quasi nessuno nota",
             title="La rilevazione dei bias è stata *estesa*, non ridotta",
             body="Prima riguardava i soli sistemi ad alto rischio. Ora si "
                  "applica a tutti i sistemi AI e ai modelli generalisti — nello "
                  "stesso pacchetto che ha rinviato le scadenze.",
             note="In cambio l'obbligo di alfabetizzazione AI è stato "
                  "ammorbidito: da «garantire» un livello di competenza a "
                  "«sostenerne lo sviluppo».",
             source="Regolamento (UE) 2026/1744"),
        dict(kind="statement", surface="navy",
             eyebrow="Cosa fare col tempo guadagnato",
             title="La proroga serve a *costruire*, non ad aspettare",
             body="Le scadenze differite non togliono il lavoro: lo spostano. "
                  "Chi arriva al dicembre 2027 senza aver mappato dove e come "
                  "usa l'AI avrà meno tempo, non più.",
             note="E c'è un cambio di perimetro da valutare adesso: la "
                  "definizione di «componente di sicurezza» è stata restretta, "
                  "quindi alcune AI incorporate nei prodotti escono dagli "
                  "obblighi. Capire se la propria ci rientra è un'analisi, non "
                  "un'opinione.",
             source="Regolamento (UE) 2026/1744"),
        dict(kind="cta", surface="navy",
             title="La compliance progressiva costa meno di una *rincorsa*",
             cta_title="Scrivici adesso ↗",
             cta_sub="AI Business Academy Digitiamo: mappare dove l'azienda usa "
                     "l'AI, capire quali obblighi si applicano davvero al proprio "
                     "caso e documentarlo — prima che diventi una scadenza."),
    ],
)

# I quattro post approvati in revisione. Sono caroselli: nessuna immagine
# singola questa settimana.
CAROUSELS = [NEWSAI, FATIGUE, AGENTI, AI_ACT]
SINGLES = []
