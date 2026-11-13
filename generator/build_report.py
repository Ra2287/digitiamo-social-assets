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
# Notizie del periodo 6-13 novembre 2026, verificate su fonte diretta (non sui
# riassunti aggregatori). Filo conduttore della settimana: gli agenti AI
# smettono di essere una demo e diventano prodotto in ufficio (Anthropic),
# nella creativita' (Adobe), nel rapporto con i clienti (OpenAI) e nel lavoro
# quotidiano misurato con numeri reali, non proiezioni (Salesforce) — mentre,
# nello stesso giro di giorni, un fornitore AI non rispetta una promessa
# contrattuale scritta nero su bianco (Notion/Fireworks) e un attaccante usa
# lo stesso tipo di strumento — un framework di agenti AI — per violare
# un'azienda (Chainstack). Chiude il quadro il recupero parziale dei chip AI
# dopo il crollo della settimana precedente, e l'uscita di Google DeepMind
# dalla sola chat verso robotica industriale e genomica.
trends = [
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
        title="Notion conferma: la violazione al fornitore AI Fireworks ha esposto chat di alcuni clienti, nonostante la promessa di \"zero data retention\"",
        what="Notion ha comunicato che una violazione subita dal proprio fornitore di infrastruttura AI, Fireworks AI (intrusione iniziata il 6 ottobre, con accesso ai sistemi di produzione confermato il 24 ottobre), ha esposto le trascrizioni delle chat AI di una minoranza degli spazi di lavoro — meno dell'1%, secondo Notion — usate per la funzione \"Insights\" e per l'inferenza di modelli open-weight. Fireworks aveva un impegno contrattuale di \"zero data retention\" con Notion, ma le indagini di Notion hanno trovato che i dati erano stati comunque conservati sugli endpoint usati. Notion ha notificato Fireworks il 2 novembre, ricevuto conferma dell'accesso non autorizzato il 6 novembre, si è disconnessa dal fornitore, ha cancellato i dati e disabilitato Insights durante l'indagine.",
        why="Colpisce un prodotto usatissimo nel lavoro quotidiano di moltissime aziende e mostra che anche una garanzia contrattuale scritta nero su bianco può non reggere nei fatti — un rischio pratico, non teorico, per chiunque affidi dati a un fornitore AI.",
        source="Notion (centro assistenza)",
        url="https://notion.com/help/security-incident-involving-a-third-party-ai-vendor",
    ),
    dict(
        title="Gli \"AI coworker\" di Salesforce crescono di 21 volte in tre mesi: le aziende iniziano davvero a delegare lavoro vero agli agenti",
        what="Il 4 novembre Salesforce ha comunicato che Agentforce Coworker — l'agente AI a cui un dipendente assegna un compito, e che da solo pianifica e coordina i passaggi necessari — ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in soli tre mesi. Tra i casi citati: Fulton Bank lo usa per oltre 20 casi d'uso su circa 3.000 utenti; Adecco Group lo sta estendendo a 40 paesi; in un caso (BACA Systems) una domanda che richiedeva 45-60 minuti di ricerca manuale tra più schermate ha trovato risposta in pochi istanti. Il coworker costa 50 dollari per utente al mese, in aggiunta alle licenze Salesforce esistenti.",
        why="Dato sorprendente e pratico: mostra con numeri concreti, non proiezioni, che l'AI agentica sta passando dalla demo all'uso quotidiano in azienda — il cuore del posizionamento di Digitiamo su Team Augmentation e AI Business Academy. I dati sono diffusi da Salesforce stessa e non sono stati verificati in modo indipendente.",
        source="Salesforce (comunicato ufficiale)",
        url="https://www.salesforce.com/news/stories/agentforce-coworker-surpasses-185k-users/",
    ),
    dict(
        title="Un attaccante usa un framework di agenti AI per violare un fornitore di infrastruttura blockchain",
        what="Il 12 novembre Chainstack, fornitore di infrastruttura blockchain, ha reso noto che un attaccante — entrato il 26 ottobre attraverso un'istanza Grafana esposta su internet e lasciata con le credenziali di amministratore di default — ha raggiunto l'ambiente di produzione il 29 ottobre usando un framework di agenti AI (ARTEX) per condurre l'attacco, prima che Chainstack bloccasse l'accesso il 31 ottobre. Sono stati esposti nomi, email e hash delle password dei clienti; Chainstack dichiara che i servizi rivolti ai clienti non si sono mai fermati e ha chiesto ai clienti di ruotare le credenziali dei nodi.",
        why="È il rovescio della medaglia del trend Salesforce della stessa settimana: non un'azienda che usa agenti AI per lavorare meglio, ma un attaccante reale che ha usato lo stesso tipo di strumento per automatizzare una violazione — una controversia con forte presa su un pubblico ampio.",
        source="The Block",
        url="https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509",
    ),
    dict(
        title="I chip AI recuperano parte del terreno perso, dopo la peggiore settimana in un anno e mezzo",
        what="Dopo il crollo registrato nella settimana del 3-7 novembre (indice SOX -12%, la peggiore dall'aprile 2025, dopo le elezioni di midterm del 3 novembre), i titoli dei semiconduttori hanno recuperato parzialmente lunedì 9 novembre. Gli analisti descrivono il movimento come gli investitori che iniziano a guardare oltre la correzione legata ai risultati elettorali, con Nvidia che resta comunque sotto osservazione per le polemiche emerse nei giorni precedenti.",
        why="Contesto pratico diretto per chi valuta il costo di infrastruttura e API AI nei prossimi mesi: lo segnaliamo come coda del trend aperto la settimana scorsa nel PED, non come notizia nuova a sé — un rimbalzo non chiude la domanda sulla sostenibilità della spesa.",
        source="Stocktwits",
        url="https://stocktwits.com/news-articles/markets/equity/amd-avgo-intc-mu-chip-stocks-inch-higher-as-investors-look-past-midterms-led-selloff-nvidia-controversy/cNGAD0CR9eR",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
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
    dict(
        name="Salesforce",
        what="Comunica che Agentforce Coworker ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in tre mesi (4/11), con casi come Fulton Bank (20+ casi d'uso, circa 3.000 utenti) e Adecco Group (40 paesi).",
        positioning="Prova a dimostrare con numeri di adozione reale, non solo demo, che gli agenti AI sono già al lavoro nelle aziende — la prova che il mercato chiede da mesi, anche se i dati vengono dall'azienda stessa.",
        angle="Una crescita di 21 volte in tre mesi è anche un segnale di rischio: quante di quelle aziende hanno davvero qualcuno che decide a cosa l'agente può accedere, prima che l'adozione superi la governance? È lo stesso nodo del caso Chainstack della stessa settimana, letto dal lato di chi adotta invece che da chi subisce.",
    ),
    dict(
        name="Google (DeepMind)",
        what="Rilascia Gemini Robotics 2.5 (robot più capaci, testati con Mercedes-Benz) e AlphaGenome 2 (predizione genetica) nello stesso giorno (11/11).",
        positioning="Mostra l'ampiezza della ricerca DeepMind oltre la chat — robotica industriale e biologia computazionale — in un momento in cui i concorrenti diretti (OpenAI, Anthropic) si concentrano su agenti da ufficio e assistenti.",
        angle="Per un'azienda italiana la ricaduta diretta oggi è limitata (robotica e genomica restano lontane dal software gestionale), ma segnala dove la capacità dei modelli di base migliora più in fretta: un buon argomento per non fermare la formazione dei team tecnici alla sola \"AI generativa per i testi\".",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: gli agenti AI smettono di essere una demo — si apre
# lunedì con il quadro d'insieme (Salesforce, Anthropic, OpenAI, Adobe tutti
# nella stessa settimana), nessuna vendita. Martedì il mito da sfatare sul
# fornitore AI di Notion che non ha rispettato la promessa di "zero data
# retention". Mercoledì il carosello dati sui numeri di adozione di
# Agentforce Coworker (promosso a Prioritario per la densità di cifre, al
# posto di una seconda idea "ad alta varietà" — nota sul mix di formati, più
# sotto: questa settimana offre un solo trend davvero da mito, non due, quindi
# lo schema si adatta con giudizio). Giovedì l'esperienza diretta riprende il
# filo del mito verificando le clausole di data retention dei fornitori AI del
# team. Venerdì la mini-lezione spiega cos'è davvero un "agente AI" e perché
# lo stesso strumento può far crescere un'azienda (Salesforce) o far entrare
# un attaccante (Chainstack). Le due riserve restano banca contenuti: un
# carosello numeri sul rimbalzo dei chip AI, e la riflessione di chiusura.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 16/11",
        format="Thought leadership — apertura settimana",
        title="Questa settimana gli agenti AI sono usciti dalla demo: Salesforce, Anthropic, OpenAI e Adobe li hanno messi al lavoro vero — e qualcuno li ha usati anche per attaccare",
        titolo_post="Gli agenti AI non sono più una demo",
        sottotitolo_post="Anthropic, OpenAI, Adobe e Salesforce li hanno messi al lavoro vero questa settimana.",
        news="Agentforce Coworker di Salesforce supera i 185.000 utenti, +21 volte in tre mesi (4/11)",
        news_url="https://www.salesforce.com/news/stories/agentforce-coworker-surpasses-185k-users/",
        hook="Questa settimana quattro grandi fornitori hanno smesso di parlare di \"agenti AI\" come una demo e li hanno trasformati in prodotto: il 4 novembre Salesforce ha comunicato che il suo \"coworker\" AI ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in tre mesi. Il 10 novembre Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud. Nello stesso giro di giorni, un fornitore di infrastruttura blockchain (Chainstack) ha reso noto che un attaccante ha usato lo stesso tipo di strumento — un framework di agenti AI — per violare i propri sistemi.",
        visual_hook="Quattro grandi fornitori hanno trasformato gli agenti AI da demo a prodotto nella stessa settimana — e un attaccante ha usato lo stesso tipo di strumento per violare un'azienda.",
        points=[
            "185.000 — gli utenti attivi di Agentforce Coworker di Salesforce a inizio novembre, con un uso cresciuto di 21 volte in tre mesi: il segnale più concreto di adozione reale visto finora.",
            "Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori diretti con Salesforce, NetSuite e Workday, mentre OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende.",
            "Un fornitore di infrastruttura blockchain, Chainstack, ha reso noto che un attaccante ha usato lo stesso tipo di strumento — un framework di agenti AI — per violare i propri sistemi: la tecnologia che fa crescere l'adozione può accelerare anche l'attacco.",
        ],
        punti_post=[
            "Agentforce Coworker: 185.000 utenti, +21 volte in tre mesi.",
            "Anthropic, OpenAI e Adobe: agenti al lavoro in ufficio e creatività.",
            "Un attacco reale ha usato lo stesso tipo di framework di agenti.",
        ],
        cta="La tua azienda sta già misurando quanto lavoro reale affida agli agenti AI, o lo guarda ancora da fuori? 👇",
        hashtags="#IntelligenzaArtificiale #AI #AgentiAI #Innovazione #B2B",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 17/11",
        format="Mito da sfatare",
        title="Il contratto con il tuo fornitore AI dice \"zero data retention\". Quindi i tuoi dati restano *intoccati*",
        titolo_post="I tuoi dati restano *intoccati*?",
        sottotitolo_post="Una violazione al fornitore AI di Notion ha esposto chat nonostante la promessa \"zero retention\".",
        barrato="intoccati",
        news="Notion conferma l'esposizione di chat AI nella violazione al fornitore Fireworks (confermata 6/11)",
        news_url="https://notion.com/help/security-incident-involving-a-third-party-ai-vendor",
        hook="🔥 Il mito: se il contratto con il tuo fornitore AI promette \"zero data retention\" — l'impegno a non conservare i tuoi dati — allora quei dati restano al sicuro, punto.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="Fireworks aveva un impegno contrattuale di \"zero data retention\" con Notion. Le indagini hanno trovato che i dati erano stati conservati comunque.",
        myth_body="Notion ha comunicato che una violazione al proprio fornitore di infrastruttura AI, Fireworks AI, ha esposto le chat AI di una minoranza dei propri spazi di lavoro. Fireworks aveva con Notion un impegno contrattuale di \"zero data retention\": il contratto c'era. Le indagini di Notion hanno trovato che i dati erano stati conservati comunque sugli endpoint usati.",
        points=[
            "L'intrusione è iniziata il 6 ottobre ed è arrivata ai sistemi di produzione di Fireworks il 24 ottobre; Fireworks ha notificato Notion il 2 novembre e confermato l'accesso non autorizzato il 6 novembre.",
            "Esposte le trascrizioni delle chat AI usate per la funzione \"Insights\" (che classifica come i membri di un'azienda usano l'AI) e per l'inferenza di modelli open-weight — meno dell'1% degli spazi di lavoro Notion, secondo l'azienda.",
            "Notion si è disconnessa da Fireworks, ha cancellato i dati conservati lì, disabilitato Insights durante l'indagine e consiglia a chi è coinvolto di ruotare password e chiavi incollate nelle chat AI nel periodo interessato.",
        ],
        punti_post=[
            "Intrusione dal 6 ottobre; accesso confermato il 6 novembre.",
            "Esposte chat AI di meno dell'1% degli spazi Notion.",
            "Il contratto \"zero data retention\" non ha retto nei fatti.",
        ],
        myth_closing="Il problema non è se il tuo fornitore AI sia in malafede — probabilmente non lo è. È che una clausola contrattuale descrive un impegno, non una verifica tecnica: senza un controllo periodico su cosa succede davvero ai dati lungo la catena di sub-fornitori, un'azienda scopre che la promessa non ha retto solo quando arriva la notifica di violazione.",
        cta="La tua azienda ha mai verificato, oltre al contratto, cosa succede davvero ai dati lungo la catena dei fornitori AI che usa? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 18/11",
        format="Carosello / documento dati — promosso a Prioritario per la densità di cifre",
        title="Gli agenti AI al lavoro vero: i numeri dietro la crescita di 21 volte in tre mesi di Agentforce Coworker",
        titolo_post="Agenti AI al lavoro: i numeri",
        sottotitolo_post="Salesforce dichiara 185.000 utenti attivi, con un uso cresciuto di 21 volte in tre mesi.",
        closing_title="Chi decide cosa può fare l'agente?",
        closing_body="Prima di misurare quanto lavoro delega un agente, qualcuno deve aver deciso a cosa può accedere.",
        news="Salesforce annuncia che Agentforce Coworker supera i 185.000 utenti, +21 volte in tre mesi (4/11)",
        news_url="https://www.salesforce.com/news/stories/agentforce-coworker-surpasses-185k-users/",
        hook="Il 4 novembre Salesforce ha comunicato che Agentforce Coworker — l'agente AI a cui un dipendente assegna un compito, e che da solo pianifica e coordina i passaggi necessari — ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in appena tre mesi.",
        points=[
            "185.000 — gli utenti attivi di Agentforce Coworker a inizio novembre 2026, secondo i dati diffusi da Salesforce.",
            "21 volte — la crescita dell'uso del coworker AI in appena tre mesi, secondo Salesforce (dato dell'azienda stessa, non verificato in modo indipendente).",
            "50 dollari — il costo mensile per utente del coworker AI, in aggiunta alle licenze Salesforce già pagate dall'azienda.",
            "3.000 — gli utenti di Fulton Bank che usano il coworker AI su oltre 20 casi d'uso diversi, dalle verifiche interne al supporto ai clienti.",
            "40 — i paesi in cui Adecco Group sta estendendo l'uso del coworker AI nei propri processi, secondo Salesforce.",
        ],
        punti_post=[
            "185.000 — utenti attivi su Agentforce Coworker (inizio novembre).",
            "21 volte — crescita dell'uso in tre mesi (dato Salesforce).",
            "50 $ — costo mensile per utente, oltre alle licenze Salesforce.",
            "3.000 — utenti Fulton Bank, oltre 20 casi d'uso.",
            "40 — paesi in cui Adecco Group lo sta estendendo.",
        ],
        closing="Il salto di adozione è reale, non solo marketing: in tre mesi l'uso di un agente che pianifica ed esegue compiti da solo è cresciuto di 21 volte. Ma un'adozione che corre più veloce della governance lascia scoperta una domanda semplice: chi, in azienda, ha deciso a quali sistemi e dati l'agente può accedere, e chi controlla cosa fa davvero quando lavora senza supervisione diretta? I dati di crescita vengono da Salesforce stessa e non sono stati verificati in modo indipendente.",
        cta="La tua azienda misura la crescita dell'uso degli agenti AI, o anche i permessi che gli ha dato? 👇",
        hashtags="#AgentiAI #IntelligenzaArtificiale #Innovazione #B2B #Automazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 19/11",
        format="Esperienza diretta",
        title="Dopo il caso Notion/Fireworks, abbiamo controllato se la \"zero data retention\" dei nostri fornitori AI era davvero attiva",
        titolo_post="Zero data retention: lo abbiamo *verificato*",
        sottotitolo_post="Dopo il caso Notion, abbiamo riletto i contratti AI del team e verificato le impostazioni reali.",
        news="Spunto dal caso Notion/Fireworks AI, promessa di \"zero data retention\" non rispettata (vedi post di martedì)",
        news_url="https://notion.com/help/security-incident-involving-a-third-party-ai-vendor",
        hook="Dopo il caso di questa settimana — un fornitore AI che prometteva contrattualmente \"zero data retention\" e non l'ha rispettata — ci siamo fatti la domanda scomoda: i fornitori AI che usiamo noi rispettano davvero quello che promettono? Questa settimana abbiamo riletto i contratti e controllato le impostazioni reali, non solo quello che c'è scritto nelle condizioni.",
        is_template=True,
        points=[
            "Abbiamo elencato tutti i fornitori AI usati dal team (modelli, strumenti di scrittura, trascrizione, analytics) e per ciascuno cercato la clausola di data retention nel contratto o nei termini di servizio.",
            "[Da personalizzare con l'esito reale della verifica del team: quali fornitori avevano impostazioni diverse da quanto promesso nel contratto, cosa avete dovuto disattivare o cambiare, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi di fornitori o esiti non verificati.]",
            "La domanda utile non è se un contratto esista — quasi sempre esiste — ma se qualcuno in azienda lo ha mai messo alla prova chiedendo al fornitore una prova tecnica, non solo una dichiarazione scritta.",
        ],
        punti_post=[
            "Abbiamo elencato tutti i fornitori AI del team e le loro clausole.",
            "[Da personalizzare con l'esito reale della verifica del team.]",
            "La vera domanda: qualcuno ha mai messo alla prova il contratto?",
        ],
        cta="La tua azienda ha mai chiesto a un fornitore AI una prova tecnica della \"zero data retention\", non solo una dichiarazione scritta? Raccontaci 👇",
        hashtags="#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 20/11",
        format="Divulgativo stile Datapizza",
        title="Cos'è davvero un \"agente AI\", e perché lo stesso strumento può far crescere un'azienda o far entrare un attaccante",
        titolo_post="Cos'è davvero un agente AI",
        sottotitolo_post="La differenza tra un chatbot che risponde e un agente che agisce da solo sui tuoi sistemi.",
        news="Spunto dai lanci \"agentic\" della settimana e dal caso Chainstack (vedi post di lunedì)",
        news_url="https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509",
        hook="Questa settimana abbiamo parlato di agenti AI che pianificano compiti, lavorano dentro Photoshop o aiutano i clienti a scoprire un'azienda su ChatGPT — e di un attaccante che ha usato lo stesso tipo di strumento per violare un'azienda. Ma cosa vuol dire davvero \"agente AI\", e perché non è solo un chatbot più furbo?",
        points=[
            "Un chatbot risponde a una domanda e si ferma lì. Un agente AI, invece, riceve un obiettivo, decide da solo i passaggi per raggiungerlo e usa degli \"strumenti\" — accesso a un database, a una casella email, a un sistema aziendale — per eseguirli senza bisogno di istruzioni passo-passo.",
            "Questa capacità di agire, non solo rispondere, è anche il motivo per cui un agente è potente quanto i permessi che gli vengono dati: nel caso Chainstack di questa settimana, l'attaccante ha usato un framework di agenti AI per automatizzare i passaggi dell'attacco, dopo essere entrato da una singola configurazione lasciata con le credenziali di default.",
            "La domanda da farsi prima di dare un obiettivo a un agente AI, in azienda o nelle mani sbagliate, è sempre la stessa: a cosa può accedere davvero, e chi se ne accorge se usa quell'accesso in un modo che non ci si aspettava?",
        ],
        punti_post=[
            "Un chatbot risponde; un agente AI agisce da solo sui tuoi sistemi.",
            "Chainstack: un attaccante ha usato un framework di agenti per violare.",
            "La domanda chiave: a cosa accede l'agente, e chi lo controlla?",
        ],
        cta="Conoscevi già la differenza tra un chatbot e un agente AI che agisce da solo? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #AgentiAI #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="Il rimbalzo dei chip AI dopo il crollo: i numeri della settimana di recupero",
        news="Il recupero parziale dei titoli dei semiconduttori dopo il crollo della settimana del 3-7 novembre",
        news_url="https://stocktwits.com/news-articles/markets/equity/amd-avgo-intc-mu-chip-stocks-inch-higher-as-investors-look-past-midterms-led-selloff-nvidia-controversy/cNGAD0CR9eR",
        hook="La settimana scorsa abbiamo aperto il PED con il crollo dei chip AI. Questa settimana i titoli hanno recuperato parte del terreno perso: ecco cosa dicono gli analisti su cosa è cambiato e cosa no.",
        points=[
            "12% — il calo dell'indice SOX nella settimana del 3-7 novembre, la peggiore dall'aprile 2025, dopo le elezioni di midterm del 3 novembre.",
            "Gli analisti descrivono il recupero di lunedì 9 novembre come investitori che iniziano a guardare oltre la correzione legata ai risultati elettorali, non come un segnale che i dubbi di fondo sulla spesa in data center siano spariti.",
            "Nvidia resta sotto osservazione per le polemiche emerse nei giorni precedenti, secondo gli stessi report che descrivono il recupero del settore.",
        ],
        closing="Un rimbalzo non è una risposta alla domanda che ci siamo fatti la settimana scorsa — se la spesa in infrastrutture AI sia sostenibile quanto si sperava — ma solo la prova che il mercato, per ora, resta diviso su quella domanda.",
        cta="La tua azienda pianifica i costi di infrastruttura AI pensando anche agli scenari in cui i prezzi tornano a salire? 👇",
        hashtags="#AI #Mercati #Infrastruttura #B2B #Chip",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice sugli agenti AI al lavoro (e su chi li controlla)",
        news="Sintesi dei trend della settimana 6-13 novembre 2026",
        news_url="https://www.salesforce.com/news/stories/agentforce-coworker-surpasses-185k-users/",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "Gli agenti AI sono usciti dalla fase demo: Salesforce dichiara 185.000 utenti attivi su Agentforce Coworker, con un uso cresciuto di 21 volte in tre mesi.",
            "Anthropic (Sheets, Whiteboards, connettori), OpenAI (Business Agent in ChatGPT) e Adobe (Creative Agent sempre attivo) hanno messo agenti AI dentro gli strumenti che usiamo ogni giorno, tutti nella stessa settimana.",
            "Un fornitore AI di Notion (Fireworks) ha esposto chat nonostante un contratto di \"zero data retention\": una promessa scritta non è una verifica tecnica.",
            "Un attaccante ha usato un framework di agenti AI per violare un fornitore di infrastruttura blockchain (Chainstack): lo stesso tipo di strumento che fa crescere l'adozione può accelerare un attacco.",
            "I chip AI hanno recuperato parte del terreno perso la settimana precedente, ma gli analisti non lo leggono come la fine dei dubbi sulla sostenibilità della spesa in infrastrutture.",
        ],
        closing="Una settimana che racconta la stessa domanda da angolazioni diverse: man mano che gli agenti AI smettono di essere una demo e iniziano a fare lavoro vero, la domanda non è più \"funzionano?\" ma \"chi ha deciso cosa possono fare, e chi se ne accorge quando sbagliano?\". La risposta non è rallentare l'adozione — è non farla correre più veloce della governance.",
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
        format="Mito da sfatare (la promessa \"zero data retention\" non rispettata da Fireworks/Notion)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — apre il filo di fiducia/governance che attraversa il resto della settimana.",
    ),
    dict(
        day="Mercoledì 18/11",
        time="12:15",
        format="Carosello / dati (i numeri di Agentforce Coworker)",
        reason="Seconda finestra pausa pranzo B2B. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i numeri di adozione (185.000 utenti, 21 volte in tre mesi) sono densi abbastanza da meritare uno spazio proprio — per questo è stato promosso da riserva a Prioritario questa settimana.",
    ),
    dict(
        day="Giovedì 19/11",
        time="08:30",
        format="Esperienza diretta (verifica delle clausole \"zero data retention\" dei nostri fornitori AI)",
        reason="Segue narrativamente il mito di martedì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 20/11",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo sugli agenti AI aperto lunedì.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello numeri sul rimbalzo dei chip AI",
        reason="Banca contenuti: utile se la settimana ha margine per un sesto post, o come approfondimento del tema aperto nel PED della settimana precedente.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
