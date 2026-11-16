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
# Rigenerazione del 16 novembre 2026, su richiesta di Ramona ("sostituisci
# tutto"): ricerca rifatta da zero includendo le due nuove fonti aggiunte in
# CLAUDE.md lo stesso giorno (Hugging Face Daily Papers, GitHub Trending).
# Due candidati emersi in un primo giro di ricerca sono stati scartati dopo
# verifica sulla fonte primaria: la causa Sullivan & Cromwell sulle citazioni
# legali inventate dall'AI risale ad aprile 2026 (non a questa settimana), e
# lo studio Berkeley/Nature sull'ECG e il rischio cardiaco è di giugno 2026,
# solo ripubblicato da un aggregatore il 12/11 — entrambi riproposti da
# aggregatori con una data di superficie fuorviante. Confermano la regola del
# repo: verificare sulla fonte diretta, non sul riassunto.
# Filo conduttore della settimana: gli agenti AI smettono di essere un
# progetto pilota e diventano infrastruttura di produzione misurata in
# miliardi di token al giorno (AT&T), mentre la stessa settimana porta nuovi
# lanci "da ufficio" (Anthropic, OpenAI, Adobe) e nuovi segnali che
# l'adozione corre più veloce della governance: una promessa contrattuale di
# "zero data retention" che non regge nei fatti (Notion/Fireworks) e un
# attaccante che usa lo stesso tipo di strumento — un framework di agenti AI
# — per violare un'azienda (Chainstack).
trends = [
    dict(
        title="AT&T gestisce quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno",
        what="Il 14 novembre SiliconANGLE ha riportato, da un intervento di Luke Corbin (vice presidente per la trasformazione digitale e l'AI di AT&T Business) a un evento AWS, che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con l'obiettivo di triplicarli entro il 2027. La piattaforma elabora circa 45 miliardi di token al giorno (da 27 miliardi a marzo 2026) e supera 1 milione di transazioni al mese. Ogni workflow parte con supervisione umana: l'autonomia arriva solo quando l'accuratezza raggiunge la fascia medio-alta del 90%, entro un profilo di rischio accettabile, con monitoraggio continuo del drift dopo la rimozione del controllo umano. I workflow che toccano i clienti passano dalla \"Business Agent Foundry\", un gruppo interno che mappa i processi ed elimina passaggi e dipendenze legacy prima di costruire l'agente; i workflow di produttività personale restano invece liberi. Tra i casi concreti: modifiche agli ordini di installazione fibra automatizzate direttamente sui sistemi mainframe, e tempi di attivazione delle connessioni internet dedicate dimezzati negli edifici già cablati.",
        why="Dato pratico e sorprendente più che proiezione: un'azienda con milioni di clienti quotidiani mostra, con cifre e soglie precise, cosa vuol dire portare gli agenti AI dalla demo alla produzione — incluso il meccanismo di governance (soglia di accuratezza, supervisione umana) che l'adozione spesso salta. Rilevante per un pubblico ampio, non solo per gli addetti ai lavori del settore telco.",
        source="SiliconANGLE",
        url="https://siliconangle.com/2026/11/14/att-uses-agentic-ai-to-reinvent-business-processes-from-the-ground-up/",
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
        title="Notion conferma: la violazione al fornitore AI Fireworks ha esposto chat di alcuni clienti, nonostante la promessa di \"zero data retention\"",
        what="Notion ha comunicato che una violazione subita dal proprio fornitore di infrastruttura AI, Fireworks AI (intrusione iniziata il 6 ottobre, con accesso ai sistemi di produzione confermato il 24 ottobre), ha esposto le trascrizioni delle chat AI di una minoranza degli spazi di lavoro — meno dell'1%, secondo Notion — usate per la funzione \"Insights\" e per l'inferenza di modelli open-weight. Fireworks aveva un impegno contrattuale di \"zero data retention\" con Notion, ma le indagini di Notion hanno trovato che i dati erano stati comunque conservati sugli endpoint usati. Notion ha notificato Fireworks il 2 novembre, ricevuto conferma dell'accesso non autorizzato il 6 novembre, si è disconnessa dal fornitore, ha cancellato i dati e disabilitato Insights durante l'indagine.",
        why="Colpisce un prodotto usatissimo nel lavoro quotidiano di moltissime aziende e mostra che anche una garanzia contrattuale scritta nero su bianco può non reggere nei fatti — un rischio pratico, non teorico, per chiunque affidi dati a un fornitore AI.",
        source="Notion (centro assistenza)",
        url="https://notion.com/help/security-incident-involving-a-third-party-ai-vendor",
    ),
    dict(
        title="Un attaccante usa un framework di agenti AI per violare un fornitore di infrastruttura blockchain",
        what="Il 12 novembre Chainstack, fornitore di infrastruttura blockchain, ha reso noto che un attaccante — entrato il 26 ottobre attraverso un'istanza Grafana esposta su internet e lasciata con le credenziali di amministratore di default — ha raggiunto l'ambiente di produzione il 29 ottobre usando un framework di agenti AI (ARTEX) per condurre l'attacco, prima che Chainstack bloccasse l'accesso il 31 ottobre. Sono stati esposti nomi, email e hash delle password dei clienti; Chainstack dichiara che i servizi rivolti ai clienti non si sono mai fermati e ha chiesto ai clienti di ruotare le credenziali dei nodi.",
        why="È il rovescio della medaglia del trend AT&T della stessa settimana: non un'azienda che governa l'autonomia di un agente con soglie e supervisione, ma un attaccante reale che ha usato lo stesso tipo di strumento senza nessuna delle due cose — una controversia con forte presa su un pubblico ampio.",
        source="The Block",
        url="https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509",
    ),
    dict(
        title="Gli \"AI coworker\" di Salesforce crescono di 21 volte in tre mesi: le aziende iniziano davvero a delegare lavoro vero agli agenti",
        what="Il 4 novembre Salesforce ha comunicato che Agentforce Coworker — l'agente AI a cui un dipendente assegna un compito, e che da solo pianifica e coordina i passaggi necessari — ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in soli tre mesi. Tra i casi citati: Fulton Bank lo usa per oltre 20 casi d'uso su circa 3.000 utenti; Adecco Group lo sta estendendo a 40 paesi. Il coworker costa 50 dollari per utente al mese, in aggiunta alle licenze Salesforce esistenti.",
        why="Insieme al trend AT&T della stessa settimana, un secondo segnale — stavolta da un fornitore — che l'AI agentica sta passando dalla demo all'uso quotidiano in azienda: i dati sono diffusi da Salesforce stessa e non sono stati verificati in modo indipendente, ma la direzione è la stessa vista da due angolazioni diverse (vendor e adottante).",
        source="Salesforce (comunicato ufficiale)",
        url="https://www.salesforce.com/news/stories/agentforce-coworker-surpasses-185k-users/",
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
        name="Google (DeepMind)",
        what="Rilascia Gemini Robotics 2.5 (robot più capaci, testati con Mercedes-Benz) e AlphaGenome 2 (predizione genetica) nello stesso giorno (11/11).",
        positioning="Mostra l'ampiezza della ricerca DeepMind oltre la chat — robotica industriale e biologia computazionale — in un momento in cui i concorrenti diretti (OpenAI, Anthropic) si concentrano su agenti da ufficio e assistenti.",
        angle="Per un'azienda italiana la ricaduta diretta oggi è limitata (robotica e genomica restano lontane dal software gestionale), ma segnala dove la capacità dei modelli di base migliora più in fretta: un buon argomento per non fermare la formazione dei team tecnici alla sola \"AI generativa per i testi\".",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana (rigenerato il 16/11/2026): lunedì il quadro d'insieme
# parte da AT&T — il caso più concreto di agenti AI già in produzione su
# scala, con soglie di governance esplicite — e lo affianca ai lanci "da
# ufficio" della stessa settimana (Anthropic, OpenAI, Adobe). Martedì il mito
# da sfatare resta sul fornitore AI di Notion che non ha rispettato la
# promessa di "zero data retention" (unico trend della settimana che si
# presta davvero al formato mito: niente secondo mito forzato). Mercoledì il
# carosello dati entra nei numeri di AT&T (promosso a Prioritario per la
# densità di cifre, al posto di una seconda idea "ad alta varietà"). Giovedì
# l'esperienza diretta riprende il filo del mito di martedì verificando le
# clausole di data retention dei fornitori AI del team. Venerdì la
# mini-lezione spiega cos'è davvero un "agente AI" a partire dal contrasto
# fra la governance di AT&T e l'assenza di governance nel caso Chainstack. Le
# due riserve restano banca contenuti: un carosello numeri sul rimbalzo dei
# chip AI, e la riflessione di chiusura.
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
        hook="Questa settimana la differenza fra parlare di agenti AI e farli lavorare davvero si è vista nei numeri: il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno e oltre 1 milione di transazioni al mese — e un obiettivo di triplicare i workflow entro il 2027. Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud.",
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
        title="Cos'è davvero un \"agente AI\": la differenza fra i quasi 500 di AT&T e quello usato per violare Chainstack",
        titolo_post="Cos'è davvero un agente AI",
        sottotitolo_post="La differenza tra un chatbot che risponde e un agente che agisce da solo sui tuoi sistemi.",
        news="Spunto dal caso AT&T (vedi post di lunedì) e dal caso Chainstack della stessa settimana",
        news_url="https://www.theblock.co/news/ecosystems/2026-11-12-chainstack-security-breach-438509",
        hook="Questa settimana abbiamo raccontato due storie opposte con lo stesso protagonista: AT&T, che gestisce quasi 500 agenti AI in produzione togliendo la supervisione umana solo sopra una soglia di accuratezza fissata in anticipo — e un attaccante che ha usato lo stesso tipo di strumento per violare Chainstack, un fornitore di infrastruttura blockchain. Ma cosa vuol dire davvero \"agente AI\", e perché non è solo un chatbot più furbo?",
        points=[
            "Un chatbot risponde a una domanda e si ferma lì. Un agente AI, invece, riceve un obiettivo, decide da solo i passaggi per raggiungerlo e usa degli \"strumenti\" — accesso a un database, a una casella email, a un sistema aziendale — per eseguirli senza bisogno di istruzioni passo-passo.",
            "Questa capacità di agire, non solo rispondere, è anche il motivo per cui un agente è potente quanto i permessi che gli vengono dati: AT&T lo governa con soglie di accuratezza esplicite prima di togliere la supervisione; nel caso Chainstack, invece, l'attaccante ha usato un framework di agenti AI per automatizzare i passaggi dell'attacco, dopo essere entrato da una singola configurazione lasciata con le credenziali di default.",
            "La domanda da farsi prima di dare un obiettivo a un agente AI, in azienda o nelle mani sbagliate, è sempre la stessa: a cosa può accedere davvero, e chi se ne accorge se usa quell'accesso in un modo che non ci si aspettava?",
        ],
        punti_post=[
            "Un chatbot risponde; un agente AI agisce da solo sui tuoi sistemi.",
            "AT&T lo governa con soglie; Chainstack mostra cosa succede senza.",
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
            "Un fornitore AI di Notion (Fireworks) ha esposto chat nonostante un contratto di \"zero data retention\": una promessa scritta non è una verifica tecnica.",
            "Un attaccante ha usato un framework di agenti AI per violare un fornitore di infrastruttura blockchain (Chainstack): lo stesso tipo di strumento che fa crescere l'adozione può accelerare un attacco, quando manca la governance che invece AT&T applica.",
            "I chip AI hanno recuperato parte del terreno perso due settimane fa, ma gli analisti non lo leggono come la fine dei dubbi sulla sostenibilità della spesa in infrastrutture.",
        ],
        closing="Una settimana che racconta la stessa domanda da angolazioni diverse: man mano che gli agenti AI smettono di essere una demo e iniziano a fare lavoro vero su scala, la domanda non è più \"funzionano?\" ma \"chi ha fissato la soglia per farli lavorare da soli, e chi se ne accorge quando sbagliano?\". AT&T e Chainstack, questa settimana, sono la stessa domanda con due risposte opposte.",
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
        format="Carosello / dati (i numeri dei quasi 500 workflow agentici di AT&T)",
        reason="Seconda finestra pausa pranzo B2B. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i numeri di AT&T (500 workflow, 45 miliardi di token/giorno, soglia di accuratezza 90%) sono densi abbastanza da meritare uno spazio proprio — per questo è stato promosso da riserva a Prioritario questa settimana.",
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
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo aperto lunedì confrontando governance (AT&T) e assenza di governance (Chainstack).",
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
