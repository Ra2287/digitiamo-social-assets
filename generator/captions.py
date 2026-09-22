# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 21-27 settembre 2026.

Post derivati dal report (caso normale): il nome e' `CAPTION_<numero
dell'idea nel report>` — `CAPTION_1` per la prima idea, e cosi' via, assegnato
da `plan.py` e legato all'indice perche' chi scrive i testi lavora sul report,
dove le idee sono numerate.

Le idee Prioritario hanno una caption: le Riserva (idee 6 e 7) non generano
asset finche' non vengono attivate (vedi week.py), quindi non servono ancora.
CAPTION_8 e' l'idea extra su Jev/TypeSafe AI, aggiunta dopo la revisione.
"""

CAPTION_1 = """Questa settimana Anthropic ha pubblicato per la prima volta un numero concreto: Claude guida oggi il 26% della propria ricerca interna, contro meno dell'1% a febbraio. Nello stesso periodo, in Italia, l'adozione dell'AI nelle imprese è raddoppiata in un anno, arrivando al 19,5%.

→ Il ritmo con cui l'AI accelera lo sviluppo di AI successiva non è più un dato di laboratorio: Anthropic misura 30.000 agenti al lavoro in contemporanea sulla propria piattaforma interna (fonte: Anthropic Institute).
→ In Italia il quadro è più incoraggiante di due settimane fa, ma resta diviso in due velocità: oltre il 50% delle grandi aziende usa già l'AI, contro il 15% delle piccole imprese (fonte: Unioncamere-Dintec).
→ Il collo di bottiglia non è mai stato l'accesso alla tecnologia: il 58,6% delle PMI indica la carenza di competenze come freno principale, e solo il 7% ha un percorso di formazione strutturato.

Nella tua azienda chi decide cosa l'AI può già fare da sola, e cosa no? Raccontacelo nei commenti 👇

#IntelligenzaArtificiale #DigitalTransformation #PMI #B2B #Tech"""


CAPTION_2 = """🔥 Il mito: gli agenti AI oggi scrivono codice di produzione da soli, il fattore umano nel «come» sta diventando superfluo.

Il caso più documentato dell'anno dice il contrario, e viene proprio da chi ha tutto l'interesse a raccontare il mito.

🔹 GitHub ha migrato 430.000 righe di Copilot da TypeScript a 832.000 righe Rust: gli agenti hanno scritto la maggior parte del codice, ma un solo sviluppatore senior ha diretto architettura, decisioni e revisione per 14,5 settimane
🔹 Lo stesso indice pubblicato da Anthropic questa settimana mostra che il 90% del lavoro di Claude sulla propria ricerca resta a livello di «collaborazione» con le persone: zero compiti rilevati come completamente autonomi
🔹 A maggio, uno sciame di agenti OpenAI aveva caricato oltre 3.000 pacchetti sospetti su RubyGems senza che nessuno se ne accorgesse per mesi: la prova di cosa succede quando quella supervisione manca

Il vibe coding abbassa la barriera per scrivere codice. Non abbassa quella per decidere l'architettura, la sicurezza e cosa può andare in produzione: quella resta — e resterà — un lavoro senior.

Nella tua azienda, chi ha oggi il compito di dire a un agente «questo codice non va in produzione»? 👇"""


CAPTION_3 = """[DA PERSONALIZZARE] Dopo il caso di GitHub di questa settimana — un runtime intero riscritto quasi solo da agenti, ma diretto da un solo sviluppatore senior — abbiamo voluto provarlo su [un progetto reale del team]: quanto lavoro possiamo davvero delegare, e dove restiamo noi a decidere.

→ [Personalizza: cosa avete fatto fare all'agente — refactoring, migrazione, un modulo nuovo — su quale codebase e con quale strumento]
→ Anche nel caso GitHub, il ruolo umano non è scomparso: si è spostato su definizione dei confini, arbitraggio delle decisioni tecniche e revisione, non sulla scrittura riga per riga
→ [Personalizza: un aneddoto reale del team, dove l'agente ha sorpreso in positivo, e dove invece ha servito l'occhio di qualcuno che conosceva l'architettura]

Il punto non è se un agente sa scrivere codice: lo sa fare, e bene. Il punto è chi decide cosa merita di arrivare in produzione.

Qual è la vostra esperienza nel delegare del codice vero a un agente? Ci interessa confrontarci 👇

#AIEngineering #SoftwareDevelopment #TeamAugmentation #Tech #Innovazione"""


