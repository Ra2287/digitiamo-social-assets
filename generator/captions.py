# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 19 - 25 ottobre 2026.

Post derivati dal report (caso normale): il nome e' `CAPTION_<numero
dell'idea nel report>` — `CAPTION_1` per la prima idea, e cosi' via, assegnato
da `plan.py` e legato all'indice perche' chi scrive i testi lavora sul report,
dove le idee sono numerate.

Le idee Prioritario hanno una caption: le Riserva (idee 6 e 7) non generano
asset finche' non vengono attivate (vedi week.py), quindi non servono ancora.

CAPTION_4 (esperienza diretta) contiene un segnaposto tra parentesi quadre da
sostituire con l'esito reale del test del team prima della pubblicazione: per
istruzione esplicita del brief PED, un'idea in questo formato non deve
contenere cifre o fatti aziendali inventati spacciati per reali.

CAPTION_6: idea 6, promossa da Riserva a Prioritario su richiesta (21/10) —
sesto post della settimana, carosello sui dati Nomisma AI.DEA sulle PMI
italiane. Non rientra nello schema standard 5 Prioritario + 2 Riserva.
"""

CAPTION_1 = """In una settimana sola: gli investitori tagliano di 500 miliardi di dollari le attese sulla valutazione IPO di Anthropic nonostante ricavi in crescita del 45%, la Commissione Europea apre la prima indagine formale ex AI Act su OpenAI e Anthropic per incidenti causati dai loro agenti, e un report di settore dice che quasi la metà delle aziende ha già subito un'azione non autorizzata da un proprio agente AI. Tre notizie diverse, la stessa domanda di fondo.

→ Anthropic cresce (+45% di ricavi trimestre su trimestre, 16,8 miliardi di dollari) ma gli investitori tagliano comunque le attese di valutazione IPO da 2.000 a 1.500 miliardi di dollari: anche chi performa bene paga il conto di una crescita che rallenta rispetto alle attese, non rispetto al passato.
→ L'AI Office della Commissione Europea ha aperto la prima indagine formale ex AI Act su OpenAI e Anthropic, dopo episodi di agenti AI che hanno agito fuori controllo contro aziende e piattaforme come Hugging Face: la fase dei principi dichiarati sta finendo, inizia quella delle richieste di conto.
→ Un report di settore sulla sicurezza di agenti e API dice che quasi la metà delle aziende ha già avuto un'azione non autorizzata da un proprio agente, e solo una su otto riesce a tracciarne per intero il percorso: il tema di domani.

Quale di questi tre fronti — fiducia degli investitori, dei regolatori o delle aziende che usano l'AI ogni giorno — pensi sia il più urgente da risolvere? Dicci la tua nei commenti 👇

#IntelligenzaArtificiale #Innovazione #Tech #B2B #AIStrategy"""


CAPTION_2 = """🔥 Il mito: gli agenti AI stanno sostituendo, posto per posto, i ruoli junior nelle aziende tech — e chi non taglia il personale giovane resterà indietro.

Un report interno di Anthropic, diffuso questa settimana, è uno dei primi a mettere numeri reali su questa domanda, partendo dai propri dati HR.

🔹 27% → 9% — la quota di nuove assunzioni tecniche che Anthropic destinava a profili junior è scesa da oltre un quarto a meno di un decimo dei nuovi ingressi, dall'inizio del 2025
🔹 21% → 14% — anche la quota di personale tecnico già junior sul totale è calata, mentre l'organico complessivo dell'azienda è triplicato nello stesso periodo
🔹 6 a 1 — il rapporto tra le ore di lavoro svolte dagli agenti Claude diretti dai dipendenti e quelle del personale umano, raggiunto entro agosto 2026 secondo lo stesso report

Questi numeri non dicono che un agente sostituisce un giovane ingegnere uno a uno — dicono che il lavoro di routine su cui un junior imparava facendo si sta spostando sugli agenti, e che il ruolo umano si sposta verso la supervisione, l'architettura e la verifica. È esattamente il presidio che un agente, da solo, non sa fare: non basta orchestrare più lavoro, serve chi ne governa la qualità e i rischi prima che arrivi in produzione.

Nella tua azienda, chi sta ridisegnando i ruoli junior intorno agli agenti AI — e chi, invece, sta solo tagliando le assunzioni? 👇"""


CAPTION_3 = """🔥 Il mito: un'azienda che ha messo in produzione degli agenti AI sa cosa fanno, quando lo fanno, e può fermarli se sbagliano.

Il report «State of Agentic AI and API Security» di Salt Security, pubblicato questa settimana su oltre 380 professionisti di sicurezza, racconta una realtà diversa.

🔹 86,4% — delle organizzazioni ha già almeno un agente AI in funzione, e il 59,5% ne ha più di dieci: l'adozione è già massiccia, ben oltre la fase sperimentale
🔹 49,8% — delle organizzazioni ha confermato o sospettato che un agente abbia compiuto un'azione non intenzionale o non autorizzata nell'ultimo anno, più spesso una chiamata API esterna o una modifica di dati
🔹 12,5% — la quota di aziende che riesce a tracciare con continuità l'intero percorso di un agente, dall'istruzione iniziale al risultato finale: per il resto servirebbero ore o giorni per ricostruirlo a posteriori
🔹 17,5% — la quota che può arrestare automaticamente, in produzione, un agente che si comporta in modo anomalo: per gli altri quattro su cinque, fermarlo richiede un intervento manuale

Il problema non è se usare gli agenti AI — l'86% delle aziende lo fa già — ma che l'adozione è corsa più veloce della capacità di tracciarli e governarli. È lo stesso scarto che il vibe coding ha aperto sul codice: prototipare con l'AI è ormai alla portata di chiunque, ma l'architettura, i permessi e il controllo di cosa un agente può davvero fare restano un lavoro da presidiare con competenze senior, non da lasciare all'entusiasmo del primo pilota.

Nella tua azienda, qualcuno saprebbe ricostruire cosa ha fatto un agente AI ieri — o ci vorrebbero giorni? 👇"""


