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

WEEK_LABEL = "16 – 22 novembre 2026"
GENERATED_ON = "Lunedì 16 novembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Seconda rigenerazione del 16 novembre 2026, su richiesta di Ramona ("le
# altre sono uguali a prima, cambia proprio stile di news"): la prima
# riscrittura aveva aggiornato solo il trend AT&T lasciando martedì/
# giovedì/venerdì identici alla versione precedente (Notion/Fireworks e
# Chainstack). Qui le notizie di sicurezza sono state sostituite con due
# storie diverse, entrambe verificate sulla fonte diretta: il rapporto di
# Google Threat Intelligence Group (via The Register, pubblicato oggi
# stesso) sul primo caso noto di un agente AI che trasforma da solo una
# patch di sicurezza in un exploit funzionante, e la violazione confermata
# da Cursor il 13/11 — una chiave rubata al fornitore AI Fireworks ha
# permesso di inserire un'estensione Claude Code malevola nel suo
# marketplace. Chainstack resta in elenco perché il framework usato in
# quell'attacco (ARTEX) è lo stesso che Google cataloga nel suo rapporto:
# il collegamento tra le due notizie è reale, non costruito a tavolino.
# Due candidati di un giro di ricerca precedente erano stati scartati dopo
# verifica sulla fonte primaria: la causa Sullivan & Cromwell sulle
# citazioni legali inventate dall'AI risale ad aprile 2026 (non a questa
# settimana), e lo studio Berkeley/Nature sull'ECG e il rischio cardiaco è
# di giugno 2026, solo ripubblicato da un aggregatore il 12/11.
# Filo conduttore della settimana: gli agenti AI smettono di essere un
# progetto pilota e diventano infrastruttura di produzione misurata in
# miliardi di token al giorno (AT&T) e nuovi lanci "da ufficio" (Anthropic,
# OpenAI, Adobe) — mentre sul lato opposto la stessa tecnologia comincia ad
# automatizzare anche l'attacco: un agente che trasforma da solo una patch
# in un exploit (Google), e una chiave rubata a un fornitore AI che diventa
# un'estensione malevola distribuita a migliaia di sviluppatori (Cursor).
trends = [
    dict(
        title="AT&T gestisce quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno",
        what="Il 14 novembre SiliconANGLE ha riportato, da un intervento di Luke Corbin (vice presidente per la trasformazione digitale e l'AI di AT&T Business) a un evento AWS, che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con l'obiettivo di triplicarli entro il 2027. La piattaforma elabora circa 45 miliardi di token al giorno (da 27 miliardi a marzo 2026) e supera 1 milione di transazioni al mese. Ogni workflow parte con supervisione umana: l'autonomia arriva solo quando l'accuratezza raggiunge la fascia medio-alta del 90%, entro un profilo di rischio accettabile, con monitoraggio continuo del drift dopo la rimozione del controllo umano. I workflow che toccano i clienti passano dalla \"Business Agent Foundry\", un gruppo interno che mappa i processi ed elimina passaggi e dipendenze legacy prima di costruire l'agente; i workflow di produttività personale restano invece liberi. Tra i casi concreti: modifiche agli ordini di installazione fibra automatizzate direttamente sui sistemi mainframe, e tempi di attivazione delle connessioni internet dedicate dimezzati negli edifici già cablati.",
        why="Dato pratico e sorprendente più che proiezione: un'azienda con milioni di clienti quotidiani mostra, con cifre e soglie precise, cosa vuol dire portare gli agenti AI dalla demo alla produzione — incluso il meccanismo di governance (soglia di accuratezza, supervisione umana) che l'adozione spesso salta. Rilevante per un pubblico ampio, non solo per gli addetti ai lavori del settore telco.",
        source="SiliconANGLE",
        url="https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/",
    ),
    dict(
        title="Google rivela il primo caso noto di un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante",
        what="Il 16 novembre il Google Threat Intelligence Group (GTIG) ha pubblicato il suo rapporto trimestrale sulle minacce AI, documentando quello che definisce il primo caso noto di un agente AI che trasforma patch di sicurezza in exploit funzionanti senza alcun intervento umano. I ricercatori hanno trovato un server di staging esposto su internet che ospitava un framework multi-agente chiamato \"exploit_agent\": integra più modelli AI (di frontiera e locali), usa strumenti in lingua russa, ed era configurato per confrontare in continuo il codice prima e dopo gli aggiornamenti di sicurezza di software web popolari, individuare le vulnerabilità introdotte dalla patch, sviluppare l'exploit ed eseguirlo — tutto in automatico. Lo stesso server conteneva dati già rubati ad altre organizzazioni e strumenti per muoversi dentro una rete una volta compromessa. GTIG segnala che questo framework si aggiunge a una lista già nota di strumenti offensivi agentici, tra cui ARTEX — lo stesso usato nell'attacco al fornitore blockchain Chainstack della settimana scorsa —, CAIRN, CyberStrikeAI, HexStrike AI e PentAGI.",
        why="Primo caso del suo genere, pubblicato oggi stesso: tocca una paura diffusa e concreta — l'AI che automatizza l'attacco, non solo la difesa — con un meccanismo spiegabile in parole semplici (confronto automatico prima/dopo una patch) e un impatto potenziale su qualunque software web popolare, non su un singolo settore.",
        source="The Register (su rapporto Google Threat Intelligence Group)",
        url="https://www.theregister.com/research/2026/11/16/google-ai-agent-turned-a-security-patch-into-a-working-exploit-with-no-human-help/5309926",
    ),
    dict(
        title="Cursor conferma: una chiave rubata al fornitore AI Fireworks ha portato a un'estensione Claude Code malevola sul suo marketplace",
        what="Il 13 novembre Cursor ha pubblicato i risultati di un'indagine di due settimane su una violazione partita da Fireworks AI, il fornitore di inferenza a cui aveva concesso accesso a un bucket di dati in sola lettura. Un attaccante ha avuto accesso ai sistemi di sviluppo di Fireworks il 24 ottobre, ha usato una chiave esposta per copiare dati dal bucket (tracce di sessioni del 2025 senza Privacy Mode, alcune con credenziali non oscurate), è passato da lì ad alcuni strumenti SaaS interni di Cursor e infine ha caricato, il 29 ottobre, versioni manomesse dell'estensione \"anthropic.claude-code\" nella cache del marketplace VS Code di Cursor — attive per circa 11 ore, scaricabili da un massimo di 5.000 sviluppatori. Il codice incorporato installava una chiave SSH non autorizzata e tentava un tunnel verso un server remoto. Cursor ha bloccato l'ultima attività dell'attaccante il 1° novembre, dichiara che meno dello 0,01% dei clienti ha avuto credenziali API esposte, e precisa che Anthropic non ha mai pubblicato quel pacchetto e il suo prodotto non era vulnerabile.",
        why="Colpisce uno strumento che moltissimi sviluppatori usano ogni giorno per scrivere codice con l'AI, e mostra lo stesso schema del caso Notion di due settimane fa — un fornitore AI terzo come anello debole della catena — ma con un esito diverso e più diretto: un'estensione malevola distribuita, non solo dati esposti.",
        source="Unite.AI (su comunicazione ufficiale Cursor)",
        url="https://www.unite.ai/cursor-traces-breach-to-access-key-exposed-by-fireworks-ai/",
    ),
    dict(
        title="Anthropic trasforma Claude in una suite per ufficio, a pochi mesi da una possibile IPO",
        what="Il 10 novembre Anthropic ha ampliato l'offerta \"da ufficio\" di Claude con Claude Sheets (fogli di calcolo) e Claude Whiteboards, affiancandoli ai già annunciati Claude Docs e Slides, e ha anticipato l'arrivo di Claude Data e Claude Meetings. Ha introdotto anche connettori interattivi che permettono di lavorare dentro app partner (Adobe, Atlassian) senza cambiare scheda, più plugin di Salesforce (beta), NetSuite e Workday (beta) con competenze integrate per preparazione vendite, analisi finanziaria e pratiche HR come ferie e note spese. L'annuncio arriva, secondo diversi osservatori, in un momento di preparazione a una possibile quotazione in borsa di Anthropic.",
        why="Broad appeal diretto: è la stessa battaglia per il posto di lavoro quotidiano che Microsoft combatte con Copilot e Google con Gemini in Workspace, e riguarda ogni azienda che deve decidere quali strumenti AI abilitare per i propri team.",
        source="Constellation Research",
        url="https://www.constellationr.com/insights/news/anthropic-rounds-out-its-office-ambitions-claude-sheets-whiteboards-and-more",
    ),
    dict(
        title="OpenAI porta le aziende dentro ChatGPT con i Business Agent verificati",
        what="Il 10 novembre OpenAI ha lanciato in beta, per ora negli Stati Uniti e per aziende di e-commerce e servizi online, i \"Business Agent\": agenti che rappresentano un marchio dentro ChatGPT quando l'azienda viene citata in una risposta. Un'azienda rivendica e verifica la propria organizzazione nel nuovo \"Business Hub\" (verifica tramite telefono, email aziendale, dominio del sito o Shopify, con controllo d'identità via Persona), imposta le istruzioni e il contesto del proprio agente, e consulta dati su quante volte viene citata nelle risposte di ChatGPT e su quali argomenti emerge. Le chat con un business agent restano etichettate e separate dalla conversazione principale dell'utente.",
        why="Cambia il modo in cui i consumatori scopriranno e parleranno con le aziende prima ancora di arrivare al loro sito: un impatto diretto su marketing e relazione col cliente, visibile a un pubblico ampio anche fuori dagli addetti ai lavori.",
        source="Let's Data Science (The Verge)",
        url="https://letsdatascience.com/news/openai-launches-verified-business-agents-in-chatgpt-beta-a88f185a",
    ),
    dict(
        title="Adobe trasforma Firefly in uno \"studio creativo AI\" con agenti sempre attivi (Adobe MAX)",
        what="Il 10 novembre, ad Adobe MAX a Miami Beach, Adobe ha ampliato Firefly come \"AI creative studio\": il Creative Agent lavora ora dentro Firefly e nei principali programmi Creative Cloud (Photoshop, Premiere, Illustrator, InDesign, After Effects, Frame.io), con una \"Plan Mode\" che mostra il piano prima di eseguirlo e agenti \"always-on\" (anteprima) che lavorano in background su compiti ricorrenti anche quando l'utente è assente. Arrivano anche Firefly Design (beta: illustrazione, foto, animazione, 3D e stampa in un solo spazio) e Firefly Builder (beta privata), che trasforma una descrizione in linguaggio naturale in un sito, una presentazione o un'app funzionante senza scrivere codice. Secondo il report Creators' Toolkit di Adobe, il 78% dei creator dichiara che l'AI generativa ha accelerato la crescita del proprio business.",
        why="Trend di design e innovazione: mostra gli strumenti creativi diventare agentic, con ricadute dirette su chi produce contenuti e grafica per il marketing — rilevante per un pubblico ampio, non solo per i designer.",
        source="Adobe (news.adobe.com)",
        url="https://news.adobe.com/news/2026/11/adobe-firefly-expands",
    ),
    dict(
        title="Google DeepMind porta l'AI nei robot di fabbrica e nella genetica, con Gemini Robotics 2.5 e AlphaGenome 2",
        what="L'11 novembre Google DeepMind ha rilasciato Gemini Robotics 2.5, descritto come il suo modello vision-language-action più capace: testato su oltre 200 compiti, con tassi di successo dal 30% al 100% a seconda del compito e il 20-30% più veloce della versione precedente; in un progetto pilota con Mercedes-Benz ha impacchettato componenti auto con un tasso di successo del 96%. È in distribuzione con partner come Apptronik, Agile Robots e Boston Dynamics. Lo stesso giorno DeepMind ha rilasciato AlphaGenome 2, un modello che predice come le sequenze di DNA e le loro varianti influenzano i diversi tipi di cellule umane, costruito sui dati dell'Human Cell Atlas — non approvato per uso clinico o diagnostico.",
        why="Mostra l'AI uscire dalla chat ed entrare nel mondo fisico e nella ricerca scientifica: due ambiti lontani dal software gestionale ma che colpiscono l'immaginazione di un pubblico ampio, con un esempio industriale (Mercedes-Benz) facilmente comprensibile.",
        source="SiliconANGLE",
        url="https://siliconangle.com/2026/11/11/google-deepmind-releases-new-advanced-robotics-ai-model-and-next-generation-gene-prediction-model",
    ),
    dict(
        title="Un attaccante usa un framework di agenti AI (ARTEX) per violare un fornitore di infrastruttura blockchain",
        what="Il 12 novembre Chainstack, fornitore di infrastruttura blockchain, ha reso noto che un attaccante — entrato il 26 ottobre attraverso un'istanza Grafana esposta su internet e lasciata con le credenziali di amministratore di default — ha raggiunto l'ambiente di produzione il 29 ottobre usando un framework di agenti AI (ARTEX) per condurre l'attacco, prima che Chainstack bloccasse l'accesso il 31 ottobre. Sono stati esposti nomi, email e hash delle password dei clienti; Chainstack dichiara che i servizi rivolti ai clienti non si sono mai fermati e ha chiesto ai clienti di ruotare le credenziali dei nodi. Il rapporto GTIG di Google di questa settimana cataloga ARTEX tra i framework offensivi agentici già noti.",
        why="Collega direttamente il trend Google della stessa settimana: non è un caso isolato, ma uno dei framework che i ricercatori di sicurezza stanno già monitorando come categoria — una controversia con forte presa su un pubblico ampio.",
        source="The Block",
        url="https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509",
    ),
    dict(
        title="I chip AI recuperano parte del terreno perso, dopo la peggiore settimana in un anno e mezzo",
        what="Dopo il crollo registrato nella settimana del 3-7 novembre (indice SOX -12%, la peggiore dall'aprile 2025, dopo le elezioni di midterm del 3 novembre), i titoli dei semiconduttori hanno recuperato parzialmente lunedì 9 novembre. Gli analisti descrivono il movimento come gli investitori che iniziano a guardare oltre la correzione legata ai risultati elettorali, con Nvidia che resta comunque sotto osservazione per le polemiche emerse nei giorni precedenti.",
        why="Contesto pratico diretto per chi valuta il costo di infrastruttura e API AI nei prossimi mesi: lo segnaliamo come coda del trend aperto nel PED precedente, non come notizia nuova a sé — un rimbalzo non chiude la domanda sulla sostenibilità della spesa.",
        source="Stocktwits",
        url="https://stocktwits.com/news-articles/markets/equity/amd-avgo-intc-mu-chip-stocks-inch-higher-as-investors-look-past-midterms-led-selloff-nvidia-controversy/cNGAD0CR9eR",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="AT&T",
        what="Rivela (via SiliconANGLE, 14/11) di gestire quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno e oltre 1 milione di transazioni al mese, con l'obiettivo di triplicare i workflow entro il 2027.",
        positioning="Non si presenta come fornitore di tecnologia AI ma come caso di adozione su scala: la narrazione è \"abbiamo governato la transizione\", con una struttura interna dedicata (Business Agent Foundry) e soglie di accuratezza esplicite prima di togliere la supervisione umana.",
        angle="È l'esempio più concreto finora di cosa serve davvero per portare un agente dalla demo alla produzione: non solo il modello, ma un processo che mappa i workflow, fissa soglie di accuratezza e tiene la supervisione umana finché quella soglia non è raggiunta — esattamente il lavoro di governance che il Team Augmentation di Digitiamo porta alle aziende che non hanno una struttura interna come la Foundry di AT&T.",
    ),
    dict(
        name="Google",
        what="In una settimana mostra due facce della stessa tecnologia: Google DeepMind rilascia Gemini Robotics 2.5 e AlphaGenome 2 (11/11), mentre il Google Threat Intelligence Group pubblica il primo caso noto di un agente AI che trasforma da solo una patch di sicurezza in un exploit (16/11).",
        positioning="Da un lato spinge l'AI oltre la chat, nella robotica industriale e nella ricerca scientifica; dall'altro si posiziona come l'azienda che per prima documenta pubblicamente i rischi offensivi degli agenti AI, rafforzando la propria credibilità come fonte di sicurezza oltre che come fornitore di modelli.",
        angle="Il rapporto GTIG è anche un promemoria pratico: se un framework di agenti AI può automatizzare la ricerca di vulnerabilità su software popolari, la velocità di applicazione delle patch diventa una competenza critica — un terreno dove la formazione mirata dell'AI Business Academy ha un impatto diretto e misurabile.",
    ),
    dict(
        name="OpenAI",
        what="Lancia in beta i Business Agent verificati dentro ChatGPT (10/11): le aziende idonee (per ora e-commerce e servizi online, solo USA) rivendicano un profilo nel Business Hub, si verificano e lasciano che un proprio agente risponda ai clienti dentro la chat, con dati su citazioni e argomenti di scoperta.",
        positioning="Si muove per diventare il punto di ingresso dove i consumatori scoprono e interagiscono con i marchi, prima ancora di arrivare al sito dell'azienda — una scommessa sulla distribuzione, non solo sul modello.",
        angle="Per un'azienda italiana B2B la domanda non è ancora \"mi serve un Business Agent\" (il programma è per ora USA/e-commerce), ma chi presidierà, quando arriverà anche qui, il contenuto e il tono con cui un agente non controllato direttamente dall'azienda risponderà per suo conto — un lavoro di governance, non di marketing spontaneo.",
    ),
    dict(
        name="Anthropic",
        what="Amplia l'offerta da ufficio di Claude con Sheets e Whiteboards, anticipa Data e Meetings, e aggiunge connettori interattivi con Salesforce, NetSuite e Workday (10/11), in un momento di preparazione a una possibile IPO.",
        positioning="Si propone sempre più come alternativa diretta a Microsoft 365 e Google Workspace, non solo come fornitore di modello — la stessa battaglia per il posto di lavoro quotidiano che Microsoft combatte con Copilot e Google con Gemini.",
        angle="Più strumenti AI finiscono nello stesso posto di lavoro, più cresce il bisogno di qualcuno che decida quali abilitare, con quali permessi e per chi: esattamente il lavoro che il Team Augmentation di Digitiamo porta in azienda prima che la scelta la faccia il reparto IT da solo, in affanno.",
    ),
    dict(
        name="Adobe",
        what="Ad Adobe MAX (10/11) trasforma Firefly in uno \"studio creativo AI\" con agenti sempre attivi dentro Photoshop, Premiere, Illustrator e gli altri programmi Creative Cloud, più Firefly Builder per generare siti e prototipi da descrizioni in linguaggio naturale.",
        positioning="Prova a restare il punto di riferimento per i professionisti creativi proprio nel momento in cui strumenti più generalisti (ChatGPT, Gemini, i modelli immagine dei concorrenti) permettono a chiunque di generare immagini: la risposta è portare l'agente dentro gli strumenti professionali, non sostituirli.",
        angle="Un'agenzia o un reparto marketing che adotta questi strumenti guadagna velocità, ma rischia di perdere coerenza di brand se nessuno definisce prima regole e guardrail per l'agente — il terreno dell'AI Business Academy, pensata su casi d'uso reali e non su formazione generica allo strumento.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana (seconda rigenerazione, 16/11/2026): lunedì il quadro
# d'insieme parte da AT&T — il caso più concreto di agenti AI già in
# produzione su scala, con soglie di governance esplicite — e lo affianca ai
# lanci "da ufficio" della stessa settimana (Anthropic, OpenAI, Adobe).
# Martedì il mito da sfatare passa dal caso Notion/Fireworks (riusato nella
# prima rigenerazione) al rapporto Google GTIG di oggi stesso: "serve sempre
# un umano esperto per trasformare una falla in un attacco" — smentito da un
# framework che lo fa da solo. Mercoledì il carosello dati resta sui numeri
# di AT&T (unico trend della settimana con la densità di cifre necessaria a
# un carosello: il caso Cursor ha pochi numeri, non abbastanza per 5 righe di
# scorecard). Giovedì l'esperienza diretta cambia argomento, dal controllo
# dei contratti AI al controllo delle estensioni AI installate negli editor
# del team — spunto diretto dal caso Cursor/Fireworks. Venerdì la
# mini-lezione spiega cos'è un "agente AI offensivo" a partire dal rapporto
# Google e dal collegamento con Chainstack (stesso framework, ARTEX). Le due
# riserve restano banca contenuti: un carosello numeri sul rimbalzo dei chip
# AI, e la riflessione di chiusura.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 16/11",
        format="Thought leadership — apertura settimana",
        title="Mentre Anthropic, OpenAI e Adobe lanciano agenti per l'ufficio, AT&T ne ha già quasi 500 in produzione: 45 miliardi di token elaborati ogni giorno",
        titolo_post="AT&T: quasi 500 agenti già al lavoro",
        sottotitolo_post="Mentre Anthropic, OpenAI e Adobe lanciano agenti per l'ufficio, AT&T ne gestisce quasi 500 in produzione.",
        news="AT&T gestisce quasi 500 workflow agentici in produzione, 45 miliardi di token al giorno (14/11)",
        news_url="https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/",
        hook="Questa settimana la differenza fra parlare di agenti AI e farli lavorare davvero si è vista nei numeri: il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno e oltre 1 milione di transazioni al mese — con l'obiettivo di triplicare i workflow entro il 2027. Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud.",
        visual_hook="Mentre Anthropic, OpenAI e Adobe lanciano agenti per l'ufficio, AT&T ne ha già quasi 500 in produzione, con soglie di accuratezza precise prima di togliere la supervisione umana.",
        points=[
            "Quasi 500 — i workflow agentici che AT&T gestisce oggi in produzione, con l'obiettivo di triplicarli entro il 2027: non una demo, ma un programma con una struttura interna dedicata (la \"Business Agent Foundry\").",
            "Ogni workflow parte con supervisione umana: l'autonomia arriva solo quando l'accuratezza raggiunge la fascia medio-alta del 90%, con monitoraggio continuo dopo la rimozione del controllo diretto.",
            "Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori diretti con Salesforce, NetSuite e Workday, mentre OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende e Adobe ha reso Firefly uno studio creativo con agenti sempre attivi.",
        ],
        punti_post=[
            "AT&T: quasi 500 workflow agentici in produzione.",
            "45 miliardi di token al giorno, soglia d'accuratezza 90%+.",
            "Anthropic, OpenAI e Adobe: agenti al lavoro in ufficio.",
        ],
        cta="La tua azienda sta già misurando quanto lavoro reale affida agli agenti AI, o lo guarda ancora da fuori? 👇",
        hashtags="#IntelligenzaArtificiale #AI #AgentiAI #Innovazione #B2B",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 17/11",
        format="Mito da sfatare",
        title="Dietro ogni exploit c'è sempre un hacker esperto che lo scrive e lo lancia. Quindi senza una persona dietro sei al sicuro",
        titolo_post="Senza un hacker dietro, sei al sicuro",
        sottotitolo_post="Un agente AI ha trasformato da solo una patch di sicurezza in un exploit, senza aiuto umano.",
        barrato="sicuro",
        news="Google (GTIG) rivela il primo agente AI che trasforma da solo una patch in un exploit funzionante (16/11)",
        news_url="https://www.theregister.com/research/2026/11/16/google-ai-agent-turned-a-security-patch-into-a-working-exploit-with-no-human-help/5309926",
        hook="🔥 Il mito: dietro un attacco informatico c'è sempre, in qualche fase, una persona che analizza la falla, scrive l'exploit e lo lancia — un agente AI può aiutare, ma il lavoro vero lo fa ancora un umano esperto.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="Il Google Threat Intelligence Group ha trovato un framework di agenti AI (exploit_agent) che confronta da solo le patch di sicurezza e genera exploit funzionanti, senza intervento umano in nessuna fase.",
        myth_body="Il 16 novembre Google ha pubblicato il suo rapporto trimestrale sulle minacce AI, documentando il primo caso noto di un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante. Il framework, chiamato \"exploit_agent\", è stato trovato su un server di staging esposto su internet: confronta in automatico il codice prima e dopo gli aggiornamenti di sicurezza di software web popolari, individua le vulnerabilità introdotte dalla patch, sviluppa l'exploit e lo esegue — senza che una persona intervenga in nessuna fase.",
        points=[
            "Il framework \"exploit_agent\" confronta il codice prima e dopo gli aggiornamenti di sicurezza di software web popolari, individua le vulnerabilità e sviluppa ed esegue l'exploit, tutto senza intervento umano.",
            "I ricercatori di Google lo hanno trovato su un server di staging esposto su internet, insieme a dati già rubati ad altre organizzazioni e a strumenti per muoversi dentro una rete una volta compromessa.",
            "Google segnala che questo framework si aggiunge a una lista già nota di strumenti offensivi agentici — tra cui ARTEX, lo stesso usato nell'attacco al fornitore blockchain Chainstack della settimana scorsa.",
        ],
        punti_post=[
            "exploit_agent: trova e sfrutta falle senza intervento umano.",
            "Trovato su un server esposto, con dati già rubati ad altri.",
            "Tra i framework noti anche ARTEX, usato contro Chainstack.",
        ],
        myth_closing="Il problema non è se la tua azienda abbia budget per attirare hacker esperti — è che il costo di trasformare una falla in un attacco si sta avvicinando a zero, perché la parte più lenta del lavoro la fa ormai un agente AI. Patchare in fretta non basta più se tra la pubblicazione di una patch e il suo sfruttamento non c'è più il tempo che serviva a un umano per capirla.",
        cta="La tua azienda applica le patch di sicurezza entro ore, o ancora entro settimane? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 18/11",
        format="Carosello / documento dati — promosso a Prioritario per la densità di cifre",
        title="Dentro i quasi 500 agenti AI di AT&T già al lavoro: i numeri della trasformazione agentica più grande vista finora",
        titolo_post="Agenti AI al lavoro: i numeri di AT&T",
        sottotitolo_post="Quasi 500 workflow agentici in produzione, 45 miliardi di token elaborati ogni giorno.",
        closing_title="Chi fissa la soglia per togliere la supervisione?",
        closing_body="Prima di contare quanti workflow delega un agente, qualcuno deve aver fissato la soglia di accuratezza per farlo lavorare da solo.",
        news="AT&T gestisce quasi 500 workflow agentici in produzione, 45 miliardi di token al giorno (14/11)",
        news_url="https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/",
        hook="Il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione — non una demo, ma un programma con una struttura di governance precisa su quando un agente può lavorare senza supervisione diretta.",
        points=[
            "500 — i workflow agentici che AT&T gestisce oggi in produzione (quasi), con l'obiettivo dichiarato di triplicarli entro il 2027.",
            "45 miliardi — i token AI elaborati ogni giorno dalla piattaforma, saliti da 27 miliardi a marzo 2026.",
            "1 milione — le transazioni mensili gestite dalla piattaforma di agenti AI di AT&T, secondo l'azienda.",
            "90 — la soglia di accuratezza (fascia medio-alta, in percentuale) che un workflow deve raggiungere prima che AT&T rimuova la supervisione umana diretta.",
            "5 volte — il ritorno sugli investimenti in AI di produzione dichiarato da AT&T entro un anno (dato dell'azienda stessa, non verificato in modo indipendente).",
        ],
        punti_post=[
            "500 — workflow agentici in produzione (obiettivo: triplicarli nel 2027).",
            "45 miliardi — token elaborati al giorno (da 27 mld a marzo).",
            "1 milione — transazioni gestite al mese dalla piattaforma.",
            "90% — soglia per togliere la supervisione umana.",
            "5x — ritorno dichiarato sugli investimenti AI in un anno (dato AT&T).",
        ],
        closing="Il salto di scala è reale: quasi 500 workflow agentici, 45 miliardi di token al giorno, un obiettivo di triplicare tutto entro il 2027. Ma il dettaglio che vale di più non è la scala — è la regola che la rende sostenibile: ogni workflow parte con supervisione umana, e la perde solo quando l'accuratezza supera una soglia fissata in anticipo, non quando qualcuno decide che \"probabilmente va bene così\". I dati di AT&T vengono dall'azienda stessa e non sono stati verificati in modo indipendente.",
        cta="La tua azienda ha già fissato una soglia esplicita prima di togliere la supervisione umana a un agente AI, o la decisione resta informale? 👇",
        hashtags="#AgentiAI #IntelligenzaArtificiale #Innovazione #B2B #Automazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 19/11",
        format="Esperienza diretta",
        title="Dopo il caso Cursor/Fireworks, abbiamo controllato le estensioni e le dipendenze che il team usa negli editor AI",
        titolo_post="Estensioni AI: le abbiamo *verificate*",
        sottotitolo_post="Dopo il caso Cursor, abbiamo controllato estensioni e dipendenze usate negli editor AI del team.",
        news="Spunto dal caso Cursor/Fireworks AI: chiave rubata, estensione Claude Code malevola nel marketplace (13/11)",
        news_url="https://www.unite.ai/cursor-traces-breach-to-access-key-exposed-by-fireworks-ai/",
        hook="Dopo il caso di questa settimana — una chiave rubata a un fornitore AI ha permesso di inserire un'estensione malevola nel marketplace di un editor di codice assistito da AI — ci siamo fatti la domanda scomoda: le estensioni e i plugin AI che il team installa nei propri editor sono davvero quelli che pensiamo? Questa settimana abbiamo controllato cosa è installato davvero, non solo cosa risulta dalla lista ufficiale.",
        is_template=True,
        points=[
            "Abbiamo elencato tutte le estensioni e i plugin AI installati negli editor di codice del team (marketplace ufficiali e non), e per ciascuno controllato la fonte e l'ultimo aggiornamento.",
            "[Da personalizzare con l'esito reale della verifica del team: quali estensioni avevano una provenienza poco chiara, cosa avete disinstallato o sostituito, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi o esiti non verificati.]",
            "La domanda utile non è se il marketplace sia affidabile — di norma lo è — ma se qualcuno in azienda controlla periodicamente cosa viene installato, non solo al momento dell'onboarding.",
        ],
        punti_post=[
            "Abbiamo elencato le estensioni AI installate dal team.",
            "[Da personalizzare con l'esito reale della verifica del team.]",
            "La vera domanda: qualcuno le controlla dopo l'onboarding?",
        ],
        cta="La tua azienda controlla periodicamente le estensioni e i plugin AI installati nei suoi editor, o solo al primo giorno? Raccontaci 👇",
        hashtags="#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 20/11",
        format="Divulgativo stile Datapizza",
        title="Cos'è un \"exploit agent\": il framework che Google ha scoperto trasformare da solo una patch in un attacco",
        titolo_post="Cos'è un \"exploit agent\"",
        sottotitolo_post="Il framework che trasforma da solo una patch di sicurezza in un attacco, senza aiuto umano.",
        news="Spunto dal rapporto Google GTIG (vedi post di martedì) e dal caso Chainstack",
        news_url="https://www.theregister.com/research/2026/11/16/google-ai-agent-turned-a-security-patch-into-a-working-exploit-with-no-human-help/5309926",
        hook="Questa settimana abbiamo raccontato un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante, e un fornitore (Cursor) che ha dovuto bloccare un'estensione malevola finita nel suo marketplace. Ma cosa vuol dire davvero \"agente AI offensivo\", e in cosa differisce da un normale strumento di sicurezza?",
        points=[
            "Uno strumento di sicurezza tradizionale segnala una vulnerabilità e si ferma lì: decide una persona se e come sfruttarla. Un agente AI offensivo, invece, riceve un obiettivo — \"trova e sfrutta le falle in questo software\" — e porta a termine da solo tutti i passaggi: confronto del codice, sviluppo dell'exploit, esecuzione.",
            "Google ha trovato un framework di questo tipo, chiamato exploit_agent, configurato per analizzare in continuo gli aggiornamenti di sicurezza di software web popolari: più il bersaglio è diffuso, più conviene automatizzare l'attacco su scala.",
            "La stessa logica vale al contrario: più un'azienda rende prevedibile e documentato chi può accedere a cosa — come fa, ad esempio, chi fissa soglie esplicite prima di dare autonomia a un agente — più stringe lo spazio in cui uno strumento come questo può muoversi senza essere notato.",
        ],
        punti_post=[
            "Uno strumento tradizionale segnala; un agente offensivo sfrutta da solo.",
            "exploit_agent: analizza da solo le patch di software popolari.",
            "La difesa: sapere sempre chi/cosa può accedere a cosa, e perché.",
        ],
        cta="Conoscevi già la differenza tra uno strumento di sicurezza tradizionale e un agente AI offensivo? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #Cybersecurity #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="Il rimbalzo dei chip AI dopo il crollo: i numeri della settimana di recupero",
        news="Il recupero parziale dei titoli dei semiconduttori dopo il crollo della settimana del 3-7 novembre",
        news_url="https://stocktwits.com/news-articles/markets/equity/amd-avgo-intc-mu-chip-stocks-inch-higher-as-investors-look-past-midterms-led-selloff-nvidia-controversy/cNGAD0CR9eR",
        hook="Due settimane fa i chip AI erano crollati del 12% in cinque giorni. Questa settimana i titoli hanno recuperato parte del terreno perso: ecco cosa dicono gli analisti su cosa è cambiato e cosa no.",
        points=[
            "12% — il calo dell'indice SOX nella settimana del 3-7 novembre, la peggiore dall'aprile 2025, dopo le elezioni di midterm del 3 novembre.",
            "Gli analisti descrivono il recupero di lunedì 9 novembre come investitori che iniziano a guardare oltre la correzione legata ai risultati elettorali, non come un segnale che i dubbi di fondo sulla spesa in data center siano spariti.",
            "Nvidia resta sotto osservazione per le polemiche emerse nei giorni precedenti, secondo gli stessi report che descrivono il recupero del settore.",
        ],
        closing="Un rimbalzo non è una risposta alla domanda che resta aperta da due settimane — se la spesa in infrastrutture AI sia sostenibile quanto si sperava — ma solo la prova che il mercato, per ora, resta diviso su quella domanda.",
        cta="La tua azienda pianifica i costi di infrastruttura AI pensando anche agli scenari in cui i prezzi tornano a salire? 👇",
        hashtags="#AI #Mercati #Infrastruttura #B2B #Chip",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice sugli agenti AI al lavoro (e su chi li controlla)",
        news="Sintesi dei trend della settimana 10-16 novembre 2026",
        news_url="https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "Gli agenti AI sono arrivati in produzione su scala: AT&T ne gestisce quasi 500, con 45 miliardi di token elaborati al giorno e un obiettivo di triplicarli entro il 2027.",
            "Anthropic (Sheets, Whiteboards, connettori), OpenAI (Business Agent in ChatGPT) e Adobe (Creative Agent sempre attivo) hanno messo agenti AI dentro gli strumenti che usiamo ogni giorno, tutti nella stessa settimana.",
            "Google ha documentato il primo caso noto di un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante, senza intervento umano.",
            "Cursor ha confermato che una chiave rubata a un fornitore AI (Fireworks, lo stesso coinvolto nel caso Notion di due settimane fa) ha portato a un'estensione malevola nel suo marketplace, scaricabile da fino a 5.000 sviluppatori.",
            "I chip AI hanno recuperato parte del terreno perso due settimane fa, ma gli analisti non lo leggono come la fine dei dubbi sulla sostenibilità della spesa in infrastrutture.",
        ],
        closing="Una settimana che racconta la stessa domanda da angolazioni diverse: man mano che gli agenti AI smettono di essere una demo e iniziano a fare lavoro vero su scala, la stessa tecnologia comincia ad automatizzare anche l'attacco. AT&T e il rapporto Google, questa settimana, sono la stessa domanda — chi governa l'autonomia di un agente, e chi se ne accorge quando manca — con due risposte opposte.",
        cta="Qual è la notizia di questa settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #AgentiAI #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 16/11",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 17/11",
        time="12:15",
        format="Mito da sfatare (serve sempre un umano esperto per sfruttare una falla — smentito dal rapporto Google GTIG)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — apre il filo di automazione/governance che attraversa il resto della settimana.",
    ),
    dict(
        day="Mercoledì 18/11",
        time="12:15",
        format="Carosello / dati (i numeri dei quasi 500 workflow agentici di AT&T)",
        reason="Seconda finestra pausa pranzo B2B. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i numeri di AT&T (500 workflow, 45 miliardi di token/giorno, soglia di accuratezza 90%) sono densi abbastanza da meritare uno spazio proprio — per questo è stato promosso da riserva a Prioritario questa settimana.",
    ),
    dict(
        day="Giovedì 19/11",
        time="08:30",
        format="Esperienza diretta (verifica delle estensioni e dei plugin AI installati negli editor del team)",
        reason="Segue narrativamente il mito di martedì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 20/11",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo sulla sicurezza aperto martedì collegando Google e Chainstack.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello numeri sul rimbalzo dei chip AI",
        reason="Banca contenuti: utile se la settimana ha margine per un sesto post, o come approfondimento del tema chip aperto due settimane fa.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
