# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 28 settembre - 4 ottobre 2026.

Post derivati dal report (caso normale): il nome e' `CAPTION_<numero
dell'idea nel report>` — `CAPTION_1` per la prima idea, e cosi' via, assegnato
da `plan.py` e legato all'indice perche' chi scrive i testi lavora sul report,
dove le idee sono numerate.

Le idee Prioritario hanno una caption: le Riserva (idee 6 e 7) non generano
asset finche' non vengono attivate (vedi week.py), quindi non servono ancora.
"""

CAPTION_1 = """Questa settimana due notizie, senza alcun collegamento apparente, dicono la stessa cosa. Microsoft ha rifatto Copilot da capo e ha messo per iscritto che ogni agente autonomo (Autopilot) richiede permessi espliciti, audit log completi e tracciamento. E da mercoledì 30 settembre, in Italia, non sorvegliare un sistema AI ad alto rischio diventa reato: fino a 8 anni di reclusione per le persone, fino a 1.000 quote di sanzione per le aziende.

→ Non è un caso che arrivino nella stessa settimana: il mercato è passato dalla domanda «quanto può fare un agente da solo» alla domanda «chi risponde di quello che fa». Anche il vendor che vuole vendere autonomia costruisce prima i freni (fonte: Microsoft).
→ Il D.Lgs. 160/2026 introduce l'articolo 437-bis del Codice penale: si applica a provider, deployer e utilizzatori professionali di sistemi AI ad alto rischio, e prevede sanzioni per le organizzazioni fino a 1.000 quote tramite il D.Lgs. 231/2001 (fonte: BibLus).
→ Nello stesso periodo, in Italia il mercato AI cresce del 50% e sfiora i 2 miliardi di euro — ma il gap di competenze tra grandi aziende e PMI resta di 37 punti percentuali (fonte: Politecnico di Milano, Istat). La crescita del mercato non chiude da sola quel divario.

Nella tua azienda chi è oggi, per iscritto, il responsabile della sorveglianza umana su un sistema AI? Raccontacelo nei commenti 👇

#IntelligenzaArtificiale #AIGovernance #DigitalTransformation #B2B #Tech"""


CAPTION_2 = """🔥 Il mito: gli agenti AI sono ormai pronti a sostituire un team di consulenza o un fornitore di servizi IT, senza bisogno di persone che li supervisionino.

Il prodotto lanciato proprio questa settimana per vendere quell'autonomia dice il contrario.

🔹 Questa settimana Ema, che vende «AI employees» capaci di orchestrare processi HR, IT e finanza, ha raccolto 77 milioni di dollari dichiarando di voler prendere il budget dei servizi IT tradizionali, non solo quello del software
🔹 La stessa settimana, Microsoft ha rifatto Copilot e ha messo per iscritto che Autopilot — il modulo pensato apposta per gli agenti autonomi — richiede permessi espliciti, audit log completi e tracciamento prima di poter agire, e resta in una fase di test più ristretta del resto della suite
🔹 Da mercoledì 30 settembre, in Italia omettere la sorveglianza umana su un sistema AI ad alto rischio non è più solo un rischio operativo: è un reato specifico, con sanzioni fino a 8 anni di reclusione per le persone e fino a 1.000 quote per le organizzazioni (D.Lgs. 160/2026)

Il vibe coding — e ora il vibe delegation — abbassano la barriera per far agire un agente. Non abbassano quella per decidere chi lo sorveglia: quella, da questa settimana, è anche un obbligo legale, non solo una buona pratica. Il lavoro non scompare: si sposta da chi implementa a chi governa l'implementazione.

Nella tua azienda, chi ha oggi il compito di dire a un agente «questa azione non la fai da solo»? 👇"""


