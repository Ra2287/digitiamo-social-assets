# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 16 - 22 novembre 2026 (rigenerata).

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
"""

CAPTION_1 = """Questa settimana la differenza fra parlare di agenti AI e farli lavorare davvero si è vista nei numeri: il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno e oltre 1 milione di transazioni al mese — con l'obiettivo di triplicare i workflow entro il 2027. Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud.

→ Quasi 500 — i workflow agentici che AT&T gestisce oggi in produzione, con l'obiettivo di triplicarli entro il 2027: non una demo, ma un programma con una struttura interna dedicata (la "Business Agent Foundry").
→ Ogni workflow parte con supervisione umana: l'autonomia arriva solo quando l'accuratezza raggiunge la fascia medio-alta del 90%, con monitoraggio continuo dopo la rimozione del controllo diretto.
→ Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori diretti con Salesforce, NetSuite e Workday, mentre OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende e Adobe ha reso Firefly uno studio creativo con agenti sempre attivi.

La tua azienda sta già misurando quanto lavoro reale affida agli agenti AI, o lo guarda ancora da fuori? 👇

#IntelligenzaArtificiale #AI #AgentiAI #Innovazione #B2B"""


CAPTION_2 = """🔥 Il mito: se il contratto con il tuo fornitore AI promette "zero data retention" — l'impegno a non conservare i tuoi dati — allora quei dati restano al sicuro, punto.

Notion ha comunicato che una violazione al proprio fornitore di infrastruttura AI, Fireworks AI, ha esposto le chat AI di una minoranza dei propri spazi di lavoro. Fireworks aveva con Notion un impegno contrattuale di "zero data retention": il contratto c'era. Le indagini di Notion hanno trovato che i dati erano stati conservati comunque sugli endpoint usati.

🔹 L'intrusione è iniziata il 6 ottobre ed è arrivata ai sistemi di produzione di Fireworks il 24 ottobre; Fireworks ha notificato Notion il 2 novembre e confermato l'accesso non autorizzato il 6 novembre
🔹 Esposte le trascrizioni delle chat AI usate per la funzione "Insights" (che classifica come i membri di un'azienda usano l'AI) e per l'inferenza di modelli open-weight — meno dell'1% degli spazi di lavoro Notion, secondo l'azienda
🔹 Notion si è disconnessa da Fireworks, ha cancellato i dati conservati lì, disabilitato Insights durante l'indagine e consiglia a chi è coinvolto di ruotare password e chiavi incollate nelle chat AI nel periodo interessato

Il problema non è se il tuo fornitore AI sia in malafede — probabilmente non lo è. È che una clausola contrattuale descrive un impegno, non una verifica tecnica: senza un controllo periodico su cosa succede davvero ai dati lungo la catena di sub-fornitori, un'azienda scopre che la promessa non ha retto solo quando arriva la notifica di violazione.

La tua azienda ha mai verificato, oltre al contratto, cosa succede davvero ai dati lungo la catena dei fornitori AI che usa? 👇"""


CAPTION_3 = """Il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione — non una demo, ma un programma con una struttura di governance precisa su quando un agente può lavorare senza supervisione diretta.

→ 500 — i workflow agentici che AT&T gestisce oggi in produzione (quasi), con l'obiettivo dichiarato di triplicarli entro il 2027
→ 45 miliardi — i token AI elaborati ogni giorno dalla piattaforma, saliti da 27 miliardi a marzo 2026
→ 1 milione — le transazioni mensili gestite dalla piattaforma di agenti AI di AT&T, secondo l'azienda
→ 90% — la soglia di accuratezza (fascia medio-alta) che un workflow deve raggiungere prima che AT&T rimuova la supervisione umana diretta
→ 5 volte — il ritorno sugli investimenti in AI di produzione dichiarato da AT&T entro un anno (dato dell'azienda stessa, non verificato in modo indipendente)

Il salto di scala è reale: quasi 500 workflow agentici, 45 miliardi di token al giorno, un obiettivo di triplicare tutto entro il 2027. Ma il dettaglio che vale di più non è la scala — è la regola che la rende sostenibile: ogni workflow parte con supervisione umana, e la perde solo quando l'accuratezza supera una soglia fissata in anticipo, non quando qualcuno decide che "probabilmente va bene così". I dati di AT&T vengono dall'azienda stessa e non sono stati verificati in modo indipendente.

La tua azienda ha già fissato una soglia esplicita prima di togliere la supervisione umana a un agente AI, o la decisione resta informale? 👇

#AgentiAI #IntelligenzaArtificiale #Innovazione #B2B #Automazione"""


CAPTION_4 = """Dopo il caso di questa settimana — un fornitore AI che prometteva contrattualmente "zero data retention" e non l'ha rispettata — ci siamo fatti la domanda scomoda: i fornitori AI che usiamo noi rispettano davvero quello che promettono? Questa settimana abbiamo riletto i contratti e controllato le impostazioni reali, non solo quello che c'è scritto nelle condizioni.

→ Abbiamo elencato tutti i fornitori AI usati dal team (modelli, strumenti di scrittura, trascrizione, analytics) e per ciascuno cercato la clausola di data retention nel contratto o nei termini di servizio.
→ [Da personalizzare con l'esito reale della verifica del team: quali fornitori avevano impostazioni diverse da quanto promesso nel contratto, cosa avete dovuto disattivare o cambiare, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi di fornitori o esiti non verificati.]
→ La domanda utile non è se un contratto esista — quasi sempre esiste — ma se qualcuno in azienda lo ha mai messo alla prova chiedendo al fornitore una prova tecnica, non solo una dichiarazione scritta.

La tua azienda ha mai chiesto a un fornitore AI una prova tecnica della "zero data retention", non solo una dichiarazione scritta? Raccontaci 👇

#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness"""


CAPTION_5 = """Questa settimana abbiamo raccontato due storie opposte con lo stesso protagonista: AT&T, che gestisce quasi 500 agenti AI in produzione togliendo la supervisione umana solo sopra una soglia di accuratezza fissata in anticipo — e un attaccante che ha usato lo stesso tipo di strumento per violare Chainstack, un fornitore di infrastruttura blockchain. Ma cosa vuol dire davvero "agente AI", e perché non è solo un chatbot più furbo?

→ Un chatbot risponde a una domanda e si ferma lì. Un agente AI, invece, riceve un obiettivo, decide da solo i passaggi per raggiungerlo e usa degli "strumenti" — accesso a un database, a una casella email, a un sistema aziendale — per eseguirli senza bisogno di istruzioni passo-passo.
→ Questa capacità di agire, non solo rispondere, è anche il motivo per cui un agente è potente quanto i permessi che gli vengono dati: AT&T lo governa con soglie di accuratezza esplicite prima di togliere la supervisione; nel caso Chainstack, invece, l'attaccante ha usato un framework di agenti AI per automatizzare i passaggi dell'attacco, dopo essere entrato da una singola configurazione lasciata con le credenziali di default.
→ La domanda da farsi prima di dare un obiettivo a un agente AI, in azienda o nelle mani sbagliate, è sempre la stessa: a cosa può accedere davvero, e chi se ne accorge se usa quell'accesso in un modo che non ci si aspettava?

Conoscevi già la differenza tra un chatbot e un agente AI che agisce da solo? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇

#AI #TechExplained #AgentiAI #B2B #Innovazione"""