CAPTION_4 = """🔥 Il mito: il gap AI delle piccole imprese italiane si chiude da solo, con il tempo e con l'adozione che via via si diffonde.

I numeri di questa settimana, letti insieme, raccontano una storia diversa.

🔹 19,5% delle imprese italiane usa oggi l'AI, il doppio rispetto a un anno fa (Unioncamere-Dintec)
🔹 Oltre il 50% delle grandi aziende la usa, contro il 15% delle piccole imprese: il divario per dimensione non si è chiuso, si è solo spostato più in alto
🔹 58,6% delle PMI indica la carenza di competenze digitali come freno principale all'adozione, non il costo, non la tecnologia
🔹 Solo il 7% delle PMI ha avviato un percorso di formazione AI strutturato sul tema
🔹 Secondo il professor Giuseppe Francesco Italiano (Luiss), almeno 6 aziende interessate su 10 abbandonano l'adozione AI per mancanza di competenze

La crescita c'è, ed è reale. Ma cresce più in fretta chi ha già le competenze per adottare l'AI di chi parte da zero: il gap non si chiude aspettando, si chiude formando le persone sui casi d'uso reali dell'azienda.

Nella tua PMI la carenza di competenze è già un freno riconosciuto, o non ne parla ancora nessuno? 👇"""


CAPTION_5 = """Questa settimana Anthropic ha detto che Claude «guida» il 26% della propria ricerca AI interna. Suona spaventoso, o rivoluzionario, a seconda di chi lo racconta. Cosa vuol dire davvero? Proviamo a spiegarlo senza fuffa.

→ «Guidare» un compito, nel linguaggio di Anthropic, non vuol dire farlo da solo: è una scala che va da assistenza a collaborazione a guida a piena autonomia. Il 90% del lavoro di Claude resta ai primi livelli, con un umano sempre nel ciclo: zero compiti classificati come completamente autonomi.
→ Il numero interessante non è il 26%, è il salto rispetto a febbraio 2026, quando era sotto l'1%: misura quanto rapidamente un laboratorio riesce a fidarsi delle proprie AI per accelerare lo sviluppo di quelle successive, non quanto le AI abbiano sostituito le persone.
→ Per questo Anthropic pubblica anche i numeri di controllo insieme al 26%: 30.000 agenti al lavoro in contemporanea, ma solo lo 0,002% delle decisioni bloccato dai sistemi automatici e circa 50 segnalazioni a settimana che arrivano a un revisore umano. Un numero senza l'altro racconterebbe solo metà della storia.

Ti sembra un buon modo di misurare quanto ci si può fidare dell'AI, o solo una statistica ben scelta? Dicci la tua 👇

#AI #TechExplained #Innovazione #B2B #RicercaAI"""


CAPTION_8 = """Questa settimana un laboratorio fondato da un ex OpenAI ha lanciato un modello che si rifiuta di scrivere testo. Si chiama Jev, risponde in meno di mezzo secondo e costa centinaia di volte meno di un modello generalista. Cosa fa, davvero?

→ Jev non genera linguaggio: restituisce decisioni strutturate con una probabilità già calcolata per ogni opzione — per esempio, smistare una richiesta cliente tra fatturazione, tecnico e vendite con un punteggio di confidenza per ciascuna. TypeSafe lo chiama «System One model»: veloce e strutturato, non conversazionale.
→ I numeri che rivendica sono netti: risposte in 70-500 millisecondi contro i minuti di un modello generalista, e un costo di 0,042 $ per milione di token in input, con output gratuito — 40 a 200 volte più veloce sui compiti per cui è stato costruito.
→ TypeSafe parla di «0% di hallucination», ma va letto con la qualifica giusta: un output strutturato non può essere malformato, ma può comunque essere sbagliato nel merito. Utile da ricordare ogni volta che un fornitore promette «zero errori»: la domanda giusta è sempre «zero errori di cosa».

Ti sembra un'evoluzione utile per automatizzare decisioni ripetitive in azienda, o resta un modello di nicchia? Dicci la tua 👇

#AI #TechExplained #Innovazione #B2B #MachineLearning"""
