# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 23 - 29 novembre 2026.

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

CAPTION_1 = """Questa settimana il fornitore più centrale dell'intero boom AI ha perso, da un giorno all'altro, l'unico CEO che abbia mai avuto: il 12 novembre Nvidia ha annunciato le dimissioni con effetto immediato di Jensen Huang da Presidente e CEO, dopo 33 anni alla guida dell'azienda che ha fondato nel 1993. Il consiglio non ha fornito alcuna motivazione ufficiale, ha nominato ad interim l'attuale CFO Colette Kress e ha aperto la ricerca di un successore permanente. Cinque giorni dopo, il 17 novembre, Nvidia ha riportato una trimestrale da record — ma il titolo ha comunque ceduto, per l'incertezza sulla governance futura.

→ Il 12 novembre Nvidia ha annunciato le dimissioni immediate di Jensen Huang da Presidente e CEO, dopo 33 anni alla guida dell'azienda: nessuna motivazione ufficiale, Colette Kress (CFO) nominata CEO ad interim, ricerca aperta per un successore permanente.
→ Il 17 novembre Nvidia ha riportato un fatturato trimestrale di 115,8 miliardi di dollari (+103% anno su anno) — ma il titolo ha comunque perso circa il 7% nella settimana, un calo attribuito esplicitamente alle preoccupazioni sulla successione.
→ È il caso scuola del rischio legato a una singola figura chiave, su scala enorme: numeri da record non bastano se manca chiarezza su chi guida l'azienda da cui dipende la roadmap hardware di quasi ogni progetto AI al mondo.

La tua azienda ha un piano esplicito per il giorno in cui una figura chiave — interna o di un fornitore critico — non c'è più? 👇

#Nvidia #IntelligenzaArtificiale #Leadership #Governance #B2B"""


CAPTION_2 = """🔥 Il mito: se un fornitore AI dichiara contrattualmente "zero data retention" sui tuoi prompt, puoi fidarti e non c'è altro da controllare — è una clausola, non una promessa che va verificata nei fatti.

Il ricercatore di sicurezza HD Moore ha inviato circa 2 milioni di prompt contenenti link di tracciamento univoci e credenziali finte attraverso provider di inferenza AI su OpenRouter etichettati "Zero Data Retention" (ZDR) — la dichiarazione contrattuale che il fornitore non legge né conserva i dati. Tre provider, tra cui MiniMax, hanno aperto quei link-trappola tra le 40 e le 130 ore dopo l'invio: prova diretta che i prompt venivano letti, nonostante l'etichetta. OpenRouter li ha rimossi dalla piattaforma dopo la segnalazione.

🔹 Il test: circa 2 milioni di prompt con link-trappola e credenziali finte, inviati attraverso provider etichettati "zero data retention"
🔹 Tre provider, tra cui MiniMax, hanno aperto quei link tra le 40 e le 130 ore dopo l'invio — prova che i prompt venivano letti nonostante la clausola
🔹 OpenRouter ha rimosso i tre provider dopo la segnalazione: l'etichetta da sola non bastava a garantire quello che prometteva

Il problema non è se il tuo fornitore AI abbia scritto "zero data retention" nel contratto — è che nessuno l'aveva verificato finché un ricercatore indipendente non ha inviato prompt-trappola per controllare. Una clausola di privacy non testata è un'ipotesi, non una garanzia.

La tua azienda ha mai verificato nei fatti, non solo nel contratto, come un fornitore AI tratta i tuoi prompt? 👇"""


CAPTION_3 = """🔥 Il mito: una volta che un chatbot ha dei guardrail di sicurezza dichiarati e dei controlli parentali, il rischio per gli utenti più vulnerabili è gestito — il resto è responsabilità di chi lo usa.

Il 17 novembre il procuratore generale dell'Oregon, Dan Rayfield, ha intentato una causa da 2,035 miliardi di dollari contro OpenAI, accusando l'azienda di aver messo consapevolmente in pericolo gli utenti minorenni di ChatGPT e di aver fuorviato il pubblico sulle misure di sicurezza adottate. La causa arriva dopo mesi in cui diverse famiglie hanno già fatto causa a OpenAI per episodi di conversazioni dannose con minori, e dopo che l'azienda aveva introdotto controlli parentali in risposta a quei casi precedenti.

🔹 Il procuratore generale dell'Oregon chiede oltre 2 miliardi di dollari, accusando OpenAI di aver saputo dei rischi per i minori e di non aver agito abbastanza in fretta
🔹 La causa arriva dopo mesi di azioni legali simili da parte di famiglie, e dopo che OpenAI aveva già introdotto controlli parentali in risposta a episodi precedenti
🔹 Avere delle misure di sicurezza dichiarate non ha impedito che la pressione legale si materializzasse comunque, con una cifra e un'accusa specifiche

Dichiarare dei guardrail non equivale a dimostrare che bastano: la differenza, per chi li costruisce come per chi li usa, è quanto spesso vengono messi davvero alla prova — non solo annunciati.

La tua azienda tratta le misure di sicurezza AI come una casella da spuntare, o come qualcosa da verificare nel tempo? 👇"""


CAPTION_4 = """Dopo la notizia di questa settimana — un ricercatore ha scoperto che alcuni fornitori di inferenza AI leggevano i prompt nonostante una clausola contrattuale di "zero data retention" — ci siamo fatti la domanda scomoda: sappiamo davvero cosa dicono, nel dettaglio, i contratti dei fornitori AI che usiamo ogni giorno? Questa settimana li abbiamo riletti.

→ Abbiamo elencato tutti i fornitori AI terzi che il team usa (modelli, provider di inferenza, estensioni), e per ciascuno recuperato la clausola esatta su conservazione e uso dei dati, non solo il riassunto commerciale.
→ [Da personalizzare con l'esito reale della verifica del team: quali clausole erano più vaghe del previsto, quali fornitori avete deciso di verificare più a fondo o sostituire, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi o esiti non verificati.]
→ La domanda utile non è se i contratti esistano — di norma esistono — ma se qualcuno in azienda li rilegge davvero, periodicamente, invece di darli per scontati dopo la firma.

La tua azienda rilegge periodicamente le clausole sui dati dei fornitori AI che usa, o solo alla firma del contratto? Raccontaci 👇

#IntelligenzaArtificiale #DataPrivacy #Esperienza #B2B #AIBusiness"""


CAPTION_5 = """Martedì abbiamo raccontato di tre fornitori AI che leggevano i prompt nonostante una clausola di "zero data retention". Ma come si fa, in pratica, a scoprire che qualcuno sta leggendo dati che ha promesso di non guardare? La risposta di questa settimana: un "canary token".

→ Un canary token è un link o una credenziale finta, unica per ogni destinatario, inserita in un documento o in un messaggio: se qualcuno la apre o la usa, lo sai — perché nessun altro aveva motivo di farlo.
→ Il ricercatore che ha scoperto il caso OpenRouter ha inserito link-canarino in circa 2 milioni di prompt inviati a provider che dichiaravano di non leggere i dati: quando tre di quei link sono stati aperti, ore o giorni dopo, la prova era inconfutabile.
→ La stessa logica si può applicare a qualunque flusso di dati aziendali che passa per terzi — fornitori cloud, partner, agenti AI con accesso a documenti — per verificare, non solo per fidarsi, chi accede davvero a cosa.

Conoscevi già questa tecnica per verificare chi accede davvero ai tuoi dati? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇

#AI #TechExplained #Cybersecurity #B2B #Innovazione"""
