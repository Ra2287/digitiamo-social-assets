# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 16 - 22 novembre 2026.

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

CAPTION_1 = """Questa settimana quattro grandi fornitori hanno smesso di parlare di "agenti AI" come una demo e li hanno trasformati in prodotto: il 4 novembre Salesforce ha comunicato che il suo "coworker" AI ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in tre mesi. Il 10 novembre Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud. Nello stesso giro di giorni, un fornitore di infrastruttura blockchain (Chainstack) ha reso noto che un attaccante ha usato lo stesso tipo di strumento — un framework di agenti AI — per violare i propri sistemi.

→ 185.000 — gli utenti attivi di Agentforce Coworker di Salesforce a inizio novembre, con un uso cresciuto di 21 volte in tre mesi: il segnale più concreto di adozione reale visto finora.
→ Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori diretti con Salesforce, NetSuite e Workday, mentre OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende.
→ Un fornitore di infrastruttura blockchain, Chainstack, ha reso noto che un attaccante ha usato lo stesso tipo di strumento — un framework di agenti AI — per violare i propri sistemi: la tecnologia che fa crescere l'adozione può accelerare anche l'attacco.

La tua azienda sta già misurando quanto lavoro reale affida agli agenti AI, o lo guarda ancora da fuori? 👇

#IntelligenzaArtificiale #AI #AgentiAI #Innovazione #B2B"""


CAPTION_2 = """🔥 Il mito: se il contratto con il tuo fornitore AI promette "zero data retention" — l'impegno a non conservare i tuoi dati — allora quei dati restano al sicuro, punto.

Notion ha comunicato che una violazione al proprio fornitore di infrastruttura AI, Fireworks AI, ha esposto le chat AI di una minoranza dei propri spazi di lavoro. Fireworks aveva con Notion un impegno contrattuale di "zero data retention": il contratto c'era. Le indagini di Notion hanno trovato che i dati erano stati conservati comunque sugli endpoint usati.

🔹 L'intrusione è iniziata il 6 ottobre ed è arrivata ai sistemi di produzione di Fireworks il 24 ottobre; Fireworks ha notificato Notion il 2 novembre e confermato l'accesso non autorizzato il 6 novembre
🔹 Esposte le trascrizioni delle chat AI usate per la funzione "Insights" (che classifica come i membri di un'azienda usano l'AI) e per l'inferenza di modelli open-weight — meno dell'1% degli spazi di lavoro Notion, secondo l'azienda
🔹 Notion si è disconnessa da Fireworks, ha cancellato i dati conservati lì, disabilitato Insights durante l'indagine e consiglia a chi è coinvolto di ruotare password e chiavi incollate nelle chat AI nel periodo interessato

Il problema non è se il tuo fornitore AI sia in malafede — probabilmente non lo è. È che una clausola contrattuale descrive un impegno, non una verifica tecnica: senza un controllo periodico su cosa succede davvero ai dati lungo la catena di sub-fornitori, un'azienda scopre che la promessa non ha retto solo quando arriva la notifica di violazione.

La tua azienda ha mai verificato, oltre al contratto, cosa succede davvero ai dati lungo la catena dei fornitori AI che usa? 👇"""


CAPTION_3 = """Il 4 novembre Salesforce ha comunicato che Agentforce Coworker — l'agente AI a cui un dipendente assegna un compito, e che da solo pianifica e coordina i passaggi necessari — ha superato i 185.000 utenti attivi, con un uso cresciuto di 21 volte in appena tre mesi.

→ 185.000 — gli utenti attivi di Agentforce Coworker a inizio novembre 2026, secondo i dati diffusi da Salesforce
→ 21 volte — la crescita dell'uso del coworker AI in appena tre mesi, secondo Salesforce (dato dell'azienda stessa, non verificato in modo indipendente)
→ 50 dollari — il costo mensile per utente del coworker AI, in aggiunta alle licenze Salesforce già pagate dall'azienda
→ 3.000 — gli utenti di Fulton Bank che usano il coworker AI su oltre 20 casi d'uso diversi, dalle verifiche interne al supporto ai clienti
→ 40 — i paesi in cui Adecco Group sta estendendo l'uso del coworker AI nei propri processi, secondo Salesforce

Il salto di adozione è reale, non solo marketing: in tre mesi l'uso di un agente che pianifica ed esegue compiti da solo è cresciuto di 21 volte. Ma un'adozione che corre più veloce della governance lascia scoperta una domanda semplice: chi, in azienda, ha deciso a quali sistemi e dati l'agente può accedere, e chi controlla cosa fa davvero quando lavora senza supervisione diretta? I dati di crescita vengono da Salesforce stessa e non sono stati verificati in modo indipendente.

La tua azienda misura la crescita dell'uso degli agenti AI, o anche i permessi che gli ha dato? 👇

#AgentiAI #IntelligenzaArtificiale #Innovazione #B2B #Automazione"""


CAPTION_4 = """Dopo il caso di questa settimana — un fornitore AI che prometteva contrattualmente "zero data retention" e non l'ha rispettata — ci siamo fatti la domanda scomoda: i fornitori AI che usiamo noi rispettano davvero quello che promettono? Questa settimana abbiamo riletto i contratti e controllato le impostazioni reali, non solo quello che c'è scritto nelle condizioni.

→ Abbiamo elencato tutti i fornitori AI usati dal team (modelli, strumenti di scrittura, trascrizione, analytics) e per ciascuno cercato la clausola di data retention nel contratto o nei termini di servizio.
→ [Da personalizzare con l'esito reale della verifica del team: quali fornitori avevano impostazioni diverse da quanto promesso nel contratto, cosa avete dovuto disattivare o cambiare, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi di fornitori o esiti non verificati.]
→ La domanda utile non è se un contratto esista — quasi sempre esiste — ma se qualcuno in azienda lo ha mai messo alla prova chiedendo al fornitore una prova tecnica, non solo una dichiarazione scritta.

La tua azienda ha mai chiesto a un fornitore AI una prova tecnica della "zero data retention", non solo una dichiarazione scritta? Raccontaci 👇

#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness"""


CAPTION_5 = """Questa settimana abbiamo parlato di agenti AI che pianificano compiti, lavorano dentro Photoshop o aiutano i clienti a scoprire un'azienda su ChatGPT — e di un attaccante che ha usato lo stesso tipo di strumento per violare un'azienda. Ma cosa vuol dire davvero "agente AI", e perché non è solo un chatbot più furbo?

→ Un chatbot risponde a una domanda e si ferma lì. Un agente AI, invece, riceve un obiettivo, decide da solo i passaggi per raggiungerlo e usa degli "strumenti" — accesso a un database, a una casella email, a un sistema aziendale — per eseguirli senza bisogno di istruzioni passo-passo.
→ Questa capacità di agire, non solo rispondere, è anche il motivo per cui un agente è potente quanto i permessi che gli vengono dati: nel caso Chainstack di questa settimana, l'attaccante ha usato un framework di agenti AI per automatizzare i passaggi dell'attacco, dopo essere entrato da una singola configurazione lasciata con le credenziali di default.
→ La domanda da farsi prima di dare un obiettivo a un agente AI, in azienda o nelle mani sbagliate, è sempre la stessa: a cosa può accedere davvero, e chi se ne accorge se usa quell'accesso in un modo che non ci si aspettava?

Conoscevi già la differenza tra un chatbot e un agente AI che agisce da solo? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇

#AI #TechExplained #AgentiAI #B2B #Innovazione"""
