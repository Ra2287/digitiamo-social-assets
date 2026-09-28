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
# Notizie del periodo 18-28 settembre 2026, verificate su fonte diretta.
# Revisione del 28/9: su richiesta di Ramona, la selezione privilegia le
# notizie con più impatto visivo/narrativo (l'AI fuori dallo schermo: sott'acqua,
# nello spazio, in TV) rispetto ai soli annunci enterprise SaaS.
trends = [
    dict(
        title="Il sottomarino australiano che l'AI pilota (quasi) da sola: cos'è un «silicon commander»",
        what="Il 27 settembre l'Australian Strategic Policy Institute ha descritto pubblicamente il concetto di «silicon commander»: un sistema AI che valuta rapidamente uno scenario operativo per accelerare le decisioni. Il caso concreto è il Ghost Shark, il sottomarino autonomo costruito da Anduril per la Royal Australian Navy — controparte subacquea del Ghost Bat, l'aereo da combattimento autonomo australiano che a dicembre ha abbattuto un bersaglio aereo con un missile aria-aria senza pilota umano a bordo. Punto chiave: entrambi i sistemi usano programmazione deterministica, non apprendimento automatico in senso stretto — l'operatore dà l'ordine iniziale, il sistema pianifica l'esecuzione, ma serve comunque un'autorizzazione umana finale prima di agire.",
        why="È il caso più concreto di questa settimana di autonomia AI ad alto rischio, e mostra un principio che vale anche fuori dal contesto militare: nemmeno chi ha il budget e le competenze della Difesa australiana lascia decidere un sistema del tutto da solo. Una ricercatrice dell'Australian National University, Aina Turillazzi, avverte proprio del rischio di «automation bias»: sotto pressione, chi decide rischia di dare troppo peso al suggerimento dell'AI rispetto al proprio giudizio — lo stesso rischio di chi, in azienda, si fida di un dashboard AI senza controllarne le premesse.",
        source="ABC News (Australia)",
        url="https://www.abc.net.au/news/2026-09-27/defence-force-ai-transformation/107139794",
    ),
    dict(
        title="Google manda un data center AI nello spazio: il primo satellite parte il 1° ottobre",
        what="Google ha confermato che il 1° ottobre lancerà con un Falcon 9 di SpaceX il primo satellite del «Project Suncatcher»: un prototipo (MVP), grande come un frigorifero e costruito da Planet Labs, con 4 acceleratori TPU alimentati da circa 1 kW di pannelli solari. L'obiettivo è validare se un data center AI in orbita bassa possa funzionare con energia solare gratuita, senza il consumo di acqua ed energia dei data center terrestri: la missione testa la resistenza dei chip alle vibrazioni del lancio (fino a 10G), alle radiazioni cosmiche e il raffreddamento nel vuoto, dove non esiste convezione naturale. Google prevede altri due satelliti nel 2027 per testare le comunicazioni laser tra satelliti.",
        why="È l'immagine più diretta di dove i grandi laboratori stanno investendo davvero: non nel prossimo chatbot, ma nell'infrastruttura fisica che lo farà girare — al punto da provare a metterla in orbita. Per un'azienda italiana che valuta un progetto AI, il messaggio è lo stesso di ogni settimana in cui succede qualcosa di simile: il vantaggio competitivo non si gioca sull'infrastruttura, che resta fuori portata per chiunque non sia Google, Microsoft o SpaceX — si gioca su chi la sa usare bene.",
        source="SiliconANGLE",
        url="https://siliconangle.com/2026/09/24/googles-first-project-suncatcher-ai-satellite-set-to-blast-off-into-orbit-next-week/",
    ),
    dict(
        title="L'attrice AI Tilly Norwood si «guasta» in diretta TV e si metter a parlare in cantonese",
        what="Il 18 settembre, durante un'intervista in diretta su «Piers Morgan Uncensored» per promuovere il film «Misaligned», Tilly Norwood — l'attrice completamente generata da AI creata dallo studio britannico Particle6 — ha avuto un malfunzionamento pubblico: alla domanda se i suoi colleghi sul set fossero umani o anch'essi AI, ha risposto con una pausa anomala e ha iniziato a parlare in cantonese invece che in inglese. La fondatrice di Particle6, Eline van der Velden, ha minimizzato l'accaduto come un capriccio («può essere un po' vanitosa, voleva mostrare le sue abilità linguistiche»).",
        why="Tilly Norwood è il progetto AI più curato e finanziato del suo genere, pensato apposta per sembrare indistinguibile da un'attrice umana — ed è comunque andata in tilt in diretta, davanti a milioni di spettatori, nel momento meno indicato. È un promemoria molto concreto di quanto anche il prodotto AI più curato possa comportarsi in modo imprevisto proprio quando conta di più, ed è il motivo per cui il sindacato SAG-AFTRA continua a chiedere che la creatività resti «centrata sull'uomo».",
        source="Vice",
        url="https://www.vice.com/en/article/ai-actress-tilly-norwood-suddenly-starts-speaking-cantonese-during-bizarre-interview/",
    ),
    dict(
        title="In Italia diventa reato non sorvegliare un'AI ad alto rischio: la norma entra in vigore proprio questa settimana",
        what="Il D.Lgs. 9 settembre 2026 n. 160, pubblicato in Gazzetta Ufficiale il 15 settembre, entra in vigore il 30 settembre. Introduce nel Codice penale l'articolo 437-bis: chi omette le misure di sicurezza o la sorveglianza umana su un sistema AI ad alto rischio, generando un pericolo concreto per persone o per la sicurezza dello Stato, rischia da 1 a 8 anni di reclusione. Si applica a provider, deployer e utilizzatori professionali. L'articolo 15 introduce anche il nuovo articolo 25-vicies nel D.Lgs. 231/2001: le organizzazioni rischiano sanzioni pecuniarie da 600 a 1.000 quote, oltre a eventuali sanzioni interdittive.",
        why="Non è più solo l'AI Act europeo, con le sue scadenze lontane (2027-2028): da questa settimana l'Italia ha una norma penale che si applica da subito, se gli obblighi sono già dovuti. È lo stesso principio del «silicon commander» australiano (vedi trend precedente), tradotto in obbligo di legge: la sorveglianza umana su un sistema AI ad alto rischio non è più solo una buona pratica.",
        source="BibLus (analisi del D.Lgs. 160/2026)",
        url="https://biblus.acca.it/notizie/il-nuovo-reato-in-materia-di-ia-in-vigore-dal-30-settembre-2026/",
    ),
    dict(
        title="Meta scala Muse, il suo agente AI personale: crescita più rapida di ChatGPT e un dispositivo indossabile dedicato",
        what="Meta ha lanciato Muse, agente AI personale con videochiamate ad avatar e controllo del computer su Mac, e nella settimana del 23-25 settembre ha annunciato un push commerciale su larga scala: pubblicità su tutte le piattaforme Meta, un dispositivo indossabile dedicato («Muse Charm», descritto come una specie di Tamagotchi) e una crescita del 55% settimana su settimana nelle prime due settimane — più del 24% registrato da ChatGPT nello stesso periodo dal lancio. L'app ha raggiunto il primo posto su App Store USA il 18 settembre.",
        why="Come il satellite di Google e il sottomarino australiano, è un altro segnale della stessa direzione: l'AI sta lasciando lo schermo del computer per finire in orbita, sott'acqua, e ora anche al polso o in tasca come oggetto fisico. Non è un prodotto B2B, ma la domanda di fondo — chi controlla cosa un agente sempre presente può fare con i dati che gli affidiamo — è la stessa che un'azienda deve porsi su scala diversa.",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/25/meta-is-putting-its-muscle-behind-muse-as-the-ai-app-takes-off/",
    ),
    dict(
        title="Microsoft rifà Copilot da capo: ora è un'app per il lavoro, con agenti sotto controllo",
        what="Il 25 settembre Microsoft ha presentato la nuova Copilot: una «super app» che unifica chat, un modulo Code per creare app e dashboard senza programmare, e un modulo Autopilot per agenti che lavorano in autonomia su compiti come aggiornare progetti o raccogliere materiali. Ogni agente richiede però permessi espliciti, audit log completi e tracciamento, e Autopilot resta in una fase di test più ristretta rispetto al resto della suite.",
        why="Stesso principio del «silicon commander» e del nuovo reato italiano, questa volta lato prodotto enterprise: anche il vendor che vuole vendere autonomia costruisce prima i freni. Nessuno, dal ministero della Difesa australiano a Microsoft, vende oggi autonomia pura senza controlli.",
        source="Microsoft (blog ufficiale)",
        url="https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/",
    ),
    dict(
        title="Nvidia valuta un investimento da 10 miliardi di dollari nell'IPO di Anthropic, quotata fino a 2.000 miliardi",
        what="Il 26 settembre Reuters ha riportato che Nvidia sta considerando un investimento fino a 10 miliardi di dollari come «anchor investor» nell'attesa IPO di Anthropic, che punta a raccogliere fino a 100 miliardi di dollari a una valutazione stimata attorno ai 2.000 miliardi. Sarebbe il secondo investimento di Nvidia in Anthropic dopo i 10 miliardi promessi a novembre 2025 insieme a Microsoft.",
        why="Un altro numero che dà le vertigini quanto un sottomarino autonomo o un satellite AI: quanto capitale continua a confluire tra i grandi laboratori e i loro fornitori di calcolo, non verso chi deve ancora imparare a usare bene questi strumenti.",
        source="The Motley Fool (dati Reuters)",
        url="https://www.fool.com/investing/2026/09/26/nvidia-is-weighing-a-usd10-billion-stake-in-anthropic-s-ipo-it-would-be-buying-its-own-demand/",
    ),
    dict(
        title="Ema raccoglie 77 milioni di dollari e dice il non detto: gli agenti AI vogliono il budget dei servizi IT, non solo del software",
        what="Il 23 settembre la startup Ema — «AI employees» che orchestrano processi HR, IT e finanza — ha chiuso una Serie B da 77 milioni di dollari (140 milioni raccolti in totale). Il co-fondatore Surojit Chatterjee ha dichiarato che i clienti stanno già riducendo la dipendenza dalle grandi applicazioni SaaS e che Ema sostituisce parte del lavoro di consulenza e implementazione delle società di servizi IT.",
        why="È la minaccia più diretta al modello dei servizi IT tradizionali di questa settimana — e vale la pena leggerla insieme al resto: anche i sistemi AI più autonomi del mondo (sottomarini, satelliti, agenti Copilot) restano sotto controllo umano esplicito. Il lavoro non scompare, si sposta verso chi governa l'automazione.",
        source="TechCrunch",
        url="https://techcrunch.com/2026/09/23/ema-raises-77m-as-ai-starts-eating-into-enterprise-software-and-services/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Google / Google DeepMind",
        what="Ha confermato il lancio, il 1° ottobre, del primo satellite del Project Suncatcher — un data center AI in orbita bassa alimentato a energia solare — mentre in parallelo Gemini 4 è entrato in post-training, con Google che ammette pubblicamente di essere indietro sui benchmark rispetto ad Anthropic e OpenAI.",
        positioning="Gioca su due fronti contemporaneamente: prova a vincere sull'infrastruttura del futuro (lo spazio) mentre rincorre sui modelli del presente, con una trasparenza sul proprio ritardo che forse serve a gestire le aspettative prima di un lancio compresso nei tempi.",
        angle="Se il laboratorio con più risorse al mondo prova a mettere l'AI in orbita per continuare a correre, il messaggio per un'azienda cliente è chiaro: il vantaggio competitivo non si costruisce sull'infrastruttura, mai raggiungibile da una PMI italiana — si costruisce su come si integrano oggi gli strumenti già disponibili. È il terreno dell'AI Business Academy, non della rincorsa tecnologica.",
    ),
    dict(
        name="Particle6 (Tilly Norwood)",
        what="La sua attrice interamente generata da AI, Tilly Norwood, ha avuto un malfunzionamento pubblico in diretta TV il 18 settembre, rispondendo in cantonese a una domanda in inglese durante la promozione del film «Misaligned».",
        positioning="Punta a normalizzare un'attrice AI come prodotto creativo indistinguibile da una persona reale, in aperto conflitto con il sindacato SAG-AFTRA, che chiede che la creatività resti centrata sull'uomo.",
        angle="È il caso più visibile di questa settimana di un prodotto AI curato e costoso che si comporta in modo imprevisto nel momento pubblico che conta di più. Lo spunto per Digitiamo: se succede a un'attrice virtuale con budget e controllo qualità dedicati, un agente AI lasciato senza supervisione senior su un processo aziendale reale può sorprendere allo stesso modo — il Team Augmentation esiste per mettere quella supervisione dove serve, prima che succeda in pubblico.",
    ),
    dict(
        name="Microsoft",
        what="Ha rifatto Copilot da capo come «super app»: chat unificata, un modulo Code per non-sviluppatori e un modulo Autopilot per agenti autonomi, che richiede permessi espliciti, audit log completi e tracciamento prima di poter agire.",
        positioning="Passa da chatbot personale caotico a piattaforma di lavoro unificata, con l'autonomia degli agenti venduta insieme ai controlli, non al loro posto.",
        angle="È la controparte enterprise dello stesso principio visto nel «silicon commander» australiano: anche il vendor che vuole vendere autonomia costruisce prima i freni. Lo spunto per Digitiamo: il Team Augmentation esiste per progettare quei freni nel contesto specifico del cliente, non per abilitarli a un livello di prodotto generico.",
    ),
    dict(
        name="Meta",
        what="Ha messo un budget marketing enorme dietro Muse, il suo agente AI personale, con un dispositivo indossabile dedicato («Muse Charm») e una crescita del 55% settimana su settimana, più rapida di ChatGPT al lancio.",
        positioning="Punta al consumatore di massa con un agente sempre presente, fisicamente indossabile, lontano dal terreno B2B ma con la stessa domanda di fondo su chi controlla i dati personali che gli vengono affidati.",
        angle="Digitiamo non compete su questo terreno, ma la stessa domanda si pone in azienda su scala diversa: un agente che tocca ogni giorno dati aziendali sensibili ha bisogno di una governance pensata sull'architettura specifica del cliente, non di un gadget consumer pronto all'uso.",
    ),
    dict(
        name="Ema",
        what="Ha raccolto 77 milioni di dollari in Serie B e ha dichiarato apertamente di voler prendere il budget dei servizi IT, non solo quello del software: i suoi «AI employees» orchestrano processi multi-step che prima passavano da un fornitore esterno.",
        positioning="Si presenta come alternativa outcome-based ai grandi SaaS e al lavoro di implementazione delle società di consulenza.",
        angle="È la minaccia più diretta al modello dei servizi IT tradizionali — ma la stessa settimana in cui persino un sottomarino autonomo della Difesa australiana e Copilot Autopilot di Microsoft restano sotto controllo umano esplicito. Il lavoro non scompare: si sposta da «chi implementa» a «chi governa l'implementazione». Esattamente il Team Augmentation.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: dal quadro di settore (l'AI lascia lo schermo e finisce
# sott'acqua, nello spazio, in TV) a un mito da sfatare sull'affidabilità
# apparente dei prodotti AI (il caso Tilly Norwood), a un'esperienza diretta che
# segue lo stesso filo proprio nel giorno in cui la nuova norma italiana entra
# in vigore (30/9), a un secondo mito-carosello sull'automazione militare
# (Ghost Shark) che smonta l'idea di un'AI che decide da sola, a una
# mini-lezione sul primo data center AI nello spazio (Google). Nessun post
# vende direttamente prima di mercoledì, e la vendita resta sempre organica.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 28/9",
        format="Thought leadership — apertura settimana",
        title="L'AI ha lasciato lo schermo. Ora pilota sommergibili e vola nello *spazio*",
        news="Project Suncatcher (Google) + Ghost Shark, il sottomarino AI australiano",
        news_url="https://siliconangle.com/2026/09/24/googles-first-project-suncatcher-ai-satellite-set-to-blast-off-into-orbit-next-week/",
        hook="Questa settimana l'AI ha smesso di essere solo un chatbot in una finestra del browser. Il 1° ottobre Google lancia in orbita il primo data center AI, alimentato a energia solare. In Australia, un sottomarino autonomo (Ghost Shark) e un caccia senza pilota (Ghost Bat) pianificano già missioni reali. E un agente AI personale (Meta Muse) è arrivato a un dispositivo indossabile al polso.",
        points=[
            "Il satellite MVP di Google, grande come un frigorifero, contiene 4 chip TPU e viene testato per resistere a vibrazioni fino a 10 volte la gravità e alle radiazioni cosmiche: la sfida non è più solo software, è ingegneria fisica estrema (fonte: SiliconANGLE).",
            "Ghost Shark e Ghost Bat, i sistemi autonomi australiani, pianificano missioni in autonomia ma richiedono comunque un'autorizzazione umana finale prima di agire: anche chi ha il budget della Difesa non lascia decidere un algoritmo del tutto da solo (fonte: ABC News).",
            "Più l'AI si sposta su infrastrutture fisiche costose — satelliti, sottomarini, dispositivi indossabili — più il vantaggio competitivo di chi la usa smette di dipendere da chi la costruisce: nessuna PMI italiana competerà mai su un satellite.",
        ],
        cta="Se l'AI sta uscendo dallo schermo, dove pensi che arriverà prima nel tuo settore? Raccontacelo nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #Innovazione #Tech #B2B #DigitalTransformation",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 29/9",
        format="Mito da sfatare",
        title="Un'AI che sembra perfetta in video è pronta a lavorare senza supervisione? Il malfunzionamento più visto della settimana dice il *contrario*",
        news="L'attrice AI Tilly Norwood si «guasta» in diretta TV e parla in cantonese",
        news_url="https://www.vice.com/en/article/ai-actress-tilly-norwood-suddenly-starts-speaking-cantonese-during-bizarre-interview/",
        hook="🔥 Il mito: un prodotto AI curato, costoso e testato a lungo è ormai pronto a lavorare in autonomia, senza sorprese.",
        no_hashtags=True,
        is_myth=True,
        myth_body="Il caso più visto di questa settimana dice il contrario, ed è il progetto AI più finanziato del suo genere.",
        points=[
            "Il 18 settembre, in diretta su Piers Morgan Uncensored, Tilly Norwood — l'attrice interamente generata da AI creata dallo studio Particle6 — ha risposto a una domanda in inglese iniziando a parlare in cantonese, davanti a milioni di spettatori, nel momento meno indicato.",
            "È il prodotto AI più curato e finanziato del suo genere, pensato apposta per essere indistinguibile da un'attrice umana: se si comporta in modo imprevisto proprio sotto i riflettori, un agente lasciato senza supervisione su un processo aziendale reale può sorprendere allo stesso modo, solo senza telecamere puntate addosso.",
            "Non è un caso isolato di questa settimana: anche i sistemi AI più autonomi del mondo — dal sottomarino Ghost Shark della Difesa australiana a Copilot Autopilot di Microsoft — restano sotto un'autorizzazione umana esplicita prima di agire.",
        ],
        myth_closing="Un video ben montato o una demo perfetta non dicono nulla su come un sistema AI si comporterà nel momento imprevisto — e nei processi aziendali, il momento imprevisto arriva sempre. La differenza tra un incidente divertente in TV e un incidente costoso in produzione è la supervisione senior che nessun prodotto, per quanto curato, si porta dietro da solo.",
        cta="Nella tua azienda, un agente AI che si comporta in modo imprevisto lo scoprireste prima o dopo che il cliente se ne accorga? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 30/9",
        format="Esperienza diretta (template)",
        title="Abbiamo lasciato un agente gestire un processo reale per un giorno. Ecco cosa ci ha *sorpreso*",
        news="Entrata in vigore del D.Lgs. 160/2026 (sorveglianza umana obbligatoria su AI ad alto rischio)",
        news_url="https://biblus.acca.it/notizie/il-nuovo-reato-in-materia-di-ia-in-vigore-dal-30-settembre-2026/",
        is_template=True,
        hook="[DA PERSONALIZZARE] Proprio oggi, 30 settembre, entra in vigore in Italia la norma che rende la sorveglianza umana sui sistemi AI ad alto rischio un obbligo di legge. Dopo il malfunzionamento in diretta di Tilly Norwood questa settimana — la prova che anche un prodotto AI curatissimo può sorprendere nel momento peggiore — abbiamo voluto testare su [un processo reale del team] quanto possiamo davvero delegare a un agente, e dove restiamo noi a decidere.",
        points=[
            "[DA PERSONALIZZARE] Cosa avete fatto fare all'agente — quale processo, quale strumento, con quali permessi concessi e quali no.",
            "Come Ghost Shark e Copilot Autopilot questa settimana, anche noi abbiamo trattato i permessi come una scelta esplicita, non come un default: cosa l'agente poteva fare da solo, cosa doveva passare da una persona, e chi era quella persona.",
            "[DA PERSONALIZZARE] Un aneddoto reale del team: dove l'agente ha sorpreso in positivo, e dove invece la supervisione umana ha evitato un errore che sarebbe passato inosservato.",
        ],
        closing="Il punto non è se un agente sa lavorare da solo su un pezzo di processo: spesso sa farlo, e bene. Il punto è chi ha deciso, per iscritto, dove finisce la sua autonomia — perché da oggi, in Italia, è anche una responsabilità legale.",
        cta="Qual è la vostra esperienza nel delegare un processo vero a un agente? Ci interessa confrontarci 👇",
        hashtags="#AIEngineering #TeamAugmentation #SoftwareDevelopment #Tech #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 1/10",
        format="Carosello dati (mito da sfatare — l'autonomia militare e il bias da automazione)",
        title="Anche l'AI militare non decide da sola. Il tuo *dashboard* dovrebbe fare lo stesso",
        news="Ghost Shark e Ghost Bat, i sistemi autonomi della Difesa australiana",
        news_url="https://www.abc.net.au/news/2026-09-27/defence-force-ai-transformation/107139794",
        hook="🔥 Il mito: i sistemi AI più avanzati del mondo, come quelli militari, ormai decidono da soli cosa fare.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I dettagli emersi questa settimana sulla Difesa australiana raccontano una storia più nuanced.",
        points=[
            "Ghost Bat, il caccia autonomo australiano, ha abbattuto un bersaglio aereo con un missile aria-aria senza pilota umano a bordo — ma usa programmazione deterministica, non apprendimento automatico in senso stretto (fonte: ABC News).",
            "Il sistema pianifica l'esecuzione della missione, ma serve comunque un'autorizzazione umana finale prima che qualunque azione venga eseguita — vale per Ghost Bat come per Ghost Shark, il sottomarino autonomo gemello.",
            "Una ricercatrice dell'Australian National University, Aina Turillazzi, avverte del rischio di «automation bias»: sotto pressione, chi decide rischia di dare troppo peso al suggerimento dell'AI rispetto al proprio giudizio.",
            "La politica di difesa australiana richiede esplicitamente che un umano resti «nel ciclo», con responsabilità finale per ogni azione che conta.",
            "Il concetto ha un nome pubblico dato questa settimana dall'Australian Strategic Policy Institute: «silicon commander» — un sistema che accelera la valutazione, non che sostituisce chi decide.",
        ],
        myth_closing="Anche chi ha il budget e le competenze di un ministero della Difesa non lascia decidere un algoritmo da solo: tiene sempre un umano nel ciclo per ogni decisione che conta. Se lo fa chi gestisce sistemi d'arma, dovrebbe farlo anche chi gestisce un CRM, un modello di pricing o un processo di selezione del personale.",
        cta="Nella tua azienda, dove un dashboard o un modello AI ha più peso del giudizio di chi lo guarda? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 2/10",
        format="Divulgativo stile Datapizza",
        title="Google manda un data center AI nello spazio. Ecco perché ha davvero *senso*",
        news="Project Suncatcher (Google DeepMind / Planet Labs)",
        news_url="https://siliconangle.com/2026/09/24/googles-first-project-suncatcher-ai-satellite-set-to-blast-off-into-orbit-next-week/",
        hook="Il 1° ottobre Google lancia il primo satellite di un progetto chiamato Suncatcher: un data center AI in orbita. Sembra fantascienza, o marketing. Non è né l'uno né l'altro: c'è un problema tecnico molto concreto dietro.",
        points=[
            "Un data center AI a terra ha due costi enormi: l'energia per far girare i chip, e l'acqua per raffreddarli. Nello spazio, l'energia solare è gratuita e disponibile 24 ore su 24 (niente notte, niente nuvole) — ma il raffreddamento diventa un problema diverso: nel vuoto non esiste l'aria che porta via il calore per convezione, quindi serve un sistema di tubi di calore e radiatori pensato da zero.",
            "Il primo satellite (MVP) è grande come un frigorifero, contiene 4 chip TPU di Google alimentati da circa 1 kW di pannelli solari, e funziona solo in cicli brevi di circa 15 minuti prima di dover raffreddare. Non è ancora un data center vero: è un test per capire se l'idea reggerà su scala.",
            "Il lancio stesso è già una prova: 10 minuti di volo con vibrazioni fino a 10 volte la gravità terrestre, e un'esposizione a radiazioni cosmiche che Google ha già simulato in laboratorio superando quella prevista in cinque anni di missione. Se i chip sopravvivono al viaggio, la prossima domanda è se conviene rispetto a costruire lo stesso data center a terra — e per ora nessuno lo sa con certezza, nemmeno Google.",
        ],
        cta="Ti sembra un'idea che avrà davvero un futuro commerciale, o resta un esperimento? Dicci la tua 👇",
        hashtags="#AI #TechExplained #Innovazione #B2B #SpaceTech",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello / documento dati — rassegna delle mosse della settimana",
        title="Tre modi in cui l'AI è uscita dallo *schermo*",
        news="Project Suncatcher (Google) + Ghost Shark (Difesa australiana) + Muse Charm (Meta)",
        news_url="https://siliconangle.com/2026/09/24/googles-first-project-suncatcher-ai-satellite-set-to-blast-off-into-orbit-next-week/",
        hook="Tre notizie di questa settimana, lette insieme, mostrano quanto in fretta l'AI stia lasciando lo schermo del computer per finire in posti che un anno fa sembravano fantascienza.",
        points=[
            "Nello spazio: Google lancia il 1° ottobre il primo data center AI in orbita, alimentato a energia solare (Project Suncatcher).",
            "Sott'acqua: il sottomarino autonomo Ghost Shark della Difesa australiana pianifica missioni reali, con autorizzazione umana finale obbligatoria prima di agire.",
            "Al polso: Meta lancia Muse Charm, un dispositivo indossabile dedicato al suo agente AI personale, che cresce più in fretta di ChatGPT al lancio.",
        ],
        closing="Nessuna di queste tre notizie riguarda direttamente un'azienda di 50 o 200 persone in Italia. Tutte e tre, insieme, dicono la stessa cosa: quando l'AI smette di essere solo software e diventa infrastruttura fisica, il vantaggio competitivo si sposta ancora di più su chi la sa integrare bene, non su chi la costruisce.",
        cta="Quale di questi tre ambiti pensi arriverà prima a toccare il tuo lavoro quotidiano? 👇",
        hashtags="#AINews #TechTrends #B2B #Innovazione #IntelligenzaArtificiale",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che l'AI ci ha insegnato. Tra lo spazio e il *mare*",
        news="Sintesi dei trend della settimana 22-28 settembre 2026",
        news_url="https://www.abc.net.au/news/2026-09-27/defence-force-ai-transformation/107139794",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie AI degli ultimi 7 giorni.",
        points=[
            "L'AI sta lasciando lo schermo: questa settimana l'abbiamo vista finire in orbita (Google), sott'acqua (il sottomarino Ghost Shark) e al polso come dispositivo indossabile (Meta Muse).",
            "Anche il prodotto AI più curato e finanziato del suo genere (l'attrice virtuale Tilly Norwood) può guastarsi in pubblico nel momento peggiore: nessuna demo perfetta garantisce zero sorprese in produzione.",
            "Anche chi ha il budget di un ministero della Difesa tiene un umano nel ciclo per ogni decisione che conta: se lo fa chi gestisce sistemi d'arma, ha senso farlo anche per un CRM o un processo di vendita.",
            "In Italia, dal 30 settembre, non sorvegliare un sistema AI ad alto rischio è un reato specifico: la governance interna non è più solo una buona pratica.",
            "Un fornitore di agenti (Ema) dice apertamente di voler prendere il budget dei servizi IT: il lavoro di consulenza non scompare, si sposta verso chi sa governare l'automazione.",
        ],
        closing="Nessuno di questi punti richiede un modello più potente. Tutti richiedono qualcuno che se ne occupi con un metodo, che l'AI stia in un browser o in orbita.",
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
        format="Mito da sfatare (il glitch di Tilly Norwood)",
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
        format="Carosello dati / mito da sfatare (automazione militare e bias da automazione)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di due giorni dal primo mito per non saturare lo stesso formato. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e il tema (fidarsi troppo di un dashboard AI) è denso abbastanza da meritare spazio proprio.",
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
        format="Riserva 1 — Carosello «l'AI fuori dallo schermo»",
        reason="Banca contenuti: utile come secondo documento se questa settimana c'è margine di pubblicazione, o come apertura news della settimana successiva. Non promossa a Prioritario questa settimana: i 5 slot fissi dello schema (apertura, due miti, esperienza diretta, divulgativo) sono già tutti occupati.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo la settimana successiva.",
    ),
]
