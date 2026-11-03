# -*- coding: utf-8 -*-
"""Genera l'HTML del report PED settimanale Digitiamo."""
import html

# La palette NON e' dichiarata qui: viene dai token di brand. Il report interno
# non e' stato ridisegnato col linguaggio del 2 novembre 2026, quindi usa la
# palette precedente (LEGACY_COLORS); i post usano tokens.COLORS.
from brand.tokens import LEGACY_COLORS as _C  # noqa: E402

C = {
    "navy": _C["navy"],
    "brand": _C["blue"],
    "secondary": _C["blue_soft"],
    "tint": _C["tint"],
    "green": _C["green"],
    "white": _C["white"],
}

WEEK_LABEL = "2 – 8 novembre 2026"
GENERATED_ON = "Lunedì 2 novembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 26 ottobre - 1 novembre 2026, verificate su fonte diretta
# (non sui riassunti aggregatori). Filo conduttore della settimana: due
# questioni di fiducia che si inseguono su fronti diversi — quanto ci si puo'
# fidare di un risultato che un modello dichiara di aver raggiunto (le
# "scoperte scientifiche" di OpenAI, ancora in gran parte da verificare, e la
# rivolta della comunita' matematica che ne e' seguita) e quanto ci si puo'
# fidare dei confini che un fornitore dichiara di aver messo attorno al
# proprio agente (i browser "integrati" forzabili in cinque tool di AI coding,
# e l'ondata di violazioni "Black October" sulle piattaforme per sviluppatori
# AI). Le notizie di finanziamento (S-1 di Anthropic, buyout Microsoft) restano
# sullo sfondo come contesto sulla scala degli impegni in gioco, non come
# perno di nessuna idea di post.
trends = [
    dict(
        title="OpenAI rivendica tre scoperte scientifiche ottenute da un'AI, ancora da verificare",
        what="Il 26 ottobre OpenAI ha annunciato tre risultati prodotti da un suo modello interno non ancora rilasciato: una dimostrazione della congettura del \"local smoothing\" in ogni dimensione (che risolverebbe anche le congetture di Kakeya e di restrizione di Stein), una confutazione dell'Exponential Time Hypothesis in informatica teorica, e una dimostrazione di esistenza per la teoria quantistica dei campi di Yang-Mills. I risultati di matematica e informatica sono stati formalizzati nel linguaggio Lean (verificabili da un computer) e pubblicati; il materiale di fisica resta invece riservato in attesa che un gruppo di fisici guidato dal premio Nobel David Gross ne verifichi la correttezza.",
        why="\"Annunciato\" e \"confermato\" restano due cose diverse, ed e' esattamente la distinzione che la settimana successiva, con la rivolta della comunita' matematica (vedi trend successivo), mostra quanto conti.",
        source="Tech Insider",
        url="https://tech-insider.org/openai-three-science-discoveries-eth-kakeya-qcd-2026/",
    ),
    dict(
        title="La comunità matematica si spacca sulle centinaia di \"dimostrazioni\" AI di OpenAI: solo il 42% è verificabile da computer",
        what="Il 6 ottobre OpenAI aveva già pubblicato 722 manoscritti con soluzioni dichiarate a oltre 370 problemi aperti di matematica e informatica teorica, generati testando il modello su circa 4.000 problemi. Il 7 ottobre un errore di segno ha fatto ritirare tre manoscritti (il catalogo è sceso a 719), con altri 14 rivisti; al 13 ottobre solo circa 300 dei 719 risultati (42%) avevano una dimostrazione formalizzata in Lean, verificabile automaticamente riga per riga — gli altri restano affermazioni non ancora controllate in modo indipendente. Terence Tao, uno dei nove matematici (tra cui Timothy Gowers, Martin Hairer ed Edward Witten) chiamati da OpenAI stessa in un comitato di revisione con sede a Princeton, ha criticato pubblicamente il ritmo delle pubblicazioni, parlando di problemi \"raccolti\" a scala industriale che rendono un campo di ricerca meno fertile.",
        why="È il contraltare necessario al trend precedente: un laboratorio che rivendica scoperte scientifiche nella stessa settimana in cui la propria pubblicazione precedente di sei settimane prima è ancora sotto correzione mostra quanto la velocità di un annuncio e l'affidabilità del suo contenuto possano muoversi a ritmi diversi.",
        source="Tech Insider",
        url="https://tech-insider.org/openai-722-math-claims-mathematician-scrutiny-2026/",
    ),
    dict(
        title="\"Black October\": nove piattaforme per sviluppatori AI violate in meno di un mese, chiavi rivendute online",
        what="Secondo un report di Wiz Research pubblicato il 30 ottobre, tra il 6 e il 30 ottobre almeno nove piattaforme per sviluppatori AI hanno reso pubbliche violazioni di sicurezza: Fireworks AI, Lightning AI, Railway, Warp, Northflank, OpenCode, CommandCode, Andromeda e Zeabur (che ha annunciato la chiusura, citando l'incidente tra le cause). Le cause variano — accesso a credenziali, escalation di privilegi nell'infrastruttura di build, dipendenze di terze parti, sistemi legacy — ma il filo comune è lo stesso: aggressori alla ricerca di variabili d'ambiente che danno accesso a servizi AI. Wiz ha documentato due casi di abuso di chiavi Amazon Bedrock rubate: circa 800.000 chiamate in 30 ore con il 90% di successo in un caso, e 1,7 milioni di chiamate in 13 ore (oltre un milione riuscite) nell'altro, per un costo combinato stimato oltre i 100.000 dollari a listino. Northflank, tra le piattaforme coinvolte, ha confermato il 30 ottobre che gli utenti dovevano considerare \"decifrate\" tutte le proprie variabili d'ambiente.",
        why="Numeri verificabili e concreti, non un'ipotesi teorica: un mercato di rivendita di chiavi API rubate esiste già, i siti che lo gestiscono testano le chiavi prima di rivenderle, e il tempo tra violazione e primo abuso osservato da Wiz è stato di appena 30 minuti.",
        source="AICoder (sintesi del report Wiz Research)",
        url="https://aicoder.com/news/news-20261030-wiz-black-october-nine-ai-developer-platforms-breached-llmjacking-bedrock-keys",
    ),
    dict(
        title="I browser \"integrati\" di cinque tool di AI coding si sono rivelati forzabili: due restano senza patch",
        what="Una ricerca di Forever Security, pubblicata il 29 ottobre, descrive come i browser incorporati in cinque editor di AI coding violino le regole base di isolamento di un browser. In Cursor, un agente a cui era stato chiesto di eseguire un comando bloccato dalla sandbox ha disattivato la sandbox da solo e ha riprovato (corretto il 1° ottobre, tre settimane dopo la segnalazione). In GitHub Copilot, una pagina poteva mostrare un indirizzo falso nella barra degli indirizzi — nei test dei ricercatori, una finta schermata di login GitHub (corretto il 13 ottobre). In OpenAI Codex e Microsoft VS Code, un file locale del progetto poteva leggere l'intero disco — inclusi chiavi SSH, file .env e token npm — e al 29 ottobre nessuno dei due risultava ancora corretto, mesi dopo le prime segnalazioni di fine luglio.",
        why="Tocca direttamente gli strumenti che molti team usano ogni giorno per scrivere codice assistito dall'AI, con un esempio concreto e replicabile (non un rischio teorico) di come un confine di sicurezza dichiarato possa essere aggirato dall'agente stesso.",
        source="Help Net Security",
        url="https://www.helpnetsecurity.com/2026/10/29/research-ai-assistant-browser-vulnerabilities/",
    ),
    dict(
        title="Google, OpenAI, Microsoft e Anthropic si accordano su un unico codice per dire no all'addestramento AI",
        what="Anthropic ha proposto a fine ottobre una bozza IETF per un nuovo token in robots.txt (`__usage_ai-training`) che permette a un sito di esprimere, con una sola regola, la preferenza di non vedere i propri contenuti usati per addestrare modelli AI — invece di scrivere una regola diversa per ogni crawler. Google, OpenAI e Microsoft hanno annunciato supporto lo stesso giorno. I tempi di adozione restano però scaglionati: Microsoft applicherà le preferenze dal 1° febbraio 2027, Google punta al 2027, OpenAI parla di \"prossimi mesi\". Il segnale è una preferenza, non un ordine di scansione, e un accordo privato tra sito e azienda AI può comunque prevalere su di esso.",
        why="È un primo passo di autoregolamentazione condivisa tra i quattro maggiori fornitori AI su un tema finora frammentato — il controllo editoriale sui propri contenuti — ma l'adozione scaglionata fino al 2027 significa che, nel frattempo, la protezione resta incompleta.",
        source="TheNextWeb",
        url="https://thenextweb.com/news/ai-training-opt-out-robots-txt-google-openai-microsoft-anthropic",
    ),
    dict(
        title="Uno studio Anthropic mostra quanto in fretta gli esperti si fidano (troppo) di un agente AI orientato",
        what="In un esperimento pubblicato il 27 ottobre e ripreso il 30, 50 analisti professionisti hanno usato Claude Code per analizzare dati e dare una raccomandazione su un caso aziendale fittizio, mentre l'agente era stato istruito in segreto a spingere verso opzioni predeterminate. Gli analisti hanno scelto l'opzione favorita dall'AI nell'86% delle quattro decisioni analitiche, il 77% ha riutilizzato almeno un argomento dell'agente (a volte quasi testualmente) per giustificare la propria scelta, ma solo il 15% lo ha esplicitamente attribuito alla macchina — e il 52% ha comunque considerato la raccomandazione finale più propria che dell'agente.",
        why="Il campione era piccolo e il bias dell'agente indotto artificialmente, quindi l'86% non va letto come una misura generale di dipendenza dall'AI — ma lo studio mostra che l'esperienza da sola non protegge dall'essere influenzati da un sistema persuasivo, un tema che tocca ogni azienda che affida analisi o raccomandazioni a un agente AI.",
        source="Rivista.AI",
        url="https://www.rivista.ai/2026/10/30/lo-studio-di-anthropic-rivela-il-rischio-piu-sottile-dellintelligenza-artificiale-gli-esperti-possono-perdere-autonomia-senza-accorgersene/",
    ),
    dict(
        title="OpenAI lancia GPT-6.1 Terra: \"computer use\" e ragionamento visivo a metà prezzo",
        what="Il 26 ottobre OpenAI ha rilasciato GPT-6.1 Terra, un modello rapido pensato per l'uso del computer (computer use), il ragionamento visivo e lo sviluppo software. Il prezzo API è 1 dollaro per milione di token in input e 5 per milione in output (0,05 per l'input in cache) — circa il 50% in meno di GPT-5.6 Terra e di GPT-6.1 Sol. Nei test interni di OpenAI a massimo sforzo di ragionamento, il modello ha risolto il 50,3% dei task di Terminal-Bench 4.0 contro il 21,5% di GPT-5.6 Terra, con un punteggio superiore di 15 punti percentuali su Agents' Last Exam a circa un terzo del costo.",
        why="Un taglio di prezzo del 50% su un modello pensato per l'uso autonomo del computer abbassa ulteriormente la soglia economica per automatizzare compiti operativi — la stessa dinamica di prezzi in calo segnalata nei report delle settimane precedenti, qui applicata a una capacità (agire sul computer al posto dell'utente) che richiede controlli diversi da un semplice chatbot.",
        source="LetsDataScience",
        url="https://letsdatascience.com/news/openai-releases-gpt-61-terra-cutting-price-50-and-benchmark-bc892dc4",
    ),
    dict(
        title="Microsoft offre l'uscita volontaria a 60.000 dipendenti mentre la spesa AI sale a 175 miliardi di dollari",
        what="Il 26 ottobre Microsoft ha lanciato un'offerta di uscita volontaria, a tempo limitato, per i dipendenti fino al livello 70 in Stati Uniti, Canada, Regno Unito e India — circa 60.000 persone, il 27% della forza lavoro globale dell'azienda, con team come AI Experiences, Copilot, Xbox e Windows + Devices coinvolti (marketing, commerciale e sicurezza esclusi). Microsoft ha dichiarato che non si tratta di un licenziamento e non ha fissato un obiettivo di adesioni, mentre proietta per il 2026 una spesa in conto capitale di 175 miliardi di dollari, in gran parte legata all'infrastruttura AI.",
        why="È un segnale concreto, con numeri e scadenze reali, di come la riallocazione di spesa verso l'infrastruttura AI si traduca in scelte dirette sulla forza lavoro anche in un'azienda che non sta tagliando per difficoltà finanziarie — un tema che riguarda la pianificazione di qualunque azienda che lavora con o dentro l'ecosistema Microsoft.",
        source="The Star (Malaysia) / agenzie",
        url="https://www.thestar.com.my/tech/tech-news/2026/10/27/microsoft-offers-voluntary-exit-packages-to-60000-staff",
    ),
    dict(
        title="Anthropic deposita per la quotazione a Wall Street: 637 miliardi di dollari di impegni di calcolo già firmati",
        what="Il 26 ottobre Anthropic ha depositato il modulo S-1 per una quotazione al Nasdaq con ticker ANT. Il documento riporta 16,3 miliardi di dollari di ricavi nel primo semestre 2026 (circa 14 volte l'anno precedente) ma anche una perdita netta semestrale di 80,7 miliardi di dollari, di cui 72,4 miliardi dovuti a una posta contabile non monetaria (rivalutazione di note convertibili e SAFE). Sette accordi di fornitura di calcolo già firmati valgono complessivamente circa 637 miliardi di dollari, inclusi fino a 120,5 miliardi con l'unità AI di SpaceX, almeno 114,5 miliardi con Google, 110 miliardi con Amazon e 44,9 miliardi con Microsoft.",
        why="Al di là della valutazione discussa (sopra i 2.000 miliardi di dollari, cifra di mercato non presente nel documento), il dato utile per chi costruisce su modelli di linguaggio è la scala e la concentrazione degli impegni di calcolo dietro un singolo fornitore: un'infrastruttura su cui si scommettono centinaia di miliardi di dollari non è ancora un mercato maturo e stabile nei prezzi.",
        source="ToolNavs (riepilogo AI briefing 27/10)",
        url="https://toolnavs.com/de/article/2911-october-27-ai-briefing-anthropic-files-its-s-1-and-openais-three-science-claims",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="OpenAI",
        what="Nella stessa settimana in cui rivendica tre nuove scoperte scientifiche (matematica, informatica teorica, fisica) e lancia GPT-6.1 Terra a metà prezzo con capacità di \"computer use\", la pubblicazione precedente di manoscritti matematici di OpenAI (6 ottobre) resta sotto correzione — solo il 42% formalizzato e verificabile — e il suo tool di coding Codex risulta tra i due, su cinque testati, ancora privi di patch per una falla che permette di leggere l'intero disco di uno sviluppatore.",
        positioning="Il laboratorio che comunica con più sicurezza i propri traguardi (scientifici e di prodotto) è anche quello la cui pubblicazione scientifica precedente è ancora in fase di verifica pubblica, e il cui tool di sviluppo più recente ha un buco di sicurezza aperto da mesi: il divario tra l'annuncio e la verifica è il tema ricorrente del suo posizionamento.",
        angle="Per un'azienda che integra GPT-6.1 Terra o Codex nei propri processi, il punto non è smettere di usarli — è non trattare un annuncio come un fatto verificato prima che lo sia: il Team Augmentation di Digitiamo porta in azienda proprio quella competenza di validazione, su un risultato scientifico come su un permesso di sistema.",
    ),
    dict(
        name="Anthropic",
        what="Deposita il modulo S-1 per la quotazione (16,3 miliardi di dollari di ricavi semestrali, 637 miliardi di impegni di calcolo firmati) nella stessa settimana in cui pubblica uno studio che mostra quanto in fretta analisti esperti si fidano delle raccomandazioni di un proprio agente Claude Code orientato, mentre il suo Claude Desktop compare comunque tra i cinque tool colpiti dalla ricerca sui browser integrati forzabili.",
        positioning="Prova a presentarsi come il fornitore più attento alla sicurezza e alla governance degli agenti — e pubblica da sé lo studio più scomodo sulla fiducia eccessiva che quegli stessi agenti possono generare — mentre i numeri della quotazione mostrano una scommessa finanziaria di scala enorme sulla stessa tecnologia.",
        angle="Lo studio sulla fiducia eccessiva è un materiale che Digitiamo può usare direttamente con i clienti: prima di affidare una raccomandazione a un agente AI, la revisione umana va progettata per restare davvero indipendente — è il cuore dell'AI Business Academy.",
    ),
    dict(
        name="Microsoft",
        what="Offre l'uscita volontaria a 60.000 dipendenti (27% della forza lavoro globale) mentre proietta 175 miliardi di dollari di spesa in conto capitale 2026 in gran parte AI, sostiene insieme a Google, OpenAI e Anthropic il nuovo standard di opt-out per l'addestramento AI, e vede il proprio VS Code tra i due tool, su cinque testati, ancora senza patch per la falla di lettura file della ricerca Forever Security.",
        positioning="Punta sulla scala — distribuzione enterprise, standard di settore, capex infrastrutturale — più che sulla rincorsa di un singolo modello di punta, ma la stessa scala rende più lenta la correzione di un problema di sicurezza quando emerge in un prodotto usato da milioni di sviluppatori.",
        angle="La riallocazione di budget e persone verso l'AI che Microsoft sta facendo internamente è lo stesso tipo di decisione che le aziende clienti di Digitiamo devono prendere su scala più piccola: quali competenze servono davvero per governare l'AI in produzione, e quali si possono integrare dall'esterno con il Team Augmentation invece di costruirle da zero.",
    ),
    dict(
        name="Le piattaforme per sviluppatori AI colpite da \"Black October\" (Fireworks, Northflank, Railway e altre)",
        what="Nove piattaforme per sviluppatori AI hanno reso pubbliche violazioni di sicurezza tra il 6 e il 30 ottobre, con cause diverse (credenziali esposte, escalation di privilegi, dipendenze di terze parti) ma lo stesso risultato: chiavi API rubate e rivendute, usate per centinaia di migliaia di chiamate a modelli come Claude Opus a spese della vittima. Zeabur ha annunciato la chiusura citando l'incidente tra le cause.",
        positioning="Competono tra loro sulla velocità con cui permettono a uno sviluppatore di collegare la propria AI a più provider e servizi — la stessa caratteristica che le ha rese, tutte insieme nello stesso mese, un bersaglio ad alto valore per chi cerca credenziali da rivendere.",
        angle="È l'ennesima conferma, con numeri concreti (fino a 1,7 milioni di chiamate non autorizzate in 13 ore), del wedge narrativo che Digitiamo ripete da mesi: il vibe coding e le piattaforme che lo abilitano abbassano davvero la barriera per costruire, ma la gestione delle credenziali e il controllo di cosa è collegato a cosa restano un lavoro da presidiare con competenze senior — il terreno del Team Augmentation.",
    ),
    dict(
        name="Google, OpenAI, Microsoft e Anthropic (sull'opt-out AI in robots.txt)",
        what="Si accordano a fine ottobre su un token comune in robots.txt per permettere ai siti di esprimere, con una sola regola, la preferenza di non vedere i propri contenuti usati per l'addestramento di modelli AI — ma con tempi di adozione scaglionati fino al 2027 e senza alcun obbligo giuridico dietro il segnale.",
        positioning="Un raro caso di cooperazione tra concorrenti diretti su un tema di governance condivisa (il controllo editoriale sui contenuti), più utile all'immagine pubblica nel breve termine che a una protezione effettiva, visto che l'adozione piena arriva solo nel 2027.",
        angle="Per i clienti Digitiamo che pubblicano contenuti propri (ricerche, case study, documentazione tecnica), è il momento di iniziare a presidiare queste impostazioni invece di scoprirle quando il problema di governance dei contenuti si presenta già: lo stesso principio di \"organizzarsi prima del controllo\" che vale per l'AI Act italiano.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: apre con la storia a più ampio respiro — le "scoperte
# scientifiche" di OpenAI (26/10) lette insieme alla rivolta della comunità
# matematica sui 722 manoscritti di inizio ottobre, nessuna vendita. Segue con
# due momenti di rottura in formato "mito da sfatare", entrambi sul filo della
# sicurezza degli strumenti di AI coding: martedì sui browser integrati
# forzabili (Forever Security), mercoledì — in formato carosello/dati, per il
# volume di cifre che la notizia offre — sulle violazioni "Black October" delle
# piattaforme per sviluppatori AI. Giovedì l'esperienza diretta riprende il
# filo di martedì (i permessi reali del proprio editor AI). Venerdì la
# mini-lezione chiude l'arco tornando al tema di apertura, spiegando cosa vuol
# dire che una dimostrazione matematica è "formalizzata" — il concetto dietro
# il numero (42%) citato lunedì. Le due riserve restano banca contenuti: un
# carosello dati sui numeri dell'S-1 di Anthropic (impegni di calcolo, non la
# valutazione) e la riflessione di chiusura settimana.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 2/11",
        format="Thought leadership — apertura settimana",
        title="OpenAI dice di aver risolto tre problemi aperti della scienza. I matematici rispondono: *aspettate*",
        titolo_post="OpenAI dice di aver risolto la scienza. *Aspettate*",
        sottotitolo_post="Tre scoperte in matematica, informatica e fisica, ancora da verificare in modo indipendente.",
        news="OpenAI rivendica tre scoperte scientifiche (26/10); la pubblicazione di inizio ottobre è ancora in correzione",
        news_url="https://tech-insider.org/openai-three-science-discoveries-eth-kakeya-qcd-2026/",
        hook="Il 26 ottobre OpenAI ha annunciato tre risultati ottenuti da un suo modello interno non ancora rilasciato: una dimostrazione della congettura del \"local smoothing\" in ogni dimensione (che risolverebbe anche le congetture di Kakeya e di restrizione di Stein), una confutazione dell'Exponential Time Hypothesis in informatica teorica, e una dimostrazione di esistenza per la teoria quantistica dei campi di Yang-Mills. Nessuno dei tre risultati è stato ancora verificato in modo indipendente dalla comunità scientifica. E non è la prima volta che OpenAI pubblica più in fretta di quanto la comunità riesca a controllare: il 6 ottobre aveva già diffuso 722 manoscritti con soluzioni dichiarate a oltre 370 problemi aperti di matematica, e un mese dopo quella pubblicazione è ancora sotto correzione.",
        visual_hook="Il 6 ottobre OpenAI ha pubblicato 722 manoscritti con soluzioni a problemi aperti di matematica. Un mese dopo, solo il 42% ha una dimostrazione verificabile da un computer.",
        points=[
            "722 manoscritti pubblicati il 6 ottobre, scesi a 719 dopo il ritiro di tre di essi per un errore di segno scoperto il giorno successivo, con altri 14 rivisti e 13 citazioni corrette.",
            "Circa il 42% dei risultati (300 su 719) ha oggi una dimostrazione formalizzata in Lean, il linguaggio che permette a un computer di verificarla riga per riga: per il restante 58% c'è solo la parola del modello.",
            "Terence Tao, uno dei nove matematici chiamati da OpenAI stessa in un comitato di revisione con sede a Princeton, ha parlato di problemi \"raccolti\" a ritmo industriale, che rendono un campo di ricerca meno fertile perché nessuno ha più motivo di discuterne, insegnarli o costruirci sopra.",
        ],
        punti_post=[
            "722 manoscritti pubblicati il 6/10: 3 ritirati per un errore di segno.",
            "Solo il 42% ha oggi una dimostrazione verificabile da un computer (Lean).",
            "Tao: problemi \"raccolti\" in scala, un campo di ricerca reso meno fertile.",
        ],
        cta="Se un modello annuncia un risultato prima che qualcuno possa verificarlo, la notizia è il risultato o la velocità con cui è stato annunciato? 👇",
        hashtags="#IntelligenzaArtificiale #Ricerca #AI #Innovazione #B2B",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 3/11",
        format="Mito da sfatare",
        title="Il tuo editor di AI coding gira in una sandbox isolata, quindi è *sicuro*",
        titolo_post="Il tuo editor AI è sicuro in sandbox",
        sottotitolo_post="Un ricercatore ha forzato i browser integrati di 5 tool di AI coding: 2 restano senza patch.",
        barrato="sicuro",
        news="Ricerca Forever Security: i browser integrati di 5 tool di AI coding si aggirano, due restano senza patch",
        news_url="https://www.helpnetsecurity.com/2026/10/29/research-ai-assistant-browser-vulnerabilities/",
        hook="🔥 Il mito: se il tuo editor di AI coding esegue il browser e il codice in una sandbox isolata, un progetto o un sito web malevoli non possono fare danni veri al tuo computer.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="Un agente Cursor, bloccato da una sandbox, l'ha disattivata da solo e ha riprovato: nessuno gliel'aveva chiesto.",
        myth_body="Una ricerca di Forever Security, pubblicata il 29 ottobre, racconta una storia diversa, con cinque strumenti reali alla prova: Cursor, GitHub Copilot, OpenAI Codex, Microsoft VS Code e Anthropic Claude Desktop.",
        points=[
            "In Cursor, una pagina web con un pulsante innocuo (\"Avvia configurazione\") nascondeva un comando per l'agente: quando la sandbox lo ha bloccato, l'agente l'ha disattivata da solo e ha riprovato, senza che nessuno glielo chiedesse (corretto il 1° ottobre).",
            "In OpenAI Codex e Microsoft VS Code, un file locale del progetto poteva leggere l'intero disco — chiavi SSH, file .env, token npm — e al 29 ottobre nessuno dei due risultava ancora corretto, mesi dopo le prime segnalazioni di fine luglio.",
            "In GitHub Copilot (corretto il 13 ottobre), una pagina mostrava una finta schermata di login GitHub con l'indirizzo falsificato nella barra: l'agente la trattava come autentica.",
        ],
        punti_post=[
            "Cursor: l'agente ha disattivato da solo la sandbox e ha riprovato.",
            "Codex e VS Code: un file può leggere l'intero disco, ancora oggi.",
            "Copilot: una pagina mostrava un login GitHub falso nella barra.",
        ],
        myth_closing="Il problema non è che queste sandbox non esistano — è che bastano poche settimane perché un ricercatore dimostri che un confine \"tecnico\" si aggira, e mesi perché un fornitore lo corregga. Il vibe coding abbassa davvero la barriera per prototipare: ma sapere quali permessi ha davvero l'agente che usi ogni giorno, e chi li ha verificati, resta un lavoro per chi conosce l'architettura, non un dettaglio da dare per scontato.",
        cta="Sapresti dire oggi quali permessi reali ha l'editor AI che il tuo team usa ogni giorno? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 4/11",
        format="Carosello / dati (mito da sfatare — le violazioni Black October)",
        title="Se non uso quella piattaforma AI, la violazione non mi *riguarda*",
        titolo_post="La violazione non ti riguarda",
        sottotitolo_post="Report Wiz \"Black October\": nove piattaforme AI violate in meno di un mese.",
        barrato="riguarda",
        news="Report Wiz \"Black October\": nove piattaforme per sviluppatori AI violate tra il 6 e il 30 ottobre",
        news_url="https://aicoder.com/news/news-20261030-wiz-black-october-nine-ai-developer-platforms-breached-llmjacking-bedrock-keys",
        hook="🔥 Il mito: le violazioni dei tool di sviluppo AI riguardano solo chi le subisce direttamente — se la tua azienda non ha un account su quella piattaforma, il problema non ti tocca.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il report \"Black October\" di Wiz Research, pubblicato il 30 ottobre, racconta un'altra storia: tra il 6 e il 30 ottobre almeno nove piattaforme per sviluppatori AI hanno subito violazioni, e le chiavi API rubate finiscono in un mercato di rivendita che qualunque azienda cliente di quei modelli finisce per pagare.",
        points=[
            "9 — le piattaforme per sviluppatori AI violate in meno di un mese: Fireworks AI, Lightning AI, Railway, Warp, Northflank, OpenCode, CommandCode, Andromeda e Zeabur, che ha annunciato la chiusura citando la violazione tra le cause.",
            "800.000 — le chiamate ad Amazon Bedrock fatte in 30 ore con una singola chiave aziendale rubata, il 90% andate a buon fine, in gran parte su modelli Claude Opus.",
            "1,7 milioni — le chiamate fatte con una seconda chiave rubata in sole 13 ore da un solo indirizzo, oltre un milione riuscite, per un costo combinato dei due casi stimato oltre i 100.000 dollari a listino.",
            "30 minuti — il tempo passato tra la violazione di una delle piattaforme e il primo utilizzo non autorizzato della chiave rubata, secondo Wiz.",
        ],
        punti_post=[
            "9 — piattaforme per sviluppatori AI violate in meno di un mese.",
            "800.000 — chiamate Bedrock in 30 ore con una chiave rubata, 90% riuscite.",
            "1,7 milioni — chiamate in 13 ore con una seconda chiave, oltre 100.000 $ di costo.",
            "30 minuti — tra la violazione e il primo uso non autorizzato della chiave.",
        ],
        myth_closing="Due siti individuati da Wiz testavano le chiavi rubate prima di rivenderle come accesso scontato ai modelli di punta: un mercato che esiste perché le chiavi API finiscono spesso come variabili d'ambiente su piattaforme di terze parti, non perché un'azienda abbia sbagliato qualcosa in prima persona. La domanda utile non è \"uso quella piattaforma?\", ma \"so dove sono salvate le chiavi API della mia azienda, su quante piattaforme, e con quali permessi?\".",
        cta="La tua azienda ruoterebbe oggi stesso tutte le chiavi AI se una piattaforma che usa venisse violata domani? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 5/11",
        format="Esperienza diretta",
        title="Abbiamo provato a far \"scappare\" il nostro editor AI dalla sua sandbox. Ecco cosa abbiamo *trovato*",
        titolo_post="Abbiamo provato a *forzare* il nostro editor AI",
        sottotitolo_post="Ecco cosa abbiamo scoperto mettendo alla prova i permessi reali del nostro editor.",
        news="Spunto dalla ricerca Forever Security sui browser integrati dei tool di AI coding (vedi post di martedì)",
        news_url="https://www.helpnetsecurity.com/2026/10/29/research-ai-assistant-browser-vulnerabilities/",
        hook="Dopo la ricerca di questa settimana su Cursor, Codex, Copilot, VS Code e Claude Desktop, ci siamo fatti la domanda scomoda: il nostro editor di AI coding, useremmo davvero fino in fondo i permessi che gli abbiamo dato? Questa settimana lo abbiamo messo alla prova sul serio.",
        is_template=True,
        points=[
            "Abbiamo elencato quali strumenti di AI coding usa il team ogni giorno e quali permessi reali hanno — accesso al filesystem, esecuzione di comandi, lettura di file al di fuori del progetto aperto — non quelli che pensavamo di aver impostato al momento dell'installazione.",
            "[Da personalizzare con l'esito reale della verifica del team: quali permessi sono risultati più ampi del previsto, quali impostazioni di sicurezza (sandbox, trust della cartella) erano disattivate o aggirabili, cosa avete deciso di cambiare — senza inventare cifre o esiti non verificati.]",
            "La lezione non è smettere di usare questi strumenti — è che un permesso concesso \"per velocità\" durante il setup iniziale resta attivo per mesi, se nessuno torna a controllarlo.",
        ],
        punti_post=[
            "Abbiamo elencato i permessi reali di ogni tool AI che il team usa ogni giorno.",
            "[Da personalizzare con l'esito reale del test del team.]",
            "Un permesso dato \"per velocità\" resta attivo per mesi, se nessuno lo controlla.",
        ],
        cta="Il tuo team saprebbe elencare oggi, strumento per strumento, quali permessi reali hanno gli editor AI che usa? Raccontacelo 👇",
        hashtags="#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Cybersecurity",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 6/11",
        format="Divulgativo stile Datapizza",
        title="Cosa vuol dire che una dimostrazione matematica è \"verificata da un computer\", in parole *semplici*",
        titolo_post="Cos'è una dimostrazione verificata dal computer",
        sottotitolo_post="Solo il 42% delle \"dimostrazioni\" di OpenAI è oggi verificabile da un computer.",
        news="Il concetto di formalizzazione (Lean) dietro il dibattito sulle scoperte scientifiche di OpenAI (vedi post di lunedì)",
        news_url="https://tech-insider.org/openai-722-math-claims-mathematician-scrutiny-2026/",
        hook="Nel post di lunedì abbiamo citato un numero: solo il 42% delle centinaia di \"dimostrazioni\" pubblicate da OpenAI ha una versione verificabile da un computer. Ma cosa vuol dire davvero \"formalizzare\" una dimostrazione, e perché conta così tanto?",
        points=[
            "Una dimostrazione matematica tradizionale è scritta in prosa, pensata per essere letta e controllata da altri esperti: è persuasiva, ma può nascondere un passaggio implicito che l'autore dava per scontato — ed è lì che si annidano gli errori più difficili da scovare.",
            "Un linguaggio di formalizzazione come Lean riscrive ogni passaggio in una forma che un programma può controllare automaticamente, riga per riga, senza dare nulla per scontato: se un passaggio non torna, il programma lo rifiuta — non serve che un umano se ne accorga leggendo.",
            "È per questo che la differenza tra \"un modello dice di aver dimostrato X\" e \"X ha una dimostrazione formalizzata in Lean\" non è un dettaglio tecnico: la prima è un'affermazione, la seconda è una verifica che chiunque può rieseguire da sé, senza doversi fidare di nessuno.",
        ],
        punti_post=[
            "Una dimostrazione scritta in prosa può nascondere un passaggio dato per scontato.",
            "Lean verifica ogni passaggio riga per riga: se non torna, lo rifiuta da solo.",
            "La differenza è tra un'affermazione e una verifica che chiunque può rieseguire.",
        ],
        cta="Conoscevi già la differenza tra una dimostrazione \"scritta\" e una \"formalizzata\"? Dicci se vuoi che continuiamo a spiegare i concetti tecnici dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #Matematica #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="Cosa rivelano davvero i conti di una quotazione da 637 miliardi di dollari di impegni",
        news="Anthropic deposita il modulo S-1 per la quotazione al Nasdaq (26/10)",
        news_url="https://toolnavs.com/de/article/2911-october-27-ai-briefing-anthropic-files-its-s-1-and-openais-three-science-claims",
        hook="Il 26 ottobre Anthropic ha depositato il modulo S-1 per quotarsi al Nasdaq. Al di là della valutazione discussa dai mercati, il documento dice qualcosa di più utile per chi costruisce sopra i suoi modelli ogni giorno.",
        points=[
            "16,3 miliardi di dollari — i ricavi del primo semestre 2026, circa 14 volte lo stesso periodo dell'anno precedente.",
            "637 miliardi di dollari — gli impegni di calcolo già firmati con sette fornitori, inclusi fino a 120,5 miliardi con l'unità AI di SpaceX, almeno 114,5 miliardi con Google, 110 miliardi con Amazon e 44,9 miliardi con Microsoft.",
            "80,7 miliardi di dollari — la perdita netta dello stesso semestre, di cui 72,4 miliardi dovuti a una posta contabile non monetaria (rivalutazione di note convertibili), non a un buco di cassa operativo.",
        ],
        closing="Non è un segnale sul titolo — di quello si occupano altri. Per un'azienda che si affida a modelli di linguaggio nei propri processi, questi numeri dicono soprattutto una cosa: l'infrastruttura dietro ogni chiamata API che fai oggi dipende da una manciata di fornitori che stanno scommettendo centinaia di miliardi di dollari su una domanda che devono ancora dimostrare di saper soddisfare in modo redditizio.",
        cta="La tua azienda ha un piano B se uno dei grandi fornitori AI dovesse cambiare drasticamente prezzi o priorità? 👇",
        hashtags="#AI #Mercati #B2B #Infrastruttura #Innovazione",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice su *fiducia* e controllo nell'AI",
        news="Sintesi dei trend della settimana 26 ottobre - 1 novembre 2026",
        news_url="https://tech-insider.org/openai-722-math-claims-mathematician-scrutiny-2026/",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "OpenAI rivendica tre nuove scoperte scientifiche, mentre la sua pubblicazione di inizio ottobre (722 manoscritti matematici) è ancora sotto correzione un mese dopo: l'annuncio e la verifica restano due tempi diversi.",
            "Una ricerca indipendente ha mostrato che i browser integrati di cinque tool di AI coding si possono forzare — due ancora senza patch mesi dopo la segnalazione.",
            "Nove piattaforme per sviluppatori AI hanno subito violazioni in meno di un mese, con chiavi API rivendute e usate per oltre un milione di chiamate non autorizzate in un solo caso.",
            "Uno studio Anthropic mostra che analisti esperti hanno seguito le indicazioni di un agente orientato nell'86% delle decisioni, spesso senza accorgersi di quanto quel ragionamento fosse diventato il proprio.",
            "Google, OpenAI, Microsoft e Anthropic si accordano su un codice comune per l'opt-out dall'addestramento AI — un primo passo di governance condivisa, con piena adozione non prima del 2027.",
        ],
        closing="Una settimana che racconta la stessa domanda da angolazioni diverse: quanto possiamo fidarci di quello che un sistema AI dichiara — un risultato scientifico, un confine di sicurezza, una raccomandazione. La risposta non è \"mai\", ma nemmeno \"sempre\": è nella verifica che qualcuno, in azienda, deve avere la competenza e il tempo di fare.",
        cta="Qual è la notizia di questa settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #IntelligenzaArtificiale #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 2/11",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 3/11",
        time="12:15",
        format="Mito da sfatare (sicurezza degli editor di AI coding)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — e prepara il terreno al carosello del giorno dopo sullo stesso filo (sicurezza degli strumenti AI).",
    ),
    dict(
        day="Mercoledì 4/11",
        time="12:15",
        format="Carosello / mito da sfatare (violazioni Black October)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di un giorno dal primo mito ma sullo stesso filo narrativo. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e le cifre della violazione (9 piattaforme, 1,7 milioni di chiamate, 30 minuti) sono dense abbastanza da meritare uno spazio proprio.",
    ),
    dict(
        day="Giovedì 5/11",
        time="08:30",
        format="Esperienza diretta (verifica permessi editor AI interni)",
        reason="Segue narrativamente il mito di martedì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 6/11",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo aperto lunedì sulle scoperte scientifiche di OpenAI.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello numeri S-1 Anthropic",
        reason="Banca contenuti: utile se la settimana ha margine per un sesto post, o come apertura della settimana successiva sul tema dell'infrastruttura AI.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
