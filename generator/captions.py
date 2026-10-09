# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 12 - 18 ottobre 2026.

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

PED anticipato su richiesta di Ramona: generato il 9/10 per la settimana del
12-18 ottobre, invece che il lunedì mattina.
"""

CAPTION_1 = """In sette giorni: Google lancia Gemini 4 Argon dopo mesi di ritardo, Anthropic apre l'accesso ridotto ai suoi modelli a team di sicurezza verificati e rende noto che il progetto Glasswing ha trovato 129.000 vulnerabilità software, e OpenAI pubblica la sua filigrana testuale per conformarsi all'AI Act europeo. Tre mosse diverse, un solo filo conduttore: i laboratori stanno rispondendo, con prodotti concreti, ai problemi di sicurezza e fiducia emersi nelle settimane scorse.

→ Google ha scelto di far partire Gemini 4 Argon da un gruppo ristretto di esperti di cybersicurezza invece che da un rilascio generale: anche chi insegue la frontiera preferisce un pilota controllato a un lancio a tutta velocità.
→ Anthropic apre l'accesso con meno limiti ai propri modelli solo a professionisti verificati, su livelli diversi a seconda dell'uso — e lo fa mentre pubblica un numero enorme (129.000 vulnerabilità trovate dal progetto Glasswing) che mostra quanto lavoro di sicurezza ci sia ancora da fare sul codice, generato dall'AI o no.
→ La filigrana di OpenAI per rispettare l'AI Act europeo è un passo concreto verso la conformità, ma rileva il testo in modo molto diverso a seconda della lingua e sparisce quasi del tutto con un editing leggero: il tema del post di domani.

Quale di queste tre mosse pensi cambierà di più il modo in cui la tua azienda userà l'AI nei prossimi mesi? Dicci la tua nei commenti 👇

#IntelligenzaArtificiale #Innovazione #Tech #B2B #AIStrategy"""


CAPTION_2 = """🔥 Il mito: il codice prodotto con l'aiuto dell'AI — o comunque il codice che gira oggi nelle aziende — è sicuro quanto quello scritto e rivisto interamente da persone esperte.

I numeri che Anthropic ha reso pubblici il 7 ottobre, con il progetto Glasswing, raccontano una scala del problema diversa da quella che si immagina di solito.

🔹 129.000 — le vulnerabilità software verificate dal progetto Glasswing di Anthropic tra aprile e luglio 2026, con altre 5.500 confermate da scansioni open-source entro ottobre
🔹 33.000 — le vulnerabilità tra quelle classificate critiche o gravi: Anthropic stessa dice che il numero reale è probabilmente almeno cinque volte più alto, perché i dati arrivano solo da alcuni partner
🔹 Uno studio indipendente di Veracode, citato nello stesso articolo, ha trovato che circa il 44% dei task di generazione di codice con l'AI introduce una vulnerabilità rischiosa, con un tasso di sicurezza medio del 56%

Questi numeri non dicono che l'AI scrive codice peggiore di una persona — dicono che la scala a cui si scrive codice oggi, con o senza AI, ha superato la capacità delle revisioni manuali di stare al passo. Il problema non è lo strumento che scrive, è chi verifica prima che quel codice arrivi in produzione.

Nella tua azienda, chi rivede il codice prima che vada in produzione — e con quale metodo, non solo con quale strumento? 👇"""


CAPTION_3 = """🔥 Il mito: quando esce un nuovo modello AI più economico e con benchmark migliori, conviene sempre passare a quello.

I numeri pubblicati su Gemini 4 Argon, il nuovo modello di Google, raccontano una storia più complicata di un semplice «vince il più nuovo».

🔹 Argon supera Claude Opus 5.5 sul Vals Index (68,9% contro 67,0%) e su DeepSWE, un benchmark di sviluppo software (77,9% contro 74,2%)
🔹 Opus 5.5 batte invece Argon sul benchmark di ingegneria ML, PostTrainBench (49,3% contro 45,3%): nessuno dei due modelli vince su tutti i fronti testati
🔹 Il prezzo di lancio di Argon è di 2$ per milione di token in input e 10$ in output, contro i 4$/20$ di Opus 5.5 e i 10$/50$ di GPT-6 Astra: un costo nettamente più basso, ma secondo gli analisti non ancora definitivo
🔹 Un modello più economico su un compito dove serve più accuratezza può costare di più in correzioni e rilavorazioni: quello che conta è il costo per risultato ottenuto sul proprio caso d'uso, non il prezzo per milione di token

Scegliere un modello AI guardando solo un benchmark pubblico o il prezzo di listino è come scegliere un fornitore guardando solo il preventivo: dice qualcosa, ma non dice se il lavoro, su quel compito specifico, verrà fatto bene.

La tua azienda sceglie uno strumento AI guardando i benchmark, il prezzo, o i risultati su un caso d'uso reale testato prima? 👇"""


CAPTION_4 = """Dopo i dati di ieri su benchmark e prezzi dei modelli più recenti, ci siamo chiesti: nella pratica, su un compito reale per un cliente, cosa cambia davvero? Questa settimana lo abbiamo provato con un caso interno.

→ Abbiamo preso un compito concreto di analisi su un documento lungo (lo stesso tipo di lavoro per cui i nuovi modelli vengono presentati come più adatti) e lo abbiamo affidato al modello in test, confrontando il risultato con il nostro metodo abituale.
→ [Da personalizzare con l'esito reale del test del team: dove il modello ha funzionato meglio, dove ha avuto bisogno di una correzione umana, quanto tempo è stato risparmiato o perso davvero — senza inventare cifre o esiti non verificati.]
→ La lezione non è «questo modello è il migliore», ma «un modello nuovo va testato sul proprio caso d'uso prima di cambiare strumento, non adottato perché vince su un benchmark pubblico».

La vostra azienda ha già testato un modello di nuova generazione su un compito reale, o si affida ancora ai soli benchmark pubblicati? Raccontatecelo 👇

#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Innovazione"""


CAPTION_5 = """Il 5 ottobre OpenAI ha pubblicato textGrain, il sistema che userà per «firmare» i testi di ChatGPT nell'Unione Europea. Non è un timbro visibile, e non è neanche invisibile nel senso che si immagina di solito. Vale la pena capire come funziona davvero.

→ Un testo scritto da ChatGPT sembra identico a uno scritto da una persona, ma a ogni parola il modello sceglie, tra le alternative possibili, quella leggermente favorita da un calcolo statistico legato a una chiave segreta e alle parole precedenti.
→ Chi ha quella chiave può rileggere il testo e misurare se quel pattern statistico c'è: non serve nessun carattere nascosto o invisibile, serve solo rifare lo stesso calcolo e confrontarlo.
→ Il limite è proprio nella sua natura statistica: su un testo lungo e non modificato il rilevamento è alto (95% su 400 token in inglese), ma scende sotto editing leggero — sostituire un quarto delle parole con sinonimi lo fa crollare al 17% — e varia molto da una lingua europea all'altra.

Ti sembra una soluzione tecnica solida per sapere cosa è stato scritto da un'AI, o un primo passo ancora facile da aggirare? Dicci la tua 👇

#AI #TechExplained #AIAct #B2B #Compliance"""
