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

WEEK_LABEL = "9 – 15 novembre 2026"
GENERATED_ON = "Lunedì 9 novembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 2-9 novembre 2026, verificate su fonte diretta (non sui
# riassunti aggregatori). Filo conduttore della settimana: mentre il mercato
# comincia apertamente a dubitare della sostenibilita' della spesa in
# infrastrutture AI (il crollo dei chip legato alle elezioni di midterm),
# l'industria stessa mostra quanto sia ancora fragile sul fronte della fiducia
# e del controllo — una violazione a un fornitore terzo di OpenAI, una frode
# da 129 milioni di dollari costruita con voci e volti clonati dall'AI, e la
# corsa di OpenAI, Perplexity e Anthropic ad affidare compiti sempre piu'
# lunghi e sensibili ad agenti autonomi, proprio mentre il controllo su quegli
# agenti diventa un problema di prodotto prima ancora che di policy.
trends = [
    dict(
        title="I titoli dei chip AI hanno la peggiore settimana da un anno e mezzo, tra dubbi sui data center",
        what="Giovedì 5 novembre l'indice Philadelphia Semiconductor (SOX) ha perso il 9,2% in una sola seduta — il calo piu' forte da giugno — portando il bilancio settimanale a circa -12%, la quinta settimana consecutiva in negativo e la peggiore dall'aprile 2025. Nvidia ha perso fino al 7,5% intraday (il suo calo piu' forte dall'aprile 2025), AMD il 15%, Micron il 13%, Intel il 9,2%; tra i fornitori di infrastrutture cloud per l'AI, CoreWeave ha perso il 12% e Nebius il 17%. Il detonatore sono le elezioni di midterm di martedi' 3 novembre, che hanno dato ai Democratici la maggioranza di Camera e Senato: secondo gli osservatori di mercato, il risultato alimenta l'opposizione politica alla costruzione di nuovi data center, già contestati per i costi energetici, l'impatto ambientale e l'affidabilità della rete elettrica — in Texas la governatrice eletta ha proposto una moratoria sulle nuove costruzioni.",
        why="E' il tipo di notizia con la ricaduta pratica più diretta della settimana per chi lavora con l'AI: un dubbio di mercato sulla sostenibilità della spesa in infrastrutture non è un film lontano da chi la usa ogni giorno, perché è la stessa spesa che tiene bassi i prezzi delle API su cui le aziende costruiscono i propri prodotti.",
        source="Stocktwits (dati intraday di mercato)",
        url="https://stocktwits.com/news-articles/markets/equity/soxx-etf-semiconductor-is-set-for-its-worst-week-in-over-18-months/cNG1sEhR94Z",
    ),
    dict(
        title="Nella stessa settimana, OpenAI chiude un'altra tranche di finanziamento da 11 miliardi e Goldman Sachs alza le stime sui data center",
        what="Venerdì 6 novembre Bloomberg ha riportato, citando fonti vicine alla trattativa, che OpenAI ha chiuso una prima tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi di dollari. Nello stesso giro di giorni Goldman Sachs ha alzato la propria stima di capacità globale dei data center nel 2030 da 217 a 273 gigawatt — un aumento che implica centinaia di miliardi di dollari di spesa cumulata in più rispetto alle stime precedenti.",
        why="E' il contrappunto diretto al trend precedente: mentre il mercato azionario inizia a dubitare della sostenibilità della scommessa sui data center, i capitali per finanziarla continuano ad arrivare e le stime di spesa continuano a salire — un disallineamento che vale la pena notare, non un segnale in una direzione sola.",
        source="GV Wire (Reuters/Bloomberg)",
        url="https://gvwire.com/2026/11/06/openai-secures-11-billion-funding-at-1-25-trillion-valuation-bloomberg-news-reports/",
    ),
    dict(
        title="Una violazione al fornitore di analytics di OpenAI espone dati di profilo degli utenti",
        what="L'8 novembre Mixpanel, il fornitore di analytics usato da OpenAI sul proprio sito per sviluppatori (platform.openai.com), ha comunicato di aver subito una violazione tramite una campagna di smishing (phishing via SMS), senza fornire dettagli tecnici su come l'attaccante abbia ottenuto l'accesso. OpenAI ha dichiarato che il dataset sottratto riguarda nome, email, posizione approssimativa (città/stato/paese) ricavata dal browser, sistema operativo, browser e ID di organizzazione o utente dei profili registrati sulla piattaforma — non contenuti o risposte di ChatGPT, non chiavi API, password o dati di pagamento. OpenAI ha rimosso Mixpanel dai servizi di produzione e sta notificando direttamente le organizzazioni coinvolte.",
        why="Tocca un punto che riguarda ogni azienda che integra un servizio AI nei propri processi, non solo chi usa ChatGPT: la sicurezza dei propri dati dipende anche dai fornitori che il fornitore scelto ha scelto a sua volta, e che l'azienda cliente non controlla né sceglie direttamente.",
        source="SecurityWeek",
        url="https://www.securityweek.com/openai-user-data-exposed-in-mixpanel-hack/",
    ),
    dict(
        title="Tre persone incriminate per una frode da 129 milioni di dollari costruita impersonando CEO e avvocati con l'AI",
        what="Il 6 novembre la procura federale del Distretto Sud di New York (SDNY) ha incriminato tre persone — Jacob Soall, Sharon Hazan e Guy Sheetrit — per una presunta frode da 129 milioni di dollari ai danni di aziende in tutto il mondo. Secondo l'accusa, il gruppo impersonava CEO e avvocati usando l'AI per clonare voci e, in alcuni casi, volti nelle videochiamate: le vittime, tipicamente nei reparti contabilità, ricevevano prima un'email che sembrava del CEO con una richiesta finanziaria riservata, poi una chiamata o videochiamata con voce o volto clonati, seguita da un falso avvocato che chiedeva un bonifico verso conti esteri; i fondi venivano poi convertiti in criptovalute. I capi d'imputazione sono frode telematica, furto aggravato d'identità e riciclaggio di denaro, con pene massime rispettivamente di 20, 2 e 20 anni per capo d'accusa. Le accuse non sono ancora state provate in tribunale.",
        why="E' il tipo di notizia che riguarda chiunque abbia un reparto contabilità e un CEO con una minima presenza pubblica, non solo chi lavora nell'AI: la tecnologia per clonare una voce o un volto da pochi secondi di video pubblico è già alla portata di chiunque, e il bersaglio non è il sistema informatico ma la procedura umana che autorizza un bonifico.",
        source="KTVU (FOX)",
        url="https://www.ktvu.com/news/three-accused-ai-impersonate-ceos-fraud-scheme",
    ),
    dict(
        title="OpenAI rilascia Codex CLI 0.167.0 con un \"centro di comando\" per più agenti in parallelo",
        what="Il 6 novembre OpenAI ha reso stabile Codex CLI 0.167.0, con un pannello (\"agent command center\") che mostra in un'unica vista gli agenti attivi, in coda e completati su tutte le sessioni aperte, segnalando i risultati non ancora letti. La versione aggiunge anche il passaggio tra backend diversi senza perdere la bozza del prompt in corso (da un executor locale a una sessione cloud, per esempio), anteprime delle immagini allegate nel composer, e un wizard di configurazione per Google Cloud Vertex AI pensato per le aziende con vincoli di residenza dei dati.",
        why="E' un segnale concreto di dove si sta spostando lo sviluppo assistito dall'AI: non più una singola richiesta a cui rispondere, ma più agenti che lavorano in parallelo e che richiedono uno strumento dedicato solo per tenerne traccia — un cambio di scala nel lavoro quotidiano di un team di sviluppo, non solo una nuova funzione.",
        source="Changelog di Codex CLI (Daniel Vaughan)",
        url="https://codex.danielvaughan.com/2026/11/06/codex-v0167-stable-agent-command-center-multi-backend-image-attachments-gcp-vertex/",
    ),
    dict(
        title="Perplexity lancia \"Teammates\", agenti AI persistenti per compiti che durano giorni o settimane",
        what="Giovedì 5 novembre Perplexity ha lanciato Teammates, agenti a cui si affida una responsabilità continuativa — gestire una campagna, smistare segnalazioni, monitorare metriche, condurre ricerche di mercato — invece di una singola richiesta. Ogni teammate ha un proprio desktop e browser con sessioni indipendenti, pianifica i compiti, coinvolge altri agenti quando il lavoro cresce, e può collaborare con i colleghi umani anche su Slack. La funzione si basa su Perplexity Computer (riprendendone plugin, progetti e memoria) ed è per ora disponibile solo via web per gli abbonati Max (200 dollari al mese).",
        why="Insieme al rilascio di Codex della stessa settimana, mostra la stessa direzione da due fornitori diversi: affidare all'AI non più singole richieste ma responsabilità continuative nel tempo — il che sposta anche il tema del controllo, perché un agente che lavora per giorni senza supervisione diretta richiede un modo diverso di verificarne l'operato.",
        source="Digital Trends (via LetsDataScience)",
        url="https://letsdatascience.com/news/perplexity-launches-teammates-persistent-ai-agents-for-max-s-704b7a36",
    ),
    dict(
        title="Anthropic aggiorna Claude Enterprise con un centro di sicurezza e una console amministrativa centralizzata",
        what="Il 5 novembre Anthropic ha annunciato un pacchetto di funzioni per Claude Enterprise rivolte ai team di sicurezza: un \"security center\" (beta) che confronta la configurazione dell'organizzazione con le raccomandazioni di Anthropic ed esporta un report; gli \"inference hooks\", ora disponibili in generale, che inviano prompt e chiamate agli strumenti a un tool di sicurezza esterno (per esempio di data-loss-prevention) prima dell'esecuzione; una console amministrativa centralizzata (admin.claude.com, beta) per le aziende con più organizzazioni collegate, con SSO, sincronizzazione directory e gruppi; e controlli di accesso come la disconnessione di un membro via API, il blocco di account Claude personali su computer aziendali e un sensore EDR per la macchina virtuale locale di Cowork.",
        why="E' la risposta diretta, sullo stesso fronte, al tipo di rischio che la violazione Mixpanel e la frode da 129 milioni rendono concreto questa settimana: dare ai team di sicurezza aziendali visibilità su cosa fa un assistente AI sui dispositivi di lavoro, non solo policy scritte su come dovrebbe comportarsi.",
        source="Blog ufficiale Anthropic/Claude",
        url="https://claude.com/blog/claude-enterprise-security-updates",
    ),
    dict(
        title="Il paradosso della produttività AI torna al centro del dibattito, mentre i CFO pianificano più tagli",
        what="Un working paper NBER del 24 marzo 2026, basato sul Duke CFO Survey condotto con le Federal Reserve Bank di Atlanta e Richmond su 750 aziende USA, stima che il 44% dei direttori finanziari pianifica per il 2026 tagli occupazionali legati all'AI, per circa 502.000 ruoli nell'intera economia — circa nove volte i circa 55.000 tagli attribuiti all'AI nel 2025. Lo stesso studio, e un commento di Goldman Sachs di inizio marzo citato nell'articolo, rilevano che i dati non mostrano ancora un aumento di produttività misurabile a livello macroeconomico che giustifichi quella scala di tagli: il divario viene attribuito a un ritardo nella realizzazione dei benefici, non a un errore di misura.",
        why="E' il contesto numerico dietro una domanda che ogni azienda che ha automatizzato o sta per automatizzare dei ruoli con l'AI dovrebbe porsi: il taglio precede il guadagno di produttività, o lo sostituisce con una scommessa? La data dello studio (marzo 2026) è più vecchia della settimana, ma il divario che descrive resta la cornice in cui vanno lette le notizie di mercato di questa settimana.",
        source="Interview Query (sintesi del working paper NBER)",
        url="https://www.interviewquery.com/p/ai-layoffs-2026-productivity-gap",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="OpenAI",
        what="Chiude una prima tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi (6/11) e rilascia Codex CLI 0.167.0 con un centro di comando per più agenti in parallelo (6/11) — nella stessa settimana in cui un suo fornitore di analytics, Mixpanel, viene violato esponendo dati di profilo degli utenti della piattaforma per sviluppatori (8/11).",
        positioning="Continua a muoversi su tre fronti insieme — capitale, prodotto, sicurezza — alla velocità più alta del settore, ma è anche il fornitore la cui catena di terze parti (analytics, hosting, pagamento) è risultata, questa settimana, il punto più debole della propria sicurezza: non un attacco diretto ai propri sistemi, ma a chi li supporta.",
        angle="Per un'azienda che integra le API OpenAI (o di qualunque altro fornitore AI) nei propri processi, il punto non è smettere di usarle — è sapere quali fornitori terzi quel servizio porta con sé, e cosa succede ai propri dati se uno di loro viene violato: è esattamente il lavoro di governance che il Team Augmentation di Digitiamo porta in azienda.",
    ),
    dict(
        name="Anthropic",
        what="Aggiorna Claude Enterprise con un centro di sicurezza, una console amministrativa centralizzata e nuovi controlli di accesso pensati per i team di sicurezza aziendali (5/11), nella stessa settimana in cui una frode da 129 milioni di dollari basata su voci clonate dall'AI finisce sotto i riflettori e un fornitore terzo di un concorrente diretto viene violato.",
        positioning="Si posiziona sempre di più come il fornitore che vende non solo il modello ma il controllo sul modello — visibilità su cosa fa un agente AI sui dispositivi aziendali, non solo policy scritte — proprio mentre il resto del settore corre verso agenti che lavorano per giorni senza supervisione diretta (vedi Perplexity, sotto).",
        angle="Gli strumenti di sicurezza di un fornitore non sostituiscono la domanda che un'azienda deve farsi prima: quali compiti vogliamo davvero affidare a un agente che lavora senza supervisione, e chi in azienda ha il tempo e la competenza di controllarne l'operato — il terreno dell'AI Business Academy.",
    ),
    dict(
        name="Perplexity",
        what="Lancia Teammates (5/11), agenti AI persistenti a cui affidare una responsabilità continuativa — non una singola richiesta — per gli abbonati Max, basati su Perplexity Computer e capaci di coinvolgere altri agenti e di collaborare con i colleghi umani su Slack.",
        positioning="Prova a conquistare il segmento dei singoli abbonati con un prodotto che finora era stato proposto solo alle organizzazioni (i workspace agent di OpenAI, Copilot Cowork di Microsoft): la scommessa è che un lavoratore singolo voglia affidare un compito per giorni a un agente, non solo farsi rispondere a una domanda.",
        angle="Un agente che lavora per giorni senza supervisione diretta sposta il rischio dal \"ha risposto bene?\" al \"cosa ha fatto davvero, nel frattempo, con quali permessi?\": prima di affidare compiti continuativi a un agente, un'azienda ha bisogno di sapere come verificarne l'operato — di nuovo, il lavoro che il Team Augmentation di Digitiamo porta in azienda.",
    ),
    dict(
        name="Il comparto chip e infrastrutture AI (Nvidia, AMD, Micron, CoreWeave, Nebius)",
        what="Perde tra il 7,5% e il 17% in una sola seduta (giovedì 5 novembre), con l'indice SOX giù del 12% nella settimana — la peggiore da un anno e mezzo — dopo le elezioni di midterm del 3 novembre, che secondo gli osservatori di mercato hanno rafforzato l'opposizione politica alla costruzione di nuovi data center.",
        positioning="Il settore che ha costruito la propria crescita sulla promessa di una domanda AI in espansione illimitata si trova, nella stessa settimana, a fare i conti con un'opposizione politica concreta (una moratoria proposta in Texas) e con un mercato che inizia a prezzare quel rischio — mentre Goldman Sachs alza comunque le stime di spesa futura.",
        angle="Per un'azienda che pianifica investimenti AI pluriennali, è un promemoria diretto: i prezzi delle API e dell'infrastruttura cloud su cui si basa un progetto AI oggi dipendono da una scommessa di mercato ancora instabile — un motivo in più per scegliere un partner che aiuti a dimensionare il progetto sul bisogno reale, non sulla capacità disponibile a buon mercato in questo momento.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: si apre con il quadro più ampio e meno "di parte" —
# il mercato dei chip AI che inizia a dubitare della sostenibilità della
# spesa in infrastrutture, proprio mentre l'industria (OpenAI, Goldman Sachs)
# continua a scommetterci sopra — nessuna vendita, solo analisi. Da martedì a
# venerdì l'arco si stringe su un unico filo, quello della fiducia e del
# controllo sugli strumenti AI: martedì il mito da sfatare sulla violazione
# del fornitore terzo di OpenAI (Mixpanel); mercoledì il carosello dati sulla
# frode da 129 milioni di dollari costruita con voci clonate dall'AI,
# promosso a Prioritario per la densità di cifre che offre (al posto di
# un'idea "ad alta varietà" più intercambiabile — nota sul mix di formati,
# più sotto); giovedì l'esperienza diretta riprende lo stesso filo
# mettendo alla prova il team su un deepfake vocale; venerdì la mini-lezione
# chiude l'arco spiegando la tecnologia di voice e face cloning dietro la
# truffa. Le due riserve restano banca contenuti: un secondo carosello dati,
# più granulare, sul crollo dei chip AI aperto lunedì, e la riflessione di
# chiusura settimana.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 9/11",
        format="Thought leadership — apertura settimana",
        title="I chip AI hanno la peggiore settimana in un anno e mezzo. L'industria, intanto, alza ancora le stime",
        titolo_post="La settimana nera dei chip AI",
        sottotitolo_post="Il comparto semiconduttori perde il 12% in cinque giorni, mentre Goldman alza le stime sui data center.",
        news="Il crollo dei titoli dei chip AI dopo le elezioni di midterm (3-5/11)",
        news_url="https://stocktwits.com/news-articles/markets/equity/soxx-etf-semiconductor-is-set-for-its-worst-week-in-over-18-months/cNG1sEhR94Z",
        hook="Giovedì 5 novembre l'indice Philadelphia Semiconductor (SOX) ha perso il 9,2% in una sola seduta, portando il bilancio della settimana a circa -12%: la quinta settimana consecutiva in negativo, la peggiore dall'aprile 2025. Nvidia ha perso fino al 7,5% intraday, AMD il 15%, Micron il 13%. Il detonatore sono le elezioni di midterm del 3 novembre, che hanno dato ai Democratici la maggioranza di Camera e Senato, alimentando l'opposizione politica alla costruzione di nuovi data center. Ma nella stessa settimana Goldman Sachs ha alzato la stima di capacità globale dei data center al 2030, e OpenAI ha chiuso una nuova tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi.",
        visual_hook="Il comparto chip AI ha perso il 12% in una settimana, la peggiore dall'aprile 2025 — mentre Goldman Sachs alza le stime di spesa sui data center.",
        points=[
            "9,2% — il calo in una sola seduta (giovedì 5 novembre) dell'indice SOX (Philadelphia Semiconductor), il più forte da giugno; -12% il bilancio dell'intera settimana, la peggiore dall'aprile 2025.",
            "Nvidia ha perso fino al 7,5% intraday (il suo calo più forte dall'aprile 2025), AMD il 15%, Micron il 13%, Intel il 9,2%; tra i fornitori di infrastrutture cloud per l'AI, CoreWeave ha perso il 12% e Nebius il 17%.",
            "Il detonatore: le elezioni di midterm del 3 novembre hanno dato ai Democratici la maggioranza di Camera e Senato, alimentando l'opposizione politica ai nuovi data center — in Texas la governatrice eletta ha proposto una moratoria sulle nuove costruzioni.",
            "Nella stessa settimana Goldman Sachs ha alzato la stima di capacità globale dei data center nel 2030 da 217 a 273 gigawatt, e OpenAI ha chiuso una prima tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi: l'offerta di capitale per l'AI non rallenta, proprio mentre il mercato inizia a dubitarne.",
        ],
        punti_post=[
            "SOX (chip): -12% in una settimana, la peggiore dall'aprile 2025.",
            "Nvidia -7,5%, AMD -15%, Micron -13% in un solo giorno.",
            "Goldman alza le stime sui data center; OpenAI chiude 11 mld $.",
        ],
        cta="Se il mercato dubita della sostenibilità della scommessa sui data center AI, la tua azienda ha un piano che non dipende da quella scommessa? 👇",
        hashtags="#IntelligenzaArtificiale #AI #Mercati #Innovazione #B2B",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 10/11",
        format="Mito da sfatare",
        title="Il tuo fornitore AI non è mai stato violato direttamente, quindi i tuoi dati restano *sicuri*",
        titolo_post="I tuoi dati restano *sicuri*?",
        sottotitolo_post="Una violazione al fornitore di analytics di OpenAI (Mixpanel) ha esposto dati utente l'8 novembre.",
        barrato="sicuri",
        news="Violazione a Mixpanel, fornitore di analytics di OpenAI, espone dati di profilo degli utenti (8/11)",
        news_url="https://www.securityweek.com/openai-user-data-exposed-in-mixpanel-hack/",
        hook="🔥 Il mito: se la tua azienda usa un fornitore AI affidabile, e quel fornitore non subisce mai una violazione diretta ai propri sistemi, i dati dei tuoi clienti restano al sicuro.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="L'8 novembre un fornitore terzo di OpenAI è stato violato. OpenAI non è stata attaccata direttamente: il suo fornitore sì.",
        myth_body="L'8 novembre Mixpanel, il fornitore di analytics usato da OpenAI sul proprio sito per sviluppatori, ha comunicato una violazione subita tramite una campagna di smishing (phishing via SMS). OpenAI non è stata attaccata direttamente: il suo fornitore sì — ed è bastato.",
        points=[
            "I dati sottratti riguardano i profili utente di platform.openai.com: nome, email, posizione approssimativa (città, stato, paese), sistema operativo, browser e ID di organizzazione o utente.",
            "OpenAI precisa che non sono stati compromessi contenuti o risposte di ChatGPT, chiavi API, password o dati di pagamento — ma avverte che i dati esposti possono comunque alimentare nuovi attacchi di phishing mirato.",
            "Mixpanel ha parlato di un \"numero limitato\" di clienti coinvolti, senza specificare quanti: la trasparenza su un fornitore terzo resta nelle mani del fornitore, non dell'azienda che lo ha scelto.",
        ],
        punti_post=[
            "Violazione a Mixpanel (smishing), non a OpenAI direttamente.",
            "Esposti nome, email, posizione, OS e browser dei profili utente.",
            "Password, chiavi API e pagamenti non coinvolti, dice OpenAI.",
        ],
        myth_closing="Il problema non è se il fornitore che hai scelto sia affidabile — probabilmente lo è. È che ogni servizio AI che usi si appoggia a sua volta su altri fornitori (analytics, hosting, pagamenti), e la sicurezza dei tuoi dati dipende anche da quelli che non hai scelto tu direttamente. Sapere quali terze parti toccano i dati che affidi a uno strumento AI, e cosa succede se una di loro viene violata, è un lavoro di governance — non un dettaglio da dare per scontato.",
        cta="La tua azienda saprebbe elencare oggi quali fornitori terzi toccano i dati che affida ai suoi strumenti AI? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 11/11",
        format="Carosello / documento dati — promosso a Prioritario per la densità di cifre",
        title="129 milioni di dollari rubati impersonando CEO e avvocati con l'AI: l'accusa federale in cifre",
        titolo_post="129 milioni rubati con CEO clonati dall'AI",
        sottotitolo_post="Tre persone incriminate a New York per una frode con voci e volti di CEO clonati dall'AI.",
        news="Tre persone incriminate dalla procura di New York (SDNY) per una frode da 129 milioni di dollari con AI (6/11)",
        news_url="https://www.ktvu.com/news/three-accused-ai-impersonate-ceos-fraud-scheme",
        hook="Il 6 novembre la procura federale del Distretto Sud di New York (SDNY) ha incriminato tre persone — Jacob Soall, Sharon Hazan e Guy Sheetrit — per una frode da 129 milioni di dollari ai danni di aziende in tutto il mondo, costruita impersonando con l'AI le voci e, in alcuni casi, i volti di CEO e avvocati nelle videochiamate con i reparti contabilità delle vittime.",
        points=[
            "129 milioni di dollari — l'importo complessivo che la procura attribuisce alla frode, costruita impersonando con l'AI le voci e i volti di CEO e avvocati nelle videochiamate con i reparti contabilità delle vittime.",
            "3 — gli imputati incriminati dal Distretto Sud di New York (SDNY): Jacob Soall, Sharon Hazan e Guy Sheetrit, indicati nell'atto d'accusa anche con soprannomi come \"Rocky Balboa\" e \"Superman Cash\".",
            "20 anni — la pena massima prevista per ciascun capo d'imputazione di frode telematica e riciclaggio di denaro, secondo la procura.",
            "2 anni — la pena massima aggiuntiva prevista per il furto aggravato d'identità, il terzo reato contestato.",
            "Il meccanismo, secondo l'accusa: un'email che sembra del CEO chiede un'operazione finanziaria riservata; segue una chiamata o videochiamata con voce o volto clonati dall'AI, poi un falso avvocato chiede un bonifico verso conti esteri, e i fondi vengono convertiti in criptovalute.",
        ],
        punti_post=[
            "129 milioni di dollari — rubati impersonando CEO e avvocati con AI.",
            "3 — gli imputati incriminati dalla procura di New York (SDNY).",
            "20 anni — pena massima per frode telematica e riciclaggio.",
            "2 anni — pena massima aggiuntiva per furto aggravato d'identità.",
        ],
        closing="Dietro ogni cifra di questa truffa c'è una procedura che un'azienda strutturata avrebbe potuto far saltare: una verifica indipendente del bonifico, fuori dalla stessa catena di comunicazione che ha portato la richiesta. Non serve diffidare di ogni videochiamata — serve un secondo canale di conferma per ogni operazione finanziaria insolita, sempre. Le accuse non sono ancora state provate in tribunale.",
        cta="La tua azienda ha oggi un secondo canale di verifica, fuori da email e videochiamata, per ogni bonifico insolito? 👇",
        hashtags="#Cybersecurity #AI #Frode #B2B #Sicurezza",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 12/11",
        format="Esperienza diretta",
        title="Dopo il caso dei 129 milioni rubati con voci clonate dall'AI, abbiamo provato a capire se il nostro team riconoscerebbe un deepfake vocale",
        titolo_post="Il nostro team riconoscerebbe un *deepfake*?",
        sottotitolo_post="Dopo la truffa dei 129 milioni di dollari, abbiamo messo alla prova il team sui deepfake vocali.",
        news="Spunto dal caso di frode da 129 milioni di dollari con voci clonate dall'AI (vedi post di mercoledì)",
        news_url="https://www.ktvu.com/news/three-accused-ai-impersonate-ceos-fraud-scheme",
        hook="Dopo il caso di questa settimana — 129 milioni di dollari rubati impersonando CEO e avvocati con voce e volto clonati dall'AI — ci siamo fatti la domanda scomoda: il nostro team riconoscerebbe una voce clonata in una chiamata reale? Questa settimana lo abbiamo messo alla prova.",
        is_template=True,
        points=[
            "Abbiamo simulato una chiamata con una voce clonata (con il consenso esplicito di chi l'ha prestata) che chiedeva un'operazione finanziaria urgente e riservata, nello stile usato nel caso reale di questa settimana.",
            "[Da personalizzare con l'esito reale del test del team: chi ha riconosciuto l'anomalia e come, quali segnali hanno insospettito o non insospettito le persone coinvolte, cosa è emerso sulle procedure di verifica attuali — senza inventare cifre o esiti non verificati.]",
            "La domanda utile non è se la tecnologia per clonare una voce esiste — esiste già ed è alla portata di chiunque — ma se esiste, nella tua azienda, un secondo canale di verifica che non dipende dalla stessa chiamata.",
        ],
        punti_post=[
            "Abbiamo simulato una chiamata con voce clonata, col consenso di chi l'ha prestata.",
            "[Da personalizzare con l'esito reale del test del team.]",
            "La vera domanda: esiste un secondo canale di verifica indipendente?",
        ],
        cta="Il tuo team saprebbe dire oggi quale procedura seguire se ricevesse una chiamata così? Raccontaci la tua esperienza 👇",
        hashtags="#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 13/11",
        format="Divulgativo stile Datapizza",
        title="Come si clona davvero una voce con l'AI: il concetto tecnico dietro la truffa da 129 milioni di dollari",
        titolo_post="Come si clona una voce con l'AI",
        sottotitolo_post="Bastano pochi secondi di audio reale per clonare una voce: ecco come funziona davvero.",
        news="Il concetto di voice e face cloning dietro la frode da 129 milioni di dollari (vedi post di mercoledì)",
        news_url="https://www.ktvu.com/news/three-accused-ai-impersonate-ceos-fraud-scheme",
        hook="Questa settimana abbiamo parlato di una frode da 129 milioni di dollari costruita con voci e volti di CEO clonati dall'AI. Ma cosa vuol dire davvero \"clonare una voce\", e perché oggi basta così poco per farlo?",
        points=[
            "Un modello di sintesi vocale moderno impara il timbro di una voce da pochi secondi o minuti di audio reale — un video pubblico, una registrazione di una call, un messaggio vocale — e lo riapplica a un testo nuovo, scritto da chi compie la truffa.",
            "La parte difficile non è più tecnica: i modelli di voice cloning sono pubblicamente disponibili e a basso costo. La parte difficile, per chi li usa a fini fraudolenti, è ottenere abbastanza audio della persona da clonare — per questo i bersagli tipici sono dirigenti con una presenza pubblica (interviste, conferenze, video aziendali).",
            "Lo stesso vale per il volto nelle videochiamate: un modello di \"face swap\" in tempo reale sovrappone un volto clonato su quello di chi parla davvero, frame per frame — la tecnologia dietro ai casi di videochiamate con CEO falsi di questa settimana.",
        ],
        punti_post=[
            "Bastano secondi di audio pubblico per clonare il timbro di una voce.",
            "Il bersaglio tipico: dirigenti con molta presenza pubblica (video, interviste).",
            "Il \"face swap\" in tempo reale fa lo stesso con il volto in videochiamata.",
        ],
        cta="Conoscevi già quanto poco audio serve oggi per clonare una voce? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #Deepfake #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="Il crollo dei chip AI in cifre: la settimana nera di Wall Street",
        news="Il crollo dei titoli dei chip AI dopo le elezioni di midterm (3-5/11), in dettaglio",
        news_url="https://stocktwits.com/news-articles/markets/equity/soxx-etf-semiconductor-is-set-for-its-worst-week-in-over-18-months/cNG1sEhR94Z",
        hook="Lunedì abbiamo aperto la settimana con il crollo dei titoli dei chip AI. Ecco i numeri per esteso di quella che gli analisti chiamano già la settimana nera di Wall Street sull'AI.",
        points=[
            "9,2% — il calo in una sola seduta (giovedì 5 novembre) dell'indice SOX (Philadelphia Semiconductor), il peggiore da giugno.",
            "12% — il calo dell'indice SOX nell'intera settimana, la quinta consecutiva in negativo e la peggiore dall'aprile 2025.",
            "15% — il calo intraday di AMD giovedì; Nvidia ha perso fino al 7,5%, il suo calo più forte dall'aprile 2025.",
            "13% — il calo di Micron nello stesso giorno; Intel ha perso il 9,2%, i fornitori di infrastrutture cloud CoreWeave il 12% e Nebius il 17%.",
            "Il detonatore: le elezioni di midterm del 3 novembre hanno dato ai Democratici la maggioranza di Camera e Senato, alimentando l'opposizione politica ai nuovi data center — in Texas la governatrice eletta ha proposto una moratoria sulle nuove costruzioni.",
        ],
        closing="Nella stessa settimana Goldman Sachs ha alzato la stima di capacità globale dei data center nel 2030 da 217 a 273 gigawatt, e OpenAI ha chiuso una prima tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi: l'offerta di capitale per l'AI non rallenta, nello stesso momento in cui il mercato inizia a dubitare della sua sostenibilità.",
        cta="La tua azienda ha un piano che regge anche se la spesa in infrastrutture AI dovesse rallentare? 👇",
        hashtags="#AI #Mercati #Infrastruttura #B2B #Innovazione",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice su fiducia e controllo nell'AI",
        news="Sintesi dei trend della settimana 2-9 novembre 2026",
        news_url="https://www.securityweek.com/openai-user-data-exposed-in-mixpanel-hack/",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "Un fornitore terzo di OpenAI (Mixpanel) è stato violato l'8 novembre, e i dati esposti non riguardano un attacco diretto ai sistemi OpenAI: la sicurezza di un servizio AI dipende anche da fornitori che non scegli tu.",
            "Tre persone sono state incriminate per una frode da 129 milioni di dollari costruita impersonando CEO e avvocati con voci e volti clonati dall'AI: la tecnologia per farlo è già alla portata di chiunque.",
            "I titoli dei chip AI hanno avuto la peggiore settimana da un anno e mezzo, tra dubbi politici sui data center — eppure Goldman Sachs alza le stime di spesa e OpenAI chiude un nuovo round da 11 miliardi di dollari.",
            "OpenAI (Codex) e Perplexity (Teammates) hanno lanciato in pochi giorni nuovi strumenti per affidare compiti interi, non solo singole richieste, ad agenti AI.",
            "Anthropic ha aggiornato Claude Enterprise con un centro di sicurezza e una console amministrativa centralizzata: il controllo sugli agenti AI in azienda è ormai anche un tema di prodotto, non solo di policy.",
        ],
        closing="Una settimana che racconta la stessa domanda da angolazioni diverse: man mano che l'AI gestisce più soldi, più dati e più compiti da sola, chi controlla davvero cosa succede quando qualcosa va storto? La risposta non è smettere di usarla — è sapere, prima che succeda, chi in azienda ha la competenza e il tempo di controllarlo.",
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
        day="Lunedì 9/11",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 10/11",
        time="12:15",
        format="Mito da sfatare (violazione del fornitore terzo di OpenAI)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — apre il filo di sicurezza/fiducia che attraversa il resto della settimana.",
    ),
    dict(
        day="Mercoledì 11/11",
        time="12:15",
        format="Carosello / dati (la frode da 129 milioni di dollari)",
        reason="Seconda finestra pausa pranzo B2B. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e le cifre del caso (129 milioni di dollari, 3 imputati, pene fino a 20 anni) sono dense abbastanza da meritare uno spazio proprio — per questo è stato promosso da riserva a Prioritario questa settimana.",
    ),
    dict(
        day="Giovedì 12/11",
        time="08:30",
        format="Esperienza diretta (test del team sui deepfake vocali)",
        reason="Segue narrativamente il carosello di mercoledì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 13/11",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo di sicurezza aperto martedì.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello numeri sul crollo dei chip AI",
        reason="Banca contenuti: utile se la settimana ha margine per un sesto post, o come approfondimento del tema aperto lunedì.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
