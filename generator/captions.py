# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 9 - 15 novembre 2026.

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

CAPTION_1 = """Giovedì 5 novembre l'indice Philadelphia Semiconductor (SOX) ha perso il 9,2% in una sola seduta, portando il bilancio della settimana a circa -12%: la quinta settimana consecutiva in negativo, la peggiore dall'aprile 2025. Nvidia ha perso fino al 7,5% intraday, AMD il 15%, Micron il 13%. Il detonatore sono le elezioni di midterm del 3 novembre, che hanno dato ai Democratici la maggioranza di Camera e Senato, alimentando l'opposizione politica alla costruzione di nuovi data center. Ma nella stessa settimana Goldman Sachs ha alzato la stima di capacità globale dei data center al 2030, e OpenAI ha chiuso una nuova tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi.

→ 9,2% — il calo in una sola seduta (giovedì 5 novembre) dell'indice SOX, il più forte da giugno; -12% il bilancio dell'intera settimana, la peggiore dall'aprile 2025.
→ Nvidia ha perso fino al 7,5% intraday (il suo calo più forte dall'aprile 2025), AMD il 15%, Micron il 13%, Intel il 9,2%; tra i fornitori di infrastrutture cloud per l'AI, CoreWeave ha perso il 12% e Nebius il 17%.
→ Il detonatore: le elezioni di midterm del 3 novembre hanno dato ai Democratici la maggioranza di Camera e Senato, alimentando l'opposizione politica ai nuovi data center — in Texas la governatrice eletta ha proposto una moratoria sulle nuove costruzioni.
→ Nella stessa settimana Goldman Sachs ha alzato la stima di capacità globale dei data center nel 2030 da 217 a 273 gigawatt, e OpenAI ha chiuso una prima tranche di finanziamento da 11 miliardi di dollari a una valutazione di 1.250 miliardi: l'offerta di capitale per l'AI non rallenta, proprio mentre il mercato inizia a dubitarne.

Se il mercato dubita della sostenibilità della scommessa sui data center AI, la tua azienda ha un piano che non dipende da quella scommessa? 👇

#IntelligenzaArtificiale #AI #Mercati #Innovazione #B2B"""


CAPTION_2 = """🔥 Il mito: se la tua azienda usa un fornitore AI affidabile, e quel fornitore non subisce mai una violazione diretta ai propri sistemi, i dati dei tuoi clienti restano al sicuro.

L'8 novembre Mixpanel, il fornitore di analytics usato da OpenAI sul proprio sito per sviluppatori, ha comunicato una violazione subita tramite una campagna di smishing (phishing via SMS). OpenAI non è stata attaccata direttamente: il suo fornitore sì — ed è bastato.

🔹 I dati sottratti riguardano i profili utente di platform.openai.com: nome, email, posizione approssimativa (città, stato, paese), sistema operativo, browser e ID di organizzazione o utente
🔹 OpenAI precisa che non sono stati compromessi contenuti o risposte di ChatGPT, chiavi API, password o dati di pagamento — ma avverte che i dati esposti possono comunque alimentare nuovi attacchi di phishing mirato
🔹 Mixpanel ha parlato di un "numero limitato" di clienti coinvolti, senza specificare quanti: la trasparenza su un fornitore terzo resta nelle mani del fornitore, non dell'azienda che lo ha scelto

Il problema non è se il fornitore che hai scelto sia affidabile — probabilmente lo è. È che ogni servizio AI che usi si appoggia a sua volta su altri fornitori (analytics, hosting, pagamenti), e la sicurezza dei tuoi dati dipende anche da quelli che non hai scelto tu direttamente. Sapere quali terze parti toccano i dati che affidi a uno strumento AI, e cosa succede se una di loro viene violata, è un lavoro di governance — non un dettaglio da dare per scontato.

La tua azienda saprebbe elencare oggi quali fornitori terzi toccano i dati che affida ai suoi strumenti AI? 👇"""