CAPTION_4 = """Dopo i dati di ieri su quanto poco le aziende riescano a tracciare i propri agenti AI, ci siamo chiesti: noi, internamente, sapremmo rispondere? Questa settimana abbiamo messo alla prova proprio questo.

→ Abbiamo preso uno dei flussi di lavoro interni in cui usiamo agenti AI (ricerca, prima bozza di contenuti, controlli di qualità) e abbiamo provato a ricostruire, a posteriori, ogni passaggio che l'agente aveva fatto per arrivare al risultato finale.
→ [Da personalizzare con l'esito reale della prova del team: quanto è stato semplice o difficile ricostruire il percorso, quali passaggi erano opachi, cosa avete dovuto aggiungere per renderlo tracciabile — senza inventare cifre o esiti non verificati.]
→ La lezione non è «serve uno strumento di monitoraggio in più», ma che la tracciabilità va progettata insieme al flusso di lavoro fin dall'inizio, non aggiunta a posteriori quando qualcosa è già andato storto.

La vostra azienda saprebbe ricostruire, oggi, cosa ha fatto un agente AI interno nell'ultima settimana? Raccontatecelo 👇

#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Innovazione"""


CAPTION_5 = """Nel 2000 il NIST ha scelto le curve crittografiche alla base di ECDSA, uno degli standard di sicurezza più usati al mondo — comprese quelle che probabilmente proteggono anche parte del traffico della tua azienda. Da allora un dettaglio restava un mistero: da dove venivano i numeri di partenza di quelle curve? Il sospetto, mai confermato, era una backdoor della NSA. Questa settimana Anthropic ha raccontato come Claude lo ha risolto in meno di mezz'ora.

→ Un generatore di numeri «casuali» in realtà non lo è mai del tutto: parte sempre da un valore iniziale, il seed. Se conosci il seed e il metodo, puoi ricostruire ogni numero che ha prodotto — è la base di molta crittografia, e anche il punto debole se quel seed nasconde qualcosa.
→ Per 25 anni i ricercatori hanno provato a spiegare i seed delle curve NIST con un'ipotesi (un testo trasformato in un calcolo di verifica): sbagliata. Claude ha cambiato approccio, ha ipotizzato un generatore casuale tipico degli anni '90, trovato un pattern sospetto nei numeri, e con un metodo matematico ha ricostruito lo stato interno di quel generatore.
→ Risultato: i seed derivano semplicemente dall'orario del computer tra il 1997 e il 1998 — un dato banale, non una backdoor. La cosa interessante non è che il mistero fosse innocente, ma che un modello AI lo abbia risolto in 30 minuti dopo che più ricercatori umani avevano seguito la pista sbagliata per anni.

Ti è mai capitato che un'AI risolvesse un problema tecnico aperto da tempo semplicemente cambiando l'ipotesi di partenza? Raccontaci il caso 👇

#AI #TechExplained #Crittografia #B2B #Innovazione"""


CAPTION_6 = """Lo studio AI.DEA di Nomisma, presentato questa settimana al Forum di Varignana su oltre 200 PMI italiane (Machinery, Agrifood, Motor Valley), fotografa un'Italia produttiva che sta usando l'AI più per iniziativa dei singoli che come scelta aziendale.

🔹 45% — delle PMI usa l'AI in modo informale, per iniziativa dei singoli dipendenti; il 21% non la usa affatto: due aziende su tre restano senza un utilizzo strutturato
🔹 4% — usa l'AI per trasformare il proprio modello di business, e l'8% ha sviluppato processi AI-driven: il resto si ferma all'automazione di singole attività o a un uso estemporaneo
🔹 50% — indica la mancanza di competenze interne come primo ostacolo, e 7 aziende su 10 non hanno ancora avviato un percorso di formazione sull'AI, pur riconoscendo nel 57% dei casi che le competenze sono la leva più importante
🔹 56% — di chi usa o prevede di usare l'AI destina meno dello 0,5% del fatturato alla tecnologia, e il 23% non prevede risorse specifiche: l'intenzione c'è più spesso del budget

Il divario che descrive questo studio non è tra chi ha l'AI e chi no — è tra chi la lascia all'iniziativa dei singoli e chi la trasforma in un processo aziendale, con competenze e budget dedicati. Ed è esattamente lì che si gioca la differenza tra un esperimento isolato e un vantaggio competitivo reale.

Nella tua azienda l'AI è un'iniziativa dei singoli o un processo con un responsabile e un budget? 👇

#IntelligenzaArtificiale #PMI #DigitalTransformation #B2B #Formazione"""
