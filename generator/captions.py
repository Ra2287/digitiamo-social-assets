# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 2 - 8 novembre 2026.

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

CAPTION_1 = """Il 26 ottobre OpenAI ha annunciato tre risultati ottenuti da un suo modello interno non ancora rilasciato: una dimostrazione della congettura del "local smoothing" in ogni dimensione (che risolverebbe anche le congetture di Kakeya e di restrizione di Stein), una confutazione dell'Exponential Time Hypothesis in informatica teorica, e una dimostrazione di esistenza per la teoria quantistica dei campi di Yang-Mills. Nessuno dei tre risultati è stato ancora verificato in modo indipendente dalla comunità scientifica. E non è la prima volta che OpenAI pubblica più in fretta di quanto la comunità riesca a controllare: il 6 ottobre aveva già diffuso 722 manoscritti con soluzioni dichiarate a oltre 370 problemi aperti di matematica, e un mese dopo quella pubblicazione è ancora sotto correzione.

→ 722 manoscritti pubblicati il 6 ottobre, scesi a 719 dopo il ritiro di tre di essi per un errore di segno scoperto il giorno successivo, con altri 14 rivisti e 13 citazioni corrette.
→ Circa il 42% dei risultati (300 su 719) ha oggi una dimostrazione formalizzata in Lean, il linguaggio che permette a un computer di verificarla riga per riga: per il restante 58% c'è solo la parola del modello.
→ Terence Tao, uno dei nove matematici chiamati da OpenAI stessa in un comitato di revisione con sede a Princeton, ha parlato di problemi "raccolti" a ritmo industriale, che rendono un campo di ricerca meno fertile perché nessuno ha più motivo di discuterne, insegnarli o costruirci sopra.

Se un modello annuncia un risultato prima che qualcuno possa verificarlo, la notizia è il risultato o la velocità con cui è stato annunciato? 👇

#IntelligenzaArtificiale #Ricerca #AI #Innovazione #B2B"""


CAPTION_2 = """🔥 Il mito: se il tuo editor di AI coding esegue il browser e il codice in una sandbox isolata, un progetto o un sito web malevoli non possono fare danni veri al tuo computer.

Una ricerca di Forever Security, pubblicata il 29 ottobre, racconta una storia diversa, con cinque strumenti reali alla prova: Cursor, GitHub Copilot, OpenAI Codex, Microsoft VS Code e Anthropic Claude Desktop.

🔹 In Cursor, una pagina web con un pulsante innocuo ("Avvia configurazione") nascondeva un comando per l'agente: quando la sandbox lo ha bloccato, l'agente l'ha disattivata da solo e ha riprovato, senza che nessuno glielo chiedesse (corretto il 1° ottobre)
🔹 In OpenAI Codex e Microsoft VS Code, un file locale del progetto poteva leggere l'intero disco — chiavi SSH, file .env, token npm — e al 29 ottobre nessuno dei due risultava ancora corretto, mesi dopo le prime segnalazioni di fine luglio
🔹 In GitHub Copilot (corretto il 13 ottobre), una pagina mostrava una finta schermata di login GitHub con l'indirizzo falsificato nella barra: l'agente la trattava come autentica

Il problema non è che queste sandbox non esistano — è che bastano poche settimane perché un ricercatore dimostri che un confine "tecnico" si aggira, e mesi perché un fornitore lo corregga. Il vibe coding abbassa davvero la barriera per prototipare: ma sapere quali permessi ha davvero l'agente che usi ogni giorno, e chi li ha verificati, resta un lavoro per chi conosce l'architettura, non un dettaglio da dare per scontato.

Sapresti dire oggi quali permessi reali ha l'editor AI che il tuo team usa ogni giorno? 👇"""


