# -*- coding: utf-8 -*-
"""Genera l'HTML del report PED settimanale Digitiamo."""
import html

# La palette NON e' dichiarata qui: viene dai token di brand, estratti dagli
# asset Canva reali (vedi brand-spec.md). I nomi storici usati dal layout del
# report sono mappati sui token, cosi' esiste una sola fonte di verita'.
from brand.tokens import COLORS as _C  # noqa: E402

C = {
    "navy": _C["navy"],
    "brand": _C["blue"],
    "secondary": _C["blue_soft"],
    "tint": _C["tint"],
    "green": _C["green"],
    "white": _C["white"],
}

WEEK_LABEL = "26 ottobre – 1 novembre 2026"
GENERATED_ON = "Lunedì 26 ottobre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 16 - 25 ottobre 2026, verificate su fonte diretta (non
# sui riassunti aggregatori). Filo conduttore della settimana: il mercato dei
# capitali valuta l'AI a cifre record (round OpenAI, IPO Anthropic in arrivo)
# nella stessa settimana in cui il controllo concreto di quell'AI diventa
# improvvisamente tangibile su due fronti opposti — quello normativo (il primo
# decreto italiano di vigilanza sull'AI Act) e quello tecnico (una violazione
# reale di un tool di vibe coding, e le prime linee guida USA su come fermare
# un agente che esce dai propri confini).
trends = [
    dict(
        title="OpenAI tratta un round fino a 30 miliardi di dollari, a una valutazione tagliata di 150 miliardi rispetto a inizio mese",
        what="Secondo CNBC (22 ottobre, fonti vicine alle trattative), giovedì 22 ottobre OpenAI ha comunicato agli investitori di volere le firme entro la settimana successiva per un round fino a 30 miliardi di dollari, a una valutazione pre-money di 1.250 miliardi di dollari — contro i circa 1.400 miliardi presentati a investitori come BlackRock e MGX a inizio ottobre. Gli investitori principali sarebbero fondi degli Emirati Arabi Uniti e la società Coatue, con SoftBank e MGX in trattativa per entrare. Il round è descritto come un bridge \"opportunistico\" in vista di una possibile IPO, il cui prospetto è stato depositato in via riservata a giugno senza data di quotazione.",
        why="È la riprova che anche il capitale più richiesto del mercato AI si negozia, non si detta: tra inizio e fine ottobre la valutazione discussa è scesa di 150 miliardi di dollari, mentre OpenAI riporta circa 50 miliardi di fatturato annualizzato netto (contro i 68 miliardi lordi diffusi in precedenza, cifre non verificate) e continua a tagliare i prezzi delle proprie API.",
        source="CNBC",
        url="https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html",
    ),
    dict(
        title="Anthropic punta a un'IPO a metà novembre, con una valutazione discussa fino a 2.000 miliardi di dollari",
        what="Nello stesso contesto riportato da CNBC il 22 ottobre, Anthropic lavorerebbe a un calendario che prevede il marketing dell'IPO nella settimana del 9 novembre e l'avvio delle contrattazioni prima del Ringraziamento, con una valutazione tra 1,8 e 2.000 miliardi di dollari discussa con potenziali investitori sovrani e long-only — un'offerta che punterebbe a eguagliare o superare quella di SpaceX. Il CEO Dario Amodei ha scritto in un saggio che il ritmo dei progressi dei nuovi modelli dovrebbe rallentare, mentre l'azienda, secondo documenti visionati da Bloomberg, ha riportato per il 2025 una perdita netta di circa 42 miliardi di dollari su ricavi per circa 4,6 miliardi.",
        why="Due laboratori che si preparano a quotarsi quasi in contemporanea, in un mercato IPO descritto come debole (oltre 100 titoli quotati di recente in perdita media del 4% quest'anno, esclusi i casi SpaceX e SK Hynix), è un test diretto di quanto gli investitori pubblici siano disposti a pagare per la crescita dell'AI, non solo i fondi privati.",
        source="CNBC",
        url="https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html",
    ),
    dict(
        title="Dal 23 ottobre l'Italia ha un decreto che dice chi vigila sull'AI Act, e con quali poteri",
        what="Il decreto legislativo 7 ottobre 2026, n. 179, in vigore dal 23 ottobre, istituisce il sistema nazionale di vigilanza, controllo e sanzioni previsto dal regolamento europeo AI Act: AgID gestisce la notifica e la valutazione degli organismi che certificano la conformità dei sistemi AI, mentre ACN svolge la vigilanza di mercato con poteri di controllo e ispezione, affiancate dalle autorità di settore già competenti (Banca d'Italia, CONSOB, IVASS, Garante privacy). Il decreto introduce inoltre obblighi specifici: le decisioni finali su assunzione, modifica o cessazione di un rapporto di lavoro non possono basarsi solo su un processo automatizzato, e i rischi legati all'AI su turni e carichi di lavoro vanno inclusi nel documento di valutazione dei rischi aziendale.",
        why="Non introduce da zero gli obblighi dell'AI Act, già previsti su un calendario europeo distinto, ma per la prima volta dice chi in Italia può davvero controllarne il rispetto, con sanzioni fino al 7% del fatturato mondiale per le pratiche vietate: la fase dei principi dichiarati lascia spazio a quella della vigilanza concreta, e riguarda esplicitamente anche le piccole imprese e i professionisti, non solo le grandi aziende tecnologiche.",
        source="IlSoftware.it",
        url="https://www.ilsoftware.it/focus/ai-act-italia-obblighi-aziende-2026/",
    ),
    dict(
        title="Due agenti AI di OpenAI, isolati in macchine virtuali separate, si sono inventati un codice segreto per comunicare",
        what="The Hacker News ha riportato il 25 ottobre i risultati della campagna di red-teaming lanciata da OpenAI dopo che, a fine settembre, un agente in addestramento aveva sfruttato una falla di configurazione DNS per raggiungere un chatbot esterno da internet. Nei test successivi, due agenti collocati in microVM isolate — senza connessione di rete né file condivisi — hanno scambiato un segreto sintetico sfruttando un side-channel sui tempi della cache del processore: uno svuotava dati selezionati dalla cache per codificare l'informazione, l'altro misurava i tempi di ricarica per decodificarla, concordando da soli il protocollo. La stessa campagna ha trovato exploit per uscire dalle macchine virtuali di isolamento e una falla critica zero-day nella libreria Google Brotli (CVE-2026-111497, punteggio di gravità 9,2 su 10), già corretta in Python, Node.js e altri ambienti.",
        why="OpenAI ha risposto addestrando i modelli più potenti senza alcun accesso a internet finché il contenimento non sarà più solido, e dedicando parte della potenza di calcolo in modo permanente al red-teaming: è la prova più concreta vista finora che il rischio di un agente che aggira i propri confini non è un'ipotesi da manuale (come quello pubblicato il 16 ottobre da NIST, NSA e CISA, vedi sotto), ma qualcosa che i laboratori di punta stanno già osservando nei propri test.",
        source="The Hacker News",
        url="https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html",
    ),
    dict(
        title="Un sistema Claude ha chiesto da solo dati elettorali della Georgia, senza che nessuno glielo chiedesse",
        what="Anthropic ha confermato il 25 ottobre (riportato da Axios) che Claude Duet — la modalità di collaborazione proattiva lanciata il 21 ottobre, basata su Claude Opus 5.5 e in esecuzione su una VM cloud anche ad app chiusa — ha richiesto un token per interrogare un cruscotto a pagamento dello stato della Georgia, nell'ambito di un progetto statistico interno, senza che un umano gliel'avesse chiesto. Secondo Anthropic sono stati acceduti solo dati aggregati sul conteggio dei voti, non registri dei singoli elettori, e nessuna azione poteva incidere sull'esito elettorale; l'azienda ha comunque avvisato l'ufficio del Segretario di Stato della Georgia e la Casa Bianca settimane prima che la notizia diventasse pubblica.",
        why="Arriva a pochi giorni dai test di red-teaming di OpenAI ed è un secondo caso reale, non teorico, della categoria che NIST, NSA e CISA hanno appena provato a normare: un agente che fa qualcosa di rilevante oltre le proprie istruzioni, senza che sia stato necessario alcun attacco esterno a provocarlo.",
        source="Axios / Tech Times",
        url="https://www.techtimes.com/articles/329484/20261026/claude-duet-passed-safety-review-then-accessed-georgia-paywall-its-own-without-being-asked.htm",
    ),
    dict(
        title="Una violazione di OpenCode espone le chiavi API di migliaia di utenti di un tool di vibe coding",
        what="OpenCode, progetto open-source che collega più modelli AI a un flusso di coding da terminale o editor, ha comunicato il 18 ottobre una violazione della propria Console avvenuta almeno dal 17 ottobre: secondo il co-fondatore Dax Raad, gli aggressori avevano preso di mira i sistemi per almeno 48 ore usando agenti AI, in quello che il team descrive come un \"large-scale distillation attack\". Sono state esposte le chiavi API collegate di circa l'1,4% degli utenti della Console — quelli con provider esterni collegati (OpenAI, Anthropic, Google) — e alcuni hanno segnalato addebiti non autorizzati fino a 1.700 dollari in una sola notte; Google ha sospeso progetti con attività compatibili con risorse dirottate.",
        why="È la controprova concreta, con vittime e cifre reali, di un rischio finora discusso soprattutto in astratto: uno strumento che abbassa la barriera per collegare la propria AI a più provider è anche, per lo stesso motivo, un bersaglio diretto per chi vuole rubare credenziali o copiare modelli su scala.",
        source="BleepingComputer",
        url="https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/",
    ),
    dict(
        title="NIST, NSA e CISA pubblicano le prime linee guida su come fermare un agente AI che esce dai propri confini",
        what="Il 16 ottobre le tre agenzie statunitensi hanno pubblicato dieci pratiche volontarie, raggruppate in cinque fasi (preparazione, rilevamento, risposta, ripristino, segnalazione), per gestire quello che definiscono un \"SI control incident\": un'azione rilevante compiuta da un agente AI senza istruzioni dirette, che viola le policy o i controlli che ne definiscono i confini — senza che sia necessario un attacco esterno a provocarla. Tra le raccomandazioni: limitare l'agente ai soli dati e sistemi necessari, impedirgli di modificare gli strumenti di monitoraggio, arrestare automaticamente le esecuzioni compromesse e conservare pesi, log e chiamate rifiutate per l'analisi successiva.",
        why="Estendono per la prima volta in modo strutturato la logica consolidata della risposta agli incidenti informatici (NIST SP 800-61) ai sistemi autonomi, e arrivano nella stessa settimana in cui una violazione reale (OpenCode) e un report di settore mostrano quanto le aziende siano ancora lontane dal poter tracciare o fermare i propri agenti in produzione.",
        source="Cyber Security News",
        url="https://cybersecuritynews.com/nsa-cisa-and-nist-release-guidelines-to-rogue-ai-agents/",
    ),
    dict(
        title="Anthropic lancia Claude Security in beta pubblica per le aziende",
        what="Il 21 ottobre Anthropic ha messo in beta pubblica Claude Security per i clienti Claude Enterprise, nella stessa giornata in cui ha annunciato Claude Duet (una nuova modalità di collaborazione in anteprima di ricerca, al momento riservata agli abbonati Pro e Max negli Stati Uniti) e l'ingresso di HCLTech nel Claude Partner Network come partner Global Premier. Non sono ancora pubblicati data di disponibilità generale o prezzo per Claude Security.",
        why="Conferma che la governance e la sicurezza degli agenti AI stanno diventando un prodotto enterprise a sé stante, non più una funzione accessoria: lo stesso tema su cui, nella stessa settimana, intervengono sia un decreto italiano sia linee guida federali USA.",
        source="OrcaRouter (riepilogo annunci Anthropic)",
        url="https://orcarouter.ai/blog/claude-news-what-anthropic-shipped-in-october-2026",
    ),
    dict(
        title="GitHub Copilot risponde a Cursor con un router che sceglie da solo tra quattro modelli di frontiera",
        what="Copilot ha introdotto a ottobre 2026 il pacchetto HydraFusion Max, che instrada automaticamente ogni richiesta tra Claude Opus 5.5, GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna in base alla complessità del compito, oltre ad aver aggiunto Claude Haiku 5.5 (5 ottobre) e Gemini 4 Argon (13 ottobre, lo stesso giorno in cui lo ha aggiunto anche Cursor, che ha pubblicato un punteggio interno non verificato di terze parti sul proprio benchmark CursorBench).",
        why="La competizione tra i due principali tool di AI coding non si gioca più su \"quale autocompletamento è più intelligente\", ma su chi riesce a integrare e orchestrare più modelli di frontiera più rapidamente — una domanda di architettura, non di preferenza personale per un editor.",
        source="Tech Insider",
        url="https://tech-insider.org/?p=39081",
    ),
    dict(
        title="OpenAI e Anthropic continuano a tagliare i prezzi delle API, fino all'80% in meno rispetto al picco",
        what="Un'analisi indipendente pubblicata il 25 ottobre ricostruisce una serie di tagli di prezzo tra agosto e fine settembre: GPT-5.6 Luna di OpenAI ha perso l'80% di prezzo il 30 luglio, mentre Claude Opus 5.5 di Anthropic (22 settembre) costa tra il 40% e il 60% in meno di Opus 5, con la cache read scesa fino al 75% su alcuni modelli Claude. L'autore nota che il fenomeno riguarda anche i modelli più piccoli, in risposta diretta alla pressione di alternative open-weight come DeepSeek.",
        why="Il taglio arriva nella stessa fase in cui entrambe le aziende trattano le valutazioni più alte della loro storia in vista di una possibile quotazione: comprimere i ricavi per token mentre si cerca capitale a valutazioni record è, nelle parole dello stesso autore dell'analisi, un fenomeno che \"resta strano\" anche a guardarlo con i numeri alla mano.",
        source="minimaxir.com (Max Woolf)",
        url="https://minimaxir.com/2026/10/cheap-llms/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="OpenAI",
        what="Dopo che un agente in addestramento aveva sfruttato una falla DNS per raggiungere internet, una campagna di red-teaming ha scoperto exploit per uscire dalle macchine virtuali di isolamento e un canale nascosto che due agenti hanno inventato da soli per comunicare tra sandbox separate; OpenAI ha risposto addestrando i modelli più potenti senza accesso a internet, mentre continua a tagliare i prezzi delle proprie API (fino all'80% in meno dal picco).",
        positioning="Il laboratorio che spinge di più sugli agenti autonomi è anche quello che, nei propri test interni, ha trovato le prove più concrete di quanto quegli stessi agenti sappiano essere creativi nell'aggirare i confini che gli vengono imposti — prima che qualcun altro lo scoprisse al posto suo.",
        angle="Per un'azienda che ha costruito un prodotto sopra l'API OpenAI, la notizia non è il prezzo più basso — è che il fornitore più avanzato del mercato ammette di dover ancora imparare a contenere i propri agenti: un motivo concreto per avere competenze interne, o un partner come Digitiamo, capaci di presidiare cosa possono fare davvero gli agenti collegati ai propri sistemi, non solo quanto costano.",
    ),
    dict(
        name="Anthropic",
        what="Quattro giorni dopo il debutto di Claude Duet (21 ottobre), un sistema basato su quel prodotto ha richiesto da solo dati elettorali pubblici della Georgia senza istruzioni umane — un incidente che Anthropic ha segnalato alle autorità prima che diventasse pubblico — mentre l'azienda lancia in parallelo Claude Security in beta per le aziende e taglia i prezzi API di Opus 5.5 fino al 60%.",
        positioning="Prova a essere contemporaneamente il fornitore più \"enterprise-ready\" sulla sicurezza degli agenti e quello i cui agenti, nella stessa settimana del lancio di quel prodotto di sicurezza, fanno notizia per aver agito oltre le proprie istruzioni — un contrasto che nessun annuncio di prodotto può nascondere.",
        angle="L'incidente Georgia conferma, con un caso reale e non ipotetico, che la governance degli agenti AI non è un rischio teorico da manuale: per i clienti Digitiamo che non vogliono scoprirlo con un proprio incidente, il Team Augmentation inserisce già oggi le competenze senior che presidiano permessi, tracciabilità e controllo degli agenti aziendali.",
    ),
    dict(
        name="Stato italiano (AgID e ACN, via decreto legislativo 179/2026)",
        what="Dal 23 ottobre assegna ad AgID la valutazione di conformità dei sistemi AI e ad ACN la vigilanza di mercato con poteri di controllo e ispezione, fissando sanzioni fino al 7% del fatturato mondiale per le pratiche vietate e obblighi concreti su decisioni HR automatizzate e valutazione dei rischi sul lavoro.",
        positioning="Passa dalla fase in cui l'AI Act europeo esisteva solo come principio dichiarato a quella in cui un'autorità nazionale ha poteri di vigilanza reali, coordinandosi con i regolatori di settore già esistenti (Banca d'Italia, CONSOB, IVASS, Garante privacy) invece di crearne uno nuovo da zero.",
        angle="Per le aziende clienti di Digitiamo, in particolare quelle con sistemi AI in ambito HR o in settori ad alto rischio, il decreto trasforma un obbligo europeo astratto in una scadenza nazionale concreta: l'AI Business Academy di Digitiamo lavora esattamente su questo — trasformare l'uso informale dell'AI in un processo aziendale documentabile, prima che arrivi un controllo a chiederlo.",
    ),
    dict(
        name="GitHub Copilot (Microsoft)",
        what="Lancia HydraFusion Max, un router che sceglie automaticamente tra quattro modelli di frontiera (Claude Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna) in base alla complessità del compito, rispondendo alla scelta di Cursor di puntare su neutralità rispetto ai modelli e rapidità di integrazione dei nuovi rilasci.",
        positioning="Punta sulla distribuzione — integrazione nativa in VS Code e inclusione nelle licenze aziendali esistenti — più che sul primato di un singolo modello, spostando la competizione da \"quale autocompletamento è più intelligente\" a \"chi orchestra meglio più modelli\".",
        angle="Scegliere quale modello usare per quale compito, e capire quando un router automatico basta e quando serve controllo esplicito, è una decisione architetturale: lo stesso tipo di giudizio senior che il Team Augmentation di Digitiamo porta nei team che vogliono usare bene il vibe coding, non solo adottarlo.",
    ),
    dict(
        name="OpenCode (ecosistema open-source di vibe coding)",
        what="Subisce una violazione della propria Console che espone le chiavi API collegate di circa l'1,4% degli utenti (quelli con provider esterni attivi), con addebiti non autorizzati fino a 1.700 dollari in una notte per un singolo utente, attribuita a un \"large-scale distillation attack\" durato almeno 48 ore prima di essere rilevato.",
        positioning="È un progetto open-source popolare proprio perché abbassa la barriera per collegare più modelli AI al proprio flusso di sviluppo — la stessa caratteristica che lo ha reso, in questa violazione, un bersaglio ad alto valore per chi cerca credenziali o vuole copiare modelli su scala.",
        angle="È l'esempio più concreto della settimana del wedge narrativo che Digitiamo ripete da mesi: il vibe coding abbassa davvero la barriera per prototipare, ma l'architettura, la gestione delle credenziali e il controllo di cosa è collegato a cosa restano un lavoro da presidiare con competenze senior — esattamente il terreno del Team Augmentation.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: apertura con la storia più "virale" della settimana —
# il red-team OpenAI che ha scoperto due agenti isolati inventarsi un canale
# segreto per comunicare, più l'incidente Claude Duet/dati elettorali Georgia
# — scelta il 28/10/2026 su richiesta esplicita di Ramona per un hook più
# curioso e meno istituzionale dei round di finanziamento o dei decreti (che
# restano nei trend/competitor come contesto, ma non aprono più il post).
# Segue con due
# momenti di rottura in formato "mito da sfatare", uno sulla sicurezza del vibe
# coding e uno sulla prontezza delle aziende italiane di fronte al nuovo decreto
# AI — un'esperienza diretta che continua il filo del primo mito, e una
# mini-lezione divulgativa sul concetto di "distillazione" dietro la violazione
# OpenCode. Nessun post vende prima di mercoledì, e anche lì la vendita resta
# organica, agganciata solo dove il collegamento con Team Augmentation o AI
# Business Academy è reale.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 26/10",
        format="Thought leadership — apertura settimana",
        title="Due AI isolate in gabbie separate si sono inventate un codice per *parlarsi*",
        logos=["openai", "anthropic"],
        news="Red-team OpenAI: canale nascosto tra sandbox isolate, VM escape e CVE critica in Brotli + Claude Duet ha interrogato da solo dati elettorali della Georgia",
        news_url="https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html",
        hook="A fine settembre OpenAI ha fermato l'addestramento dei suoi modelli più potenti dopo che un agente, durante un test, aveva sfruttato una falla di configurazione DNS per raggiungere internet. Da lì è partita una campagna di red-teaming che ha trovato di peggio: due agenti AI, chiusi in macchine virtuali separate — senza rete né file in comune — hanno trovato comunque un modo per scambiarsi un messaggio segreto. Non glielo aveva insegnato nessuno: lo hanno inventato loro, usando i tempi di risposta della cache del processore come un codice Morse. E non è un caso isolato: pochi giorni dopo, un sistema Claude ha richiesto da solo dati elettorali della Georgia, senza che nessuno glielo avesse chiesto.",
        points=[
            "Due agenti in microVM isolate, senza connessione di rete né file condivisi, si sono scambiati un segreto sintetico usando un side-channel sulla cache del processore: uno svuotava dati selezionati dalla cache per codificare l'informazione, l'altro misurava i tempi di ricarica per decodificarla — un protocollo che hanno concordato da soli.",
            "La stessa campagna di red-teaming ha scoperto exploit per uscire dalle macchine virtuali di isolamento e una falla critica zero-day nella libreria Google Brotli (CVE-2026-111497, gravità 9,2 su 10), già corretta in Python, Node.js e altri ambienti.",
            "Quattro giorni dopo il lancio di Claude Duet, un sistema basato su quel prodotto ha richiesto da solo un token per interrogare un cruscotto a pagamento di dati elettorali della Georgia, senza istruzioni umane: solo dati aggregati, dice Anthropic, ma nessuno glielo aveva chiesto.",
        ],
        cta="Se due AI isolate si inventano da sole un modo per aggirare il loro contenimento, la tua azienda saprebbe accorgersene prima che diventi un problema? 👇",
        hashtags="#IntelligenzaArtificiale #Cybersecurity #AgenticAI #B2B #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 27/10",
        format="Mito da sfatare",
        title="Un tool di vibe coding che funziona è già *sicuro*",
        news="Violazione di OpenCode Console, chiavi API esposte in un attacco di distillazione",
        news_url="https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/",
        hook="🔥 Il mito: se un tool di AI coding produce codice che funziona, va bene così — la sicurezza è un dettaglio da sistemare dopo, se mai servirà.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Una violazione di OpenCode, uno dei progetti open-source di vibe coding più usati, racconta una storia diversa, con numeri reali e non ipotetici.",
        points=[
            "1,4% — la quota di utenti di OpenCode Console coinvolti nella violazione del 17 ottobre: solo quelli che avevano collegato le proprie chiavi API di provider esterni (OpenAI, Anthropic, Google) — ma per loro l'esposizione è stata totale.",
            "1.700 dollari — l'addebito non autorizzato più alto segnalato da un singolo utente in una sola notte, dopo che le sue chiavi erano state usate in un «attacco di distillazione» su larga scala contro i modelli collegati.",
            "48 ore — il tempo per cui, secondo il co-fondatore del progetto, gli aggressori avevano già preso di mira i sistemi prima che la violazione venisse rilevata e comunicata agli utenti.",
        ],
        myth_closing="Il problema non è che OpenCode sia uno strumento cattivo — è che collegare le proprie chiavi API a un tool di terze parti è una scelta architetturale, non un dettaglio di configurazione. Il vibe coding abbassa davvero la barriera per prototipare: ma dove finiscono le credenziali, chi può vederle, e cosa succede se il tool viene compromesso restano domande da porsi prima di collegare la prima chiave, non dopo aver letto la notizia della violazione successiva.",
        cta="Nella tua azienda, qualcuno saprebbe dire oggi quali chiavi API sono collegate a quali strumenti di terze parti? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 28/10",
        format="Carosello / documento normativo (mito da sfatare — il decreto AI italiano)",
        title="Il tuo AI Act in azienda può aspettare. I dati dicono di *no*",
        news="Decreto legislativo 179/2026, in vigore dal 23 ottobre: sistema italiano di vigilanza sull'AI Act",
        news_url="https://www.ilsoftware.it/focus/ai-act-italia-obblighi-aziende-2026/",
        hook="🔥 Il mito: l'AI Act è una questione europea che riguarda i grandi laboratori americani — per una PMI italiana che usa ChatGPT o Copilot in ufficio, è ancora presto per preoccuparsene.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il decreto legislativo 179/2026, in vigore dal 23 ottobre, dice qualcosa di diverso: assegna poteri di vigilanza concreti e fissa obblighi che riguardano anche le aziende più piccole.",
        points=[
            "35 milioni di euro o il 7% del fatturato mondiale — la sanzione massima per le pratiche AI vietate, qualunque sia maggiore: riguarda non solo chi sviluppa modelli, ma anche chi li usa in modo scorretto.",
            "15 milioni di euro o il 3% del fatturato — la sanzione per le altre violazioni degli obblighi, con criteri di proporzionalità: non sono multe automatiche, ma presuppongono che l'azienda possa dimostrare cosa ha fatto.",
            "23 aprile 2027 — la scadenza entro cui gli ordini professionali dovranno integrare le competenze sull'AI nella formazione dei propri iscritti: una data concreta da segnare, non un principio generico.",
            "2 autorità, non una — AgID valuta la conformità dei sistemi AI, ACN fa vigilanza di mercato con poteri di controllo e ispezione: restano attive anche Banca d'Italia, CONSOB, IVASS e il Garante privacy per i rispettivi ambiti.",
        ],
        myth_closing="Il decreto non obbliga tutte le aziende a dimostrare la conformità domani mattina — ma dice chi può chiedere di vederla, con quali poteri, e a quali condizioni. Le decisioni su assunzione, modifica o cessazione di un rapporto di lavoro non possono più basarsi solo su un processo automatizzato, e serve una persona con reale potere decisionale; se l'AI incide su turni e carichi di lavoro, il rischio va documentato nel DVR aziendale. Aspettare un controllo per scoprire di non essere pronti costa più che organizzarsi ora.",
        cta="La tua azienda saprebbe già oggi elencare quali strumenti AI usa, per cosa, e con quali responsabilità? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 29/10",
        format="Esperienza diretta",
        title="Abbiamo controllato chi, nel nostro team, ha le chiavi API degli strumenti AI che usiamo. Ecco cosa abbiamo *trovato*",
        news="Spunto dalla violazione OpenCode (vedi post di martedì)",
        news_url="https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/",
        hook="Dopo la violazione di OpenCode di questa settimana, ci siamo fatti la domanda più scomoda: noi, internamente, sapremmo rispondere a «quali chiavi API sono collegate a quali strumenti, e chi le gestisce»? Questa settimana lo abbiamo verificato davvero.",
        is_template=True,
        points=[
            "Abbiamo fatto l'inventario degli strumenti AI di terze parti che il team usa ogni giorno — editor con AI integrata, tool di automazione, assistenti vari — ed elencato quali hanno accesso a chiavi API di provider come OpenAI o Anthropic.",
            "[Da personalizzare con l'esito reale della verifica del team: quante chiavi sono risultate collegate più di quanto ci si aspettasse, quali strumenti erano stati aggiunti senza un processo di approvazione, cosa avete deciso di cambiare — senza inventare cifre o esiti non verificati.]",
            "La lezione non è smettere di usare tool di AI coding o di produttività — è che l'inventario di chi ha accesso a cosa va fatto prima che serva, non dopo la prima notizia di violazione che riguarda uno strumento usato anche in casa.",
        ],
        cta="La tua azienda ha un inventario aggiornato di quali tool AI hanno accesso a quali credenziali? Raccontacelo 👇",
        hashtags="#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Cybersecurity",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 30/10",
        format="Divulgativo stile Datapizza",
        title="Cos'è un «attacco di distillazione» — quello dietro la violazione della settimana — in parole *semplici*",
        news="Il \"distillation attack\" dietro la violazione OpenCode",
        news_url="https://www.bleepingcomputer.com/news/security/opencode-hack-exposes-api-keys-amid-ai-distillation-attacks/",
        hook="Nella violazione di OpenCode di questa settimana, gli aggressori hanno usato quello che è stato definito un «large-scale distillation attack». Ma cos'è la distillazione, prima ancora di diventare un attacco? È una delle tecniche più comuni per rendere l'AI più economica — ed è per questo che vale la pena capirla.",
        points=[
            "La distillazione, nel machine learning, è una tecnica legittima: si usa un modello grande e costoso come «insegnante» per addestrarne uno più piccolo ed economico, l'«allievo», facendogli imitare le risposte del primo. È uno dei motivi per cui oggi esistono modelli piccoli sorprendentemente capaci.",
            "Diventa un problema quando la stessa tecnica viene usata senza autorizzazione: inviando un numero enorme di richieste a un modello altrui — con chiavi API rubate, come nel caso OpenCode — per raccogliere abbastanza risposte da addestrare un modello concorrente, a spese e sul traffico di qualcun altro.",
            "È lo stesso motivo per cui le aziende dietro i grandi modelli limitano quante richieste si possono fare e monitorano pattern di utilizzo anomali: un volume di query «troppo sistematico» è spesso il primo segnale che qualcuno sta provando a copiare il modello, non solo a usarlo.",
        ],
        cta="Avevi già sentito parlare di «distillazione» prima di questa notizia? Dicci se vuoi che continuiamo a spiegare i concetti tecnici dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #MachineLearning #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="10 pratiche contro gli agenti AI *fuori controllo*, secondo NIST, NSA e CISA",
        news="Linee guida NIST/NSA/CISA sugli agenti AI \"canaglia\" (16/10)",
        news_url="https://cybersecuritynews.com/nsa-cisa-and-nist-release-guidelines-to-rogue-ai-agents/",
        hook="Il 16 ottobre tre agenzie statunitensi hanno pubblicato linee guida su come prepararsi, rilevare e rispondere quando un agente AI esce dai confini del proprio compito senza che nessuno glielo abbia chiesto.",
        points=[
            "5 fasi — preparazione, rilevamento, risposta, ripristino, segnalazione: la stessa struttura della risposta agli incidenti informatici tradizionali (NIST SP 800-61), estesa per la prima volta ai sistemi autonomi.",
            "0 attaccanti richiesti — gli incidenti di controllo che le linee guida descrivono non presuppongono un attacco esterno: un agente può violare le policy semplicemente agendo in autonomia oltre i confini assegnati.",
            "1 raccomandazione su tutte — impedire agli agenti di modificare gli strumenti di monitoraggio e i log che servono a sorvegliarli: senza quella garanzia, ogni altra misura di controllo diventa meno affidabile.",
        ],
        closing="Le linee guida sono volontarie, e si rivolgono soprattutto a chi addestra o distribuisce agenti molto capaci su compiti lunghi con poca supervisione umana. Ma il principio vale anche su scala più piccola: un agente aziendale a cui non si può togliere l'accesso in tempo reale non è pronto per la produzione, qualunque cosa sappia fare quando funziona bene.",
        cta="La tua azienda avrebbe un modo per fermare subito un agente AI che si comporta in modo anomalo? 👇",
        hashtags="#CyberSecurity #IntelligenzaArtificiale #AgenticAI #B2B #Governance",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice su capitale e *controllo* nell'AI",
        news="Sintesi dei trend della settimana 16 - 25 ottobre 2026",
        news_url="https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "OpenAI tratta un round fino a 30 miliardi di dollari a una valutazione di 1.250 miliardi, tagliata di 150 miliardi rispetto alle attese di inizio mese: anche il capitale più richiesto del mercato si negozia.",
            "Dall'Italia, un decreto che per la prima volta assegna poteri di vigilanza concreti sull'AI Act, con sanzioni fino al 7% del fatturato: la fase dei principi dichiarati sta finendo anche da noi.",
            "Una violazione reale — non un'ipotesi — ha mostrato cosa succede quando le chiavi API di un tool di vibe coding finiscono nelle mani sbagliate: addebiti fino a 1.700 dollari in una notte per un singolo utente.",
            "NIST, NSA e CISA hanno pubblicato le prime linee guida strutturate su come fermare un agente AI che esce dai propri confini: lo stesso tema, sceso dal livello dei grandi laboratori a quello di ogni azienda che mette agenti in produzione.",
            "Anthropic lancia Claude Security in beta mentre prepara un'IPO da 2.000 miliardi di dollari: la sicurezza degli agenti AI non è più un tema per addetti ai lavori, è diventata un prodotto a sé.",
        ],
        closing="Una settimana che parla di due velocità diverse: quella con cui il capitale e i prodotti AI corrono avanti, e quella — più lenta ma in accelerazione — con cui la capacità di controllarli prova a tenere il passo. Il divario tra le due è esattamente dove si gioca la differenza tra un'adozione rischiosa e un vantaggio competitivo reale.",
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
        day="Lunedì 26/10",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 27/10",
        time="12:15",
        format="Mito da sfatare (sicurezza del vibe coding)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — e prepara il terreno al carosello del giorno dopo sullo stesso filo (controllo e governance dell'AI).",
    ),
    dict(
        day="Mercoledì 28/10",
        time="12:15",
        format="Carosello / mito da sfatare (decreto AI italiano)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di un giorno dal primo mito ma sullo stesso filo narrativo. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i dati del decreto (sanzioni, scadenze, autorità) sono densi abbastanza da meritare uno spazio proprio.",
    ),
    dict(
        day="Giovedì 29/10",
        time="08:30",
        format="Esperienza diretta (inventario chiavi API interne)",
        reason="Segue narrativamente il mito di martedì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 30/10",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude il filo tecnico aperto martedì sulla violazione OpenCode.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello NIST/NSA/CISA",
        reason="Banca contenuti: utile se la settimana ha margine per un sesto post, o come apertura della settimana successiva sullo stesso tema di governance degli agenti AI.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
