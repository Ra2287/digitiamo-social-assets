# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 26 ottobre - 1 novembre 2026.

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

CAPTION_1 = """Giovedì scorso OpenAI ha detto ai propri investitori di volere le firme entro la settimana successiva per un round fino a 30 miliardi di dollari, a una valutazione di 1.250 miliardi di dollari — tagliata di 150 miliardi rispetto alla cifra discussa solo tre settimane prima. Lo stesso giorno, in Italia, era già in vigore da poco il decreto che per la prima volta dice chi vigila sull'AI Act e con quali poteri. E qualche giorno prima, un attacco informatico aveva già mostrato perché quella vigilanza serve: le chiavi API di migliaia di utenti di un tool di vibe coding, esposte in un attacco su larga scala.

→ OpenAI tratta un round fino a 30 miliardi di dollari a una valutazione pre-money di 1.250 miliardi di dollari — 150 miliardi in meno rispetto alla cifra di 1.400 miliardi circolata a inizio ottobre: anche i capitali più cercati del mercato si negoziano, non si dettano.
→ Dal 23 ottobre l'Italia ha un decreto che assegna ad AgID la valutazione di conformità dei sistemi AI e ad ACN la vigilanza di mercato, con sanzioni fino al 7% del fatturato mondiale per le pratiche vietate: la fase dei principi europei dichiarati lascia spazio a un'autorità che può davvero bussare alla porta.
→ Una settimana prima, una violazione di OpenCode — uno strumento open-source di vibe coding — aveva esposto le chiavi API collegate di circa l'1,4% dei suoi utenti, con addebiti non autorizzati fino a 1.700 dollari in una notte: il promemoria pratico di cosa succede quando l'adozione corre più veloce del controllo.

Nella tua azienda, chi tiene insieme la velocità con cui si adotta l'AI e la capacità di controllarla? Raccontacelo nei commenti 👇

#IntelligenzaArtificiale #Innovazione #Tech #B2B #AIStrategy"""


CAPTION_2 = """🔥 Il mito: se un tool di AI coding produce codice che funziona, va bene così — la sicurezza è un dettaglio da sistemare dopo, se mai servirà.

Una violazione di OpenCode, uno dei progetti open-source di vibe coding più usati, racconta una storia diversa, con numeri reali e non ipotetici.

🔹 1,4% — la quota di utenti di OpenCode Console coinvolti nella violazione del 17 ottobre: solo quelli che avevano collegato le proprie chiavi API di provider esterni (OpenAI, Anthropic, Google) — ma per loro l'esposizione è stata totale
🔹 1.700 dollari — l'addebito non autorizzato più alto segnalato da un singolo utente in una sola notte, dopo che le sue chiavi erano state usate in un «attacco di distillazione» su larga scala contro i modelli collegati
🔹 48 ore — il tempo per cui, secondo il co-fondatore del progetto, gli aggressori avevano già preso di mira i sistemi prima che la violazione venisse rilevata e comunicata agli utenti

Il problema non è che OpenCode sia uno strumento cattivo — è che collegare le proprie chiavi API a un tool di terze parti è una scelta architetturale, non un dettaglio di configurazione. Il vibe coding abbassa davvero la barriera per prototipare: ma dove finiscono le credenziali, chi può vederle, e cosa succede se il tool viene compromesso restano domande da porsi prima di collegare la prima chiave, non dopo aver letto la notizia della violazione successiva.

Nella tua azienda, qualcuno saprebbe dire oggi quali chiavi API sono collegate a quali strumenti di terze parti? 👇"""


