# -*- coding: utf-8 -*-
"""Genera l'HTML del report PED settimanale Digitiamo."""
import html

# La palette NON e' dichiarata qui: viene dai token di brand, estratti dagli
# asset Canva reali (vedi brand-spec.md). I nomi storici usati dal layout del
# report sono mappati sui token, cosi' esiste una sola fonte di verita'.
from brand.tokens import COLORS as _C  # noqa: E402

C = {
    "navy": _C["navy"],
    "brand": _C["blue"],
    "secondary": _C["blue_soft"],
    "tint": _C["tint"],
    "green": _C["green"],
    "white": _C["white"],
}

WEEK_LABEL = "28 settembre – 4 ottobre 2026"
GENERATED_ON = "Lunedì 28 settembre 2026"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 22-28 settembre 2026, verificate su fonte diretta.
trends = [
    dict(
        title="Microsoft rifà Copilot da capo: ora è un'app per il lavoro, con agenti sotto controllo",
        what="Il 25 settembre Microsoft ha presentato la nuova Copilot: una \"super app\" che unifica chat, un modulo Code per creare app e dashboard senza programmare, e un modulo Autopilot per agenti che lavorano in autonomia su compiti come aggiornare progetti o raccogliere materiali. Ogni agente richiede però permessi espliciti, audit log completi e tracciamento, e Autopilot resta in una fase di test più ristretta rispetto al resto della suite. Microsoft 365 Copilot ha superato 30 milioni di postazioni pagate a luglio 2026, con le nuove attivazioni raddoppiate trimestre su trimestre.",
        why="È il primo grande vendor enterprise a mettere per iscritto, nel prodotto e non solo nel marketing, che l'autonomia degli agenti si vende insieme a permessi, log e tracciamento — non al loro posto. Per un'azienda che valuta un agente AI è la controprova pratica di quanto lavoro di governance serva davvero prima di lasciarlo agire da solo.",
        source="Microsoft (blog ufficiale)",
        url="https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/",
    ),
    dict(
        title="In Italia diventa reato non sorvegliare un'AI ad alto rischio: la norma entra in vigore proprio questa settimana",
        what="Il D.Lgs. 9 settembre 2026 n. 160, pubblicato in Gazzetta Ufficiale il 15 settembre, entra in vigore il 30 settembre. Introduce nel Codice penale l'articolo 437-bis: chi omette le misure di sicurezza o la sorveglianza umana su un sistema AI ad alto rischio, generando un pericolo concreto per persone o per la sicurezza dello Stato, rischia da 1 a 8 anni di reclusione. Si applica a provider, deployer e utilizzatori professionali. L'articolo 15 introduce anche il nuovo articolo 25-vicies nel D.Lgs. 231/2001: le organizzazioni rischiano sanzioni pecuniarie da 600 a 1.000 quote, oltre a eventuali sanzioni interdittive.",
        why="Non è più solo l'AI Act europeo, con le sue scadenze lontane (2027-2028): da questa settimana l'Italia ha una norma penale che si applica da subito, se gli obblighi sono già dovuti. La domanda «chi sorveglia i nostri sistemi AI ad alto rischio, e chi lo ha messo per iscritto» smette di essere teorica per chi lavora con clienti su selezione del personale, infrastrutture critiche o dispositivi con componenti di sicurezza AI.",
        source="BibLus (analisi del D.Lgs. 160/2026)",
        url="https://biblus.acca.it/notizie/il-nuovo-reato-in-materia-di-ia-in-vigore-dal-30-settembre-2026/",
    ),
    dict(
        title="Google ammette il ritardo: Gemini 4 entra in post-training, ma parte indietro sui benchmark",
        what="Il 23-24 settembre Koray Kavukcuoglu, a capo di Google DeepMind, ha confermato che Gemini 4 è entrato in post-training — la fase di ottimizzazione successiva all'addestramento iniziale, partito il 21 luglio — e punta a un rilascio «il prima possibile», senza indicare una data. Sull'Intelligence Index v4.3.2, il modello Google attualmente disponibile (Gemini 3.6 Flash) segna 34,0 punti, contro 57,6 di Claude Opus 5.5 (Anthropic) e 47,5 di GPT-6 Sol (OpenAI).",
        why="Quando il laboratorio con più risorse al mondo dichiara pubblicamente di essere indietro e di correre per recuperare, il messaggio per chi adotta l'AI in azienda è chiaro: aspettare «il modello definitivo» prima di investire in competenze non premia mai, perché il divario tra i laboratori si misura in settimane, non in anni.",
        source="Yahoo Finance / Forkast",
        url="https://finance.yahoo.com/technology/ai/articles/google-gemini-4-enters-post-122454510.html",
    ),
    dict(
        title="Ema raccoglie 77 milioni di dollari e dice il non detto: gli agenti AI vogliono il budget dei servizi IT, non solo del software",
        what="Il 23 settembre la startup Ema — «AI employees» che orchestrano processi HR, IT e finanza attraverso più applicazioni — ha chiuso una Serie B da 77 milioni di dollari (140 milioni raccolti in totale), guidata da Creaegis, con Accel, Section 32 e Prosus tra gli investitori. Il co-fondatore Surojit Chatterjee ha dichiarato che i clienti stanno già riducendo la dipendenza dalle grandi applicazioni SaaS — trasformandole «quasi solo in un database» — e che Ema sostituisce parte del lavoro di consulenza e implementazione delle società di servizi IT.",
        why="È la prima volta che un fornitore di agenti AI lo dice così esplicitamente: non punta solo al budget del software, punta al budget dei servizi. Per una società di consulenza tech è un avviso diretto, non un'ipotesi accademica — e la stessa settimana Microsoft mostra quanta governance serva davvero perché un agente possa agire in autonomia (vedi trend precedente).",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/23/ema-raises-77m-as-ai-starts-eating-into-enterprise-software-and-services/",
    ),
    dict(
        title="Il mercato AI italiano vale 1,8 miliardi (+50%), ma il divario delle PMI si misura ora in 37 punti percentuali",
        what="Il 25 settembre, in un confronto alla Camera dei Deputati, sono stati presentati i numeri più recenti sull'AI in Italia: il mercato ha raggiunto 1,8 miliardi di euro nel 2025, +50% sul 2024 (Osservatorio Artificial Intelligence, Politecnico di Milano). I dati Istat mostrano che il 16,4% delle imprese con almeno 10 addetti usa oggi tecnologie AI, il doppio rispetto all'8,2% del 2024 — ma le grandi aziende sono oltre il 50% e le PMI restano indietro di 37 punti percentuali. Gli annunci di lavoro che richiedono competenze AI sono cresciuti del 93% nel 2025. Al convegno, più di un relatore ha indicato la formazione — non l'investimento tecnologico — come la vera leva.",
        why="È la controprova, con fonti diverse (Istat, Politecnico di Milano, Camera dei Deputati), di quanto la crescita del mercato non chiuda da sola il divario tra chi ha già le competenze per adottare l'AI e chi ancora no: la domanda di competenze cresce più in fretta dell'offerta, esattamente il collo di bottiglia che un'azienda B2B italiana deve saper affrontare con un metodo, non con un modello migliore.",
        source="Teleborsa",
        url="https://www.teleborsa.it/News/2026/09/25/l-ai-vale-1-8-miliardi-in-italia-al-via-confronto-alla-camera-su-pmi-e-competenze-103.html",
    ),
    dict(
        title="Meta scala Muse, il suo agente AI personale: crescita più rapida di ChatGPT e un dispositivo indossabile dedicato",
        what="Meta ha lanciato Muse, agente AI personale con videochiamate ad avatar e controllo del computer su Mac, e nella settimana del 23-25 settembre ha annunciato un push commerciale su larga scala: pubblicità su tutte le piattaforme Meta, un dispositivo indossabile dedicato («Muse Charm») e una crescita del 55% settimana su settimana nelle prime due settimane — più del 24% registrato da ChatGPT nello stesso periodo dal lancio. L'app ha raggiunto il primo posto su App Store USA il 18 settembre.",
        why="Non è un prodotto B2B, ma segna quanto in fretta un agente AI «sempre presente», con accesso profondo a dati personali e dispositivi, possa diffondersi senza che nessuna azienda si sia posta la domanda di governance: lo stesso tema dei primi due trend, letto dal lato consumer.",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    ),
    dict(
        title="Nvidia valuta un investimento da 10 miliardi di dollari nell'IPO di Anthropic, quotata fino a 2.000 miliardi",
        what="Il 26 settembre Reuters ha riportato che Nvidia sta considerando un investimento fino a 10 miliardi di dollari come «anchor investor» nell'attesa IPO di Anthropic, che punta a raccogliere fino a 100 miliardi di dollari a una valutazione stimata attorno ai 2.000 miliardi. Sarebbe il secondo investimento di Nvidia in Anthropic dopo i 10 miliardi promessi a novembre 2025 (insieme a 5 miliardi di Microsoft), legati a un impegno di Anthropic di acquistare 30 miliardi di dollari di capacità Azure. Il CEO Jensen Huang aveva detto a marzo che quel primo investimento sarebbe stato «probabilmente l'ultimo» di Nvidia in Anthropic.",
        why="Un altro segnale di quanto capitale continui a confluire tra i grandi laboratori e i loro fornitori di calcolo — non verso chi deve ancora imparare a usare bene questi strumenti. Per le aziende italiane, il vantaggio competitivo non si giocherà mai su questi numeri: si gioca su chi sa integrare bene quello che l'infrastruttura rende disponibile a tutti.",
        source="The Motley Fool (dati Reuters)",
        url="https://www.fool.com/investing/2026/09/26/nvidia-is-weighing-a-usd10-billion-stake-in-anthropic-s-ipo-it-would-be-buying-its-own-demand/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Microsoft",
        what="Ha rifatto Copilot da capo come «super app»: chat unificata, un modulo Code per non-sviluppatori e un modulo Autopilot per agenti autonomi, che però richiede permessi espliciti, audit log completi e tracciamento prima di poter agire — e resta in una fase di test più ristretta del resto della suite.",
        positioning="Passa da chatbot personale caotico e disperso su più prodotti a piattaforma di lavoro unificata, con l'autonomia degli agenti venduta insieme ai controlli, non al loro posto.",
        angle="È la prova, dal vendor più grande del mercato, che oggi nessuno vende davvero «autonomia pura»: si vende autonomia più governance. Lo spunto per Digitiamo: il Team Augmentation esiste per mettere in campo chi quei controlli li sa progettare e gestire nel contesto specifico del cliente, non solo abilitarli a un livello di prodotto generico.",
    ),
    dict(
        name="Google DeepMind",
        what="Ha confermato pubblicamente che Gemini 4 è entrato in post-training, con l'obiettivo di lanciarlo «il prima possibile», mentre il modello attuale (Gemini 3.6 Flash) resta indietro di oltre 20 punti sull'Intelligence Index rispetto a Claude Opus 5.5 e GPT-6 Sol.",
        positioning="Gioca la carta della trasparenza sul proprio ritardo, forse per gestire le aspettative prima di un lancio compresso nei tempi rispetto al piano originale.",
        angle="Se il laboratorio con più risorse al mondo è pubblicamente indietro, il messaggio per un'azienda cliente è che il vantaggio competitivo non arriva aspettando il prossimo modello: arriva da come si integrano oggi gli strumenti già disponibili. È il terreno dell'AI Business Academy, non dell'attesa.",
    ),
    dict(
        name="Meta",
        what="Ha messo un budget marketing enorme dietro Muse, il suo agente AI personale, con pubblicità su tutte le piattaforme Meta e un dispositivo indossabile dedicato: crescita del 55% settimana su settimana, più rapida di ChatGPT al lancio.",
        positioning="Punta al consumatore di massa con un agente sempre presente, lontano dal terreno B2B, ma con la stessa domanda di fondo: chi controlla cosa un agente può fare con i dati personali che gli vengono affidati.",
        angle="Digitiamo non compete su questo terreno, ma la stessa domanda si pone in azienda su scala diversa: un agente che tocca ogni giorno dati aziendali sensibili ha bisogno di una governance pensata sull'architettura specifica del cliente, non di un prodotto consumer pronto all'uso.",
    ),
    dict(
        name="Ema",
        what="Ha raccolto 77 milioni di dollari in Serie B (140 totali) e ha dichiarato apertamente di voler prendere il budget dei servizi IT, non solo quello del software: i suoi «AI employees» orchestrano processi multi-step che prima passavano da un fornitore esterno.",
        positioning="Si presenta come alternativa outcome-based ai grandi SaaS e al lavoro di implementazione delle società di consulenza, non come un tool in più da affiancare a quelli esistenti.",
        angle="È la minaccia più diretta al modello di business dei servizi IT tradizionali — ma la stessa settimana Microsoft mostra che l'autonomia reale degli agenti richiede permessi, log e sorveglianza umana espliciti, e in Italia la sorveglianza umana su un sistema AI ad alto rischio diventa da questa settimana anche un obbligo di legge. Il lavoro non scompare: si sposta da «chi implementa» a «chi governa l'implementazione». Esattamente il Team Augmentation.",
    ),
    dict(
        name="Anthropic",
        what="Valuta un'IPO fino a 100 miliardi di dollari a una valutazione stimata di 2.000 miliardi, con Nvidia pronta a investire altri 10 miliardi come anchor investor, dopo i 10 miliardi già promessi a novembre 2025 insieme a Microsoft.",
        positioning="Consolida il proprio ruolo di laboratorio frontier più ricercato dai grandi investitori infrastrutturali, mentre il suo modello Opus 5.5 resta davanti nei benchmark citati questa settimana dalla stessa Google.",
        angle="Altri miliardi che continuano a confluire tra laboratori e fornitori di calcolo, non verso chi deve adottare questi strumenti bene. Lo spunto per Digitiamo: il vantaggio competitivo delle PMI italiane non si giocherà mai su questi numeri — si gioca su chi sa integrare bene quello che l'infrastruttura rende disponibile a tutti.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: dal quadro di settore (governance al posto
# dell'autonomia pura, sullo sfondo del nuovo reato AI italiano) a un mito da
# sfatare sull'autonomia degli agenti senza supervisione, a un'esperienza
# diretta che segue lo stesso filo proprio nel giorno in cui la norma entra
# in vigore (30/9), a un secondo mito-carosello sul gap delle PMI italiane, a
# una mini-lezione su cosa vuol dire "post-training" a partire da Gemini 4.
# Nessun post vende direttamente prima di mercoledì, e la vendita resta
# sempre organica.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 28/9",
        format="Thought leadership — apertura settimana",
        title="Il settore ha smesso di vendere autonomia. Ora vende *governance*",
        news="Nuova Copilot di Microsoft (Autopilot con permessi e audit log) + D.Lgs. 160/2026",
        news_url="https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/",
        hook="Questa settimana due notizie, senza alcun collegamento apparente, dicono la stessa cosa. Microsoft ha rifatto Copilot da capo e ha messo per iscritto che ogni agente autonomo (Autopilot) richiede permessi espliciti, audit log completi e tracciamento. E da mercoledì 30 settembre, in Italia, non sorvegliare un sistema AI ad alto rischio diventa reato: fino a 8 anni di reclusione per le persone, fino a 1.000 quote di sanzione per le aziende.",
        points=[
            "Non è un caso che arrivino nella stessa settimana: il mercato è passato dalla domanda «quanto può fare un agente da solo» alla domanda «chi risponde di quello che fa». Anche il vendor che vuole vendere autonomia costruisce prima i freni (fonte: Microsoft).",
            "Il D.Lgs. 160/2026 introduce l'articolo 437-bis del Codice penale: si applica a provider, deployer e utilizzatori professionali di sistemi AI ad alto rischio, e prevede sanzioni per le organizzazioni fino a 1.000 quote tramite il D.Lgs. 231/2001 (fonte: BibLus).",
            "Nello stesso periodo, in Italia il mercato AI cresce del 50% e sfiora i 2 miliardi di euro — ma il gap di competenze tra grandi aziende e PMI resta di 37 punti percentuali (fonte: Politecnico di Milano, Istat). La crescita del mercato non chiude da sola quel divario.",
        ],
        cta="Nella tua azienda chi è oggi, per iscritto, il responsabile della sorveglianza umana su un sistema AI? Raccontacelo nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #AIGovernance #DigitalTransformation #B2B #Tech",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 29/9",
        format="Mito da sfatare",
        title="Gli agenti AI possono già sostituire un fornitore di servizi senza supervisione umana? Il prodotto pensato apposta per l'autonomia dice il *contrario*",
        news="Copilot Autopilot (Microsoft) + raccolta Serie B di Ema",
        news_url="https://techcrunch.com/2026/09/23/ema-raises-77m-as-ai-starts-eating-into-enterprise-software-and-services/",
        hook="🔥 Il mito: gli agenti AI sono ormai pronti a sostituire un team di consulenza o un fornitore di servizi IT, senza bisogno di persone che li supervisionino.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il prodotto lanciato proprio questa settimana per vendere quell'autonomia dice il contrario.",
        points=[
            "Questa settimana Ema, che vende «AI employees» capaci di orchestrare processi HR, IT e finanza, ha raccolto 77 milioni di dollari dichiarando di voler prendere il budget dei servizi IT tradizionali, non solo quello del software.",
            "La stessa settimana, Microsoft ha rifatto Copilot e ha messo per iscritto che Autopilot — il modulo pensato apposta per gli agenti autonomi — richiede permessi espliciti, audit log completi e tracciamento prima di poter agire, e resta in una fase di test più ristretta del resto della suite.",
            "Da mercoledì 30 settembre, in Italia omettere la sorveglianza umana su un sistema AI ad alto rischio non è più solo un rischio operativo: è un reato specifico, con sanzioni fino a 8 anni di reclusione per le persone e fino a 1.000 quote per le organizzazioni (D.Lgs. 160/2026).",
        ],
        myth_closing="Il vibe coding — e ora il vibe delegation — abbassano la barriera per far agire un agente. Non abbassano quella per decidere chi lo sorveglia: quella, da questa settimana, è anche un obbligo legale, non solo una buona pratica. Il lavoro non scompare: si sposta da chi implementa a chi governa l'implementazione.",
        cta="Nella tua azienda, chi ha oggi il compito di dire a un agente «questa azione non la fai da solo»? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 30/9",
        format="Esperienza diretta (template)",
        title="Abbiamo dato a un agente accesso reale a un processo interno. Ecco dove abbiamo tenuto la sorveglianza *umana*",
        news="Copilot Autopilot (Microsoft) + entrata in vigore del D.Lgs. 160/2026",
        news_url="https://biblus.acca.it/notizie/il-nuovo-reato-in-materia-di-ia-in-vigore-dal-30-settembre-2026/",
        is_template=True,
        hook="[DA PERSONALIZZARE] Proprio oggi, 30 settembre, entra in vigore in Italia la norma che rende la sorveglianza umana sui sistemi AI ad alto rischio un obbligo di legge, non solo una buona pratica. Questa settimana abbiamo voluto testare su [un processo reale del team] quanto possiamo davvero delegare a un agente, e dove restiamo noi a decidere.",
        points=[
            "[DA PERSONALIZZARE] Cosa avete fatto fare all'agente — quale processo, quale strumento, con quali permessi concessi e quali no.",
            "Come Microsoft con Autopilot questa settimana, anche noi abbiamo trattato i permessi come una scelta esplicita, non come un default: cosa l'agente poteva fare da solo, cosa doveva passare da una persona, e chi era quella persona.",
            "[DA PERSONALIZZARE] Un aneddoto reale del team: dove l'agente ha sorpreso in positivo, e dove invece la supervisione umana ha evitato un errore che sarebbe passato inosservato.",
        ],
        closing="Il punto non è se un agente sa lavorare da solo su un pezzo di processo: spesso sa farlo. Il punto è chi ha deciso, per iscritto, dove finisce la sua autonomia — perché da oggi, in Italia, è anche una responsabilità legale.",
        cta="Qual è la vostra esperienza nel delegare un processo vero a un agente? Ci interessa confrontarci 👇",
        hashtags="#AIEngineering #TeamAugmentation #SoftwareDevelopment #Tech #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 1/10",
        format="Carosello dati (mito da sfatare — il gap delle PMI italiane)",
        title="Il mercato AI italiano cresce del 50%. Le PMI stanno recuperando terreno? I numeri raccontano un'altra *storia*",
        news="Confronto alla Camera dei Deputati, dati Politecnico di Milano e Istat",
        news_url="https://www.teleborsa.it/News/2026/09/25/l-ai-vale-1-8-miliardi-in-italia-al-via-confronto-alla-camera-su-pmi-e-competenze-103.html",
        hook="🔥 Il mito: se il mercato AI italiano cresce così in fretta, il divario tra grandi aziende e PMI si sta chiudendo da solo.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I numeri presentati questa settimana alla Camera dei Deputati raccontano una storia diversa.",
        points=[
            "1,8 miliardi di euro: il valore del mercato AI in Italia nel 2025, +50% sul 2024 (Osservatorio Artificial Intelligence, Politecnico di Milano).",
            "16,4% delle imprese italiane con almeno 10 addetti usa oggi tecnologie AI, il doppio rispetto all'8,2% del 2024 (Istat).",
            "37 punti percentuali: il divario di adozione tra grandi aziende (oltre il 50%) e PMI, ampio quasi quanto è veloce la crescita del mercato.",
            "+93% gli annunci di lavoro che richiedono competenze AI nel 2025 (Osservatorio Politecnico di Milano): la domanda di competenze cresce più in fretta dell'offerta.",
            "Al convegno alla Camera, più di un relatore ha detto la stessa cosa con parole diverse: la formazione deve precedere l'investimento tecnologico, non seguirlo.",
        ],
        myth_closing="Il mercato può crescere del 50% all'anno senza che il divario si chiuda di un solo punto: cresce chi ha già le competenze per adottare l'AI, non chi aspetta che il mercato lo faccia per lui. Il gap si chiude formando le persone sui casi d'uso reali dell'azienda, non aspettando che la tecnologia diventi più semplice da sola.",
        cta="Nella tua PMI la carenza di competenze AI è già un freno riconosciuto, o non ne parla ancora nessuno? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 2/10",
        format="Divulgativo stile Datapizza",
        title="Cosa vuol dire davvero che un modello AI «entra in post-training»? Spiegato *semplice*",
        news="Gemini 4 entra in post-training (Google DeepMind)",
        news_url="https://finance.yahoo.com/technology/ai/articles/google-gemini-4-enters-post-122454510.html",
        hook="Questa settimana Google ha detto che Gemini 4 è «entrato in post-training». Suona come gergo interno da laboratorio. Cosa vuol dire davvero, e perché dovrebbe interessare a un'azienda che adotta l'AI?",
        points=[
            "Il pre-training è la fase in cui un modello impara a prevedere il testo leggendo enormi quantità di dati: è potente ma grezzo, e da solo produce un modello che sa «continuare» un testo, non che sa essere utile o sicuro. Gemini 4 ha iniziato questa fase il 21 luglio 2026.",
            "Il post-training è tutto quello che viene dopo: si insegna al modello a seguire istruzioni, a essere utile su compiti specifici e a rifiutare richieste dannose — di solito con tecniche come l'apprendimento per rinforzo dal feedback umano. È la fase che trasforma un modello grezzo in un prodotto usabile davvero in azienda.",
            "Per questo la notizia non è «Gemini 4 sta arrivando»: è che Google ha ammesso pubblicamente il proprio ritardo (34 punti contro 57,6 di Claude Opus 5.5 sull'Intelligence Index) proprio mentre entra nella fase decisiva. Il post-training è spesso dove si vede la differenza reale tra un modello che sembra potente sulla carta e uno che funziona bene sui casi d'uso concreti — la stessa differenza che conta quando un'azienda valuta quale modello adottare, non solo quale ha il punteggio più alto.",
        ],
        cta="Quando scegli un modello AI per la tua azienda, guardi più ai benchmark o ai test sui tuoi casi d'uso reali? Dicci la tua 👇",
        hashtags="#AI #TechExplained #Innovazione #B2B #MachineLearning",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati — rassegna delle mosse della settimana",
        title="Quattro mosse, una direzione sola: la settimana vista dai *numeri*",
        news="Copilot (Microsoft) + Ema + Muse (Meta) + possibile investimento Nvidia nell'IPO di Anthropic",
        news_url="https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/",
        hook="Quattro notizie separate di questa settimana, lette insieme, raccontano la stessa direzione: dall'autonomia pura alla governance, dal software ai servizi, dal consumatore all'azienda, e capitali sempre più grandi sull'infrastruttura.",
        points=[
            "30 milioni di postazioni Microsoft 365 Copilot pagate a luglio 2026, con nuove attivazioni raddoppiate trimestre su trimestre — ma ogni agente autonomo richiede permessi espliciti e audit log.",
            "77 milioni di dollari raccolti da Ema in una settimana in cui dichiara di voler prendere il budget dei servizi IT, non solo del software.",
            "55% di crescita settimanale per Muse, l'agente AI personale di Meta, più rapida del 24% registrato da ChatGPT al lancio.",
            "10 miliardi di dollari: l'investimento che Nvidia valuta come anchor investor nell'IPO di Anthropic, a una valutazione stimata di 2.000 miliardi.",
        ],
        closing="Nessuna di queste quattro notizie riguarda direttamente un'azienda di 50 o 200 persone in Italia. Tutte e quattro, insieme, spiegano perché il vantaggio competitivo si giocherà su chi integra bene questi strumenti con le persone giuste, non su chi li costruisce o su chi ci investe.",
        cta="Quale di queste quattro mosse pensi avrà il maggiore impatto sul modo in cui lavoriamo entro un anno? 👇",
        hashtags="#AINews #TechTrends #B2B #Innovazione #IntelligenzaArtificiale",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci ha insegnato sull'AI in *azienda*",
        news="Sintesi dei trend della settimana 22-28 settembre 2026",
        news_url="https://biblus.acca.it/notizie/il-nuovo-reato-in-materia-di-ia-in-vigore-dal-30-settembre-2026/",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie AI degli ultimi 7 giorni.",
        points=[
            "Anche il vendor che vuole vendere autonomia (Microsoft, con Copilot Autopilot) costruisce prima i permessi e i controlli: l'autonomia pura non è ancora — e forse non sarà mai — il prodotto che si vende davvero.",
            "In Italia, dal 30 settembre, non sorvegliare un sistema AI ad alto rischio è un reato specifico: la governance interna non è più solo una buona pratica.",
            "Il mercato AI italiano cresce del 50% e sfiora i 2 miliardi, ma il divario di competenze tra grandi aziende e PMI resta di 37 punti percentuali: la crescita del mercato non forma le persone al posto tuo.",
            "Un fornitore di agenti (Ema) dice apertamente di voler prendere il budget dei servizi IT: il lavoro di consulenza non scompare, si sposta verso chi sa governare l'automazione, non verso chi la subisce.",
            "Anche Google, il laboratorio con più risorse, ammette di essere indietro sui benchmark: il vantaggio competitivo non arriva aspettando il modello definitivo.",
        ],
        closing="Nessuno di questi punti richiede un modello migliore. Tutti richiedono qualcuno che se ne occupi con un metodo.",
        cta="Qual è la notizia della settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #IntelligenzaArtificiale #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 28/9",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 29/9",
        time="12:15",
        format="Mito da sfatare (autonomia degli agenti)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — e prepara il terreno al post del giorno dopo, quando la norma sulla sorveglianza umana entra in vigore.",
    ),
    dict(
        day="Mercoledì 30/9",
        time="08:30",
        format="Esperienza diretta",
        reason="Picco assoluto di traffico professionale B2B della settimana, e giorno esatto in cui entra in vigore il D.Lgs. 160/2026: massima tempestività. Il formato genera meno reach ma più commenti/DM da decision maker, per questo va nel giorno di massima visibilità organica.",
    ),
    dict(
        day="Giovedì 1/10",
        time="12:15",
        format="Carosello dati / mito da sfatare (gap PMI italiane)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di due giorni dal primo mito per non saturare lo stesso formato. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e qui porta un secondo dato pesante (gap di competenze PMI) che merita spazio proprio, non solo un accenno nell'apertura.",
    ),
    dict(
        day="Venerdì 2/10",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello «la settimana vista dai numeri»",
        reason="Banca contenuti: utile come secondo documento se questa settimana c'è margine di pubblicazione, o come apertura news della settimana successiva. Non promossa a Prioritario questa settimana: i 5 slot fissi dello schema (apertura, due miti, esperienza diretta, divulgativo) sono già tutti occupati, e nessuno di essi va sacrificato per fare spazio a un secondo carosello.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo la settimana successiva.",
    ),
]
