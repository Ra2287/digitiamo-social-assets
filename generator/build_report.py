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

WEEK_LABEL = "23 – 29 novembre 2026"
GENERATED_ON = "Lunedì 23 novembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Prima generazione della settimana (23/11/2026). Nota editoriale: questa
# settimana la ricerca ha prodotto SEI trend verificati sulla fonte primaria,
# non otto-dieci come da indicazione standard. Diversi filoni promettenti
# sono stati scartati dopo verifica diretta, invece di essere forzati con un
# caveat (regola esplicita del brief: "un dato che non regge non va usato,
# nemmeno con un caveat"): il presunto vantaggio del 30% di AMD Instinct
# MI450X/MI455X su Nvidia Vera Rubin (claim aziendale non verificata in modo
# indipendente, fonte borncity.com); un presunto attacco "jailbroken AI
# agent" contro 50+ organizzazioni europee (due versioni incompatibili dei
# fatti — "BabidiGhost" vs "Operation Snowball" — su fonti non verificabili,
# nessuna testata di sicurezza con verifica incrociata le riprende); un nuovo
# modello GPT-5.3-Codex-Spark (risalente in realtà a febbraio 2026, non a
# questa settimana); uno studio Fortune su AI e produttività sviluppatori
# (ripubblicazione dello studio METR di luglio 2025, non una notizia nuova).
# Anche la ricerca dedicata al design (richiesta di Fabio) non ha prodotto
# un trend abbastanza solido e specifico di QUESTA settimana esatta: i
# candidati trovati (Figma Config, Adobe Firefly/Adobe MAX, Canva AI 2.0,
# Runway, Framer) risalgono tutti a settimane o mesi precedenti, e diversi
# pezzi su UX Collective erano opinioni non verificabili su fonte primaria.
# Meglio sei trend solidi che dieci forzati.
#
# Filo conduttore della settimana: con l'AI che diventa infrastruttura
# critica — hardware (Nvidia), fornitori di inferenza (OpenRouter), strumenti
# di lavoro quotidiano (Microsoft/Salesforce) — la domanda che conta di più
# non è più "funziona?" ma "chi risponde quando qualcosa va storto, ed è
# verificabile o solo dichiarato?". Il 12 novembre Nvidia ha perso il suo
# fondatore-CEO da un giorno all'altro, senza successore designato: la
# trimestrale record del 17 novembre non ha rassicurato il mercato. Nella
# stessa settimana un ricercatore di sicurezza ha dimostrato che una clausola
# contrattuale di "zero data retention" può essere semplicemente falsa
# (OpenRouter), Microsoft e Salesforce hanno scelto di integrarsi sul livello
# agentico invece di competere (CopilotForce), e l'Oregon ha trasformato in
# una causa da oltre 2 miliardi di dollari la pressione legale sulla
# sicurezza dei minori su ChatGPT.
trends = [
    dict(
        title="Jensen Huang si dimette da CEO e Presidente di Nvidia con effetto immediato, dopo 33 anni, senza successore designato",
        what="Il 12 novembre Nvidia ha annunciato, con un comunicato ufficiale e un deposito SEC 8-K depositato lo stesso giorno, le dimissioni di Jensen Huang da Presidente, CEO e membro del consiglio, con effetto immediato — dopo 33 anni alla guida dell'azienda che ha fondato nel 1993. Colette Kress, attuale CFO, ha accettato il ruolo di CEO ad interim mantenendo anche la carica di CFO, mentre il consiglio ha nominato Harvey Jones (ex CEO ed Executive Chairman di Synopsys) primo Chairman della storia dell'azienda e ha aperto la ricerca di un successore permanente, valutando candidati interni ed esterni. Né il comunicato né il deposito SEC indicano un motivo per le dimissioni: il board si limita a ringraziare Huang per \"i contributi incommensurabili all'azienda e al settore\". Circolano ricostruzioni di stampa su cause personali della sua uscita, non confermate dalla fonte societaria ufficiale: questo report riporta solo i fatti aziendali verificati.",
        why="Nvidia è il fornitore critico di hardware per quasi ogni iniziativa AI aziendale al mondo, e il suo fondatore-CEO ne era il volto pubblico più riconoscibile: un cambio improvviso e senza preavviso ai vertici di un fornitore così centrale tocca chiunque pianifichi una roadmap che dipende dai suoi chip, non solo gli addetti ai lavori finanziari.",
        source="Nvidia (comunicato ufficiale e deposito SEC 8-K)",
        url="https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition",
    ),
    dict(
        title="Nonostante una trimestrale record, il titolo Nvidia cede il 7% nella settimana: il mercato teme il dopo-Huang",
        what="Il 17 novembre, cinque giorni dopo l'annuncio delle dimissioni di Huang, Nvidia ha riportato i risultati del terzo trimestre dell'anno fiscale 2027: fatturato di 115,8 miliardi di dollari (+103% anno su anno), di cui 107,6 miliardi dalla sola divisione data center, con una guidance per il quarto trimestre di 130 miliardi di dollari. Nonostante numeri da record, il titolo ha perso il 2,9% il 18 novembre — un calo attribuito esplicitamente da più fonti finanziarie alle \"preoccupazioni sulla successione del CEO\" — e ha ceduto complessivamente circa il 7% nella settimana, in un ribasso diffuso che ha coinvolto l'intero comparto dei titoli legati all'AI.",
        why="È la prima prova concreta di quanto pesi, agli occhi degli investitori, il rischio legato a una singola figura chiave anche nell'azienda più centrale dell'intera infrastruttura AI: numeri da record non bastano a rassicurare il mercato quando manca chiarezza sulla guida futura.",
        source="Nvidia (investor relations) / Yahoo Finance",
        url="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2027/default.aspx",
    ),
    dict(
        title="Un ricercatore di sicurezza scopre che tre fornitori di inferenza AI su OpenRouter leggevano i prompt nonostante la clausola \"zero data retention\"",
        what="Il ricercatore di sicurezza HD Moore (creatore di Metasploit, fondatore di runZero) ha inviato circa 2 milioni di prompt contenenti link di tracciamento univoci (\"canary token\") e credenziali finte attraverso provider di inferenza AI disponibili su OpenRouter ed etichettati \"Zero Data Retention\" (ZDR) — la dichiarazione contrattuale secondo cui il fornitore non legge né conserva i dati. Tre provider, tra cui MiniMax, hanno aperto quei link-trappola tra le 40 e le 130 ore dopo l'invio: prova diretta che i prompt venivano effettivamente letti, nonostante l'etichetta. OpenRouter ha rimosso i tre provider dalla piattaforma dopo la segnalazione, pubblicata il 20-21 novembre.",
        why="Tocca una clausola contrattuale che moltissime aziende danno per scontata quando adottano strumenti AI di terze parti, e mostra che un'etichetta di privacy non verificata può essere semplicemente falsa — un problema di fiducia comprensibile anche a chi non è tecnico.",
        source="The Hacker News",
        url="https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html",
    ),
    dict(
        title="Microsoft ridisegna Copilot come \"motore autonomo del lavoro aziendale\" a Ignite 2026",
        what="Il 18 novembre, al keynote di apertura di Microsoft Ignite 2026, Satya Nadella ha presentato una revisione profonda di Microsoft 365 Copilot: non più un assistente conversazionale, ma un livello di orchestrazione che agisce in autonomia sui task aziendali, con agenti sempre attivi integrati più in profondità in Office e Teams, e un'enfasi dichiarata su governance e sicurezza degli agenti.",
        why="Tocca lo strumento Office che la stragrande maggioranza delle aziende italiane usa già ogni giorno: è la stessa battaglia per il \"posto di lavoro quotidiano\" raccontata la settimana scorsa da un altro fornitore, ma questa volta è il fornitore più diffuso nelle PMI italiane a muoversi.",
        source="SiliconANGLE",
        url="https://siliconangle.com/2026/11/18/at-ignite-2026-microsoft-reinvents-copilot-as-the-autonomous-engine-of-enterprise-work/",
    ),
    dict(
        title="Salesforce e Microsoft, storici concorrenti nel software aziendale, si alleano con CopilotForce",
        what="Tra il 17 e il 19 novembre Salesforce e Microsoft hanno annunciato CopilotForce: il contesto clienti e i flussi di vendita del CRM Salesforce entrano direttamente dentro Microsoft Copilot, Teams e Fabric, con decine di funzioni di vendita integrate — alcune già disponibili al pubblico generale, altre ancora in anteprima.",
        why="Due fornitori che per anni si sono contesi lo stesso cliente enterprise scelgono di integrarsi invece di competere sul livello agentico: segnala che nessuno dei due vuole restare escluso dal punto dove, da ora, lavoreranno gli agenti AI aziendali.",
        source="Microsoft (news.microsoft.com/source) / Salesforce",
        url="https://news.microsoft.com/source/2026/11/17/microsoft-and-salesforce-announce-copilotforce-bringing-trusted-customer-context-and-action-into-microsoft-ai-experiences/",
    ),
    dict(
        title="L'Oregon fa causa a OpenAI per oltre 2 miliardi di dollari sulla sicurezza dei minori su ChatGPT",
        what="Il 17 novembre il procuratore generale dell'Oregon, Dan Rayfield, ha intentato una causa da 2,035 miliardi di dollari contro OpenAI, accusando l'azienda di aver messo consapevolmente in pericolo gli utenti minorenni di ChatGPT e di aver fuorviato il pubblico sulle misure di sicurezza adottate. La causa arriva dopo mesi in cui diverse famiglie hanno già fatto causa a OpenAI per episodi di conversazioni dannose con minori, e dopo che l'azienda aveva introdotto controlli parentali in risposta a quei casi precedenti.",
        why="Mostra che la pressione legale e normativa sulla sicurezza dei chatbot conversazionali sta diventando concreta, con cifre e azioni legali misurabili — un tema che tocca la fiducia pubblica nell'AI ben oltre gli addetti ai lavori.",
        source="Oregon Public Broadcasting (OPB), con riscontro su più testate locali indipendenti",
        url="https://www.opb.org/article/2026/11/17/oregon-ag-sues-openai-claims-company-knowingly-endangers-teens/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Nvidia",
        what="Perde il suo fondatore-CEO Jensen Huang con effetto immediato (12/11), senza successore designato; nonostante una trimestrale record (17/11, fatturato +103% anno su anno) il titolo cede circa il 7% nella settimana sulle preoccupazioni di governance.",
        positioning="Fino a oggi Nvidia si era costruita attorno alla figura di un singolo fondatore-visionario, diventato quasi sinonimo del boom AI stesso: ora deve dimostrare, in tempo reale e sotto gli occhi del mercato, che l'azienda è più grande della persona che l'ha guidata per 33 anni.",
        angle="È il caso scuola del rischio legato a una singola figura chiave, applicato a scala enorme: ogni azienda che dipende da un singolo fornitore critico, da una singola figura tecnica interna o da un singolo partner AI dovrebbe chiedersi oggi, non quando la crisi arriva, chi prende le decisioni se quella persona non c'è più — esattamente il lavoro di continuità e governance che il Team Augmentation di Digitiamo aiuta a mettere a terra prima che serva davvero.",
    ),
    dict(
        name="Microsoft",
        what="A Ignite 2026 (18/11) ridisegna Copilot come livello di orchestrazione autonomo per il lavoro aziendale, con agenti sempre attivi dentro Office e Teams, e nella stessa settimana (17-19/11) annuncia con Salesforce l'integrazione CopilotForce.",
        positioning="Si muove su due fronti insieme — rendere Copilot più autonomo e portare dentro al proprio ecosistema il contesto CRM di un concorrente storico — per restare il punto di ingresso unico dove un'azienda gestisce lavoro e dati, invece di competere strumento per strumento.",
        angle="Più un singolo fornitore diventa il \"sistema operativo\" del lavoro quotidiano, più aumenta la posta in gioco di chi decide quali agenti abilitare, con quali permessi e su quali dati — una scelta che richiede competenze specifiche, non la configurazione di default lasciata all'IT da solo: il terreno dell'AI Business Academy, pensata sui casi d'uso reali dell'azienda cliente.",
    ),
    dict(
        name="Salesforce",
        what="Accetta di portare il proprio contesto clienti e i flussi di vendita dentro Microsoft Copilot con CopilotForce (17-19/11), dopo anni passati a competere direttamente con gli strumenti Microsoft sul terreno enterprise.",
        positioning="Sceglie l'interoperabilità con un concorrente storico piuttosto che isolare i propri dati CRM in un ecosistema chiuso, scommettendo che restare presente ovunque lavorino i team vendita valga più del controllo esclusivo sull'interfaccia.",
        angle="Per un'azienda cliente, la domanda pratica diventa chi presidia le regole quando i dati commerciali più sensibili iniziano a fluire anche dentro lo strumento di un altro fornitore — un lavoro di governance dei permessi che il Team Augmentation di Digitiamo porta in azienda prima che la scelta la faccia il reparto IT da solo, in affanno.",
    ),
    dict(
        name="OpenAI",
        what="Affronta una causa da oltre 2 miliardi di dollari dello stato dell'Oregon (17/11) sulla sicurezza dei minori su ChatGPT, nella stessa settimana in cui resta il fornitore AI più citato nelle conversazioni enterprise su agenti e automazione.",
        positioning="Si trova a gestire in parallelo due narrazioni opposte — il fornitore AI più ambizioso sul fronte agentico e di prodotto, e il bersaglio principale della pressione legale e normativa sulla sicurezza dei chatbot conversazionali — un equilibrio che pesa sulla fiducia pubblica nel marchio.",
        angle="Per un'azienda B2B la lezione non riguarda solo la sicurezza dei minori: riguarda quanto in fretta la pressione legale e reputazionale su un fornitore AI possa materializzarsi, e quanto sia prudente non far dipendere i processi critici da un singolo fornitore senza un piano di governance e di controllo esplicito.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana (prima generazione, 23/11/2026): lunedì il quadro
# d'insieme parte dalla notizia più grande e trasversale — le dimissioni di
# Jensen Huang da Nvidia e la reazione del mercato nonostante la trimestrale
# record — inquadrata come caso di rischio legato a una singola figura
# chiave, senza vendita. Martedì e mercoledì due miti da sfatare, entrambi
# sul tema "una dichiarazione di sicurezza/conformità non equivale a una
# garanzia verificata": il caso OpenRouter (clausola "zero data retention"
# non rispettata) e il caso Oregon/OpenAI (guardrail dichiarati non bastano
# a prevenire la causa). Giovedì l'esperienza diretta riprende il filo di
# martedì: la rilettura dei contratti dei fornitori AI del team. Venerdì la
# mini-lezione spiega il meccanismo tecnico dietro la scoperta di martedì
# (il "canary token"), chiudendo l'arco sicurezza/fiducia. Le due riserve
# restano banca contenuti: un carosello dati sui numeri della trimestrale
# Nvidia (l'unico trend della settimana con densità di cifre sufficiente per
# un carosello — nessun secondo candidato da promuovere a Prioritario questa
# settimana), e la riflessione di chiusura.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 23/11",
        format="Thought leadership — apertura settimana",
        title="Jensen Huang lascia Nvidia da un giorno all'altro, senza successore: il rischio legato a una singola figura chiave diventa reale su scala mondiale",
        titolo_post="Nvidia perde il suo fondatore-CEO",
        sottotitolo_post="Jensen Huang si dimette da CEO con effetto immediato, senza un successore designato.",
        news="Nvidia annuncia le dimissioni immediate di Jensen Huang da CEO, senza successore designato (12/11)",
        news_url="https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition",
        hook="Questa settimana il fornitore più centrale dell'intero boom AI ha perso, da un giorno all'altro, l'unico CEO che abbia mai avuto: il 12 novembre Nvidia ha annunciato le dimissioni con effetto immediato di Jensen Huang da Presidente e CEO, dopo 33 anni alla guida dell'azienda che ha fondato nel 1993. Il consiglio non ha fornito alcuna motivazione ufficiale, ha nominato ad interim l'attuale CFO Colette Kress e ha aperto la ricerca di un successore permanente. Cinque giorni dopo, il 17 novembre, Nvidia ha riportato una trimestrale da record — ma il titolo ha comunque ceduto, per l'incertezza sulla governance futura.",
        visual_hook="Il fornitore più centrale del boom AI perde il suo unico CEO da un giorno all'altro, senza successore designato: anche una trimestrale record non basta a rassicurare il mercato.",
        points=[
            "Il 12 novembre Nvidia ha annunciato le dimissioni immediate di Jensen Huang da Presidente e CEO, dopo 33 anni alla guida dell'azienda: nessuna motivazione ufficiale, Colette Kress (CFO) nominata CEO ad interim, ricerca aperta per un successore permanente.",
            "Il 17 novembre Nvidia ha riportato un fatturato trimestrale di 115,8 miliardi di dollari (+103% anno su anno) — ma il titolo ha comunque perso circa il 7% nella settimana, un calo attribuito esplicitamente alle preoccupazioni sulla successione.",
            "È il caso scuola del rischio legato a una singola figura chiave, su scala enorme: numeri da record non bastano se manca chiarezza su chi guida l'azienda da cui dipende la roadmap hardware di quasi ogni progetto AI al mondo.",
        ],
        punti_post=[
            "Nvidia: dimissioni immediate di Jensen Huang, nessun successore.",
            "Trimestrale record (+103%), ma titolo giù 7% nella settimana.",
            "Il rischio chiave-persona, applicato alla scala più grande.",
        ],
        cta="La tua azienda ha un piano esplicito per il giorno in cui una figura chiave — interna o di un fornitore critico — non c'è più? 👇",
        hashtags="#Nvidia #IntelligenzaArtificiale #Leadership #Governance #B2B",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 24/11",
        format="Mito da sfatare",
        title="Il fornitore dichiara \"zero data retention\" sui tuoi prompt aziendali. Quindi i tuoi dati sono al sicuro",
        titolo_post="I tuoi prompt sono al sicuro",
        sottotitolo_post="OpenRouter ha rimosso 3 fornitori che leggevano i prompt nonostante la clausola zero data retention.",
        barrato="sicuro",
        news="OpenRouter rimuove 3 fornitori di inferenza AI dopo la scoperta di furto di prompt nonostante l'etichetta ZDR (20-21/11)",
        news_url="https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html",
        hook="🔥 Il mito: se un fornitore AI dichiara contrattualmente \"zero data retention\" sui tuoi prompt, puoi fidarti e non c'è altro da controllare — è una clausola, non una promessa che va verificata nei fatti.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="Un ricercatore di sicurezza ha inviato 2 milioni di prompt con link-trappola attraverso provider etichettati \"zero data retention\": tre di loro li hanno aperti, anche giorni dopo.",
        myth_body="Il ricercatore di sicurezza HD Moore ha inviato circa 2 milioni di prompt contenenti link di tracciamento univoci e credenziali finte attraverso provider di inferenza AI su OpenRouter etichettati \"Zero Data Retention\" (ZDR) — la dichiarazione contrattuale che il fornitore non legge né conserva i dati. Tre provider, tra cui MiniMax, hanno aperto quei link-trappola tra le 40 e le 130 ore dopo l'invio: prova diretta che i prompt venivano letti, nonostante l'etichetta. OpenRouter li ha rimossi dalla piattaforma dopo la segnalazione.",
        points=[
            "Il test: circa 2 milioni di prompt con link-trappola e credenziali finte, inviati attraverso provider etichettati \"zero data retention\".",
            "Tre provider, tra cui MiniMax, hanno aperto quei link tra le 40 e le 130 ore dopo l'invio — prova che i prompt venivano letti nonostante la clausola.",
            "OpenRouter ha rimosso i tre provider dopo la segnalazione: l'etichetta da sola non bastava a garantire quello che prometteva.",
        ],
        punti_post=[
            "2 milioni di prompt-trappola inviati a provider \"zero retention\".",
            "3 provider li hanno aperti: la clausola non reggeva nei fatti.",
            "OpenRouter li ha rimossi dopo la scoperta.",
        ],
        myth_closing="Il problema non è se il tuo fornitore AI abbia scritto \"zero data retention\" nel contratto — è che nessuno l'aveva verificato finché un ricercatore indipendente non ha inviato prompt-trappola per controllare. Una clausola di privacy non testata è un'ipotesi, non una garanzia.",
        cta="La tua azienda ha mai verificato nei fatti, non solo nel contratto, come un fornitore AI tratta i tuoi prompt? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 25/11",
        format="Mito da sfatare",
        title="Un chatbot con guardrail di sicurezza dichiarati ha reso le conversazioni con gli utenti più vulnerabili un problema sotto controllo",
        titolo_post="Guardrail non vuol dire controllo",
        sottotitolo_post="L'Oregon fa causa a OpenAI per oltre 2 miliardi di dollari sulla sicurezza dei minori su ChatGPT.",
        barrato="controllo",
        news="L'Oregon intenta una causa da 2,035 miliardi di dollari contro OpenAI sulla sicurezza dei minori su ChatGPT (17/11)",
        news_url="https://www.opb.org/article/2026/11/17/oregon-ag-sues-openai-claims-company-knowingly-endangers-teens/",
        hook="🔥 Il mito: una volta che un chatbot ha dei guardrail di sicurezza dichiarati e dei controlli parentali, il rischio per gli utenti più vulnerabili è gestito — il resto è responsabilità di chi lo usa.",
        no_hashtags=True,
        is_myth=True,
        visual_hook="Il procuratore generale dell'Oregon accusa OpenAI di aver messo in pericolo consapevolmente gli utenti minorenni di ChatGPT, nonostante le misure di sicurezza dichiarate pubblicamente.",
        myth_body="Il 17 novembre il procuratore generale dell'Oregon, Dan Rayfield, ha intentato una causa da 2,035 miliardi di dollari contro OpenAI, accusando l'azienda di aver messo consapevolmente in pericolo gli utenti minorenni di ChatGPT e di aver fuorviato il pubblico sulle misure di sicurezza adottate. La causa arriva dopo mesi in cui diverse famiglie hanno già fatto causa a OpenAI per episodi di conversazioni dannose con minori, e dopo che l'azienda aveva introdotto controlli parentali in risposta a quei casi precedenti.",
        points=[
            "Il procuratore generale dell'Oregon chiede oltre 2 miliardi di dollari, accusando OpenAI di aver saputo dei rischi per i minori e di non aver agito abbastanza in fretta.",
            "La causa arriva dopo mesi di azioni legali simili da parte di famiglie, e dopo che OpenAI aveva già introdotto controlli parentali in risposta a episodi precedenti.",
            "Avere delle misure di sicurezza dichiarate non ha impedito che la pressione legale si materializzasse comunque, con una cifra e un'accusa specifiche.",
        ],
        punti_post=[
            "Oregon: causa da oltre 2 miliardi di dollari contro OpenAI.",
            "Accusa: pericolo noto per i minori, misure insufficienti.",
            "Arriva dopo mesi di cause simili e controlli già introdotti.",
        ],
        myth_closing="Dichiarare dei guardrail non equivale a dimostrare che bastano: la differenza, per chi li costruisce come per chi li usa, è quanto spesso vengono messi davvero alla prova — non solo annunciati.",
        cta="La tua azienda tratta le misure di sicurezza AI come una casella da spuntare, o come qualcosa da verificare nel tempo? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 26/11",
        format="Esperienza diretta",
        title="Dopo il caso OpenRouter, abbiamo riletto i contratti dei fornitori AI che usiamo per capire cosa dicono davvero sulla conservazione dei dati",
        titolo_post="Contratti AI: li abbiamo *riletti*",
        sottotitolo_post="Dopo il caso OpenRouter, abbiamo riletto le clausole di conservazione dati dei fornitori AI che usiamo.",
        news="Spunto dal caso OpenRouter: tre fornitori leggevano i prompt nonostante la clausola \"zero data retention\" (20-21/11)",
        news_url="https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html",
        hook="Dopo la notizia di questa settimana — un ricercatore ha scoperto che alcuni fornitori di inferenza AI leggevano i prompt nonostante una clausola contrattuale di \"zero data retention\" — ci siamo fatti la domanda scomoda: sappiamo davvero cosa dicono, nel dettaglio, i contratti dei fornitori AI che usiamo ogni giorno? Questa settimana li abbiamo riletti.",
        is_template=True,
        points=[
            "Abbiamo elencato tutti i fornitori AI terzi che il team usa (modelli, provider di inferenza, estensioni), e per ciascuno recuperato la clausola esatta su conservazione e uso dei dati, non solo il riassunto commerciale.",
            "[Da personalizzare con l'esito reale della verifica del team: quali clausole erano più vaghe del previsto, quali fornitori avete deciso di verificare più a fondo o sostituire, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi o esiti non verificati.]",
            "La domanda utile non è se i contratti esistano — di norma esistono — ma se qualcuno in azienda li rilegge davvero, periodicamente, invece di darli per scontati dopo la firma.",
        ],
        punti_post=[
            "Abbiamo riletto i contratti dei fornitori AI del team.",
            "[Da personalizzare con l'esito reale della verifica.]",
            "La vera domanda: qualcuno li rilegge dopo la firma?",
        ],
        cta="La tua azienda rilegge periodicamente le clausole sui dati dei fornitori AI che usa, o solo alla firma del contratto? Raccontaci 👇",
        hashtags="#IntelligenzaArtificiale #DataPrivacy #Esperienza #B2B #AIBusiness",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 27/11",
        format="Divulgativo stile Datapizza",
        title="Cos'è un \"canary token\" (link-trappola): lo strumento che ha smascherato chi non rispettava la promessa \"zero data retention\"",
        titolo_post="Cos'è un \"canary token\"",
        sottotitolo_post="Il link-trappola che ha svelato chi leggeva i prompt nonostante la promessa di non farlo.",
        news="Spunto dal caso OpenRouter (vedi post di martedì): il canary token che ha smascherato 3 provider (20-21/11)",
        news_url="https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html",
        hook="Martedì abbiamo raccontato di tre fornitori AI che leggevano i prompt nonostante una clausola di \"zero data retention\". Ma come si fa, in pratica, a scoprire che qualcuno sta leggendo dati che ha promesso di non guardare? La risposta di questa settimana: un \"canary token\".",
        points=[
            "Un canary token è un link o una credenziale finta, unica per ogni destinatario, inserita in un documento o in un messaggio: se qualcuno la apre o la usa, lo sai — perché nessun altro aveva motivo di farlo.",
            "Il ricercatore che ha scoperto il caso OpenRouter ha inserito link-canarino in circa 2 milioni di prompt inviati a provider che dichiaravano di non leggere i dati: quando tre di quei link sono stati aperti, ore o giorni dopo, la prova era inconfutabile.",
            "La stessa logica si può applicare a qualunque flusso di dati aziendali che passa per terzi — fornitori cloud, partner, agenti AI con accesso a documenti — per verificare, non solo per fidarsi, chi accede davvero a cosa.",
        ],
        punti_post=[
            "Canary token: un link-trappola unico per destinatario.",
            "2 milioni inviati, 3 aperti: la prova che i dati erano letti.",
            "La stessa logica vale per qualunque fornitore terzo con accesso ai tuoi dati.",
        ],
        cta="Conoscevi già questa tecnica per verificare chi accede davvero ai tuoi dati? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇",
        hashtags="#AI #TechExplained #Cybersecurity #B2B #Innovazione",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati",
        title="Dentro la trimestrale record di Nvidia, arrivata nel pieno della crisi di leadership: i numeri di una settimana turbolenta",
        titolo_post="Agenti AI al lavoro: i numeri di Nvidia",
        sottotitolo_post="Trimestrale record, cinque giorni dopo le dimissioni del fondatore-CEO: i numeri di una settimana turbolenta.",
        closing_title="Chi guida l'azienda quando il titolo non si fida?",
        closing_body="I numeri dicono che la domanda di chip AI non rallenta. Il mercato dice che la domanda sulla governance pesa comunque.",
        news="Nvidia riporta una trimestrale record il 17/11, cinque giorni dopo le dimissioni di Jensen Huang; il titolo cede il 7% nella settimana",
        news_url="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2027/default.aspx",
        hook="Il 17 novembre, cinque giorni dopo l'uscita di scena improvvisa di Jensen Huang, Nvidia ha riportato la trimestrale più alta della sua storia. Il mercato, però, ha reagito al contrario di quello che i numeri avrebbero fatto pensare.",
        points=[
            "115,8 miliardi di dollari — il fatturato del terzo trimestre fiscale 2027, in crescita del 103% anno su anno.",
            "107,6 miliardi — la quota di quel fatturato arrivata dalla sola divisione data center.",
            "130 miliardi — la guidance di fatturato che Nvidia indica per il quarto trimestre.",
            "2,9% — il calo del titolo Nvidia il 18 novembre, il giorno dopo la trimestrale, attribuito alle preoccupazioni sulla successione del CEO.",
            "7% — il calo complessivo del titolo nella settimana, in un ribasso che ha coinvolto l'intero comparto dei titoli AI.",
        ],
        punti_post=[
            "115,8 mld $ — fatturato Q3 (+103% anno su anno).",
            "107,6 mld $ — solo dalla divisione data center.",
            "130 mld $ — guidance per il quarto trimestre.",
            "-2,9% — il titolo il giorno dopo la trimestrale.",
            "-7% — calo complessivo nella settimana.",
        ],
        closing="I numeri della trimestrale dicono che la domanda di infrastruttura AI non si è fermata. Il comportamento del titolo, nella stessa settimana, dice che gli investitori stanno valutando qualcos'altro: chi guiderà l'azienda da cui dipende buona parte dell'infrastruttura AI mondiale, e quando lo sapremo.",
        cta="La tua azienda valuta anche il rischio di governance dei fornitori critici, non solo i loro numeri trimestrali? 👇",
        hashtags="#Nvidia #AI #Mercati #Infrastruttura #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice su governance, fiducia e AI (e su chi decide quando qualcosa va storto)",
        news="Sintesi dei trend della settimana 16-23 novembre 2026",
        news_url="https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie degli ultimi giorni.",
        points=[
            "Nvidia ha perso il suo fondatore-CEO da un giorno all'altro, senza successore designato: anche un'azienda da trimestrali record non è immune al rischio legato a una singola figura chiave.",
            "OpenRouter ha scoperto che tre fornitori di inferenza AI leggevano i prompt nonostante una clausola di \"zero data retention\": una promessa contrattuale non verificata può semplicemente essere falsa.",
            "Microsoft ha ridisegnato Copilot come motore autonomo del lavoro a Ignite 2026, e nella stessa settimana ha integrato il CRM di Salesforce — due storici concorrenti che scelgono di integrarsi sul livello agentico.",
            "L'Oregon ha fatto causa a OpenAI per oltre 2 miliardi di dollari sulla sicurezza dei minori su ChatGPT, dopo mesi di cause simili: la pressione legale sui chatbot conversazionali si sta materializzando in cifre concrete.",
            "Il filo comune: man mano che l'AI diventa infrastruttura critica — hardware, fornitori, strumenti di lavoro — la domanda che conta di più non è più \"funziona?\" ma \"chi risponde quando qualcosa va storto, ed è verificabile o solo dichiarato?\".",
        ],
        closing="Una settimana che, da angolazioni diverse, ha raccontato la stessa domanda: con l'AI che diventa infrastruttura su cui si costruisce — chip, fornitori di inferenza, strumenti di lavoro quotidiano — la fiducia dichiarata conta sempre meno di quella verificabile.",
        cta="Qual è la notizia di questa settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #Governance #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 23/11",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 24/11",
        time="12:15",
        format="Mito da sfatare (\"zero data retention\" non garantita — caso OpenRouter)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — apre il filo fiducia/verifica che attraversa il resto della settimana.",
    ),
    dict(
        day="Mercoledì 25/11",
        time="08:30",
        format="Mito da sfatare (guardrail dichiarati non bastano — causa Oregon/OpenAI)",
        reason="Finestra mattutina, per dare risalto a un tema delicato (sicurezza dei minori) in un momento di lettura più attenta rispetto alla pausa pranzo; varia l'orario rispetto al mito di martedì per non ripetere lo stesso slot due giorni di fila.",
    ),
    dict(
        day="Giovedì 26/11",
        time="08:00",
        format="Esperienza diretta (rilettura dei contratti dei fornitori AI del team)",
        reason="Segue narrativamente il mito di martedì, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 27/11",
        time="12:15",
        format="Divulgativo (Datapizza style — cos'è un canary token)",
        reason="Pausa pranzo di chiusura settimana, quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale, chiude l'arco narrativo su fiducia e verifica aperto martedì.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Carosello numeri sulla trimestrale Nvidia",
        reason="Banca contenuti: unico trend della settimana con densità di cifre sufficiente per un carosello — utile se la settimana ha margine per un sesto post, o come approfondimento la settimana successiva se la vicenda Nvidia evolve.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
]