CAPTION_3 = """🔥 Il mito: l'AI Act è una questione europea che riguarda i grandi laboratori americani — per una PMI italiana che usa ChatGPT o Copilot in ufficio, è ancora presto per preoccuparsene.

Il decreto legislativo 179/2026, in vigore dal 23 ottobre, dice qualcosa di diverso: assegna poteri di vigilanza concreti e fissa obblighi che riguardano anche le aziende più piccole.

🔹 35 milioni di euro o il 7% del fatturato mondiale — la sanzione massima per le pratiche AI vietate, qualunque sia maggiore: riguarda non solo chi sviluppa modelli, ma anche chi li usa in modo scorretto
🔹 15 milioni di euro o il 3% del fatturato — la sanzione per le altre violazioni degli obblighi, con criteri di proporzionalità: non sono multe automatiche, ma presuppongono che l'azienda possa dimostrare cosa ha fatto
🔹 23 aprile 2027 — la scadenza entro cui gli ordini professionali dovranno integrare le competenze sull'AI nella formazione dei propri iscritti: una data concreta da segnare, non un principio generico
🔹 2 autorità, non una — AgID valuta la conformità dei sistemi AI, ACN fa vigilanza di mercato con poteri di controllo e ispezione: restano attive anche Banca d'Italia, CONSOB, IVASS e il Garante privacy per i rispettivi ambiti

Il decreto non obbliga tutte le aziende a dimostrare la conformità domani mattina — ma dice chi può chiedere di vederla, con quali poteri, e a quali condizioni. Le decisioni su assunzione, modifica o cessazione di un rapporto di lavoro non possono più basarsi solo su un processo automatizzato, e serve una persona con reale potere decisionale; se l'AI incide su turni e carichi di lavoro, il rischio va documentato nel DVR aziendale. Aspettare un controllo per scoprire di non essere pronti costa più che organizzarsi ora.

La tua azienda saprebbe già oggi elencare quali strumenti AI usa, per cosa, e con quali responsabilità? 👇"""


CAPTION_4 = """Dopo la violazione di OpenCode di questa settimana, ci siamo fatti la domanda più scomoda: noi, internamente, sapremmo rispondere a «quali chiavi API sono collegate a quali strumenti, e chi le gestisce»? Questa settimana lo abbiamo verificato davvero.

→ Abbiamo fatto l'inventario degli strumenti AI di terze parti che il team usa ogni giorno — editor con AI integrata, tool di automazione, assistenti vari — ed elencato quali hanno accesso a chiavi API di provider come OpenAI o Anthropic.
→ [Da personalizzare con l'esito reale della verifica del team: quante chiavi sono risultate collegate più di quanto ci si aspettasse, quali strumenti erano stati aggiunti senza un processo di approvazione, cosa avete deciso di cambiare — senza inventare cifre o esiti non verificati.]
→ La lezione non è smettere di usare tool di AI coding o di produttività — è che l'inventario di chi ha accesso a cosa va fatto prima che serva, non dopo la prima notizia di violazione che riguarda uno strumento usato anche in casa.

La tua azienda ha un inventario aggiornato di quali tool AI hanno accesso a quali credenziali? Raccontacelo 👇

#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Cybersecurity"""


CAPTION_5 = """Nella violazione di OpenCode di questa settimana, gli aggressori hanno usato quello che è stato definito un «large-scale distillation attack». Ma cos'è la distillazione, prima ancora di diventare un attacco? È una delle tecniche più comuni per rendere l'AI più economica — ed è per questo che vale la pena capirla.

→ La distillazione, nel machine learning, è una tecnica legittima: si usa un modello grande e costoso come «insegnante» per addestrarne uno più piccolo ed economico, l'«allievo», facendogli imitare le risposte del primo. È uno dei motivi per cui oggi esistono modelli piccoli sorprendentemente capaci.
→ Diventa un problema quando la stessa tecnica viene usata senza autorizzazione: inviando un numero enorme di richieste a un modello altrui — con chiavi API rubate, come nel caso OpenCode — per raccogliere abbastanza risposte da addestrare un modello concorrente, a spese e sul traffico di qualcun altro.
→ È lo stesso motivo per cui le aziende dietro i grandi modelli limitano quante richieste si possono fare e monitorano pattern di utilizzo anomali: un volume di query «troppo sistematico» è spesso il primo segnale che qualcuno sta provando a copiare il modello, non solo a usarlo.

Avevi già sentito parlare di «distillazione» prima di questa notizia? Dicci se vuoi che continuiamo a spiegare i concetti tecnici dietro le notizie della settimana 👇

#AI #TechExplained #MachineLearning #B2B #Innovazione"""
