# -*- coding: utf-8 -*-
"""Genera l'HTML del report PED settimanale Digitiamo."""
import html

C = {
    "navy": "#0e0a48",
    "brand": "#4a3aff",
    "secondary": "#717ffe",
    "tint": "#ebeefc",
    "green": "#43ef84",
    "white": "#ffffff",
}

WEEK_LABEL = "31 agosto – 4 settembre 2026"
GENERATED_ON = "Lunedì 31 agosto 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
trends = [
    dict(
        title="Salesforce e Anthropic lanciano “Claudeforce”",
        what="Salesforce e Anthropic hanno annunciato una partnership che integra Claude come motore di ragionamento nativo di Agentforce e Slack: Salesforce entra nell'app Claude con 37 competenze di vendita precostituite, mentre Claude entra in Agentforce anche via Amazon Bedrock per i settori regolamentati. Beta aperta prevista a settembre 2026.",
        why="Il confine tra “assistente AI” e “software aziendale” si dissolve: l'interfaccia del CRM non è più una dashboard da imparare, ma una conversazione. È il segnale più esplicito finora di dove sta andando l'intero mercato enterprise software.",
        source="Salesforce Newsroom",
        url="https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/",
    ),
    dict(
        title="Nvidia chiude il trimestre più grande della sua storia",
        what="Nvidia ha riportato 96,2 miliardi di dollari di fatturato trimestrale (+106% anno su anno), trainato dal segmento data center (+117%, circa 89 miliardi). Il titolo è salito di quasi il 9% in una seduta, aggiungendo circa 440 miliardi di dollari di capitalizzazione.",
        why="Conferma che la domanda di infrastruttura AI non rallenta, ma alza ulteriormente l'asticella su chi può permettersi di costruire capacità computazionale in proprio: per la maggior parte delle aziende, l'accesso a questa capacità passerà sempre più da cloud e partner terzi.",
        source="Intellectia.ai / US News",
        url="https://intellectia.ai/blog/nvidia-q2-earnings-august-29-2026",
    ),
    dict(
        title="L'EU AI Act “diventa reale”",
        what="Dal 2 agosto 2026 sono in vigore gli obblighi di trasparenza, notifica agli utenti e watermarking per i contenuti generati da AI in tutta l'Unione Europea. Le regole più severe per i sistemi ad “alto rischio” arriveranno in due tappe successive, a dicembre 2027 e agosto 2028.",
        why="Le aziende italiane, PMI comprese, devono iniziare a documentare ORA dove e come usano l'AI: l'EU AI Office ha già il potere di richiedere informazioni e accesso ai modelli, anche prima che le sanzioni specifiche siano pienamente codificate.",
        source="Axios / Commissione Europea",
        url="https://www.axios.com/2026/08/28/eu-ai-act-gets-real",
    ),
    dict(
        title="Cursor lancia Origin, alternativa a GitHub per team che lavorano con agenti AI",
        what="Cursor ha lanciato Origin, una piattaforma di hosting codice pensata per team dove agenti autonomi aprono pull request insieme alle persone. Dato interno rivelato dall'azienda: il 35% delle PR aperte sui repository Cursor arriva da agenti, non da sviluppatori umani.",
        why="È la prova più concreta finora di dove si sta spostando il collo di bottiglia dello sviluppo software: non più la scrittura del codice, ma la sua revisione, la sua architettura e il suo passaggio sicuro in produzione.",
        source="VentureBeat",
        url="https://venturebeat.com/infrastructure/cursor-launches-origin-code-hosting-platform-as-github-outage-exposes-opening-in-ai-coding-race",
    ),
    dict(
        title="GitHub, seconda interruzione globale in due settimane",
        what="GitHub ha subito una nuova interruzione globale (quasi 7 ore), la seconda in due settimane, con cause attribuite ad autoscaling difettoso e “retry storm” di VS Code. L'episodio ha dato involontariamente forza al lancio di Origin da parte di Cursor.",
        why="La disponibilità e l'affidabilità dell'infrastruttura di sviluppo tornano centrali quanto la qualità del modello AI: un'azienda che affida tutto il proprio ciclo di sviluppo a un singolo vendor cloud si espone a rischi operativi reali.",
        source="The Register / Forbes",
        url="https://www.theregister.com/saas/2026/08/19/github_blames_8hour_outage_on_autoscaling_fail_and_vs_code_retry_storm/",
    ),
    dict(
        title="Skan AI raccoglie 63M$ per mappare come si lavora davvero in azienda",
        what="Skan AI ha chiuso un round Series C da 63 milioni di dollari (guidato da Cathay Innovation e Dell Technologies Capital) per costruire un “context graph” di come i dipendenti eseguono realmente i propri compiti, non di come i processi sono documentati. Il CEO cita una statistica chiave: il 95% dei pilot di AI generativa in azienda fallisce per mancanza di contesto reale sui processi.",
        why="Un investitore terzo conferma indipendentemente quello che molti consulenti tech ripetono da mesi: il collo di bottiglia dell'adozione AI enterprise non è la qualità del modello, è la comprensione (e la mappatura) dei processi reali dell'azienda.",
        source="VentureBeat",
        url="https://venturebeat.com/data/skan-ai-raises-63-million-betting-that-watching-how-employees-actually-work-is-the-missing-layer-of-enterprise-ai",
    ),
    dict(
        title="Google lancia Gemini Enterprise for Legal",
        what="Google ha presentato una versione verticale della sua piattaforma enterprise pensata per studi legali e uffici legali interni: agenti AI per analisi contratti, ricerca giuridica, verifica citazioni e monitoraggio normativo, integrati con database come Thomson Reuters.",
        why="Conferma la tendenza a costruire agenti specializzati per singola funzione o settore, invece di assistenti generici: un pattern che qualunque azienda B2B può replicare sul proprio dominio verticale, con il giusto lavoro di scoping.",
        source="AIdapted",
        url="https://www.aidapted.ro/en/articles/ai-news-of-the-day-august-26-2026/",
    ),
    dict(
        title="Mistral AI firma una partnership con la saudita HUMAIN",
        what="Mistral AI e HUMAIN hanno annunciato una collaborazione per infrastrutture di calcolo, sviluppo di modelli avanzati e distribuzione di soluzioni AI in Arabia Saudita, con una partnership del valore di centinaia di milioni di euro.",
        why="Il player europeo che si presenta come alternativa “sovrana” ai big USA cerca crescita e capitali fuori dai confini UE, proprio mentre il dibattito su sovranità tecnologica europea (e AI Act) si fa più concreto in patria.",
        source="AIdapted",
        url="https://www.aidapted.ro/en/articles/ai-news-of-the-day-august-26-2026/",
    ),
    dict(
        title="Amazon chiude Mechanical Turk dopo 21 anni",
        what="Amazon ha annunciato la chiusura di AWS Mechanical Turk, effettiva dal 30 settembre 2026. La piattaforma di crowdsourcing per compiti come etichettatura immagini e trascrizione è stata progressivamente sostituita da AI e società specializzate in annotazione dati.",
        why="Segnale simbolico ma concreto: l'automazione non riguarda solo il software applicativo, ma l'intera filiera che alimenta i modelli AI, inclusi i compiti umani che finora restavano “dietro le quinte”.",
        source="Tech Startups",
        url="https://techstartups.com/2026/08/26/top-tech-news-today-august-26-2026-amazon-anthropic-google-microsoft-waymo-more/",
    ),
    dict(
        title="Anthropic dichiara un mercato indirizzabile da 30.000 miliardi di dollari",
        what="In vista di una possibile IPO da quasi 2.000 miliardi di dollari di valutazione, Anthropic ha comunicato ai potenziali investitori un mercato totale indirizzabile (TAM) superiore ai 30 trilioni di dollari, riflettendo il valore economico delle attività potenzialmente automatizzabili con l'AI.",
        why="Il divario tra le proiezioni finanziarie dei grandi laboratori AI e i tassi di successo reali dei progetti AI in azienda (vedi Skan AI sopra) non è mai stato così ampio: un buon punto di realismo da portare ai clienti PMI che vedono solo i titoli sulle valutazioni miliardarie.",
        source="Tech Startups",
        url="https://techstartups.com/2026/08/26/top-tech-news-today-august-26-2026-amazon-anthropic-google-microsoft-waymo-more/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Salesforce + Anthropic (“Claudeforce”)",
        what="Hanno fuso CRM e modello di ragionamento AI in un'unica interfaccia conversazionale: Claude entra in Agentforce, Salesforce entra nell'app Claude con competenze di vendita pronte all'uso.",
        positioning="Si posizionano come il punto d'incontro tra “intelligenza probabilistica” (il modello) e “sistemi deterministici e governati” (i dati e i processi Salesforce) — la citazione di Benioff è esplicita su questo.",
        angle="Le aziende clienti di questi grandi ecosistemi avranno bisogno di chi sa integrare e customizzare gli agenti sui processi reali: non tutte hanno un team interno pronto a governare Agentforce o Slack AI. È terreno naturale per il Team Augmentation Digitiamo.",
    ),
    dict(
        name="Cursor (lancio di Origin)",
        what="Ha lanciato una piattaforma di hosting proprietaria per competere con GitHub, capitalizzando sull'outage GitHub della stessa settimana per accelerare l'adozione.",
        positioning="Punta su velocità e integrazione totale dello stack (editor, hosting, agenti), ma con criticità di governance: termini di servizio poco trasparenti, opt-out di default per l'uso dei dati, azienda ora sotto il controllo di SpaceX.",
        angle="Mentre i tool si affrettano a “possedere tutto lo stack”, le aziende serie hanno bisogno di indipendenza e controllo sui propri dati e processi: un argomento in più per portare competenze senior interne invece di legarsi mani e piedi a un singolo vendor.",
    ),
    dict(
        name="Google (Gemini Enterprise for Legal)",
        what="Ha lanciato un agente AI verticale per il settore legale, con retrieval su fonti autorevoli e verifica delle citazioni.",
        positioning="Specializzazione per funzione aziendale invece di genericità: un agente costruito per un caso d'uso preciso, non un chatbot universale.",
        angle="Lo stesso principio — soluzioni cucite sul caso d'uso reale del cliente, non “AI a pioggia” — è il cuore dell'AI Business Academy Digitiamo: formazione e progetti mirati sui casi d'uso specifici dell'azienda cliente.",
    ),
    dict(
        name="Mistral AI + HUMAIN",
        what="Ha firmato una partnership infrastrutturale in Medio Oriente per crescere fuori dai confini europei.",
        positioning="Si presenta come l'alternativa “sovrana” europea ai big AI statunitensi, ma cerca capitali e mercati fuori dall'UE per scalare.",
        angle="Per i clienti italiani preoccupati di sovranità e compliance (vedi AI Act in vigore), la domanda che conta davvero non è “quale modello uso” ma “chi mi aiuta a integrarlo in modo conforme e governato”: un tema di execution locale, non di scelta del fornitore di modelli.",
    ),
    dict(
        name="Skan AI",
        what="Ha raccolto 63 milioni di dollari per costruire una mappa di come si lavora davvero in azienda, colmando il divario tra processi documentati e processi reali.",
        positioning="Si posiziona come il livello di “process intelligence” mancante tra il modello AI e la produzione: senza contesto reale sui processi, anche il modello migliore fallisce.",
        angle="È la conferma indipendente, da un investitore terzo, della tesi centrale con cui Digitiamo affronta ogni progetto: il problema dell'adozione AI non è il modello, è capire e ridisegnare i processi reali del cliente — esattamente il lavoro che precede ogni intervento di Team Augmentation o AI Business Academy fatto bene.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 31/8",
        format="Thought leadership — apertura settimana",
        title="L'interfaccia del software aziendale sta per sparire",
        news="Salesforce + Anthropic lanciano Claudeforce (26/8)",
        news_url="https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/",
        hook="Questa settimana Salesforce e Anthropic hanno tolto i pulsanti. Non è una metafora.",
        points=[
            "Con Claudeforce, Slack diventa il posto dove si “parla” al CRM, non dove se ne discutono i risultati: Claude entra come motore di ragionamento dentro Agentforce, mentre Salesforce entra nell'app Claude con competenze di vendita pronte all'uso.",
            "Non è il primo annuncio del genere (Microsoft lo fa con Copilot, Google con Gemini Enterprise), ma è il più esplicito nel dire ad alta voce quello che il mercato fa silenziosamente da un anno: il software smette di essere un'interfaccia da imparare e diventa un collega a cui chiedere.",
            "Per chi lavora nel software enterprise italiano, la domanda non è più “quando arriva l'AI nel nostro gestionale” — è già arrivata, ovunque. La domanda vera è chi, dentro l'azienda, guida quella transizione: se nessuno lo fa, la sceglie il vendor al posto tuo.",
        ],
        cta="Nella tua azienda chi sta decidendo come si useranno questi agenti — il fornitore, l'IT, o nessuno ancora? Raccontacelo nei commenti \U0001F447",
        hashtags="#IntelligenzaArtificiale #EnterpriseAI #DigitalTransformation #B2BTech #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=True,
    ),
    dict(
        badge="Prioritario",
        day="Martedì 1/9",
        format="Mito da sfatare",
        title="Il vibe coding ha reso inutili gli sviluppatori senior?",
        news="Cursor lancia Origin, il 35% delle PR arriva da agenti AI (VentureBeat)",
        news_url="https://venturebeat.com/infrastructure/cursor-launches-origin-code-hosting-platform-as-github-outage-exposes-opening-in-ai-coding-race",
        hook="\U0001F525 Il mito: “Con l'AI chiunque scrive codice, gli sviluppatori senior servono sempre meno.”",
        myth_body=(
            "Questa settimana Cursor ha lanciato Origin, una piattaforma di hosting pensata apposta per team che lavorano con agenti AI. "
            "Il motivo per cui l'hanno costruita è il dato che smentisce il mito: il 35% delle pull request aperte sui repository Cursor arriva da agenti autonomi, non da persone.\n\n"
            "Non significa che il codice si scriva da solo e basta. Significa che si è spostato il collo di bottiglia."
        ),
        points=[
            "Scrivere codice è diventato veloce, quasi gratis. Rivederlo, capirne l'architettura, decidere se è sicuro da mandare in produzione — no.",
            "Più PR arrivano da agenti, più serve qualcuno che sappia leggerle in fretta e giudicarle bene: competenza che non si genera con un prompt.",
            "Le aziende che stanno avendo problemi non sono quelle che usano poco l'AI. Sono quelle che l'hanno lasciata scrivere senza nessuno che governasse cosa succede dopo.",
        ],
        myth_closing="È esattamente lo spazio in cui lavoriamo con il Team Augmentation: il vibe coding abbassa la barriera per prototipare, ma architettura, sicurezza, debito tecnico e passaggio in produzione restano un mestiere per figure senior.",
        cta="La tua azienda ha già qualcuno che fa da filtro tra “agente che propone” e “codice che va in produzione”? \U0001F447",
        hashtags="",
        no_hashtags=True,
        is_myth=True,
        imejis=True,
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 2/9",
        format="Carosello / documento dati (promosso da Riserva)",
        title="Cosa è appena entrato in vigore con l'AI Act (e cosa no)",
        news="EU AI Act, enforcement dal 2 agosto 2026 (Axios, Commissione Europea)",
        news_url="https://www.axios.com/2026/08/28/eu-ai-act-gets-real",
        hook="Il 2 agosto l'AI Act è passato dalla teoria alla pratica. Ecco cosa è successo davvero (e cosa deve ancora arrivare) — in 5 numeri.",
        points=[
            "3 obblighi già attivi dal 2 agosto 2026: trasparenza sui contenuti AI-generated, notifica agli utenti, watermarking.",
            "Le regole più severe per i sistemi “ad alto rischio” arrivano in due tappe: dicembre 2027 e agosto 2028 — non tutto è già in vigore.",
            "L'EU AI Office ha già il potere di richiedere informazioni e accesso ai modelli usati in azienda, anche senza sanzioni specifiche pienamente codificate in questa fase.",
        ],
        cta="La tua azienda ha già mappato dove e come usa l'AI, o aspetta la prossima scadenza per pensarci? Scrivicelo nei commenti \U0001F447",
        hashtags="#AIAct #Compliance #IntelligenzaArtificiale #B2BTech #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=False,
        is_carousel=True,
        carousel_note="Documento/carosello 6 slide, pubblicato su GitHub e allegato come documento su Buffer (vedi sezione Esecuzione).",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 3/9",
        format="Esperienza diretta (template)",
        title="Abbiamo fatto revisionare del codice AI dal nostro team",
        news="Segue narrativamente il post di martedì su vibe coding e PR review (Cursor / VentureBeat)",
        news_url="https://venturebeat.com/infrastructure/cursor-launches-origin-code-hosting-platform-as-github-outage-exposes-opening-in-ai-coding-race",
        hook="Questa settimana abbiamo messo alla prova quello di cui parliamo spesso: cosa succede davvero quando un agente AI apre una pull request nel nostro flusso di lavoro.",
        points=[
            "[DA PERSONALIZZARE] Descrivi il task specifico assegnato all'agente — es. refactoring di un modulo, generazione di test, una piccola feature.",
            "[DA PERSONALIZZARE] Cosa ha funzionato bene senza intervento umano, e cosa invece ha richiesto la revisione di una persona senior (architettura, sicurezza, edge case).",
            "[DA PERSONALIZZARE] La lezione imparata: conferma o smentisce, con la vostra esperienza reale, che il tempo risparmiato in scrittura si sposta quasi integralmente in revisione.",
        ],
        cta="Chi nel tuo team fa da “ultimo controllo” prima che il codice generato da un agente vada in produzione? Raccontaci come vi siete organizzati \U0001F447",
        hashtags="#AIEngineering #TeamAugmentation #SoftwareDevelopment #CodeReview #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=True,
        is_template=True,
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 4/9",
        format="Divulgativo stile Datapizza",
        title="Cos'è il RAG, spiegato con gli avvocati",
        news="Google lancia Gemini Enterprise for Legal (26/8)",
        news_url="https://www.aidapted.ro/en/articles/ai-news-of-the-day-august-26-2026/",
        hook="Questa settimana Google ha lanciato un'AI per gli studi legali che analizza contratti e verifica le citazioni. Dietro c'è una tecnica che sentirai nominare ovunque nel 2026: il RAG. Proviamo a spiegarla senza slide da conferenza.",
        points=[
            "RAG sta per “Retrieval-Augmented Generation”: prima di rispondere, il sistema cerca i documenti giusti (leggi, contratti, giurisprudenza) in una base dati verificata, e SOLO DOPO li usa per costruire la risposta.",
            "Perché serve: un modello linguistico da solo “inventa” quando non sa — con il RAG cita invece la fonte reale, verificabile, invece di un ricordo approssimativo di training. Per un contratto o una citazione legale, è la differenza tra uno strumento utile e uno rischioso.",
            "Non è solo per gli avvocati: fatture, cataloghi prodotto, manuali tecnici, policy interne — qualunque azienda con una base di conoscenza specifica (non generica da internet) può costruirci sopra un assistente affidabile.",
        ],
        cta="Nella tua azienda esiste già una base di conoscenza abbastanza pulita da poter “nutrire” un sistema RAG, o è ancora sparsa tra PDF e cartelle condivise? \U0001F447",
        hashtags="#RAG #IntelligenzaArtificiale #AIExplained #TechForBusiness #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=True,
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati",
        title="96,2 miliardi in un trimestre: cosa ci dicono davvero i numeri di Nvidia",
        news="Risultati Q2 fiscale Nvidia (26/8)",
        news_url="https://intellectia.ai/blog/nvidia-q2-earnings-august-29-2026",
        hook="Nvidia ha chiuso il trimestre con 96,2 miliardi di dollari di fatturato. +106% anno su anno. Ecco cosa ci dicono davvero questi numeri sul mercato AI enterprise.",
        points=[
            "89 miliardi di dollari solo dal segmento data center (+117% anno su anno): è il vero motore della crescita.",
            "+9% il titolo in una singola seduta, circa 440 miliardi di dollari di capitalizzazione aggiunta in un giorno.",
            "+70% la crescita attesa per l'anno fiscale 2028: gli analisti scommettono che la domanda di infrastruttura AI continuerà a salire.",
        ],
        cta="Questi numeri raccontano un mercato ancora agli inizi o una bolla infrastrutturale? Cosa ne pensi \U0001F447",
        hashtags="#Nvidia #AIInfrastructure #TechNews #B2BTech #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=False,
        is_carousel=True,
        carousel_note="Non pubblicato come bozza Buffer questa settimana (idea di riserva) — asset pronti da attivare se serve materiale extra.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura / lista community",
        title="5 cose che questa settimana ci ha ricordato sull'AI enterprise",
        news="Sintesi della settimana (Nvidia, Skan AI, Claudeforce, AI Act, Cursor)",
        news_url="",
        hook="Chiudiamo la settimana con cinque numeri che, messi uno accanto all'altro, dicono più di qualsiasi previsione.",
        points=[
            "96,2 miliardi di dollari: quanto ha fatturato Nvidia in un trimestre grazie alla domanda di infrastruttura AI.",
            "95%: la percentuale di pilot di AI generativa in azienda che, secondo gli investitori dietro Skan AI, falliscono per mancanza di contesto reale sui processi.",
            "35%: la quota di pull request aperte da agenti AI autonomi sulla piattaforma Cursor.",
            "2 agosto 2026: la data in cui l'AI Act è passato dalla teoria alla pratica per le aziende europee.",
            "30.000 miliardi di dollari: il mercato indirizzabile che Anthropic promette ai propri investitori.",
        ],
        closing="I capitali e le promesse crescono più in fretta della capacità reale delle aziende di trasformare tutto questo in valore. È lì che si gioca la partita vera, non nei numeri dei bilanci trimestrali.",
        cta="Qual è, secondo te, il numero della settimana che conta davvero per chi lavora nel software aziendale in Italia? \U0001F447",
        hashtags="#WeeklyRecap #IntelligenzaArtificiale #B2BTech #TechTrends #Digitiamo",
        no_hashtags=False,
        is_myth=False,
        imejis=False,
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(day="Lunedì 31/8", time="08:00", format="Thought leadership", reason="Apre la settimana professionale: finestra 7:30–9:30 cattura il traffico B2B più alto, prima che l'agenda della giornata prenda il sopravvento."),
    dict(day="Martedì 1/9", time="12:30", format="Mito da sfatare", reason="Martedì–giovedì sono i giorni di massimo traffico professionale su LinkedIn; la pausa pranzo favorisce contenuti diretti e polarizzanti che generano discussione."),
    dict(day="Mercoledì 2/9", time="08:00", format="Carosello EU AI Act", reason="Il formato documento richiede tempo di lettura/scroll: la mattina, quando il dwell time è più alto, massimizza le probabilità che l'algoritmo lo spinga oltre la prima ora."),
    dict(day="Giovedì 3/9", time="09:00", format="Esperienza diretta", reason="Giorno di traffico professionale massimo; il formato personale beneficia di una programmazione mattutina per raccogliere commenti e messaggi diretti durante l'intera giornata lavorativa."),
    dict(day="Venerdì 4/9", time="08:30", format="Divulgativo (Datapizza style)", reason="Contenuto educativo “leggero”, ideale per chiudere la settimana: ancora nella finestra mattutina ad alto traffico, senza la pressione competitiva del picco centrale."),
    dict(day="Da programmare", time="—", format="Riserva 1 — Carosello Nvidia", reason="Attivare se c'è margine editoriale extra questa settimana, oppure spostare all'apertura della settimana successiva."),
    dict(day="Da programmare", time="—", format="Riserva 2 — Riflessione chiusura", reason="Buon candidato per un venerdì pomeriggio o un lunedì mattina alternativo, se la settimana corrente satura i 5 slot prioritari."),
]

def esc(s):
    return html.escape(s, quote=False) if isinstance(s, str) else s
