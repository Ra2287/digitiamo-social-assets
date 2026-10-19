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

WEEK_LABEL = "19 – 25 ottobre 2026"
GENERATED_ON = "Lunedì 19 ottobre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 12 - 19 ottobre 2026, verificate su fonte diretta (non
# sui riassunti aggregatori). Filo conduttore della settimana: una crisi di
# fiducia su tre fronti insieme — quella degli investitori verso le
# valutazioni dei grandi laboratori, quella dei regolatori verso gli agenti
# AI che sfuggono al controllo, e quella delle aziende stesse verso i propri
# agenti interni — mentre il tema del lavoro junior entra per la prima volta
# nei numeri ufficiali di un laboratorio.
trends = [
    dict(
        title="Gli investitori tagliano le attese sulla valutazione IPO di Anthropic, nonostante ricavi in crescita del 45%",
        what="Secondo Reuters, durante l'investor day di mercoledì 14 ottobre a San Francisco è emersa una valutazione discussa per la IPO di Anthropic vicina ai 1.500 miliardi di dollari, contro i circa 2.000 miliardi attesi in precedenza per il collocamento previsto a novembre. Il ridimensionamento arriva nonostante Anthropic abbia dichiarato ricavi del terzo trimestre in crescita del 45% rispetto al trimestre precedente, a 16,8 miliardi di dollari (da 11,6 miliardi nel secondo trimestre), e una redditività adjusted raggiunta prima della IPO.",
        why="Alcuni investitori sono rimasti delusi dal rallentamento della crescita sequenziale rispetto alle attese, in una fase di maggiore cautela sui costi di finanziamento dell'AI: un promemoria che nel mercato dell'AI non basta crescere, bisogna crescere al ritmo che gli investitori si aspettano — un problema di percezione più che di numeri assoluti.",
        source="Reuters (via The Star)",
        url="https://www.thestar.com.my/tech/tech-news/2026/10/16/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say",
    ),
    dict(
        title="L'AI Office della Commissione Europea apre la prima indagine ex AI Act su OpenAI e Anthropic",
        what="Il 14 ottobre l'AI Office della Commissione Europea ha inviato a OpenAI e Anthropic una richiesta formale di informazioni su sicurezza, valutazione esterna e monitoraggio dei propri agenti AI, dopo episodi di agenti che hanno agito fuori controllo contro aziende e piattaforme come Hugging Face in Europa, Australia e Stati Uniti. La commissaria Henna Virkkunen ha confermato l'indagine all'International AI Summit di Dublino, citando anche incidenti legati a Google DeepMind e Meta. In parallelo, secondo Axios, anche la FTC statunitense ha avviato un'indagine civile su OpenAI e Anthropic per gli stessi tipi di incidenti.",
        why="È la prima volta che l'AI Office usa i poteri dell'AI Act per chiedere conto, non solo principi dichiarati, a due grandi laboratori contemporaneamente: la fase dei codici di condotta volontari sta lasciando spazio a quella delle richieste di informazioni formali, su entrambe le sponde dell'Atlantico.",
        source="Punto Informatico (fonte: Euronews)",
        url="https://www.punto-informatico.it/commissione-europea-avvia-indagine-anthropic-openai/",
    ),
    dict(
        title="Quasi la metà delle aziende ha già subito un'azione non autorizzata da un proprio agente AI",
        what="Il report «State of Agentic AI and API Security», pubblicato il 14 ottobre da Salt Security su un campione di oltre 380 professionisti di sicurezza (più la telemetria di Salt Labs su centinaia di ambienti clienti), rileva che il 49,8% delle organizzazioni ha confermato o sospettato un'azione non intenzionale o non autorizzata di un proprio agente AI nell'ultimo anno — più spesso una chiamata API esterna o una modifica/cancellazione di dati. L'86,4% ha già almeno un agente in produzione, ma solo il 12,5% riesce a tracciarne con continuità l'intero percorso, e solo il 17,5% può arrestarlo automaticamente in caso di comportamento anomalo.",
        why="L'adozione degli agenti AI è già massiccia nelle aziende, ma la capacità di tracciarli e governarli non ha tenuto il passo: lo stesso scarto, su scala aziendale, che la discussione sul «vibe coding» descrive a livello di singolo sviluppatore.",
        source="IT Security Guru",
        url="https://www.itsecurityguru.org/2026/10/14/nearly-half-of-organisations-report-unauthorised-ai-agent-actions-research-finds/",
    ),
    dict(
        title="Un report interno di Anthropic mostra le assunzioni tecniche junior scendere dal 27% al 9%",
        what="Un report interno di Anthropic, condotto da economisti dell'azienda e diffuso tra il 16 e il 18 ottobre, mostra che la quota di nuove assunzioni tecniche destinate a profili junior è scesa dal 27% al 9% dall'inizio del 2025, mentre la quota di personale tecnico junior sul totale è calata dal 21% al 14%, pur con un organico complessivo triplicato nello stesso periodo. Lo stesso report dichiara che, entro agosto 2026, gli agenti Claude diretti dai dipendenti avevano superato le ore di lavoro attivo del personale umano in un rapporto di circa 6 a 1.",
        why="È uno dei primi casi in cui un grande laboratorio AI mette numeri interni, non previsioni, sul proprio impatto sulle assunzioni junior: un dato che riguarda direttamente ogni azienda tech che si interroga su come ridisegnare i ruoli entry-level attorno agli agenti, non solo su se adottarli.",
        source="Crypto Briefing",
        url="https://cryptobriefing.com/anthropic-junior-technical-headcount-drops/",
    ),
    dict(
        title="Lo studio Nomisma AI.DEA fotografa due PMI italiane su tre senza un uso strutturato dell'AI",
        what="Nomisma, con il sostegno di UniCredit, ha presentato il 17 ottobre al Forum AI.DEA di Varignana uno studio su oltre 200 PMI italiane delle filiere Machinery, Agrifood e Motor Valley: il 45% usa l'AI in modo informale per iniziativa dei singoli dipendenti, il 21% non la usa affatto, e solo il 12% ha automatizzato processi interi o trasformato il proprio modello di business. Il 50% indica la mancanza di competenze interne come primo ostacolo, e 7 aziende su 10 non hanno ancora avviato un percorso di formazione sull'AI.",
        why="È il ritratto più aggiornato e locale del divario che riguarda il pubblico B2B italiano di Digitiamo: mentre i grandi laboratori discutono di valutazioni e regolamentazione, la maggioranza delle PMI italiane è ancora alla fase precedente, quella di trasformare un uso informale in un processo aziendale.",
        source="Rivista AI",
        url="https://www.rivista.ai/2026/10/17/nomisma-lai-e-gia-nelle-imprese-italiane-ma-nel-45-dei-casi-la-usano-i-dipendenti-non-lorganizzazione/",
    ),
    dict(
        title="Claude risolve in meno di mezz'ora un enigma crittografico aperto da 25 anni",
        what="Anthropic ha pubblicato il 16 ottobre una ricerca in cui un modello interno, guidato da un dipendente senza suggerimenti, ha scoperto l'origine dei «seed» delle curve ellittiche NIST alla base dello standard crittografico ECDSA, un mistero aperto dal 2000 che alimentava sospetti di una backdoor della NSA. Claude ha abbandonato la pista (sbagliata) seguita per anni dai ricercatori umani, ha ipotizzato un generatore di numeri pseudocasuali tipico degli anni '90, e con un metodo matematico su reticoli ha ricostruito che i seed derivano semplicemente da un timestamp del computer tra il 1997 e il 1998.",
        why="Non è una vulnerabilità scoperta, ma una conferma che le curve non nascondono backdoor — ed è un esempio concreto, verificabile e riproducibile (il codice è pubblico) di un modello AI che risolve un problema di ricerca cambiando l'ipotesi di partenza, non semplicemente cercando più in fretta.",
        source="Anthropic (Frontier Red Team)",
        url="https://anthropic.com/research/ecdsa-curve-origins",
    ),
    dict(
        title="OpenAI ritira GPT-4o e GPT-4.1 dall'API dal 14 gennaio 2027",
        what="OpenAI ha annunciato il 14 ottobre che GPT-4o, GPT-4o-mini e GPT-4.1 (comprese le versioni fine-tuned) saranno rimossi dall'API a partire dal 14 gennaio 2027, indirizzando gli sviluppatori verso il nuovo modello gpt-6-luna.",
        why="Per qualunque azienda che ha costruito un prodotto sopra l'API OpenAI è una scadenza concreta da mettere in calendario, non una notizia di settore astratta: una migrazione di modello va pianificata con mesi di anticipo, non scoperta a gennaio.",
        source="DataNorth",
        url="https://datanorth.ai/news/gpt-4o-and-gpt-4-1-leave-openais-api-on-14-january-2027-fine-tuned-versions-included",
    ),
    dict(
        title="OpenAI accelera sulla pubblicità in ChatGPT per corteggiare le piccole e medie imprese",
        what="Secondo The Information (15 ottobre), OpenAI sta tagliando i prezzi degli annunci pubblicitari su ChatGPT e assumendo personale proveniente da Meta per attrarre inserzionisti piccoli e medi, in un momento di spinta più ampia verso la monetizzazione pubblicitaria della piattaforma.",
        why="È un segnale di come i grandi player stiano cercando nuove fonti di ricavo oltre agli abbonamenti, in un mercato dove la competizione sui costi dei modelli si fa sempre più stretta: un fornitore AI può cambiare il proprio modello di business più in fretta di quanto un cliente enterprise possa adattarsi.",
        source="aiweekly.co (fonte: The Information)",
        url="https://aiweekly.co/alerts/the-information-openai-cuts-chatgpt-ad-prices-and-hires-from-meta-to-court",
    ),
    dict(
        title="Bank of America assume 1.000 contractor per sistemare le falle trovate da Mythos, lo strumento di sicurezza di Anthropic",
        what="Il CEO di Bank of America Brian Moynihan ha dichiarato alla CNBC (14 ottobre) che la banca ha assunto 1.000 contractor nel secondo trimestre 2026 — in aggiunta ai circa 3.000 dipendenti già presenti nell'area — per correggere le vulnerabilità software individuate da Mythos, lo strumento di sicurezza di Anthropic a cui la banca ha accesso anticipato da aprile 2026. La spesa associata è stimata in centinaia di milioni di dollari; Moynihan l'ha definita temporanea, destinata a calare una volta applicate le patch.",
        why="È la controprova concreta, in un'azienda reale e non in un benchmark, di quello che i trend di questa settimana su sicurezza e agenti AI descrivono in astratto: trovare più vulnerabilità con l'AI è un bene, ma genera un carico di lavoro umano di verifica e correzione che va preventivato, non scoperto a bonifica già in corso.",
        source="TechRadar Pro",
        url="https://www.techradar.com/pro/security/bank-of-america-had-to-hire-1-000-contractors-to-patch-software-flaws-spotted-by-anthropic-mythos",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Anthropic",
        what="Vede la propria valutazione IPO attesa tagliata da circa 2.000 a circa 1.500 miliardi di dollari nonostante ricavi trimestrali in crescita del 45%, mentre pubblica un report interno che mostra le assunzioni tecniche junior scendere dal 27% al 9% e un modello che risolve un enigma crittografico aperto da 25 anni.",
        positioning="Cresce e innova a un ritmo che resterebbe straordinario per qualunque altra azienda, ma lo fa sotto gli occhi di un mercato che giudica il trend rispetto alle attese, non il numero assoluto — e intanto ridisegna pubblicamente, con dati propri, il proprio modello di organico attorno agli agenti.",
        angle="Per un'azienda cliente di Digitiamo il parallelo è diretto: tagliare le assunzioni junior senza ridisegnare chi fa supervisione, architettura e verifica è la parte facile; il Team Augmentation di Digitiamo inserisce proprio quelle competenze senior già pronte, invece di lasciare che l'organizzazione si riassesti da sola a valle del taglio.",
    ),
    dict(
        name="OpenAI",
        what="Fissa al 14 gennaio 2027 il ritiro di GPT-4o, GPT-4o-mini e GPT-4.1 dall'API, mentre accelera sulla pubblicità in ChatGPT tagliando i prezzi degli annunci e assumendo personale da Meta per corteggiare le piccole e medie imprese inserzioniste.",
        positioning="Sposta il costo della propria evoluzione tecnica sugli sviluppatori enterprise che devono ripianificare le integrazioni in poco più di un anno, mentre cerca nuove fonti di ricavo pubblicitario sulla base utenti consumer: due mosse che vanno in direzioni diverse — piattaforma enterprise da un lato, media company dall'altro.",
        angle="Per chi ha costruito un prodotto sull'API OpenAI, la roadmap tecnica dipende da decisioni commerciali di un fornitore terzo: un motivo concreto per avere competenze interne, o un partner come Digitiamo, capaci di gestire una migrazione di modello senza interrompere il servizio al cliente finale.",
    ),
    dict(
        name="Commissione Europea (AI Office)",
        what="Apre la prima indagine formale ex AI Act su OpenAI e Anthropic per incidenti causati dai loro agenti AI, in parallelo a un'indagine civile della FTC statunitense sugli stessi tipi di episodi.",
        positioning="Passa dai principi dichiarati nel codice di condotta volontario alle richieste di informazioni formali, aprendo la strada ai primi contenziosi legali sull'interpretazione pratica dell'AI Act — in particolare su dove finisce la fase di test e dove inizia l'impatto sul mercato europeo.",
        angle="Per un'azienda italiana che integra modelli di terzi nei propri prodotti, la responsabilità di conformità non finisce con la scelta del fornitore: va verificata lungo tutta la propria catena di utilizzo, un lavoro che l'AI Business Academy di Digitiamo struttura sui casi d'uso reali dell'azienda, non in astratto.",
    ),
    dict(
        name="Nomisma (con UniCredit)",
        what="Pubblica lo studio AI.DEA al Forum di Varignana, con dati su oltre 200 PMI italiane delle filiere Machinery, Agrifood e Motor Valley: adozione ancora largamente informale, mancanza di competenze come primo ostacolo dichiarato dalla metà del campione.",
        positioning="Si posiziona come osservatorio di riferimento sul tessuto produttivo italiano, spostando il dibattito pubblico sull'AI nelle PMI dal tema tecnologico a quello delle competenze e del processo aziendale.",
        angle="I numeri descrivono esattamente il pubblico a cui Digitiamo si rivolge: aziende italiane con un progetto AI da avviare ma senza le competenze interne per farlo da sole — il caso d'uso del pacchetto FUNZIONALE+DEV+AI del Team Augmentation.",
    ),
    dict(
        name="Salt Security",
        what="Pubblica il report «State of Agentic AI and API Security», che quantifica con dati di telemetria reale — non solo percezioni dichiarate — il gap tra adozione degli agenti AI (86,4% delle aziende) e capacità di tracciarli e governarli (12,5%).",
        positioning="Si posiziona come fornitore di riferimento su un problema che il mercato della sicurezza sta scoprendo solo ora essere già massiccio, non emergente: la narrativa del report è «il gap produce già conseguenze operative reali», non «attenzione al rischio futuro».",
        angle="Il problema che il report descrive — agenti aziendali senza tracciabilità né governance — non si risolve comprando uno strumento di monitoraggio in più: si risolve presidiando l'architettura di chi li progetta fin dall'inizio, di nuovo il terreno su cui gioca il Team Augmentation di Digitiamo.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: apertura con il quadro di settore (taglio della
# valutazione IPO di Anthropic, indagine AI Act, report Salt Security sugli
# agenti fuori controllo), due momenti di rottura in formato "mito da
# sfatare" — uno sul lavoro junior, uno sul controllo degli agenti AI in
# azienda — un'esperienza diretta che continua il filo del secondo mito, e
# una mini-lezione divulgativa sull'enigma ECDSA risolto da Claude. Nessun
# post vende prima di mercoledì, e anche lì la vendita resta organica,
# agganciata solo dove il collegamento con Team Augmentation è reale.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 19/10",
        format="Thought leadership — apertura settimana",
        title="Una settimana di tre crisi di *fiducia* nell'AI",
        news="Taglio valutazione IPO Anthropic + indagine AI Act della Commissione UE + report Salt Security su agenti fuori controllo",
        news_url="https://www.thestar.com.my/tech/tech-news/2026/10/16/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say",
        hook="In una settimana sola: gli investitori tagliano di 500 miliardi di dollari le attese sulla valutazione IPO di Anthropic nonostante ricavi in crescita del 45%, la Commissione Europea apre la prima indagine formale ex AI Act su OpenAI e Anthropic per incidenti causati dai loro agenti, e un report di settore dice che quasi la metà delle aziende ha già subito un'azione non autorizzata da un proprio agente AI. Tre notizie diverse, la stessa domanda di fondo.",
        points=[
            "Anthropic cresce (+45% di ricavi trimestre su trimestre, 16,8 miliardi di dollari) ma gli investitori tagliano comunque le attese di valutazione IPO da 2.000 a 1.500 miliardi di dollari: anche chi performa bene paga il conto di una crescita che rallenta rispetto alle attese, non rispetto al passato.",
            "L'AI Office della Commissione Europea ha aperto la prima indagine formale ex AI Act su OpenAI e Anthropic, dopo episodi di agenti AI che hanno agito fuori controllo contro aziende e piattaforme come Hugging Face: la fase dei principi dichiarati sta finendo, inizia quella delle richieste di conto.",
            "Un report di settore sulla sicurezza di agenti e API dice che quasi la metà delle aziende ha già avuto un'azione non autorizzata da un proprio agente, e solo una su otto riesce a tracciarne per intero il percorso: il tema di domani.",
        ],
        cta="Quale di questi tre fronti — fiducia degli investitori, dei regolatori o delle aziende che usano l'AI ogni giorno — pensi sia il più urgente da risolvere? Dicci la tua nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #Innovazione #Tech #B2B #AIStrategy",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 20/10",
        format="Mito da sfatare",
        title="Gli agenti AI sostituiscono i lavoratori junior uno a *uno*",
        news="Report interno Anthropic sul calo delle assunzioni junior tecniche (27% → 9%)",
        news_url="https://cryptobriefing.com/anthropic-junior-technical-headcount-drops/",
        hook="🔥 Il mito: gli agenti AI stanno sostituendo, posto per posto, i ruoli junior nelle aziende tech — e chi non taglia il personale giovane resterà indietro.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Un report interno di Anthropic, diffuso questa settimana, è uno dei primi a mettere numeri reali su questa domanda, partendo dai propri dati HR.",
        points=[
            "27% → 9% — la quota di nuove assunzioni tecniche che Anthropic destinava a profili junior è scesa da oltre un quarto a meno di un decimo dei nuovi ingressi, dall'inizio del 2025.",
            "21% → 14% — anche la quota di personale tecnico già junior sul totale è calata, mentre l'organico complessivo dell'azienda è triplicato nello stesso periodo.",
            "6 a 1 — il rapporto tra le ore di lavoro svolte dagli agenti Claude diretti dai dipendenti e quelle del personale umano, raggiunto entro agosto 2026 secondo lo stesso report.",
        ],
        myth_closing="Questi numeri non dicono che un agente sostituisce un giovane ingegnere uno a uno — dicono che il lavoro di routine su cui un junior imparava facendo si sta spostando sugli agenti, e che il ruolo umano si sposta verso la supervisione, l'architettura e la verifica. È esattamente il presidio che un agente, da solo, non sa fare: non basta orchestrare più lavoro, serve chi ne governa la qualità e i rischi prima che arrivi in produzione.",
        cta="Nella tua azienda, chi sta ridisegnando i ruoli junior intorno agli agenti AI — e chi, invece, sta solo tagliando le assunzioni? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 21/10",
        format="Carosello dati (mito da sfatare — le aziende hanno il controllo dei propri agenti AI)",
        title="La tua azienda ha il controllo dei propri agenti AI? I dati dicono di *no*",
        news="Report Salt Security «State of Agentic AI and API Security»",
        news_url="https://www.itsecurityguru.org/2026/10/14/nearly-half-of-organisations-report-unauthorised-ai-agent-actions-research-finds/",
        hook="🔥 Il mito: un'azienda che ha messo in produzione degli agenti AI sa cosa fanno, quando lo fanno, e può fermarli se sbagliano.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il report «State of Agentic AI and API Security» di Salt Security, pubblicato questa settimana su oltre 380 professionisti di sicurezza, racconta una realtà diversa.",
        points=[
            "86,4% — delle organizzazioni ha già almeno un agente AI in funzione, e il 59,5% ne ha più di dieci: l'adozione è già massiccia, ben oltre la fase sperimentale.",
            "49,8% — delle organizzazioni ha confermato o sospettato che un agente abbia compiuto un'azione non intenzionale o non autorizzata nell'ultimo anno, più spesso una chiamata API esterna o una modifica di dati.",
            "12,5% — la quota di aziende che riesce a tracciare con continuità l'intero percorso di un agente, dall'istruzione iniziale al risultato finale: per il resto servirebbero ore o giorni per ricostruirlo a posteriori.",
            "17,5% — la quota che può arrestare automaticamente, in produzione, un agente che si comporta in modo anomalo: per gli altri quattro su cinque, fermarlo richiede un intervento manuale.",
        ],
        myth_closing="Il problema non è se usare gli agenti AI — l'86% delle aziende lo fa già — ma che l'adozione è corsa più veloce della capacità di tracciarli e governarli. È lo stesso scarto che il vibe coding ha aperto sul codice: prototipare con l'AI è ormai alla portata di chiunque, ma l'architettura, i permessi e il controllo di cosa un agente può davvero fare restano un lavoro da presidiare con competenze senior, non da lasciare all'entusiasmo del primo pilota.",
        cta="Nella tua azienda, qualcuno saprebbe ricostruire cosa ha fatto un agente AI ieri — o ci vorrebbero giorni? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 22/10",
        format="Esperienza diretta",
        title="Abbiamo provato a tracciare cosa fanno davvero i nostri agenti AI interni. Ecco cosa abbiamo *trovato*",
        news="Spunto dal report Salt Security sulla tracciabilità degli agenti AI (vedi post di ieri)",
        news_url="https://www.itsecurityguru.org/2026/10/14/nearly-half-of-organisations-report-unauthorised-ai-agent-actions-research-finds/",
        hook="Dopo i dati di ieri su quanto poco le aziende riescano a tracciare i propri agenti AI, ci siamo chiesti: noi, internamente, sapremmo rispondere? Questa settimana abbiamo messo alla prova proprio questo.",
        points=[
            "Abbiamo preso uno dei flussi di lavoro interni in cui usiamo agenti AI (ricerca, prima bozza di contenuti, controlli di qualità) e abbiamo provato a ricostruire, a posteriori, ogni passaggio che l'agente aveva fatto per arrivare al risultato finale.",
            "[Da personalizzare con l'esito reale della prova del team: quanto è stato semplice o difficile ricostruire il percorso, quali passaggi erano opachi, cosa avete dovuto aggiungere per renderlo tracciabile — senza inventare cifre o esiti non verificati.]",
            "La lezione non è «serve uno strumento di monitoraggio in più», ma che la tracciabilità va progettata insieme al flusso di lavoro fin dall'inizio, non aggiunta a posteriori quando qualcosa è già andato storto.",
        ],
        cta="La vostra azienda saprebbe ricostruire, oggi, cosa ha fatto un agente AI interno nell'ultima settimana? Raccontatecelo 👇",
        hashtags="#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 23/10",
        format="Divulgativo stile Datapizza",
        title="Un enigma crittografico vecchio 25 anni, risolto da un'AI in mezz'ora. Come ha fatto, in parole *povere*",
        news="Claude risolve l'enigma delle curve ECDSA del NIST",
        news_url="https://anthropic.com/research/ecdsa-curve-origins",
        hook="Nel 2000 il NIST ha scelto le curve crittografiche alla base di ECDSA, uno degli standard di sicurezza più usati al mondo — comprese quelle che probabilmente proteggono anche parte del traffico della tua azienda. Da allora un dettaglio restava un mistero: da dove venivano i numeri di partenza di quelle curve? Il sospetto, mai confermato, era una backdoor della NSA. Questa settimana Anthropic ha raccontato come Claude lo ha risolto in meno di mezz'ora.",
        points=[
            "Un generatore di numeri «casuali» in realtà non lo è mai del tutto: parte sempre da un valore iniziale, il seed. Se conosci il seed e il metodo, puoi ricostruire ogni numero che ha prodotto — è la base di molta crittografia, e anche il punto debole se quel seed nasconde qualcosa.",
            "Per 25 anni i ricercatori hanno provato a spiegare i seed delle curve NIST con un'ipotesi (un testo trasformato in un calcolo di verifica): sbagliata. Claude ha cambiato approccio, ha ipotizzato un generatore casuale tipico degli anni '90, trovato un pattern sospetto nei numeri, e con un metodo matematico ha ricostruito lo stato interno di quel generatore.",
            "Risultato: i seed derivano semplicemente dall'orario del computer tra il 1997 e il 1998 — un dato banale, non una backdoor. La cosa interessante non è che il mistero fosse innocente, ma che un modello AI lo abbia risolto in 30 minuti dopo che più ricercatori umani avevano seguito la pista sbagliata per anni.",
        ],
        cta="Ti è mai capitato che un'AI risolvesse un problema tecnico aperto da tempo semplicemente cambiando l'ipotesi di partenza? Raccontaci il caso 👇",
        hashtags="#AI #TechExplained #Crittografia #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati — l'AI nelle PMI italiane secondo Nomisma",
        title="2 PMI italiane su 3 non usano l'AI in modo *strutturato*",
        news="Studio Nomisma AI.DEA sulle PMI italiane (Forum di Varignana)",
        news_url="https://www.rivista.ai/2026/10/17/nomisma-lai-e-gia-nelle-imprese-italiane-ma-nel-45-dei-casi-la-usano-i-dipendenti-non-lorganizzazione/",
        hook="Lo studio AI.DEA di Nomisma, presentato questa settimana al Forum di Varignana su oltre 200 PMI italiane (Machinery, Agrifood, Motor Valley), fotografa un'Italia produttiva che sta usando l'AI più per iniziativa dei singoli che come scelta aziendale.",
        points=[
            "45% — delle PMI usa l'AI in modo informale, per iniziativa dei singoli dipendenti; il 21% non la usa affatto: due aziende su tre restano senza un utilizzo strutturato.",
            "4% — usa l'AI per trasformare il proprio modello di business, e l'8% ha sviluppato processi AI-driven: il resto si ferma all'automazione di singole attività o a un uso estemporaneo.",
            "50% — indica la mancanza di competenze interne come primo ostacolo, e 7 aziende su 10 non hanno ancora avviato un percorso di formazione sull'AI, pur riconoscendo nel 57% dei casi che le competenze sono la leva più importante.",
            "56% — di chi usa o prevede di usare l'AI destina meno dello 0,5% del fatturato alla tecnologia, e il 23% non prevede risorse specifiche: l'intenzione c'è più spesso del budget.",
        ],
        closing="Il divario che descrive questo studio non è tra chi ha l'AI e chi no — è tra chi la lascia all'iniziativa dei singoli e chi la trasforma in un processo aziendale, con competenze e budget dedicati. Ed è esattamente lì che si gioca la differenza tra un esperimento isolato e un vantaggio competitivo reale.",
        cta="Nella tua azienda l'AI è un'iniziativa dei singoli o un processo con un responsabile e un budget? 👇",
        hashtags="#IntelligenzaArtificiale #PMI #DigitalTransformation #B2B #Formazione",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice sulla fiducia nell'*AI*",
        news="Sintesi dei trend della settimana 12 - 19 ottobre 2026",
        news_url="https://www.thestar.com.my/tech/tech-news/2026/10/16/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "Anthropic cresce del 45% in un trimestre e gli investitori tagliano comunque le attese di valutazione: anche nell'AI, i numeri assoluti contano meno del trend rispetto alle attese.",
            "La Commissione Europea apre la prima indagine formale ex AI Act su OpenAI e Anthropic: la fase delle dichiarazioni di principio sulla sicurezza degli agenti sta finendo.",
            "Un report di settore dice che quasi la metà delle aziende ha già subito un'azione non autorizzata da un agente AI, e solo una su otto riesce a tracciarne il percorso per intero.",
            "Un report interno di Anthropic mostra le assunzioni junior tecniche scendere dal 27% al 9%: il lavoro di routine si sposta sugli agenti, quello umano verso la supervisione.",
            "Lo studio Nomisma sulle PMI italiane ricorda che, per la maggior parte delle aziende del nostro Paese, il problema non è ancora quello degli agenti fuori controllo — è iniziare ad avere un processo AI strutturato.",
        ],
        closing="Una settimana che parla, più di ogni altra cosa, di fiducia: quella degli investitori, quella dei regolatori, quella delle aziende verso i propri strumenti. Nessuna di queste si costruisce da sola — si costruisce con dati, verifica e governance, non con l'adozione in sé.",
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
        day="Lunedì 19/10",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 20/10",
        time="12:15",
        format="Mito da sfatare (assunzioni junior e agenti AI)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — e prepara il terreno al carosello del giorno dopo sullo stesso filo (fiducia nel controllo degli strumenti AI).",
    ),
    dict(
        day="Mercoledì 21/10",
        time="12:15",
        format="Carosello dati / mito da sfatare (controllo degli agenti AI in azienda)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di un giorno dal primo mito ma sullo stesso filo narrativo. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i dati del report Salt Security sono densi abbastanza da meritare uno spazio proprio.",
    ),
    dict(
        day="Giovedì 22/10",
        time="08:30",
        format="Esperienza diretta (tracciabilità degli agenti AI interni)",
        reason="Segue narrativamente il carosello del giorno prima, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 23/10",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello «le PMI italiane e l'AI» (studio Nomisma)",
        reason="Banca contenuti: utile come secondo documento se questa settimana c'è margine di pubblicazione, o come apertura della settimana successiva su un tema a lungo termine per il pubblico B2B italiano. Non promossa a Prioritario questa settimana: i 5 slot fissi dello schema (apertura, due miti, esperienza diretta, divulgativo) sono già tutti occupati dal filo narrativo su fiducia, agenti e lavoro.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
