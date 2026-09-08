# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 7-13 settembre 2026.

## Come si chiamano

Due casi, e questa settimana e' il secondo:

1. **Post derivati dal report** (il caso normale): il nome e'
   `CAPTION_<numero dell'idea nel report>` — `CAPTION_1` per la prima idea,
   e cosi' via. Lo assegna `plan.py`, ed e' legato all'indice perche' chi
   scrive i testi lavora sul report, dove le idee sono numerate.
2. **Post dichiarati a mano in `week.py`**: usano il nome che il post scrive
   nel proprio campo `caption`, come qui sotto. La corrispondenza non e'
   posizionale.

`python3 plan.py` elenca quali servono; `publish_buffer.py` si ferma se ne
manca uno, invece di creare una bozza senza testo.

I fatti citati qui sono gli stessi delle slide, con le stesse fonti. Se una
caption va corretta dopo la revisione umana, si corregge qui e si alza la
revisione del post in `week.REDO`: l'immagine non cambia, ma la bozza Buffer va
rifatta perche' il testo e' parte del post.
"""

CAPTION_NEWSAI = """Tre laboratori hanno annunciato qualcosa questa settimana. E hanno raccontato tre strategie completamente diverse.

OpenAI ha presentato GPT-6 Astra il 3 settembre. Greg Brockman lo ha definito «un salto generazionale», ma l'accesso iniziale è rimasto ai soli clienti del programma Daybreak — Forbes ha parlato di «curioso falso avvio».

Google ha rilasciato Gemini 3.8 Flash: il quarto modello «Flash» in 106 giorni. Il modello di punta 3.5 Pro, promesso per giugno, non si è visto.

Zhipu AI e Alibaba, fra il 26 e il 28 agosto, sono arrivate in modo indipendente alla stessa scelta architetturale, con un pricing open-weight molto aggressivo.

Il filo comune non è tecnico, è di metodo: chi deve scegliere una stack si trova davanti annunci che parlano di svolte, cadenze che cambiano ogni tre settimane e prezzi che ribaltano i conti. Il modello giusto quasi mai è l'ultimo uscito — è quello che si può cambiare senza riscrivere il prodotto.

Nella tua azienda la scelta del modello è una decisione di architettura, o si decide annuncio per annuncio? Raccontacelo nei commenti 👇

#IntelligenzaArtificiale #EnterpriseAI #AIStrategy #B2BTech #Digitiamo"""


CAPTION_FATIGUE = """Nel 2023 usciva un modello AI importante ogni 37 giorni e mezzo. Oggi ogni 11.

Il ciclo di valutazione di un'azienda, però, non si è accorciato allo stesso modo. E si vede.

Suresh Vasudevan, CEO di Clockwork Systems, citato da CNBC, lo dice senza giri di parole: «Se una startup vuole valutare dieci modelli AI per un certo compito, magari ne prende cinque». Metà delle opzioni non viene guardata — e la scelta finisce per premiare la notorietà del fornitore, non il caso d'uso.

Il costo di questa rincorsa non è il progresso: è la migrazione. Chi ha costruito un'astrazione fra il proprio prodotto e il fornitore di modelli aggiorna un endpoint. Chi non l'ha fatta riscrive — e lo rifà undici giorni dopo.

Non serve il modello più nuovo. Serve poterlo cambiare.

Quanto tempo passa, nella tua azienda, fra «questo modello è interessante» e «è in produzione»? 👇

#AIEngineering #IntelligenzaArtificiale #TeamAugmentation #B2BTech #Digitiamo"""


CAPTION_AGENTI = """Gli agenti AI non si schiantano. Derivano.

Il motivo per cui un agente smette di funzionare in azienda non è quasi mai «non ha capito». È molto più banale, e molto più prevedibile: funziona per due mesi, poi scade una chiave.

Un invalid_grant di Google o un INVALID_SESSION_ID di Salesforce, generati da un refresh token scaduto, non si recuperano riprovando. Nessuna logica di retry aiuta.

Il problema è che questi fallimenti sono silenziosi:

🔹 il tool restituisce un risultato vuoto e il modello lo legge come «nessun dato», non come errore;
🔹 scritture parziali corrompono lo stato dei passaggi successivi, senza alcun messaggio;
🔹 il modello inventa percorsi di recupero che somigliano a progresso e non lo sono.

Poi c'è l'inventario: gli agenti orfani — attivi, con credenziali valide, e nessuno che ne possieda il ciclo di vita — sono la norma, non l'eccezione. Non è una vulnerabilità esotica: è la conseguenza di non aver mai deciso chi ne risponde.

E quando il contesto diventa ostile, le catene di strumenti sono la superficie d'attacco. Casi documentati nel 2025-2026: una RCE nel protocollo MCP (CVE-2025-6514, CVSS 9,6) e un'iniezione via hooks in un agente di coding (CVE-2025-59536).

Il prototipo lo fa l'AI. La produzione è un mestiere: rotazione delle credenziali, allarmi sui fallimenti silenziosi, inventario degli agenti.

Nella tua azienda, chi si accorge se un agente ha smesso di funzionare davvero? 👇

#AIAgents #AIEngineering #Cybersecurity #TeamAugmentation #Digitiamo"""


CAPTION_AIACT = """Il pacchetto Omnibus ha rinviato le scadenze dell'AI Act. Nello stesso testo, però, ha allargato il perimetro — e questa parte è passata quasi inosservata.

In vigore dal 27 luglio 2026. Cosa si applica già adesso, senza rinvii:

🔹 Trasparenza (art. 50): dichiarare quando una persona sta interagendo con un sistema AI — dal 2 agosto 2026.
🔹 Watermarking dei contenuti generati: dal 2 agosto 2026, con tolleranza per i sistemi preesistenti fino al 2 dicembre 2026.
🔹 Divieti sui casi inaccettabili e obblighi sui modelli generalisti: già in vigore da febbraio e agosto 2025.

Cosa è stato rinviato: l'Allegato III al 2 dicembre 2027 (selezione del personale, credito, istruzione, infrastrutture critiche), l'Allegato I al 2 agosto 2028 (AI incorporata in prodotti già regolati), le sandbox al 2 agosto 2027.

Il dettaglio che ribalta la lettura corrente: la rilevazione dei bias è stata estesa, non ridotta. In cambio l'obbligo di alfabetizzazione AI è stato ammorbidito — da «garantire» un livello di competenza a «sostenerne lo sviluppo».

C'è anche un cambio di perimetro da valutare subito: la definizione di «componente di sicurezza» è stata restretta, quindi alcune AI incorporate nei prodotti cambiano classificazione.

La proroga serve a costruire, non ad aspettare. La compliance progressiva costa meno di una rincorsa.

La tua azienda ha già mappato dove usa l'AI, o aspetta la prossima scadenza per pensarci? 👇

Fonte: Regolamento (UE) 2026/1744

#AIAct #Compliance #IntelligenzaArtificiale #AIGovernance #Digitiamo"""
