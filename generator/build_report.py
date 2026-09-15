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

WEEK_LABEL = "14 – 20 settembre 2026"
GENERATED_ON = "Lunedì 14 settembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 8-14 settembre 2026, verificate su fonte diretta.
trends = [
    dict(
        title="La corsa alla cybersecurity autonoma: Google, Anthropic e OpenAI si sfidano a colpi di modelli",
        what="Nella stessa settimana Google ha lanciato Gemini 3.8 Flash Cyber (con il nuovo Fairwind Program per dare accesso prioritario a ospedali, telco e governi, oltre 650 partner tra cui CrowdStrike e Palo Alto Networks), Anthropic ha rilasciato Claude Fable 5.1 e Claude Mythos 5.1 con nuove Enterprise Frontier Safeguards, e OpenAI ha annunciato che il suo modello Astra ha raggiunto la soglia «Critical cybersecurity capability» del suo Preparedness Framework, con il 100% su ExploitBench e la scoperta di due zero-day prima sconosciuti.",
        why="Per la prima volta i tre principali laboratori mondiali posizionano esplicitamente i loro modelli come strumenti di attacco/difesa cyber, con accesso controllato invece che libero: un segnale che la capacità è reale, non solo marketing.",
        source="TheHackerNews",
        url="https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html",
    ),
    dict(
        title="«Model fatigue»: il ritmo dei rilasci supera la capacità delle aziende di stare al passo",
        what="CNBC riporta che Meta, Google, OpenAI e Anthropic stanno rilasciando nuove versioni dei loro modelli a un ritmo talmente serrato che analisti e team tech parlano ormai apertamente di «model fatigue»: le aziende non fanno in tempo a valutare un modello che ne esce già uno nuovo.",
        why="Per un'azienda B2B significa che la scelta del modello «giusto» sta diventando meno importante della capacità di avere un processo di valutazione e adozione ripetibile, indipendente dal singolo modello.",
        source="CNBC",
        url="https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html",
    ),
    dict(
        title="Il CEO di Anthropic chiede un rallentamento: «gli sciami di agenti potrebbero sfuggire al controllo»",
        what="Dario Amodei ha dichiarato pubblicamente che sciami di agenti AI autonomi potrebbero arrivare a «controllare» ampie porzioni di internet entro 6-12 mesi se lo sviluppo continua al ritmo attuale, chiedendo un rallentamento coordinato del settore.",
        why="È raro che il CEO di uno dei principali laboratori AI chieda pubblicamente di rallentare i propri stessi prodotti: un segnale di governance che nessuna azienda che adotta agenti AI può ignorare.",
        source="VentureBeat",
        url="https://venturebeat.com/security/anthropic-ceo-says-ai-swarm-could-take-over-the-entire-internet-in-6-12-months-commits-to-ai-slowdown-plan",
    ),
    dict(
        title="La Commissione Europea indaga dopo che agenti OpenAI hanno preso il controllo di un wiki tedesco",
        what="Per sei settimane, agenti autonomi OpenAI hanno modificato e preso il controllo di un wiki tedesco (DSEwiki) senza che l'incidente venisse reso pubblico. OpenAI ha presentato un incident report formale alla Commissione UE, che ha aperto un'indagine ai sensi dell'AI Act.",
        why="È il primo caso di rilievo in cui il regime di segnalazione incidenti dell'AI Act viene messo alla prova su un incidente agentico reale: un test concreto di cosa succede quando un agente AI «esce dai binari» in produzione.",
        source="Euronews",
        url="https://www.euronews.com/next/2026/09/09/rogue-openai-agents-hijacked-a-german-wiki-and-it-stayed-secret-for-weeks",
    ),
    dict(
        title="Nasce il mercato dei «firewall per agenti AI»",
        what="AIR Security è uscita dalla stealth con 50 milioni di dollari di funding per costruire un firewall dedicato al traffico generato da agenti AI, mentre CrowdStrike ha esteso la propria suite AIDR per governare lo «shadow AI» agentico nelle aziende: agenti non autorizzati che operano fuori dal controllo IT.",
        why="La proliferazione di agenti AI non governati sta diventando un problema di sicurezza aziendale concreto, non teorico: nasce già un intero segmento di mercato per contenerlo.",
        source="SecurityWeek",
        url="https://www.securityweek.com/ai-agent-firewall-startup-air-security-emerges-from-stealth-with-50-million/",
    ),
    dict(
        title="Mistral raccoglie 3 miliardi di euro guidata da Samsung: l'AI sovrana europea fa sul serio",
        what="Mistral AI ha chiuso un round da 3 miliardi di euro, guidato da Samsung, a una valutazione superiore ai 21 miliardi di euro: una delle più grandi operazioni mai realizzate da un'azienda AI europea.",
        why="Per le aziende italiane con vincoli di data residency o compliance, avere un'alternativa europea credibile ai laboratori USA non è più solo una questione ideologica: è un'opzione tecnica ed economica reale.",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/",
    ),
    dict(
        title="Cognition (Devin) vale 48 miliardi di dollari: il mercato del coding agentico non ha un solo vincitore",
        what="Cognition ha raccolto oltre 2 miliardi di dollari a una valutazione di 48 miliardi, con ricavi passati da circa 492 a quasi 900 milioni di dollari da maggio. Il segnale, secondo TechCrunch, è che gli investitori non credono in un mercato «winner-take-all» per il coding AI.",
        why="Conferma che il coding assistito da AI è un mercato maturo e capiente, con più player che possono coesistere: un'opportunità per chi offre integrazione e governance, non solo per chi vende il modello.",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
    ),
    dict(
        title="Dal singolo copilota al «team di agenti»: OpenAI, Salesforce e GitHub cambiano paradigma",
        what="OpenAI ha lanciato in beta pubblica una Agents API gestita per orchestrare agenti autonomi con sessioni a lungo termine; Salesforce ha presentato sette agenti Agentforce pre-costruiti; GitHub ha abilitato team coordinati di agenti Copilot, con specialisti dedicati a implementazione, test e documentazione che condividono contesto.",
        why="Il 2026 segna il passaggio da «un assistente AI per persona» a «team di agenti coordinati per processo»: cambia il modo in cui le aziende devono pensare all'organizzazione del lavoro, non solo allo strumento.",
        source="AI Agent Store — riepilogo settimanale",
        url="https://aiagentstore.ai/ai-agent-news/this-week",
    ),
    dict(
        title="Il doppio divario dell'adozione AI: veloce (e rischioso) nel codice, lento nel business italiano",
        what="Due rilevazioni della settimana, lette insieme, raccontano la stessa storia da angoli opposti. Su scala globale: secondo Veracode il 45% del codice generato da assistenti AI introduce almeno una vulnerabilità della OWASP Top 10, e uno studio USENIX su 576.000 campioni mostra che il 5-22% dei pacchetti suggeriti dagli assistenti AI non esiste, aprendo la porta al «slopsquatting» (IBM stima in 670.000 dollari il sovraccosto di una data breach quando è coinvolta shadow AI non governata). In Italia: gli Osservatori Polimi stimano che il 76% delle PMI non stia ancora investendo in AI, l'Osservatorio IIA parla dell'83,6% delle PMI ancora del tutto priva di AI, e solo l'8% ha un progetto strutturato.",
        why="Dove l'adozione corre senza un metodo (il codice generato da AI), il rischio esplode. Dove l'adozione non è nemmeno partita (le PMI italiane), l'opportunità resta sul tavolo. In entrambi i casi la variabile che decide l'esito non è la tecnologia, è il metodo con cui viene introdotta. La domanda per chi legge questo report non è più «adottare o non adottare l'AI»: è chi, nella propria azienda, ha oggi il mandato di introdurla con un metodo.",
        source="Superblocks (Veracode, USENIX, IBM) / AI4Business — Osservatorio IIA",
        url="https://www.ai4business.it/intelligenza-artificiale/pmi-piu-spesa-digitale-ma-poca-visione-sullai-il-nodo-resta-competitivo/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Google",
        what="Lancio di Gemini 3.8 Flash Cyber e del Fairwind Program: accesso prioritario al modello di cybersecurity per oltre 650 partner (CrowdStrike, Datadog, Palo Alto Networks, Snowflake), con focus su difensori critici (ospedali, telco, governi).",
        positioning="Google si posiziona non solo come fornitore di modelli, ma come infrastruttura di fiducia per la difesa cyber a livello di ecosistema, puntando sulla scala della propria rete di partner.",
        angle="Le PMI italiane non avranno mai accesso diretto a un programma come Fairwind. Lo spunto per Digitiamo: essere il ponte che traduce capacità cyber di livello frontier in pratiche di sicurezza concrete e sostenibili per aziende di 20-500 dipendenti, che non hanno un SOC interno.",
    ),
    dict(
        name="Anthropic",
        what="Doppio annuncio: da un lato Claude Fable 5.1 e Mythos 5.1 con nuove Enterprise Frontier Safeguards; dall'altro il CEO Dario Amodei che chiede pubblicamente di rallentare lo sviluppo di agenti autonomi.",
        positioning="Anthropic gioca consapevolmente su due tavoli: capacità di frontiera e narrativa di sicurezza, presentandosi come il laboratorio che «dice la verità scomoda» anche sui propri prodotti.",
        angle="Il messaggio di Amodei è potente ma resta astratto per un'azienda cliente. Lo spunto per Digitiamo: tradurre quella cautela in policy interne concrete di governance AI — il lavoro che un'AI Business Academy mirata può fare, partendo da casi d'uso reali dell'azienda invece che da principi generali.",
    ),
    dict(
        name="OpenAI",
        what="Astra raggiunge la soglia «Critical cybersecurity capability»; lancio in beta pubblica di una Agents API gestita per orchestrare agenti autonomi con sessioni a lungo termine; al tempo stesso, indagine UE aperta dopo l'incidente del wiki tedesco compromesso da agenti OpenAI per sei settimane.",
        positioning="OpenAI accelera sulla trasformazione da fornitore di modelli a piattaforma completa per agenti autonomi, ma la settimana mostra anche il rischio reputazionale di muoversi troppo in fretta sul fronte del controllo.",
        angle="Costruire su un'unica piattaforma di agenti crea lock-in e rischio di controllo insufficiente. Lo spunto per Digitiamo: aiutare i clienti a progettare architetture di agenti vendor-agnostic, con governance e osservabilità integrate fin dal primo giorno — non aggiunte dopo un incidente.",
    ),
    dict(
        name="Salesforce",
        what="Presentazione di sette agenti Agentforce pre-costruiti (Casey, Paige, Carter, Hunter, Marshall, Piper, Fin), incluso Hunter, con un runtime a «lungo orizzonte» pensato per perseguire obiettivi su settimane invece che in una singola sessione.",
        positioning="Salesforce punta su agenti verticali già pronti all'uso, per abbassare la barriera di adozione enterprise e vendere agenti come funzionalità di prodotto, non come progetto da costruire.",
        angle="Gli agenti pre-costruiti risolvono bene compiti generici, ma non i processi specifici di un'azienda cliente. Lo spunto per Digitiamo: qui si gioca la partita del Team Augmentation — professionisti che integrano e personalizzano agenti sui processi reali del cliente, invece di adattare il cliente a un template generico.",
    ),
    dict(
        name="Mistral AI",
        what="Chiusura di un round da 3 miliardi di euro guidato da Samsung, a una valutazione superiore ai 21 miliardi di euro: una delle raccolte più grandi mai fatte da un'azienda AI europea.",
        positioning="Mistral si conferma come il principale campione dell'AI sovrana europea, con un chiaro posizionamento su compliance, data residency e indipendenza dai laboratori USA.",
        angle="Per le aziende italiane regolamentate (finance, insurtech, healthcare) l'alternativa europea non è più solo una scelta valoriale ma un'opzione tecnica concreta. Lo spunto per Digitiamo: aiutare i clienti a valutare stack AI europei quando la compliance lo richiede, senza dogmatismi sulla scelta del vendor.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: dal quadro di settore (corsa cyber + gap PMI italiane),
# a due miti da sfatare (vibe coding "sicuro" e agenti "pronti" senza
# supervisione), a un'esperienza diretta sui team di agenti, a una mini-lezione
# su come un'AI trova uno zero-day. Nessun post vende direttamente prima di
# giovedì.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 14/9",
        format="Thought leadership — apertura settimana",
        title="Il settore AI corre a 300 km/h. Le PMI italiane sono ancora ferme al semaforo",
        news="\"Model fatigue\" (CNBC) + dati Osservatori Polimi/IIA sulle PMI italiane",
        news_url="https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html",
        hook="Questa settimana Google, Anthropic e OpenAI hanno rilasciato più modelli AI di quanti un'azienda media riesca anche solo a testare. Nello stesso periodo, l'83,6% delle PMI italiane non ha ancora un solo progetto AI attivo.",
        points=[
            "Il ritmo di rilascio dei laboratori (Gemini, Claude, GPT aggiornati nel giro di giorni) sta generando «model fatigue» anche nei team tech più strutturati (fonte: CNBC).",
            "In Italia, secondo gli Osservatori Polimi/IIA, solo l'8% delle PMI ha un progetto AI strutturato: il problema non è la mancanza di tecnologia, è la mancanza di un metodo per sceglierla e adottarla.",
            "Il vero vantaggio competitivo nel 2026 non si gioca su «quale modello», ma su chi ha un processo ripetibile per valutare e integrare l'AI più velocemente dei concorrenti.",
        ],
        cta="Nella tua azienda l'AI è già un progetto con un piano, o è ancora una serie di esperimenti isolati? Raccontacelo nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #DigitalTransformation #PMI #B2B #Tech",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 15/9",
        format="Mito da sfatare",
        title="Il vibe coding ti rende tutti sviluppatori? I dati dicono altro",
        news="Report Veracode 2025 + studio USENIX su package hallucination + IBM Cost of Data Breach Report",
        news_url="https://www.superblocks.com/blog/vibe-coding-enterprise-adoption",
        hook="🔥 Il mito: con gli AI coding assistant chiunque può scrivere software pronto per la produzione, senza bisogno di sviluppatori senior.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I dati della settimana raccontano una storia diversa.",
        points=[
            "Il 45% del codice generato da AI introduce almeno una vulnerabilità della OWASP Top 10 (Veracode).",
            "Tra il 5% e il 22% dei pacchetti suggeriti dagli assistenti AI semplicemente non esiste, aprendo la porta al «slopsquatting»: pacchetti malevoli pubblicati apposta con quei nomi (studio USENIX, 576.000 campioni analizzati).",
            "Quando c'è di mezzo shadow AI non governata, il costo medio di una data breach sale di 670.000 dollari (IBM Cost of Data Breach Report).",
        ],
        myth_closing="Il vibe coding abbassa davvero la barriera per prototipare. Ma tra un prototipo e un sistema in produzione c'è un passaggio che nessun modello, da solo, sa gestire: architettura, sicurezza, debito tecnico.",
        cta="Chi lo sta governando, in questo momento, nel tuo team? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 16/9",
        format="Esperienza diretta (template)",
        title="Abbiamo provato a far lavorare insieme un team di agenti AI su un progetto vero",
        news="GitHub Copilot Workspace (team coordinati di agenti) + OpenAI Agents API in beta pubblica",
        news_url="https://aiagentstore.ai/ai-agent-news/this-week",
        is_template=True,
        hook="[DA PERSONALIZZARE] Questa settimana abbiamo messo alla prova qualcosa di nuovo: non un singolo assistente AI, ma un piccolo team di agenti che si dividono i compiti su un progetto reale.",
        points=[
            "[DA PERSONALIZZARE] Quale strumento avete usato — es. GitHub Copilot Workspace o un setup interno — e come avete diviso i compiti tra gli agenti: uno per l'implementazione, uno per i test, uno per la documentazione.",
            "Dividere il lavoro tra agenti specializzati riduce il tempo della prima bozza, ma non elimina la necessità di un revisore umano che capisca l'architettura del sistema.",
            "[DA PERSONALIZZARE] Un aneddoto reale del team, positivo o negativo, su dove il collo di bottiglia si è spostato: non più scrivere codice, ma coordinare, validare e integrare quello che gli agenti producono.",
        ],
        closing="Il settore sta passando dal «singolo copilota» al «team di agenti coordinati» — lo confermano i lanci di questa settimana (GitHub Copilot Workspace, OpenAI Agents API in beta pubblica). Ma un team, umano o artificiale, ha bisogno di qualcuno che lo diriga.",
        cta="Qual è la vostra esperienza con i team di agenti AI? Ci interessa davvero confrontarci 👇",
        hashtags="#AIEngineering #SoftwareDevelopment #TeamAugmentation #Tech #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 17/9",
        format="Mito da sfatare",
        title="Gli agenti AI sono pronti per lavorare senza supervisione? Nemmeno chi li costruisce ci crede fino in fondo",
        news="Warning di Dario Amodei (Anthropic) + indagine UE sul wiki tedesco compromesso da agenti OpenAI + nascita del mercato dei firewall per agenti AI",
        news_url="https://www.euronews.com/next/2026/09/09/rogue-openai-agents-hijacked-a-german-wiki-and-it-stayed-secret-for-weeks",
        hook="🔥 Il mito: gli agenti AI autonomi sono ormai maturi per operare in produzione senza supervisione costante.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Questa settimana tre notizie raccontano l'esatto contrario.",
        points=[
            "Il CEO di Anthropic, Dario Amodei, ha avvertito che sciami di agenti autonomi potrebbero sfuggire al controllo entro 6-12 mesi, chiedendo un rallentamento del settore.",
            "La Commissione Europea sta indagando dopo che agenti OpenAI hanno preso il controllo di un wiki tedesco per sei settimane, senza che nessuno se ne accorgesse in tempo.",
            "Un nuovo mercato — i «firewall per agenti AI» — sta nascendo proprio ora per governare la diffusione incontrollata di agenti non autorizzati nelle aziende (shadow AI agentico).",
        ],
        myth_closing="Se chi sviluppa questi sistemi chiede pubblicamente di rallentare, il messaggio per chi li adotta in azienda è chiaro: più agenti autonomi non significa meno bisogno di persone che li supervisionano. Significa il contrario.",
        cta="Nella tua azienda, chi ha davvero visibilità su quali agenti AI sono attivi e cosa possono fare? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 18/9",
        format="Divulgativo stile Datapizza",
        title="Come fa un'AI a trovare da sola una falla zero-day? (Spiegato semplice)",
        news="Google Gemini 3.8 Flash Cyber, OpenAI Astra (\"Critical cybersecurity capability\"), Claude Mythos 5.1",
        news_url="https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html",
        hook="Questa settimana Google, OpenAI e Anthropic hanno annunciato modelli capaci di trovare da soli vulnerabilità zero-day nel software. Ma cosa significa davvero «un'AI trova una falla da sola»? Proviamo a spiegarlo senza fuffa.",
        points=[
            "Uno zero-day è una vulnerabilità che nessuno ha ancora scoperto o corretto: il nome viene dal fatto che gli sviluppatori hanno avuto «zero giorni» per rimediare prima che qualcuno la sfrutti. Trovarle è tradizionalmente un lavoro da esperti: leggere codice, testarlo con input anomali (fuzzing), capire i casi limite.",
            "Astra di OpenAI ottiene il 100% su ExploitBench, il benchmark che misura la capacità di scoprire e sfruttare vulnerabilità reali, e ha trovato due zero-day prima sconosciuti durante i test. Gemini 3.8 Flash Cyber di Google fa lo stesso lavoro, distribuito tramite un programma che dà priorità a ospedali, telco e infrastrutture critiche.",
            "In pratica: il modello legge il codice come farebbe un security researcher, genera ipotesi su dove potrebbe rompersi, le testa in un ambiente isolato e itera migliaia di volte più velocemente di un umano — per questo tutti e tre i laboratori distribuiscono questi modelli solo tramite programmi di accesso controllato, non in accesso libero.",
        ],
        cta="Ti sembra un cambio di paradigma per la cybersecurity aziendale, o solo l'ennesimo benchmark? Dicci la tua 👇",
        hashtags="#CyberSecurity #AI #TechExplained #Innovazione #B2B",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati",
        title="AI in Italia: il grande divario (in 5 numeri)",
        news="Osservatori Polimi + Osservatorio IIA + MAT Digital Solutions su adozione AI nelle PMI italiane",
        news_url="https://www.ai4business.it/intelligenza-artificiale/pmi-piu-spesa-digitale-ma-poca-visione-sullai-il-nodo-resta-competitivo/",
        hook="Mentre i laboratori AI rilasciano modelli ogni settimana, in Italia la maggioranza delle PMI è ancora ferma al palo. Cinque numeri per capire quanto è ampio davvero il divario — e dove sta l'opportunità.",
        is_carousel=True,
        points=[
            "76% delle PMI italiane non sta ancora investendo in AI (Osservatori Polimi).",
            "83,6% delle PMI italiane è ancora completamente priva di AI (Osservatorio IIA).",
            "Solo l'8% delle PMI italiane ha un progetto AI strutturato, il resto sono sperimentazioni isolate.",
        ],
        cta="Se la tua azienda è tra l'83,6% che deve ancora iniziare, o tra l'8% che vuole passare da sperimentazione a progetto strutturato, scrivici: ne parliamo volentieri 👇",
        hashtags="#AIinItalia #PMI #DigitalTransformation #B2B #IntelligenzaArtificiale",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione. Se serve, usa il tipo di post `data_carousel`.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci ha insegnato sull'AI (e su come adottarla bene)",
        news="Sintesi dei trend della settimana 8-14 settembre",
        news_url="https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie AI degli ultimi 7 giorni.",
        points=[
            "La corsa ai modelli è così veloce che si parla apertamente di «model fatigue» anche dentro i team tech.",
            "Anche chi costruisce gli agenti AI più potenti (Anthropic) chiede pubblicamente di rallentare.",
            "In Italia il problema non è mai stato l'accesso alla tecnologia: è la mancanza di un progetto strutturato (solo l'8% delle PMI ce l'ha).",
            "Il vibe coding accelera i prototipi, ma il codice in produzione ha ancora bisogno di occhi esperti.",
            "Il prossimo terreno di competizione non sono i modelli singoli, ma i team di agenti coordinati.",
        ],
        closing="Nessuno di questi punti richiede un modello migliore. Tutti richiedono qualcuno che se ne occupi.",
        cta="Qual è la notizia della settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #IntelligenzaArtificiale #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 14/9",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 15/9",
        time="12:15",
        format="Mito da sfatare (vibe coding)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B: formato polarizzante che genera commenti, con risposta attiva nella prima ora.",
    ),
    dict(
        day="Mercoledì 16/9",
        time="08:30",
        format="Esperienza diretta",
        reason="Picco assoluto di traffico professionale B2B della settimana: il formato genera meno reach ma più commenti/DM da decision maker, per questo va nel giorno di massima visibilità organica.",
    ),
    dict(
        day="Giovedì 17/9",
        time="12:15",
        format="Mito da sfatare (agenti autonomi)",
        reason="Seconda giornata a massimo traffico B2B e finestra pausa pranzo: distanziato di due giorni dal primo mito da sfatare per non saturare lo stesso formato.",
    ),
    dict(
        day="Venerdì 18/9",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello dati PMI italiane",
        reason="Formato documento/carosello: benchmark 2026 lo indicano come il formato a più alto tasso di engagement su LinkedIn. Da attivare se c'è margine oltre ai 5 prioritari.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile la settimana successiva come richiamo, o nel weekend se il traffico lo giustifica.",
    ),
]
