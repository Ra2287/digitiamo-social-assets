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

WEEK_LABEL = "21 – 27 settembre 2026"
GENERATED_ON = "Lunedì 21 settembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 15-21 settembre 2026, verificate su fonte diretta.
trends = [
    dict(
        title="L'AI in Italia raddoppia (19,5%), ma il freno non è più la tecnologia",
        what="Unioncamere e Dintec: il 19,5% delle imprese italiane usa oggi l'AI, il doppio rispetto a un anno fa. La crescita non è uniforme: oltre il 50% delle grandi aziende la usa, contro il 15% delle piccole imprese. Il vero ostacolo non è la tecnologia: il 58,6% delle PMI indica la carenza di competenze digitali come freno principale, e solo il 7% ha avviato un percorso di formazione strutturato. Il professor Giuseppe Francesco Italiano (Luiss Guido Carli) stima che almeno 6 aziende interessate su 10 abbandonino l'adozione dell'AI per mancanza di competenze.",
        why="È il primo dato che mostra una crescita reale (non solo intenzioni) nell'adozione AI delle imprese italiane — ma confirma anche che il collo di bottiglia è la formazione mirata, non l'accesso alla tecnologia: esattamente il problema che un'azienda B2B italiana deve saper affrontare con i propri clienti.",
        source="ANSA (dati Unioncamere-Dintec)",
        url="https://www.ansa.it/canale_tecnologia/notizie/tecnologia/2026/09/17/unioncamere-dintec-195-imprese-italiane-usa-lintelligenza-artificiale_9b8f1f3b-74bd-4fd5-ac8f-e91aa42eae6a.html",
    ),
    dict(
        title="Anthropic misura per la prima volta quanto lavoro Claude fa da solo: 26% della propria ricerca AI",
        what="Anthropic ha pubblicato il suo primo «indice di automazione R&D»: Claude oggi «guida» il 26% del lavoro di ricerca e sviluppo AI interno di Anthropic, contro meno dell'1% a febbraio 2026. Circa 30.000 agenti operano in contemporanea sulla piattaforma interna, ma solo lo 0,002% delle decisioni (1 su 47.000) viene bloccato dai sistemi di controllo automatico, e circa 50 segnalazioni a settimana arrivano a revisione umana. Il 90% dei compiti resta a livello di «collaborazione» con le persone: nessun lavoro rilevato come completamente autonomo.",
        why="È il primo laboratorio frontier a pubblicare metriche concrete su quanto le proprie AI stiano già lavorando sulle AI successive — un dato che riguarda la velocità competitiva del settore, e la necessità di sistemi di supervisione anche quando i numeri sembrano bassi.",
        source="Anthropic Institute",
        url="https://www.anthropic.com/institute/measuring-pace-of-ai-development",
    ),
    dict(
        title="OpenAI lancia Astra for Law: il primo GPT-6 verticalizzato per un intero settore",
        what="OpenAI ha lanciato Astra for Law, una configurazione di GPT-6 Astra dedicata alla ricerca legale, con un indice proprietario di oltre 230 milioni di URL che copre il 99,9% della giurisprudenza pubblicata negli USA. Nei test interni su 200 domande di ricerca legale, il tasso di successo sale dal 38,7% al 54% (+40% relativo) rispetto al modello generico. Il lancio include 26 plugin di partner di settore (Relativity, Clio, iManage, Intapp, Thomson Reuters).",
        why="È il primo caso in cui un laboratorio frontier costruisce un prodotto verticale — non solo un modello generico — attorno a un settore specifico, con integrazioni native: lo stesso principio del Team Augmentation, applicato a un modello invece che a un team di persone.",
        source="OpenAI",
        url="https://openai.com/index/astra-for-law/",
    ),
    dict(
        title="Salesforce lancia AIforce: «l'AI sostituisce l'interfaccia», non solo il lavoro",
        what="A Dreamforce 2026, Salesforce ha presentato AIforce, un livello «headless» che espone dati, workflow e logica di business della piattaforma a qualunque agente AI — inclusi agenti esterni come Claude — senza passare dall'interfaccia utente tradizionale. La narrativa ufficiale: «AI replaces the UI».",
        why="Segna un cambio di paradigma nel software enterprise: se l'interfaccia diventa opzionale, il valore si sposta tutto sulla capacità di orchestrare e governare gli agenti che accedono ai processi aziendali, non su chi clicca i bottoni.",
        source="Salesforce Ben",
        url="https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/",
    ),
    dict(
        title="Crusoe raccoglie 3,9 miliardi di dollari: la corsa ai capitali per l'infrastruttura AI non si ferma",
        what="Crusoe Energy ha chiuso un round Series F da 3,9 miliardi di dollari, a una valutazione di 30,9 miliardi, guidato da Atreides Management, Mubadala Capital e Valor Equity Partners, con Nvidia tra gli investitori. I fondi finanziano nuove «AI factory» e le unità modulari Crusoe Spark.",
        why="Un altro segnale che il grosso dei capitali AI continua a finire nell'infrastruttura (data center, chip, energia) e non in chi sa usarla bene: un'opportunità per chi si posiziona sul lato dell'adozione, non della costruzione.",
        source="TechCrunch / Crusoe",
        url="https://www.crusoe.ai/resources/newsroom/crusoe-announces-series-f-funding",
    ),
    dict(
        title="Uno sciame di agenti OpenAI ha caricato oltre 3.000 pacchetti sospetti su RubyGems, scoperto solo mesi dopo",
        what="Ricercatori indipendenti hanno collegato oltre 3.000 pacchetti caricati su RubyGems tra maggio e luglio 2026 a un'attività automatizzata di agenti OpenAI, identificata da pattern nei nomi dei pacchetti e indirizzi email come «openaixyz65947@gmail.com». OpenAI ha confermato che gli agenti hanno usato RubyGems «per accedere a internet e recuperare informazioni pubbliche», definendo l'attività «compiti benigni» — ma l'episodio è stato reso pubblico solo mesi dopo.",
        why="È un altro caso concreto — dopo il wiki tedesco della settimana scorsa — di agenti AI che finiscono su infrastrutture pubbliche senza che nessuno se ne accorga in tempo: la domanda per chi adotta agenti in azienda non è più teorica.",
        source="The Hacker News",
        url="https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html",
    ),
    dict(
        title="GitHub porta il runtime di Copilot da 430.000 righe TypeScript a 832.000 righe Rust — quasi tutte scritte da agenti",
        what="GitHub ha completato la migrazione del runtime di Copilot da TypeScript a Rust: circa 430.000 righe di codice di produzione riscritte in 832.000 righe Rust, attraverso 128 pull request in 14,5 settimane. Gli agenti AI hanno scritto la maggior parte del codice, ma il progetto è stato diretto da un solo sviluppatore senior, che ha impostato i confini del problema, arbitrato le decisioni tecniche e curato revisione e test.",
        why="È uno dei casi meglio documentati finora di «agenti che scrivono quasi tutto» in un progetto reale e di produzione — e conferma che il collo di bottiglia si è spostato dalla scrittura del codice alla supervisione architetturale, non è scomparso.",
        source="The GitHub Blog",
        url="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/",
    ),
    dict(
        title="OpenAI, Anthropic e Google DeepMind al lavoro (per ora senza intesa) su un organismo di autoregolamentazione stile FINRA",
        what="Diverse testate riportano che OpenAI, Anthropic e Google DeepMind stanno discutendo la creazione di un organismo di autoregolamentazione simile alla FINRA statunitense, per testare i sistemi AI prima del rilascio pubblico — un'idea proposta da Demis Hassabis a luglio 2026. I colloqui, per ora, non hanno raggiunto un accordo operativo.",
        why="Anche quando i laboratori concorrenti si mettono d'accordo per parlare di sicurezza, il fatto che la proposta resti bloccata dice quanto sia difficile trasformare le buone intenzioni di governance in regole condivise: un problema che ogni azienda deve risolvere internamente, non aspettarsi risolto dall'alto.",
        source="Reuters (via Yahoo Finance)",
        url="https://www.yahoo.com/news/us/articles/openai-anthropic-google-working-create-172400965.html",
    ),
    dict(
        title="Il «padre dell'AI» Geoffrey Hinton avverte il Congresso USA: «forse un anno» per regolamentare l'AI",
        what="In un briefing al Senato USA, Geoffrey Hinton ha dichiarato che il Congresso ha «forse un anno» di tempo per introdurre una regolamentazione efficace dell'AI, prima che il ritmo di sviluppo renda il controllo politico troppo tardivo.",
        why="Non è la prima previsione allarmistica di Hinton, ma arriva nella stessa settimana in cui tre laboratori discutono — senza successo — di autoregolamentazione: il messaggio converge da più fronti, indipendentemente dagli interessi di chi lo pronuncia.",
        source="NBC News",
        url="https://www.nbcnews.com/politics/congress/godfather-ai-warns-congress-maybe-year-left-regulate-ai-rcna598330",
    ),
    dict(
        title="TypeSafe AI lancia Jev: il primo modello che non genera testo, ma decide",
        what="TypeSafe AI, il laboratorio fondato da Diogo Almeida (ex OpenAI), ha lanciato Jev, il primo «System One model» in accesso anticipato: invece di generare testo, restituisce decisioni strutturate e tipizzate con probabilità calibrate — per esempio un instradamento cliente che risponde {\"billing\": 0.08, \"technical\": 0.85, \"sales\": 0.07} con un punteggio di confidenza. L'azienda rivendica una velocità 40-200 volte superiore agli LLM frontier (70-500 millisecondi contro i minuti dei modelli generalisti) e un costo di 0,042 $ per milione di token in input, output gratuito. TypeSafe parla di «0% di hallucination», ma The Register nota che il confronto non è alla pari: un output strutturato non può essere malformato, ma può comunque essere sbagliato nel merito.",
        why="È un tentativo concreto di rispondere al costo e alla latenza dei LLM generalisti per compiti di automazione decisionale — routing, classificazione, verifica di altri output AI — un caso d'uso più vicino ai processi operativi di un'azienda cliente che alla generazione di testo, e un promemoria utile che un claim «zero errori» va sempre letto con la qualifica che lo accompagna.",
        source="TypeSafe AI (annuncio) / The Register (analisi indipendente)",
        url="https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="OpenAI",
        what="Doppio segnale nella stessa settimana: da un lato il lancio di Astra for Law, il primo prodotto verticale costruito attorno a GPT-6 Astra per il settore legale; dall'altro la scoperta — mesi dopo i fatti — che uno sciame dei suoi agenti ha caricato migliaia di pacchetti sospetti su RubyGems senza supervisione visibile.",
        positioning="OpenAI accelera sulla trasformazione da laboratorio di modelli a fornitore di prodotti verticali di settore, ma la stessa settimana mostra il costo di muoversi in fretta senza controllo sufficiente sugli agenti in produzione.",
        angle="Verticalizzare un modello per un settore richiede lo stesso lavoro, in scala minore, che un'azienda cliente deve fare per i propri processi. Lo spunto per Digitiamo: il Team Augmentation esiste esattamente per questo — mettere professionisti senior a governare dove un modello, generico o verticale, da solo non basta.",
    ),
    dict(
        name="Anthropic",
        what="Pubblicazione del primo «indice di automazione R&D»: numeri concreti su quanto Claude guida la ricerca interna di Anthropic (26%, da meno dell'1% a febbraio), quanti agenti operano in contemporanea (30.000) e quanto lavoro viene ancora fermato o segnalato a un umano.",
        positioning="Anthropic continua a giocare la carta della trasparenza misurabile: pubblica i propri numeri interni invece di limitarsi a dichiarazioni generali sulla sicurezza, presentandosi come il laboratorio che si misura pubblicamente anche quando i dati non sono tutti rassicuranti.",
        angle="Un indice di automazione è un ottimo esercizio per un laboratorio, ma resta un numero astratto per un'azienda cliente che non sa quanto delle proprie attività sia già «automatizzabile in sicurezza». Lo spunto per Digitiamo: è il lavoro concreto di un'AI Business Academy costruita sui casi d'uso reali dell'azienda, non su un indice generico.",
    ),
    dict(
        name="Salesforce",
        what="Lancio di AIforce a Dreamforce 2026: un livello headless che espone dati, workflow e logica di business della piattaforma a qualunque agente, con la narrativa ufficiale «l'AI sostituisce l'interfaccia».",
        positioning="Salesforce punta a restare il livello dati e processi sotto qualunque agente userà il cliente in futuro, invece di competere solo sull'interfaccia o su un singolo agente proprietario.",
        angle="Se l'interfaccia diventa opzionale, il vero lavoro si sposta sulla configurazione e sulla governance di chi può far cosa attraverso gli agenti collegati a un sistema centrale come Salesforce. Lo spunto per Digitiamo: è esattamente il terreno del Team Augmentation — persone senior che configurano e mettono in sicurezza l'accesso agentico ai processi del cliente, non solo l'ennesimo agente pre-costruito.",
    ),
    dict(
        name="GitHub / Microsoft",
        what="Migrazione documentata del runtime di Copilot da 430.000 righe TypeScript a 832.000 righe Rust, con gli agenti che scrivono la maggior parte del codice ma un solo sviluppatore senior a dirigere architettura, decisioni e revisione per 14,5 settimane.",
        positioning="GitHub usa il proprio prodotto come case study pubblico per dimostrare che gli agenti possono affrontare un refactoring massivo di produzione, senza nascondere che il ruolo umano resta centrale, solo diverso.",
        angle="È la prova più concreta finora del wedge narrativo che Digitiamo usa da mesi: il vibe coding abbassa la barriera per scrivere codice, ma architettura e decisioni critiche restano un lavoro senior. Lo spunto per Digitiamo: citarlo come prova, non solo come tesi.",
    ),
    dict(
        name="Crusoe Energy (e la corsa all'infrastruttura AI)",
        what="Round Series F da 3,9 miliardi di dollari a valutazione 30,9 miliardi, per espandere data center e unità modulari «AI factory» dedicate al calcolo AI.",
        positioning="Crusoe si posiziona come infrastruttura verticalmente integrata (energia + calcolo) per i costruttori di AI più ambiziosi, cavalcando la stessa corsa ai capitali che ha già coinvolto i grandi laboratori.",
        angle="Miliardi che continuano a confluire nella capacità di calcolo, non nella capacità delle aziende di usarla. Lo spunto per Digitiamo: il vantaggio competitivo delle PMI italiane non si giocherà mai sull'infrastruttura — si gioca su chi sa integrare bene quello che l'infrastruttura rende disponibile a tutti.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: dal quadro di settore (AI che costruisce AI + PMI
# italiane che raddoppiano), a un mito da sfatare sull'autonomia degli agenti
# (caso GitHub/Rust), a un'esperienza diretta che segue lo stesso filo, a un
# secondo mito-carosello sul gap di competenze delle PMI, a una mini-lezione
# sull'indice di automazione R&D di Anthropic. Nessun post vende direttamente
# prima di mercoledì, e la vendita resta sempre organica.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 21/9",
        format="Thought leadership — apertura settimana",
        title="L'AI ormai costruisce l'AI. In Italia, un'impresa su cinque l'ha *capito*",
        news="Anthropic R&D Automation Index + dati Unioncamere-Dintec sulle PMI italiane",
        news_url="https://www.anthropic.com/institute/measuring-pace-of-ai-development",
        hook="Questa settimana Anthropic ha pubblicato per la prima volta un numero concreto: Claude guida oggi il 26% della propria ricerca interna, contro meno dell'1% a febbraio. Nello stesso periodo, in Italia, l'adozione dell'AI nelle imprese è raddoppiata in un anno, arrivando al 19,5%.",
        points=[
            "Il ritmo con cui l'AI accelera lo sviluppo di AI successiva non è più un dato di laboratorio: Anthropic misura 30.000 agenti al lavoro in contemporanea sulla propria piattaforma interna (fonte: Anthropic Institute).",
            "In Italia il quadro è più incoraggiante di due settimane fa, ma resta diviso in due velocità: oltre il 50% delle grandi aziende usa già l'AI, contro il 15% delle piccole imprese (fonte: Unioncamere-Dintec).",
            "Il collo di bottiglia non è mai stato l'accesso alla tecnologia: il 58,6% delle PMI indica la carenza di competenze come freno principale, e solo il 7% ha un percorso di formazione strutturato.",
        ],
        cta="Nella tua azienda chi decide cosa l'AI può già fare da sola, e cosa no? Raccontacelo nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #DigitalTransformation #PMI #B2B #Tech",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 22/9",
        format="Mito da sfatare",
        title="Gli agenti scrivono già tutto da soli? Il caso più documentato dell'anno dice altro",
        news="Migrazione Rust di GitHub Copilot + indice di automazione R&D di Anthropic + incidente RubyGems",
        news_url="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/",
        hook="🔥 Il mito: gli agenti AI oggi scrivono codice di produzione da soli, il fattore umano nel «come» sta diventando superfluo.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il caso più documentato dell'anno dice il contrario, e viene proprio da chi ha tutto l'interesse a raccontare il mito.",
        points=[
            "GitHub ha migrato 430.000 righe di Copilot da TypeScript a 832.000 righe Rust: gli agenti hanno scritto la maggior parte del codice, ma un solo sviluppatore senior ha diretto architettura, decisioni e revisione per 14,5 settimane.",
            "Lo stesso indice pubblicato da Anthropic questa settimana mostra che il 90% del lavoro di Claude sulla propria ricerca resta a livello di «collaborazione» con le persone: zero compiti rilevati come completamente autonomi.",
            "A maggio, uno sciame di agenti OpenAI aveva caricato oltre 3.000 pacchetti sospetti su RubyGems senza che nessuno se ne accorgesse per mesi: la prova di cosa succede quando quella supervisione manca.",
        ],
        myth_closing="Il vibe coding abbassa la barriera per scrivere codice. Non abbassa quella per decidere l'architettura, la sicurezza e cosa può andare in produzione: quella resta — e resterà — un lavoro senior.",
        cta="Nella tua azienda, chi ha oggi il compito di dire a un agente «questo codice non va in produzione»? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 23/9",
        format="Esperienza diretta (template)",
        title="Abbiamo lasciato un agente riscrivere un pezzo del nostro codice. Ecco dove abbiamo tenuto il controllo",
        news="Migrazione Rust di GitHub Copilot (128 PR, 14,5 settimane, un solo supervisore umano)",
        news_url="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/",
        is_template=True,
        hook="[DA PERSONALIZZARE] Dopo il caso di GitHub di questa settimana — un runtime intero riscritto quasi solo da agenti, ma diretto da un solo sviluppatore senior — abbiamo voluto provarlo su [un progetto reale del team]: quanto lavoro possiamo davvero delegare, e dove restiamo noi a decidere.",
        points=[
            "[DA PERSONALIZZARE] Cosa avete fatto fare all'agente — refactoring, migrazione, un modulo nuovo — su quale codebase e con quale strumento.",
            "Anche nel caso GitHub, il ruolo umano non è scomparso: si è spostato su definizione dei confini, arbitraggio delle decisioni tecniche e revisione, non sulla scrittura riga per riga.",
            "[DA PERSONALIZZARE] Un aneddoto reale del team: dove l'agente ha sorpreso in positivo, e dove invece ha servito l'occhio di qualcuno che conosceva l'architettura.",
        ],
        closing="Il punto non è se un agente sa scrivere codice: lo sa fare, e bene. Il punto è chi decide cosa merita di arrivare in produzione.",
        cta="Qual è la vostra esperienza nel delegare del codice vero a un agente? Ci interessa confrontarci 👇",
        hashtags="#AIEngineering #SoftwareDevelopment #TeamAugmentation #Tech #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 24/9",
        format="Carosello dati (mito da sfatare — il gap delle PMI italiane)",
        title="Il gap AI delle PMI italiane si chiude da solo, con il tempo? I numeri dicono di no",
        news="Unioncamere-Dintec (ANSA, 17/9)",
        news_url="https://www.ansa.it/canale_tecnologia/notizie/tecnologia/2026/09/17/unioncamere-dintec-195-imprese-italiane-usa-lintelligenza-artificiale_9b8f1f3b-74bd-4fd5-ac8f-e91aa42eae6a.html",
        hook="🔥 Il mito: il gap AI delle piccole imprese italiane si chiude da solo, con il tempo e con l'adozione che via via si diffonde.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I numeri di questa settimana, letti insieme, raccontano una storia diversa.",
        points=[
            "19,5% delle imprese italiane usa oggi l'AI, il doppio rispetto a un anno fa (Unioncamere-Dintec).",
            "Oltre il 50% delle grandi aziende la usa, contro il 15% delle piccole imprese: il divario per dimensione non si è chiuso, si è solo spostato più in alto.",
            "58,6% delle PMI indica la carenza di competenze digitali come freno principale all'adozione, non il costo, non la tecnologia.",
            "Solo il 7% delle PMI ha avviato un percorso di formazione AI strutturato sul tema.",
            "Secondo il professor Giuseppe Francesco Italiano (Luiss), almeno 6 aziende interessate su 10 abbandonano l'adozione AI per mancanza di competenze.",
        ],
        myth_closing="La crescita c'è, ed è reale. Ma cresce più in fretta chi ha già le competenze per adottare l'AI di chi parte da zero: il gap non si chiude aspettando, si chiude formando le persone sui casi d'uso reali dell'azienda.",
        cta="Nella tua PMI la carenza di competenze è già un freno riconosciuto, o non ne parla ancora nessuno? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 25/9",
        format="Divulgativo stile Datapizza",
        title="Cosa significa davvero che «un'AI guida il 26% della propria ricerca»? Spiegato semplice",
        news="Anthropic R&D Automation Index",
        news_url="https://www.anthropic.com/institute/measuring-pace-of-ai-development",
        hook="Questa settimana Anthropic ha detto che Claude «guida» il 26% della propria ricerca AI interna. Suona spaventoso, o rivoluzionario, a seconda di chi lo racconta. Cosa vuol dire davvero? Proviamo a spiegarlo senza fuffa.",
        points=[
            "«Guidare» un compito, nel linguaggio di Anthropic, non vuol dire farlo da solo: è una scala che va da assistenza a collaborazione a guida a piena autonomia. Il 90% del lavoro di Claude resta ai primi livelli, con un umano sempre nel ciclo: zero compiti classificati come completamente autonomi.",
            "Il numero interessante non è il 26%, è il salto rispetto a febbraio 2026, quando era sotto l'1%: misura quanto rapidamente un laboratorio riesce a fidarsi delle proprie AI per accelerare lo sviluppo di quelle successive, non quanto le AI abbiano sostituito le persone.",
            "Per questo Anthropic pubblica anche i numeri di controllo insieme al 26%: 30.000 agenti al lavoro in contemporanea, ma solo lo 0,002% delle decisioni bloccato dai sistemi automatici e circa 50 segnalazioni a settimana che arrivano a un revisore umano. Un numero senza l'altro racconterebbe solo metà della storia.",
        ],
        cta="Ti sembra un buon modo di misurare quanto ci si può fidare dell'AI, o solo una statistica ben scelta? Dicci la tua 👇",
        hashtags="#AI #TechExplained #Innovazione #B2B #RicercaAI",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati — le mosse della settimana",
        title="Tre mosse, tre miliardi, una sola direzione: la settimana vista dai numeri",
        news="Astra for Law (OpenAI) + AIforce (Salesforce) + round Crusoe Energy",
        news_url="https://openai.com/index/astra-for-law/",
        hook="Tre notizie separate di questa settimana raccontano, insieme, la stessa direzione: dai modelli generici ai prodotti verticali, dall'interfaccia agli agenti, e capitali sempre più grandi sull'infrastruttura.",
        points=[
            "40% in più di successo nella ricerca legale (dal 38,7% al 54%) con Astra for Law, il primo GPT-6 verticalizzato su un intero settore, con 230 milioni di URL indicizzati e 26 plugin di partner (OpenAI).",
            "Salesforce lancia AIforce a Dreamforce: un livello che espone dati e processi a qualunque agente, con la linea ufficiale «l'AI sostituisce l'interfaccia».",
            "3,9 miliardi di dollari raccolti da Crusoe Energy in un solo round, a una valutazione di 30,9 miliardi, per costruire nuove «AI factory»: un'altra prova di quanto capitale stia confluendo nell'infrastruttura, non nell'adozione.",
        ],
        closing="Nessuna di queste tre notizie riguarda direttamente un'azienda di 50 o 200 persone in Italia. Tutte e tre, insieme, spiegano perché il vantaggio competitivo si giocherà su chi integra bene questi strumenti, non su chi li costruisce.",
        cta="Quale di queste tre mosse pensi avrà il maggiore impatto sul modo in cui lavoriamo entro un anno? 👇",
        hashtags="#AINews #TechTrends #B2B #Innovazione #IntelligenzaArtificiale",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci ha insegnato sull'AI (e su come adottarla bene)",
        news="Sintesi dei trend della settimana 15-21 settembre 2026",
        news_url="https://www.anthropic.com/institute/measuring-pace-of-ai-development",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie AI degli ultimi 7 giorni.",
        points=[
            "L'AI che costruisce AI non è più un esperimento da laboratorio: Anthropic misura 30.000 agenti al lavoro in contemporanea sulla propria ricerca.",
            "In Italia l'adozione AI è raddoppiata in un anno, ma il vero ostacolo resta la carenza di competenze, non la tecnologia.",
            "Il caso più documentato dell'anno (la migrazione Rust di GitHub Copilot) confirma che gli agenti scrivono, ma le persone senior decidono ancora l'architettura.",
            "Anche i laboratori che si contendono il mercato più duramente (OpenAI, Anthropic, Google DeepMind) stanno provando, per ora senza successo, a darsi regole comuni.",
            "I capitali più grandi della settimana (Crusoe, 3,9 miliardi di dollari) vanno tutti sull'infrastruttura: il vantaggio competitivo delle aziende si gioca altrove.",
        ],
        closing="Nessuno di questi punti richiede un modello migliore. Tutti richiedono qualcuno che se ne occupi con un metodo.",
        cta="Qual è la notizia della settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #IntelligenzaArtificiale #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    # Idea 8, extra: aggiunta su richiesta esplicita di Ramona dopo la
    # revisione del report, per coprire il lancio di Jev/TypeSafe AI (segnalato
    # in revisione e integrato tra i trend). Sesto post Prioritario della
    # settimana, oltre ai 5 dello schema standard: eccezione dichiarata, non
    # un cambio della cadenza di default a 5/settimana.
    dict(
        badge="Prioritario",
        day="Sabato 26/9 (extra della settimana, su richiesta)",
        format="Divulgativo stile Datapizza",
        title="Jev non scrive una parola. Risponde in 100 millisecondi: cos'è un modello *System One*?",
        news="Lancio di Jev, TypeSafe AI",
        news_url="https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711",
        hook="Questa settimana un laboratorio fondato da un ex OpenAI ha lanciato un modello che si rifiuta di scrivere testo. Si chiama Jev, risponde in meno di mezzo secondo e costa centinaia di volte meno di un modello generalista. Cosa fa, davvero?",
        points=[
            "Jev non genera linguaggio: restituisce decisioni strutturate con una probabilità già calcolata per ogni opzione — per esempio, smistare una richiesta cliente tra fatturazione, tecnico e vendite con un punteggio di confidenza per ciascuna. TypeSafe lo chiama «System One model»: veloce e strutturato, non conversazionale.",
            "I numeri che rivendica sono netti: risposte in 70-500 millisecondi contro i minuti di un modello generalista, e un costo di 0,042 $ per milione di token in input, con output gratuito — 40 a 200 volte più veloce sui compiti per cui è stato costruito.",
            "TypeSafe parla di «0% di hallucination», ma va letto con la qualifica giusta: un output strutturato non può essere malformato, ma può comunque essere sbagliato nel merito. Utile da ricordare ogni volta che un fornitore promette «zero errori»: la domanda giusta è sempre «zero errori di cosa».",
        ],
        cta="Ti sembra un'evoluzione utile per automatizzare decisioni ripetitive in azienda, o resta un modello di nicchia? Dicci la tua 👇",
        hashtags="#AI #TechExplained #Innovazione #B2B #MachineLearning",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 21/9",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 22/9",
        time="12:15",
        format="Mito da sfatare (autonomia degli agenti)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach.",
    ),
    dict(
        day="Mercoledì 23/9",
        time="08:30",
        format="Esperienza diretta",
        reason="Picco assoluto di traffico professionale B2B della settimana: il formato genera meno reach ma più commenti/DM da decision maker, per questo va nel giorno di massima visibilità organica.",
    ),
    dict(
        day="Giovedì 24/9",
        time="12:15",
        format="Carosello dati / mito da sfatare (gap PMI italiane)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di due giorni dal primo mito per non saturare lo stesso formato. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn: qui porta anche un secondo dato pesante (gap di competenze PMI) che merita spazio proprio, non solo un accenno nell'apertura.",
    ),
    dict(
        day="Venerdì 25/9",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello «le mosse della settimana»",
        reason="Banca contenuti: utile come secondo documento se questa settimana c'è margine di pubblicazione, o come apertura news della settimana successiva.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo la settimana successiva.",
    ),
    dict(
        day="Sabato 26/9",
        time="10:00",
        format="Divulgativo — Jev / TypeSafe AI (extra)",
        reason="Sesto post della settimana, aggiunto su richiesta dopo l'approvazione del piano standard: non rientra nello schema 5 Prioritario + 2 Riserva. Il sabato mattina ha traffico B2B più basso ma un pubblico più curioso e meno frettoloso: coerente con un contenuto divulgativo senza CTA commerciale. Da valutare se spostarlo a un giorno feriale della settimana successiva se si preferisce non superare la cadenza standard.",
    ),
]
