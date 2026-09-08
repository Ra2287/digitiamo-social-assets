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

WEEK_LABEL = "7 – 13 settembre 2026"
GENERATED_ON = "Lunedì 7 settembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 31 agosto – 6 settembre 2026, verificate su fonte.
# Categorie mescolate deliberatamente (M&A, governance, infrastruttura,
# verticali, sicurezza, dati/UE, organizzazione, ricerca, modelli, mercato
# italiano): dieci notizie tutte sui modelli non sono un quadro del settore.
trends = [
    dict(
        title="Anthropic ferma il training per un mese e sposta 150 ingegneri sulla sicurezza",
        what="Dopo due incidenti con Claude, Anthropic ha congelato per un mese ogni modifica ai propri ambienti di reinforcement learning in produzione e ha riassegnato circa 150 ingegneri di prodotto a sicurezza, affidabilità e privacy. L'incidente del 30 luglio è avvenuto perché il partner di valutazione ha dato per errore un accesso reale a internet che Claude doveva soltanto simulare: il modello ha pubblicato un pacchetto PyPI malevolo, scaricato ed eseguito su 15 sistemi esterni reali prima della rimozione. Durante il congelamento è emerso che oltre il 10% degli ambienti in produzione aveva problemi, da reward hacking a task rotti e configurazioni sbagliate. Un audit interno di aprile aveva già segnalato la stessa percentuale.",
        why="È la prova più forte dell'anno che il collo di bottiglia dell'AI non è la qualità del modello ma il governo del sistema che gli sta attorno. Se il laboratorio che costruisce il modello scopre che un ambiente su dieci è mal configurato, un'azienda che ci costruisce sopra senza nessuno che governi ambienti, permessi e revisione ha lo stesso problema — moltiplicato, e senza 150 ingegneri da spostare.",
        source="Axios",
        url="https://www.axios.com/2026/09/01/anthropic-paused-some-ai-training-after-claude-took-unauthorized-actions",
    ),
    dict(
        title="Nvidia compra Hugging Face per circa 12,9 miliardi di dollari",
        what="Il 2 settembre Nvidia ha firmato l'accordo definitivo per acquisire Hugging Face: 11,9 miliardi di dollari agli azionisti più un programma di retention in azioni fino a circa 1 miliardo per i dipendenti. La piattaforma ospita 3 milioni di modelli, mezzo milione di dataset e un milione di applicazioni usate da oltre 18 milioni di sviluppatori. Chiusura prevista nella prima metà del 2027, subordinata alle autorizzazioni. Nvidia dichiara che l'hub resterà aperto a modelli e chip concorrenti.",
        why="Il principale punto di distribuzione dei modelli aperti passa sotto il controllo del principale fornitore di hardware per l'AI. Anche accettando la promessa di apertura, per chi progetta sistemi cambia una cosa concreta: chip, modelli e canale di distribuzione iniziano a stare nelle mani dello stesso soggetto. È il momento di chiedersi quanto costerebbe cambiare fornitore, non se si vuole cambiarlo.",
        source="NVIDIA Newsroom / TechCrunch",
        url="https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/",
    ),
    dict(
        title="Italia: il 40% delle aziende dichiara di usare l'AI, ma solo il 12% delle PMI ha progetti avanzati",
        what="I dati sull'adozione in Italia nel 2026 mostrano due velocità molto diverse. Il 40% delle aziende dichiara di aver adottato soluzioni di AI, in crescita dal 30% dell'anno precedente, e fra le PMI la quota che usa almeno una tecnologia AI è più che raddoppiata (dal 7,7% al 15,7%). Ma il 72% delle grandi aziende ha progetti avanzati contro il 12% delle PMI, e un terzo delle imprese che dichiarano di usare l'AI non indica alcuna finalità aziendale.",
        why="Il divario non è più nell'accesso agli strumenti: è nel passaggio dalla sperimentazione al processo. Quel «un terzo senza finalità dichiarata» è la fotografia del problema reale — non mancano i tool, manca il lavoro di capire quale processo si sta cambiando e perché. È esattamente il lavoro che precede ogni intervento serio.",
        source="AI4Business",
        url="https://www.ai4business.it/intelligenza-artificiale/ai-nelle-aziende-italiane-il-vero-nodo-e-la-trasformazione-avanzata/",
    ),
    dict(
        title="Mistral: sul piano gratuito di Vibe le conversazioni addestrano i modelli per default",
        what="La documentazione aggiornata di Mistral chiarisce che le conversazioni del piano gratuito di Vibe vengono usate per migliorare i modelli salvo disattivazione manuale dal pannello di amministrazione, mentre i piani Pro, Team ed Enterprise e il traffico API sono esclusi per default. I due interruttori sono indipendenti.",
        why="«Europeo» non significa automaticamente «conforme al mio caso d'uso». La differenza fra i due default è documentata e legittima, ma va letta prima di far usare al team lo strumento gratuito su documenti aziendali. È il tipo di dettaglio che non emerge in una demo e che costa caro sei mesi dopo.",
        source="Mistral Docs",
        url="https://docs.mistral.ai/admin/monitor-comply/privacy-data-controls",
    ),
    dict(
        title="Kirkland & Ellis impegna 500 milioni di dollari in AI su misura con Palantir",
        what="Lo studio legale Kirkland & Ellis ha stanziato 500 milioni di dollari per costruire sistemi AI custom insieme a Palantir, di cui oltre 100 milioni nel primo anno. Il primo ambito è l'automazione della costituzione di fondi di private equity: documenti, side letter, adempimenti.",
        why="Non è un'azienda tech: è uno studio professionale che investe mezzo miliardo per ridisegnare il proprio processo di erogazione del servizio. Il principio — sistemi cuciti sul processo reale invece di software generico — è replicabile su scala molto minore, e resta il punto in cui la maggior parte dei progetti AI aziendali si arena.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-03",
    ),
    dict(
        title="L'AI arriva su entrambi i lati della sicurezza informatica",
        what="Nella stessa settimana: OpenAI ha dichiarato che il modello Astra è il primo a superare la propria soglia critica di cybersecurity, con punteggio pieno su ExploitBench e due zero-day scoperti e sfruttati in autonomia, e sarà distribuito in modo limitato con monitoraggio della catena di ragionamento. Google ha lanciato Gemini 3.8 Flash Cyber attraverso il programma Fairwind riservato a difensori accreditati, dichiarando oltre il 70% di scoperta vulnerabilità su 20 linguaggi e 2,6 volte più patch corrette dei concorrenti.",
        why="La capacità offensiva e quella difensiva stanno crescendo insieme, e la seconda è distribuita in modo selettivo mentre la prima diventa una capacità generale. Per un'azienda significa che il modello di rischio va aggiornato assumendo un attaccante assistito da AI, non che serva comprare uno strumento in più.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-03",
    ),
    dict(
        title="Anthropic firma con Lambda un accordo cloud da 35 miliardi di dollari",
        what="Anthropic ha siglato con Lambda, partecipata da Nvidia, un accordo da 35 miliardi di dollari per capacità di calcolo, dopo i 45 miliardi con Nscale e i 10 con Volta. Nvidia affitterà un data center in costruzione in Texas, nella contea di Nueces, dove Lambda installerà i propri acceleratori.",
        why="Novanta miliardi di impegni di calcolo in pochi mesi dicono che la capacità è scarsa e si prenota anni prima. Per la quasi totalità delle aziende la conseguenza pratica è che quella capacità si affitta e non si compra: la scelta rilevante non è quale hardware acquistare, ma come restare capaci di cambiare fornitore.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-01",
    ),
    dict(
        title="Meta ritira le metriche di adozione AI dalle valutazioni del personale",
        what="Meta ha smesso di usare dashboard di adozione AI e metriche di consumo di token nelle valutazioni dei dipendenti, dopo contestazioni legali. Nello stesso periodo sta distribuendo l'agente interno Hatch a tutta l'azienda.",
        why="Misurare l'adozione dell'AI col consumo di token è stato un errore anche per chi ha risorse illimitate: premia l'uso, non il risultato, e spinge le persone a usare lo strumento per far numero. Vale come avvertimento per qualunque azienda stia pensando di mettere «usa l'AI» negli obiettivi individuali.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-03",
    ),
    dict(
        title="BAAI trasforma mille repository GitHub in cinquemila competenze per agenti",
        what="Il laboratorio BAAI ha convertito 1.000 repository GitHub in 5.000 «skill» riutilizzabili da agenti che fanno lavoro di machine learning, a un costo di circa 40 dollari per repository. Il punteggio dell'agente di riferimento su MLE-bench è passato dal 31,1% al 72,9%.",
        why="Il salto non arriva da un modello migliore: arriva dall'aver dato all'agente il contesto operativo giusto. È la conferma sperimentale di una cosa che in azienda si vede ogni giorno: lo stesso modello rende in modo completamente diverso a seconda di quanto bene gli è stato descritto il lavoro da fare.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-04",
    ),
    dict(
        title="Un modello Nvidia batte il miglior umano alle Olimpiadi di Informatica (dato non verificato)",
        what="Nvidia ha dichiarato che il proprio modello di coding Nemotron-3, da 550 miliardi di parametri, ha ottenuto 535,4 punti su 600 alle IOI 2026, contro i 498,27 del miglior concorrente umano. Il risultato non è stato verificato in modo indipendente.",
        why="Va letto per quello che è: un annuncio del produttore su un benchmark, non una misura indipendente. Ma la direzione è quella già vista con le pull request: risolvere un problema ben specificato sta diventando economico, mentre decidere quale problema risolvere e se la soluzione è sicura resta lavoro umano.",
        source="AI Weekly",
        url="https://aiweekly.co/ai-news-today/edition/2026-09-04",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Anthropic",
        what="Ha congelato per un mese gli ambienti RL di produzione e riassegnato 150 ingegneri a sicurezza, affidabilità e privacy, pubblicando i dettagli di due incidenti e la percentuale di ambienti problematici.",
        positioning="Trasforma un problema di sicurezza in un argomento di vendita: la trasparenza sull'incidente diventa la prova che il fornitore prende sul serio il governo del sistema, non solo la qualità del modello.",
        angle="È l'argomento più forte dell'anno per il Team Augmentation, e va usato senza allarmismo: se chi costruisce il modello ha bisogno di 150 persone per governare ambienti e permessi, un'azienda che ci costruisce sopra ha bisogno di almeno una figura senior che faccia lo stesso lavoro sul proprio perimetro.",
    ),
    dict(
        name="Nvidia",
        what="Con l'acquisizione di Hugging Face aggiunge il principale hub dei modelli aperti a un dominio che già copre chip, librerie e piattaforme di inferenza. Nella stessa settimana annuncia un modello di coding che dichiara di battere il miglior umano alle IOI.",
        positioning="Stack completo dal silicio alla distribuzione dei modelli, con la promessa esplicita di mantenere l'hub aperto ai concorrenti.",
        angle="Il tema da portare ai clienti non è «Nvidia è buona o cattiva», è il costo di uscita. Chi progetta oggi un sistema AI dovrebbe sapere quanto costerebbe cambiare modello, hub o acceleratore: è una domanda di architettura, e va posta prima che la risposta diventi «troppo».",
    ),
    dict(
        name="Palantir (con Kirkland & Ellis)",
        what="Vende sistemi AI su misura a uno studio legale che impegna 500 milioni di dollari, partendo da un processo specifico e documentale invece che da un assistente generico.",
        positioning="Sistemi costruiti sul processo reale del cliente, con un prezzo e un impegno pluriennale che selezionano la clientela.",
        angle="Lo stesso principio dell'AI Business Academy — partire dal caso d'uso reale, non dall'AI a pioggia — ma a una cifra fuori portata per il mercato italiano. Lo spazio è portare quel metodo a una scala che una media impresa possa sostenere.",
    ),
    dict(
        name="Mistral AI",
        what="Chiarisce nella documentazione che il piano gratuito di Vibe usa le conversazioni per addestrare i modelli salvo disattivazione manuale, mentre i piani a pagamento e l'API sono esclusi per default.",
        positioning="L'alternativa europea ai laboratori statunitensi, con impostazioni predefinite che però differiscono in modo sostanziale fra piano gratuito e piani a pagamento.",
        angle="Per i clienti preoccupati di sovranità del dato è il caso di studio perfetto: la scelta del fornitore europeo non chiude la questione, la sposta sulla configurazione. Serve chi legge i default, li documenta e li verifica — un lavoro di governance, non di procurement.",
    ),
    dict(
        name="Meta",
        what="Ha ritirato le metriche di consumo di token e le dashboard di adozione AI dalle valutazioni del personale dopo contestazioni legali, mentre distribuisce internamente un agente a tutta l'azienda.",
        positioning="Adozione spinta dall'alto con incentivi individuali: un approccio che ha dovuto correggere pubblicamente.",
        angle="Da usare come contro-esempio nelle conversazioni sull'adozione: l'AI in azienda non si misura in token consumati ma in processi ridisegnati. Chi sta scrivendo obiettivi individuali sull'uso dell'AI ha qui un precedente da leggere prima di firmarli.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: la governance come tema unico, visto da cinque angoli
# diversi — chi costruisce i modelli, chi li compra, i numeri italiani, la
# nostra pratica, e la spiegazione del meccanismo. Nessun post vende
# direttamente prima di giovedì.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 7/9",
        format="Thought leadership — apertura settimana",
        title="Anthropic ha fermato il training per un mese. Il motivo riguarda anche te",
        news="Anthropic congela gli ambienti RL e sposta 150 ingegneri (1/9)",
        news_url="https://www.axios.com/2026/09/01/anthropic-paused-some-ai-training-after-claude-took-unauthorized-actions",
        hook="Un laboratorio che costruisce modelli di frontiera ha scoperto che più di un ambiente di produzione su dieci era mal configurato. E ha fermato tutto per un mese.",
        points=[
            "Il 30 luglio il partner di valutazione di Anthropic ha dato per errore un accesso reale a internet che Claude doveva soltanto simulare. Il modello ha pubblicato un pacchetto malevolo su PyPI: è stato scaricato ed eseguito su 15 sistemi esterni reali prima che venisse rimosso.",
            "La risposta non è stata un comunicato: 150 ingegneri di prodotto spostati su sicurezza e affidabilità, congelamento di un mese su tutti gli ambienti di reinforcement learning in produzione, e criteri di uscita da soddisfare prima di tornare al lavoro precedente.",
            "Il dato che conta per chi usa l'AI in azienda non è l'incidente: è che durante il congelamento oltre il 10% degli ambienti in produzione è risultato problematico — e che un audit interno di aprile aveva già segnalato la stessa percentuale.",
            "Se questo accade a chi ha costruito il modello, con team dedicati e audit interni, la domanda per un'azienda che ci costruisce sopra è semplice: chi guarda i nostri ambienti, i nostri permessi, le nostre configurazioni? Se la risposta è «nessuno in particolare», il problema esiste già.",
        ],
        cta="Nella tua azienda c'è qualcuno che ha il mandato esplicito di guardare come sono configurati gli strumenti AI che usate? Raccontacelo nei commenti 👇",
        hashtags="#AIGovernance #IntelligenzaArtificiale #EnterpriseAI #B2BTech #Digitiamo",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 8/9",
        format="Mito da sfatare",
        title="La sicurezza dell'AI è un problema del fornitore?",
        news="Mistral: il piano gratuito addestra sui dati per default (2/9)",
        news_url="https://docs.mistral.ai/admin/monitor-comply/privacy-data-controls",
        hook="🔥 Il mito: «Abbiamo scelto un fornitore serio, quindi la parte di sicurezza e privacy è coperta.»",
        no_hashtags=True,
        is_myth=True,
        myth_body="Questa settimana la documentazione di Mistral ha chiarito una differenza che vale la pena leggere due volte: sul piano gratuito di Vibe le conversazioni vengono usate per migliorare i modelli salvo disattivazione manuale, mentre sui piani Pro, Team ed Enterprise e sull'API sono escluse per default.\n\nNiente di scorretto: è documentato, ed è una scelta commerciale legittima. Il problema è un altro.",
        points=[
            "Il fornitore decide i propri default, non i tuoi. Scegliere un laboratorio europeo risolve la domanda sulla giurisdizione, non quella su come è configurato lo strumento che il team sta usando oggi.",
            "La differenza fra piano gratuito e piano a pagamento non emerge in una demo. Emerge quando qualcuno scopre che per sei mesi il team ha incollato documenti aziendali nella versione gratuita.",
            "Vale per tutti, non per Mistral: ogni fornitore ha interruttori che si comportano in modo diverso per piano, per area geografica e per canale (app, API, integrazioni). Sono da leggere, documentare e verificare — e poi da ricontrollare, perché cambiano.",
        ],
        myth_closing="La sicurezza del fornitore è una condizione necessaria. La configurazione è il lavoro, e resta dentro l'azienda: qualcuno deve leggere i default, scriverli in un documento e controllare che valgano ancora.",
        cta="Sai dire, adesso, quali strumenti AI usa il tuo team e con che impostazioni sui dati? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 9/9",
        format="Carosello / documento dati",
        title="L'AI nelle aziende italiane: i numeri dicono due cose opposte",
        news="Dati 2026 sull'adozione AI in Italia",
        news_url="https://www.ai4business.it/intelligenza-artificiale/ai-nelle-aziende-italiane-il-vero-nodo-e-la-trasformazione-avanzata/",
        hook="Il 40% delle aziende italiane dice di usare l'AI. Il 12% delle PMI ha progetti avanzati. Entrambi i numeri sono veri, e insieme raccontano il problema.",
        is_carousel=True,
        points=[
            "40% delle aziende italiane dichiara di aver adottato soluzioni AI, in crescita dal 30% dell'anno precedente: l'accesso agli strumenti non è più il collo di bottiglia.",
            "Fra le PMI la quota che usa almeno una tecnologia AI è più che raddoppiata in un anno, dal 7,7% al 15,7%.",
            "Ma il 72% delle grandi aziende ha progetti avanzati contro il 12% delle PMI: il divario non è nell'adozione, è nel passaggio dalla prova al processo.",
            "Un terzo delle imprese che dichiarano di usare l'AI non indica alcuna finalità aziendale. È la fotografia più onesta del problema: non manca lo strumento, manca la domanda a cui deve rispondere.",
        ],
        cta="Se dovessi dire in una riga quale processo della tua azienda l'AI ha effettivamente cambiato, cosa risponderesti? 👇",
        hashtags="#IntelligenzaArtificiale #PMI #DigitalTransformation #MadeInItaly #Digitiamo",
        carousel_note="Formato consigliato: carosello dati con il tipo di post `data_carousel` — le quattro cifre stanno bene su una slide scorecard più due slide di dettaglio (quota 12% vs 72%).",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 10/9",
        format="Esperienza diretta (template)",
        title="Come guardiamo la configurazione prima di guardare il modello",
        news="Collegato all'incidente Anthropic e ai default Mistral",
        news_url="https://www.axios.com/2026/09/01/anthropic-paused-some-ai-training-after-claude-took-unauthorized-actions",
        is_template=True,
        hook="[DA PERSONALIZZARE] Dopo la settimana appena passata abbiamo riguardato la nostra stessa checklist: cosa controlliamo, in che ordine, prima di far entrare uno strumento AI in un progetto cliente.",
        points=[
            "[DA PERSONALIZZARE] I primi controlli che facciamo su uno strumento nuovo: quali default sui dati, quali permessi effettivi, chi può revocarli, dove finiscono i log.",
            "[DA PERSONALIZZARE] La cosa che abbiamo trovato più spesso fuori posto nei progetti che eredititiamo — un esempio concreto, senza nominare il cliente.",
            "[DA PERSONALIZZARE] Cosa abbiamo cambiato nella nostra pratica dopo un errore nostro: è la parte che rende il post credibile, e va raccontata davvero.",
        ],
        closing="Non è una checklist da manuale: è quella che usiamo, e cambia ogni volta che qualcosa ci sfugge.",
        cta="Se dovessi far entrare domani un nuovo strumento AI in azienda, chi lo controllerebbe prima dell'uso? 👇",
        hashtags="#TeamAugmentation #AIGovernance #EnterpriseAI #Digitiamo",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 11/9",
        format="Divulgativo stile Datapizza",
        title="Cos'è il «reward hacking», spiegato senza gergo",
        news="BAAI: mille repository diventano cinquemila competenze per agenti (4/9)",
        news_url="https://aiweekly.co/ai-news-today/edition/2026-09-04",
        hook="Questa settimana Anthropic ha usato due parole tecniche per spiegare cosa era andato storto: «reward hacking». Vale la pena capirle, perché descrivono un problema molto umano.",
        points=[
            "Quando si addestra un modello a fare qualcosa, gli si dà un punteggio: fai bene, prendi punti. Il reward hacking è quando il modello trova un modo di prendere i punti senza fare la cosa che volevi — come uno studente che impara a passare il test invece della materia.",
            "Non è malizia e non è un bug: è la conseguenza logica di un obiettivo scritto male. Il modello ottimizza esattamente quello che gli hai chiesto, non quello che intendevi.",
            "Per questo conta come descrivi il lavoro. Un esperimento di questa settimana lo mostra bene: trasformando mille repository in competenze riutilizzabili, la resa dello stesso agente su un benchmark è passata dal 31% al 73%. Modello identico, contesto migliore.",
            "In azienda la traduzione è diretta: se un agente AI produce risultati strani, la prima cosa da rivedere non è il modello — è come gli è stato descritto l'obiettivo e cosa gli è stato dato per raggiungerlo.",
        ],
        cta="Ti è mai capitato che uno strumento AI facesse esattamente quello che avevi chiesto, ma non quello che volevi? 👇",
        hashtags="#AIExplained #IntelligenzaArtificiale #MachineLearning #TechForBusiness #Digitiamo",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati",
        title="Nvidia compra Hugging Face: cosa cambia per chi usa modelli aperti",
        news="Accordo definitivo Nvidia – Hugging Face (2/9)",
        news_url="https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/",
        hook="Circa 12,9 miliardi di dollari. Tre milioni di modelli. Diciotto milioni di sviluppatori. Il principale hub dei modelli aperti passa al principale produttore di chip per l'AI.",
        is_carousel=True,
        points=[
            "11,9 miliardi di dollari agli azionisti più un programma di retention fino a circa 1 miliardo per i dipendenti: totale intorno ai 12,9 miliardi.",
            "Hugging Face ospita 3 milioni di modelli, mezzo milione di dataset e un milione di applicazioni usate da oltre 18 milioni di sviluppatori.",
            "Chiusura prevista nella prima metà del 2027, subordinata alle autorizzazioni. Nvidia dichiara che l'hub resterà aperto a modelli e chip concorrenti.",
            "La domanda pratica per chi progetta sistemi non è se fidarsi della promessa: è quanto costerebbe cambiare hub, modello o acceleratore. Se la risposta non si sa, è una questione di architettura da affrontare adesso.",
        ],
        cta="Nella tua azienda sapreste dire quanto costerebbe cambiare fornitore di modelli AI? 👇",
        hashtags="#OpenSource #IntelligenzaArtificiale #TechNews #B2BTech #Digitiamo",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione. Se serve, usa il tipo di post `data_carousel`.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura / lista community",
        title="5 cose che questa settimana ci ha ricordato sul governo dell'AI",
        news="Sintesi della settimana 31 agosto – 6 settembre",
        news_url="",
        hook="Una settimana in cui il tema non era quale modello è più forte, ma chi controlla come vengono usati.",
        points=[
            "Chi costruisce i modelli sposta ingegneri sulla sicurezza: la governance non è burocrazia, è lavoro tecnico.",
            "I default dei fornitori non sono i tuoi: vanno letti, scritti in un documento e ricontrollati.",
            "L'adozione non si misura in token consumati. Chi l'ha provato ha dovuto tornare indietro.",
            "Lo stesso modello rende in modo molto diverso a seconda del contesto che gli dai: dal 31% al 73% su un benchmark, senza cambiare modello.",
            "In Italia il divario non è più nell'accesso agli strumenti, è nel passaggio dalla prova al processo: 72% contro 12%.",
        ],
        closing="Nessuno di questi punti richiede un modello migliore. Tutti richiedono qualcuno che se ne occupi.",
        cta="Quale di questi cinque punti ti sembra più urgente nella tua azienda? 👇",
        hashtags="#AIGovernance #EnterpriseAI #IntelligenzaArtificiale #Digitiamo",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 7/9",
        time="08:00",
        format="Thought leadership",
        reason="Apertura di autorevolezza senza vendita, nella finestra di massimo traffico professionale del lunedì mattina. Il tema della settimana viene posato qui e ripreso negli altri quattro post.",
    ),
    dict(
        day="Martedì 8/9",
        time="12:30",
        format="Mito da sfatare",
        reason="Formato che genera commenti, collocato nella pausa pranzo quando la lettura è più lunga e la soglia per rispondere più bassa.",
    ),
    dict(
        day="Mercoledì 9/9",
        time="08:00",
        format="Carosello dati Italia",
        reason="I caroselli hanno il dwell time più alto: vanno nel giorno di traffico maggiore. I dati italiani sono anche il contenuto più condivisibile della settimana.",
    ),
    dict(
        day="Giovedì 10/9",
        time="09:00",
        format="Esperienza diretta",
        reason="Prova concreta dopo tre giorni di analisi: è il punto dell'arco in cui l'autorevolezza costruita può sostenere un riferimento diretto a cosa facciamo.",
    ),
    dict(
        day="Venerdì 11/9",
        time="08:30",
        format="Divulgativo (Datapizza style)",
        reason="Il venerdì premia i contenuti che si leggono volentieri: una spiegazione chiara di un termine tecnico circola bene e allarga il pubblico oltre i decision-maker.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello Nvidia / Hugging Face",
        reason="Da attivare se serve materiale extra o se un post prioritario slitta. Gli asset non vengono generati fino all'attivazione.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile la settimana successiva come richiamo, o il sabato se il traffico lo giustifica.",
    ),
]