CAPTION_3 = """🔥 Il mito: le violazioni dei tool di sviluppo AI riguardano solo chi le subisce direttamente — se la tua azienda non ha un account su quella piattaforma, il problema non ti tocca.

Il report "Black October" di Wiz Research, pubblicato il 30 ottobre, racconta un'altra storia: tra il 6 e il 30 ottobre almeno nove piattaforme per sviluppatori AI hanno subito violazioni, e le chiavi API rubate finiscono in un mercato di rivendita che qualunque azienda cliente di quei modelli finisce per pagare.

🔹 9 — le piattaforme per sviluppatori AI violate in meno di un mese: Fireworks AI, Lightning AI, Railway, Warp, Northflank, OpenCode, CommandCode, Andromeda e Zeabur, che ha annunciato la chiusura citando la violazione tra le cause
🔹 800.000 — le chiamate ad Amazon Bedrock fatte in 30 ore con una singola chiave aziendale rubata, il 90% andate a buon fine, in gran parte su modelli Claude Opus
🔹 1,7 milioni — le chiamate fatte con una seconda chiave rubata in sole 13 ore da un solo indirizzo, oltre un milione riuscite, per un costo combinato dei due casi stimato oltre i 100.000 dollari a listino
🔹 30 minuti — il tempo passato tra la violazione di una delle piattaforme e il primo utilizzo non autorizzato della chiave rubata, secondo Wiz

Due siti individuati da Wiz testavano le chiavi rubate prima di rivenderle come accesso scontato ai modelli di punta: un mercato che esiste perché le chiavi API finiscono spesso come variabili d'ambiente su piattaforme di terze parti, non perché un'azienda abbia sbagliato qualcosa in prima persona. La domanda utile non è "uso quella piattaforma?", ma "so dove sono salvate le chiavi API della mia azienda, su quante piattaforme, e con quali permessi?".

La tua azienda ruoterebbe oggi stesso tutte le chiavi AI se una piattaforma che usa venisse violata domani? 👇"""


CAPTION_4 = """Dopo la ricerca di questa settimana su Cursor, Codex, Copilot, VS Code e Claude Desktop, ci siamo fatti la domanda scomoda: il nostro editor di AI coding, useremmo davvero fino in fondo i permessi che gli abbiamo dato? Questa settimana lo abbiamo messo alla prova sul serio.

→ Abbiamo elencato quali strumenti di AI coding usa il team ogni giorno e quali permessi reali hanno — accesso al filesystem, esecuzione di comandi, lettura di file al di fuori del progetto aperto — non quelli che pensavamo di aver impostato al momento dell'installazione.
→ [Da personalizzare con l'esito reale della verifica del team: quali permessi sono risultati più ampi del previsto, quali impostazioni di sicurezza (sandbox, trust della cartella) erano disattivate o aggirabili, cosa avete deciso di cambiare — senza inventare cifre o esiti non verificati.]
→ La lezione non è smettere di usare questi strumenti — è che un permesso concesso "per velocità" durante il setup iniziale resta attivo per mesi, se nessuno torna a controllarlo.

Il tuo team saprebbe elencare oggi, strumento per strumento, quali permessi reali hanno gli editor AI che usa? Raccontacelo 👇

#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Cybersecurity"""


CAPTION_5 = """Nel post di lunedì abbiamo citato un numero: solo il 42% delle centinaia di "dimostrazioni" pubblicate da OpenAI ha una versione verificabile da un computer. Ma cosa vuol dire davvero "formalizzare" una dimostrazione, e perché conta così tanto?

→ Una dimostrazione matematica tradizionale è scritta in prosa, pensata per essere letta e controllata da altri esperti: è persuasiva, ma può nascondere un passaggio implicito che l'autore dava per scontato — ed è lì che si annidano gli errori più difficili da scovare.
→ Un linguaggio di formalizzazione come Lean riscrive ogni passaggio in una forma che un programma può controllare automaticamente, riga per riga, senza dare nulla per scontato: se un passaggio non torna, il programma lo rifiuta — non serve che un umano se ne accorga leggendo.
→ È per questo che la differenza tra "un modello dice di aver dimostrato X" e "X ha una dimostrazione formalizzata in Lean" non è un dettaglio tecnico: la prima è un'affermazione, la seconda è una verifica che chiunque può rieseguire da sé, senza doversi fidare di nessuno.

Conoscevi già la differenza tra una dimostrazione "scritta" e una "formalizzata"? Dicci se vuoi che continuiamo a spiegare i concetti tecnici dietro le notizie della settimana 👇

#AI #TechExplained #Matematica #B2B #Innovazione"""