CAPTION_3 = """Il 6 novembre la procura federale del Distretto Sud di New York (SDNY) ha incriminato tre persone — Jacob Soall, Sharon Hazan e Guy Sheetrit — per una frode da 129 milioni di dollari ai danni di aziende in tutto il mondo, costruita impersonando con l'AI le voci e, in alcuni casi, i volti di CEO e avvocati nelle videochiamate con i reparti contabilità delle vittime.

→ 129 milioni di dollari — l'importo complessivo che la procura attribuisce alla frode, costruita impersonando con l'AI le voci e i volti di CEO e avvocati nelle videochiamate con i reparti contabilità delle vittime
→ 3 — gli imputati incriminati dal Distretto Sud di New York (SDNY): Jacob Soall, Sharon Hazan e Guy Sheetrit, indicati nell'atto d'accusa anche con soprannomi come "Rocky Balboa" e "Superman Cash"
→ 20 anni — la pena massima prevista per ciascun capo d'imputazione di frode telematica e riciclaggio di denaro, secondo la procura
→ 2 anni — la pena massima aggiuntiva prevista per il furto aggravato d'identità, il terzo reato contestato
→ Il meccanismo, secondo l'accusa: un'email che sembra del CEO chiede un'operazione finanziaria riservata; segue una chiamata o videochiamata con voce o volto clonati dall'AI, poi un falso avvocato chiede un bonifico verso conti esteri, e i fondi vengono convertiti in criptovalute

Dietro ogni cifra di questa truffa c'è una procedura che un'azienda strutturata avrebbe potuto far saltare: una verifica indipendente del bonifico, fuori dalla stessa catena di comunicazione che ha portato la richiesta. Non serve diffidare di ogni videochiamata — serve un secondo canale di conferma per ogni operazione finanziaria insolita, sempre. Le accuse non sono ancora state provate in tribunale.

La tua azienda ha oggi un secondo canale di verifica, fuori da email e videochiamata, per ogni bonifico insolito? 👇

#Cybersecurity #AI #Frode #B2B #Sicurezza"""


CAPTION_4 = """Dopo il caso di questa settimana — 129 milioni di dollari rubati impersonando CEO e avvocati con voce e volto clonati dall'AI — ci siamo fatti la domanda scomoda: il nostro team riconoscerebbe una voce clonata in una chiamata reale? Questa settimana lo abbiamo messo alla prova.

→ Abbiamo simulato una chiamata con una voce clonata (con il consenso esplicito di chi l'ha prestata) che chiedeva un'operazione finanziaria urgente e riservata, nello stile usato nel caso reale di questa settimana.
→ [Da personalizzare con l'esito reale del test del team: chi ha riconosciuto l'anomalia e come, quali segnali hanno insospettito o non insospettito le persone coinvolte, cosa è emerso sulle procedure di verifica attuali — senza inventare cifre o esiti non verificati.]
→ La domanda utile non è se la tecnologia per clonare una voce esiste — esiste già ed è alla portata di chiunque — ma se esiste, nella tua azienda, un secondo canale di verifica che non dipende dalla stessa chiamata.

Il tuo team saprebbe dire oggi quale procedura seguire se ricevesse una chiamata così? Raccontaci la tua esperienza 👇

#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness"""


CAPTION_5 = """Questa settimana abbiamo parlato di una frode da 129 milioni di dollari costruita con voci e volti di CEO clonati dall'AI. Ma cosa vuol dire davvero "clonare una voce", e perché oggi basta così poco per farlo?

→ Un modello di sintesi vocale moderno impara il timbro di una voce da pochi secondi o minuti di audio reale — un video pubblico, una registrazione di una call, un messaggio vocale — e lo riapplica a un testo nuovo, scritto da chi compie la truffa.
→ La parte difficile non è più tecnica: i modelli di voice cloning sono pubblicamente disponibili e a basso costo. La parte difficile, per chi li usa a fini fraudolenti, è ottenere abbastanza audio della persona da clonare — per questo i bersagli tipici sono dirigenti con una presenza pubblica (interviste, conferenze, video aziendali).
→ Lo stesso vale per il volto nelle videochiamate: un modello di "face swap" in tempo reale sovrappone un volto clonato su quello di chi parla davvero, frame per frame — la tecnologia dietro ai casi di videochiamate con CEO falsi di questa settimana.

Conoscevi già quanto poco audio serve oggi per clonare una voce? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇

#AI #TechExplained #Deepfake #B2B #Innovazione"""