CAPTION_3 = """[DA PERSONALIZZARE] Proprio oggi, 30 settembre, entra in vigore in Italia la norma che rende la sorveglianza umana sui sistemi AI ad alto rischio un obbligo di legge, non solo una buona pratica. Questa settimana abbiamo voluto testare su [un processo reale del team] quanto possiamo davvero delegare a un agente, e dove restiamo noi a decidere.

→ [Personalizza: cosa avete fatto fare all'agente — quale processo, quale strumento, con quali permessi concessi e quali no]
→ Come Microsoft con Autopilot questa settimana, anche noi abbiamo trattato i permessi come una scelta esplicita, non come un default: cosa l'agente poteva fare da solo, cosa doveva passare da una persona, e chi era quella persona
→ [Personalizza: un aneddoto reale del team, dove l'agente ha sorpreso in positivo, e dove invece la supervisione umana ha evitato un errore che sarebbe passato inosservato]

Il punto non è se un agente sa lavorare da solo su un pezzo di processo: spesso sa farlo. Il punto è chi ha deciso, per iscritto, dove finisce la sua autonomia — perché da oggi, in Italia, è anche una responsabilità legale.

Qual è la vostra esperienza nel delegare un processo vero a un agente? Ci interessa confrontarci 👇

#AIEngineering #TeamAugmentation #SoftwareDevelopment #Tech #Innovazione"""


CAPTION_4 = """🔥 Il mito: se il mercato AI italiano cresce così in fretta, il divario tra grandi aziende e PMI si sta chiudendo da solo.

I numeri presentati questa settimana alla Camera dei Deputati raccontano una storia diversa.

🔹 1,8 miliardi di euro: il valore del mercato AI in Italia nel 2025, +50% sul 2024 (Osservatorio Artificial Intelligence, Politecnico di Milano)
🔹 16,4% delle imprese italiane con almeno 10 addetti usa oggi tecnologie AI, il doppio rispetto all'8,2% del 2024 (Istat)
🔹 37 punti percentuali: il divario di adozione tra grandi aziende (oltre il 50%) e PMI, ampio quasi quanto è veloce la crescita del mercato
🔹 +93% gli annunci di lavoro che richiedono competenze AI nel 2025 (Osservatorio Politecnico di Milano): la domanda di competenze cresce più in fretta dell'offerta
🔹 Al convegno alla Camera, più di un relatore ha detto la stessa cosa con parole diverse: la formazione deve precedere l'investimento tecnologico, non seguirlo

Il mercato può crescere del 50% all'anno senza che il divario si chiuda di un solo punto: cresce chi ha già le competenze per adottare l'AI, non chi aspetta che il mercato lo faccia per lui. Il gap si chiude formando le persone sui casi d'uso reali dell'azienda, non aspettando che la tecnologia diventi più semplice da sola.

Nella tua PMI la carenza di competenze AI è già un freno riconosciuto, o non ne parla ancora nessuno? 👇"""


CAPTION_5 = """Questa settimana Google ha detto che Gemini 4 è «entrato in post-training». Suona come gergo interno da laboratorio. Cosa vuol dire davvero, e perché dovrebbe interessare a un'azienda che adotta l'AI?

→ Il pre-training è la fase in cui un modello impara a prevedere il testo leggendo enormi quantità di dati: è potente ma grezzo, e da solo produce un modello che sa «continuare» un testo, non che sa essere utile o sicuro. Gemini 4 ha iniziato questa fase il 21 luglio 2026.
→ Il post-training è tutto quello che viene dopo: si insegna al modello a seguire istruzioni, a essere utile su compiti specifici e a rifiutare richieste dannose — di solito con tecniche come l'apprendimento per rinforzo dal feedback umano. È la fase che trasforma un modello grezzo in un prodotto usabile davvero in azienda.
→ Per questo la notizia non è «Gemini 4 sta arrivando»: è che Google ha ammesso pubblicamente il proprio ritardo (34 punti contro 57,6 di Claude Opus 5.5 sull'Intelligence Index) proprio mentre entra nella fase decisiva. Il post-training è spesso dove si vede la differenza reale tra un modello che sembra potente sulla carta e uno che funziona bene sui casi d'uso concreti — la stessa differenza che conta quando un'azienda valuta quale modello adottare, non solo quale ha il punteggio più alto.

Quando scegli un modello AI per la tua azienda, guardi più ai benchmark o ai test sui tuoi casi d'uso reali? Dicci la tua 👇

#AI #TechExplained #Innovazione #B2B #MachineLearning"""
