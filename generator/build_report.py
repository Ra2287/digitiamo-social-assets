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

WEEK_LABEL = "12 – 18 ottobre 2026"
GENERATED_ON = "Venerdì 9 ottobre 2026 (PED anticipato su richiesta di Ramona)"

# ---------------------------------------------------------------------------
# TREND DEL SETTORE
# ---------------------------------------------------------------------------
# Notizie del periodo 1 - 9 ottobre 2026, verificate su fonte diretta (non sui
# riassunti aggregatori). Filo conduttore della settimana: i grandi laboratori
# cominciano a rispondere, con prodotti e processi concreti, ai due problemi
# emersi la settimana scorsa — sicurezza degli agenti e fiducia nei loro
# output — mentre la regolamentazione europea impone le prime scadenze reali.
trends = [
    dict(
        title="Google lancia Gemini 4 «Argon», in ritardo ma competitivo sulla frontiera",
        what="Il 1° ottobre Google ha presentato Gemini 4, nome in codice Argon, dopo aver saltato la tappa intermedia Gemini 3.5 Pro prevista per giugno — un ritardo di tre-quattro mesi sulla propria roadmap, secondo l'analista Pareekh Jain. Il modello è distribuito per ora solo a un gruppo ristretto di esperti di cybersicurezza tramite il programma Fairwind, non in rilascio generale. Punta su contesto lungo (output fino a 1 milione di token, contro i 64.000 precedenti) per lavoro multi-step su codice, analisi legale e finanziaria.",
        why="È la prima risposta diretta di Google al duopolio OpenAI-Anthropic sulla frontiera dei modelli, e arriva con un rilascio controllato a un gruppo verificato invece che un lancio generale immediato — lo stesso approccio che Digitiamo consiglia per l'adozione AI in azienda.",
        source="InfoWorld",
        url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
    ),
    dict(
        title="Gemini 4 Argon contro Opus 5.5 e GPT-6 Astra: nessuno vince su tutto, e costa meno",
        what="Sui benchmark pubblici, Argon supera Claude Opus 5.5 sul Vals Index (68,9% contro 67,0%) e su DeepSWE v1.1 (77,9% contro 74,2%), ma perde su PostTrainBench, il benchmark di ingegneria ML (45,3% contro 49,3% di Opus). Sul fronte prezzo, il listino di lancio di Argon è di 2$ per milione di token in input e 10$ in output, contro i 4$/20$ di Opus 5.5 e i 10$/50$ di GPT-6 Astra.",
        why="Nessun modello vince su ogni fronte, e il prezzo più basso non significa automaticamente il miglior risultato: come nota l'analista Pareekh Jain, quello che conta per un'azienda è il costo per risultato ottenuto, non il costo per token — un principio che vale per qualunque fornitore AI si scelga.",
        source="InfoWorld",
        url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
    ),
    dict(
        title="Anthropic apre l'accesso ridotto ai suoi modelli ai team di cybersicurezza, mentre il progetto Glasswing trova 129.000 vulnerabilità",
        what="Il 7 ottobre Anthropic ha ampliato il Cyber Verification Program, che consente a professionisti della sicurezza verificati di testare Claude Opus 5.5, Sonnet 5.5 e Mythos 5.1 con le misure di sicurezza standard ridotte, su tre livelli di accesso (difesa, red team, specializzato). Nello stesso annuncio, Anthropic ha reso noto che il progetto Glasswing, condotto con partner del settore, ha verificato almeno 129.000 vulnerabilità software tra aprile e luglio 2026, con altre 5.500 confermate da scansioni open-source entro ottobre; oltre 33.000 sono classificate critiche o gravi, e Anthropic stessa stima che l'impatto reale sia probabilmente almeno cinque volte superiore.",
        why="È la dimostrazione più concreta finora di un laboratorio che usa i propri modelli per trovare, su larga scala, i problemi di sicurezza che il codice — scritto da umani o generato dall'AI — porta con sé: un dato enorme, ma anche la prova che l'accesso con meno limiti va dato solo a chi è verificato, non aperto a tutti.",
        source="The Hacker News",
        url="https://thehackernews.com/2026/10/anthropic-expands-claude-access-for.html",
    ),
    dict(
        title="OpenAI introduce la filigrana textGrain per conformarsi all'AI Act europeo",
        what="Il 5 ottobre OpenAI ha pubblicato il report tecnico di textGrain, il sistema di filigrana statistica che applicherà ai testi generati da ChatGPT e Codex nell'Unione Europea per rispettare l'articolo 50(2) del Regolamento AI Act, che impone di rendere i contenuti generati dall'AI riconoscibili in formato leggibile da una macchina. Il sistema non inserisce caratteri nascosti: modifica la scelta statistica delle parole in base a una chiave segreta. Il tasso di rilevamento dichiarato è del 95% su un testo inglese di 400 token, ma scende all'80% su 200 token, crolla al 17% se un quarto delle parole viene sostituito con sinonimi, e varia molto tra le lingue ufficiali UE (dal 69% dello spagnolo al 42,2% del rumeno). Nell'API resta disattivata di default: tocca a chi la integra attivarla.",
        why="È la prima misura tecnica concreta con cui un grande laboratorio prova a rispondere a un obbligo normativo europeo specifico, e mostra già i suoi limiti: un'etichetta che sparisce con un editing leggero non è una garanzia di tracciabilità, è un primo passo.",
        source="ActuIA",
        url="https://www.actuia.com/en/news/openai-will-watermark-chatgpt-in-the-eu-but-leaves-the-api-opt-in/",
    ),
    dict(
        title="L'AI Act si allenta su alcuni obblighi, ma la scadenza del 2 dicembre sulla marcatura resta ferma",
        what="Il regolamento 2026/1744 (il cosiddetto «omnibus digitale») introduce proroghe e semplificazioni mirate ad alcuni obblighi dell'AI Act, dopo che l'articolo 50 sulla trasparenza dei contenuti generati dall'AI è entrato in vigore il 2 agosto 2026. Per i sistemi già sul mercato prima di quella data, la Commissione europea ha fissato al 2 dicembre 2026 la scadenza per conformarsi all'obbligo di marcatura — mentre un dibattito istituzionale, con un intervento della Banque de France il 9 settembre, mette in dubbio se il quadro attuale basti davvero per i modelli più avanzati.",
        why="Per un'azienda italiana significa una cosa pratica: la proroga su alcuni obblighi non tocca la scadenza sulla marcatura dei contenuti, che resta a dicembre — un calendario di conformità che vale la pena avere già segnato, non da scoprire a novembre.",
        source="ActuIA",
        url="https://www.actuia.com/en/news/ai-ethics-and-regulation-the-state-of-play-on-6-october-2026/",
    ),
    dict(
        title="Manus, l'agente AI cinese, cerca una valutazione da 4 miliardi di dollari dopo la rottura con Meta",
        what="Secondo The Information e TechCrunch, Manus — lo sviluppatore cinese dell'omonimo agente AI generalista, diventato noto a inizio 2025 — sta negoziando un round da circa 500 milioni di dollari che la valuterebbe fino a 4 miliardi, dopo la fine della sua partnership con Meta e una crescita rapida di utenti e costi.",
        why="È un altro segnale di quanto capitale continui a confluire verso gli agenti AI generalisti, nello stesso periodo in cui i dati su sicurezza e affidabilità di questi stessi agenti (vedi i due trend sopra) restano un problema aperto: il prodotto corre, la fiducia nel prodotto rincorre.",
        source="TechCrunch / The Information",
        url="https://techcrunch.com/?p=3166149",
    ),
    dict(
        title="Il divario AI tra grandi imprese e PMI italiane sale a 37,4 punti",
        what="Secondo i dati dell'Osservatorio IIA (Intelligenza Artificiale per l'Italia), presentati a giugno 2026, l'adozione dell'AI tra le imprese italiane è quasi raddoppiata tra il 2024 e il 2025 (dall'8,2% al 16,4%), ma il divario tra grandi imprese (53,1% di adozione) e PMI (15,7%) è salito a 37,4 punti percentuali, dai 20 punti del 2023. Il 58,6% delle PMI indica la mancanza di competenze interne come primo ostacolo.",
        why="Il dato non è di questa settimana (l'Osservatorio l'ha presentato a giugno), ma resta il più rilevante per il pubblico B2B italiano di Digitiamo: mentre i grandi laboratori rilasciano modelli sempre più potenti, la maggioranza delle PMI italiane non ha ancora iniziato — e il divario, non il ritardo assoluto, è quello che si allarga più in fretta.",
        source="TecnoAndroid / Osservatorio IIA",
        url="https://www.tecnoandroid.it/news/osservatorio-iia-l836-delle-pmi-italiane-e-ancora-senza-ai-1908305/",
    ),
]

# ---------------------------------------------------------------------------
# ANALISI COMPETITOR
# ---------------------------------------------------------------------------
competitors = [
    dict(
        name="Google DeepMind",
        what="Ha lanciato Gemini 4 Argon dopo mesi di ritardo sulla propria roadmap, con un rilascio iniziale ristretto a un gruppo di esperti di cybersicurezza (programma Fairwind) e un prezzo di lancio nettamente inferiore a Opus 5.5 e GPT-6 Astra.",
        positioning="Recupera gran parte del divario sulla frontiera ma non lo chiude ovunque: vince su alcuni benchmark, perde su altri, e punta sul prezzo e sul contesto lungo (1 milione di token) come leva competitiva più che sulla superiorità assoluta.",
        angle="Per un'azienda cliente di Digitiamo è un promemoria utile: scegliere un fornitore AI solo guardando un benchmark o un prezzo per token è un errore — conta il costo per risultato ottenuto sul proprio caso d'uso specifico, non la classifica generale.",
    ),
    dict(
        name="Anthropic",
        what="Ha ampliato il Cyber Verification Program per team di sicurezza verificati e reso pubblici i risultati del progetto Glasswing: almeno 129.000 vulnerabilità software verificate in quattro mesi, oltre 33.000 critiche o gravi.",
        positioning="Si posiziona come il laboratorio che usa i propri modelli per la difesa su scala, ma lo fa con un accesso a più livelli e riservato a chi è verificato — non un rilascio di funzionalità senza limiti a chiunque.",
        angle="È lo stesso principio alla base del Team Augmentation di Digitiamo: dare accesso a capacità più potenti solo a chi ha le competenze e la responsabilità per usarle bene, non aprirle a tutta l'azienda in un colpo solo.",
    ),
    dict(
        name="OpenAI",
        what="Ha pubblicato textGrain, la filigrana statistica per i testi di ChatGPT e Codex nell'Unione Europea, in risposta diretta all'obbligo di trasparenza dell'articolo 50 dell'AI Act — ma con rilevamento che crolla sotto editing leggero o in alcune lingue UE, e disattivata di default nell'API.",
        positioning="Sceglie la conformità minima dichiarata (l'obbligo normativo) invece di una soluzione tecnica robusta in ogni condizione, lasciando a chi integra l'API la responsabilità di attivare la marcatura o di trovare un'alternativa.",
        angle="Per un'azienda che usa l'AI generativa nei propri contenuti o processi, significa che la conformità normativa di un fornitore non si eredita automaticamente: va verificata nel proprio caso d'uso, soprattutto se si lavora con l'API e non con l'app finale.",
    ),
    dict(
        name="Ecosistema cinese degli agenti AI (Manus e affini)",
        what="Manus, lo sviluppatore dell'omonimo agente AI generalista, negozia un round da circa 500 milioni di dollari a una valutazione fino a 4 miliardi, dopo la fine della partnership con Meta.",
        positioning="Continua a crescere sul fronte del capitale e degli utenti nello stesso periodo in cui i dati sulla sicurezza e l'affidabilità degli agenti AI restano un tema aperto in tutto il settore, non solo per i laboratori cinesi.",
        angle="Per un'azienda italiana cliente di Digitiamo la corsa tra agenti generalisti non è il terreno su cui giocare: il vantaggio si costruisce sulla governance e sulla verifica di qualunque agente si scelga di usare, non sull'inseguire il prossimo lancio.",
    ),
]

# ---------------------------------------------------------------------------
# 7 IDEE DI POST
# ---------------------------------------------------------------------------
# Arco della settimana: apertura con il quadro di settore (Gemini 4 Argon,
# Cyber Verification Program/Glasswing, textGrain), due momenti di rottura in
# formato "mito da sfatare" sul codice e sui modelli generati dall'AI
# (sicurezza del codice, poi benchmark/prezzo), un'esperienza diretta che
# mette alla prova un modello su un compito reale, e una mini-lezione
# divulgativa sul concetto tecnico della filigrana nei testi AI. Nessun post
# vende prima di giovedì, e anche lì la vendita resta organica.
ideas = [
    dict(
        badge="Prioritario",
        day="Lunedì 12/10",
        format="Thought leadership — apertura settimana",
        title="Google torna in corsa, Anthropic si apre alla sicurezza, OpenAI prova a rispettare l'UE. Una settimana di *correzioni*",
        news="Lancio Gemini 4 Argon + Cyber Verification Program/Glasswing (Anthropic) + textGrain (OpenAI)",
        news_url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
        hook="In sette giorni: Google lancia Gemini 4 Argon dopo mesi di ritardo, Anthropic apre l'accesso ridotto ai suoi modelli a team di sicurezza verificati e rende noto che il progetto Glasswing ha trovato 129.000 vulnerabilità software, e OpenAI pubblica la sua filigrana testuale per conformarsi all'AI Act europeo. Tre mosse diverse, un solo filo conduttore: i laboratori stanno rispondendo, con prodotti concreti, ai problemi di sicurezza e fiducia emersi nelle settimane scorse.",
        points=[
            "Google ha scelto di far partire Gemini 4 Argon da un gruppo ristretto di esperti di cybersicurezza invece che da un rilascio generale: anche chi insegue la frontiera preferisce un pilota controllato a un lancio a tutta velocità.",
            "Anthropic apre l'accesso con meno limiti ai propri modelli solo a professionisti verificati, su livelli diversi a seconda dell'uso — e lo fa mentre pubblica un numero enorme (129.000 vulnerabilità trovate dal progetto Glasswing) che mostra quanto lavoro di sicurezza ci sia ancora da fare sul codice, generato dall'AI o no.",
            "La filigrana di OpenAI per rispettare l'AI Act europeo è un passo concreto verso la conformità, ma rileva il testo in modo molto diverso a seconda della lingua e sparisce quasi del tutto con un editing leggero: il tema del post di domani.",
        ],
        cta="Quale di queste tre mosse pensi cambierà di più il modo in cui la tua azienda userà l'AI nei prossimi mesi? Dicci la tua nei commenti 👇",
        hashtags="#IntelligenzaArtificiale #Innovazione #Tech #B2B #AIStrategy",
    ),
    dict(
        badge="Prioritario",
        day="Martedì 13/10",
        format="Mito da sfatare",
        title="Il codice scritto (o controllato) dall'AI è sicuro quanto quello *umano*",
        news="Progetto Glasswing di Anthropic: 129.000 vulnerabilità verificate",
        news_url="https://thehackernews.com/2026/10/anthropic-expands-claude-access-for.html",
        hook="🔥 Il mito: il codice prodotto con l'aiuto dell'AI — o comunque il codice che gira oggi nelle aziende — è sicuro quanto quello scritto e rivisto interamente da persone esperte.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I numeri che Anthropic ha reso pubblici il 7 ottobre, con il progetto Glasswing, raccontano una scala del problema diversa da quella che si immagina di solito.",
        points=[
            "129.000 — le vulnerabilità software verificate dal progetto Glasswing di Anthropic tra aprile e luglio 2026, con altre 5.500 confermate da scansioni open-source entro ottobre.",
            "33.000 — le vulnerabilità tra quelle classificate critiche o gravi: Anthropic stessa dice che il numero reale è probabilmente almeno cinque volte più alto, perché i dati arrivano solo da alcuni partner.",
            "Uno studio indipendente di Veracode, citato nello stesso articolo, ha trovato che circa il 44% dei task di generazione di codice con l'AI introduce una vulnerabilità rischiosa, con un tasso di sicurezza medio del 56%.",
        ],
        myth_closing="Questi numeri non dicono che l'AI scrive codice peggiore di una persona — dicono che la scala a cui si scrive codice oggi, con o senza AI, ha superato la capacità delle revisioni manuali di stare al passo. Il problema non è lo strumento che scrive, è chi verifica prima che quel codice arrivi in produzione.",
        cta="Nella tua azienda, chi rivede il codice prima che vada in produzione — e con quale metodo, non solo con quale strumento? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Mercoledì 14/10",
        format="Carosello dati (mito da sfatare — il modello più nuovo è sempre il migliore)",
        title="Gemini 4 Argon batte Opus 5.5 e GPT-6 Astra? Dipende da cosa gli *chiedi*",
        news="Benchmark e prezzi di Gemini 4 Argon contro Claude Opus 5.5 e GPT-6 Astra",
        news_url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
        hook="🔥 Il mito: quando esce un nuovo modello AI più economico e con benchmark migliori, conviene sempre passare a quello.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I numeri pubblicati su Gemini 4 Argon, il nuovo modello di Google, raccontano una storia più complicata di un semplice «vince il più nuovo».",
        points=[
            "Argon supera Claude Opus 5.5 sul Vals Index (68,9% contro 67,0%) e su DeepSWE, un benchmark di sviluppo software (77,9% contro 74,2%).",
            "Opus 5.5 batte invece Argon sul benchmark di ingegneria ML, PostTrainBench (49,3% contro 45,3%): nessuno dei due modelli vince su tutti i fronti testati.",
            "Il prezzo di lancio di Argon è di 2$ per milione di token in input e 10$ in output, contro i 4$/20$ di Opus 5.5 e i 10$/50$ di GPT-6 Astra: un costo nettamente più basso, ma secondo gli analisti non ancora definitivo.",
            "Un modello più economico su un compito dove serve più accuratezza può costare di più in correzioni e rilavorazioni: quello che conta è il costo per risultato ottenuto sul proprio caso d'uso, non il prezzo per milione di token.",
        ],
        myth_closing="Scegliere un modello AI guardando solo un benchmark pubblico o il prezzo di listino è come scegliere un fornitore guardando solo il preventivo: dice qualcosa, ma non dice se il lavoro, su quel compito specifico, verrà fatto bene.",
        cta="La tua azienda sceglie uno strumento AI guardando i benchmark, il prezzo, o i risultati su un caso d'uso reale testato prima? 👇",
        hashtags="",
    ),
    dict(
        badge="Prioritario",
        day="Giovedì 15/10",
        format="Esperienza diretta",
        title="Abbiamo messo alla prova un modello di nuova generazione su un compito vero. Ecco cosa abbiamo *visto*",
        news="Spunto dal confronto tra Gemini 4 Argon, Opus 5.5 e GPT-6 Astra (vedi post di ieri)",
        news_url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
        hook="Dopo i dati di ieri su benchmark e prezzi dei modelli più recenti, ci siamo chiesti: nella pratica, su un compito reale per un cliente, cosa cambia davvero? Questa settimana lo abbiamo provato con un caso interno.",
        points=[
            "Abbiamo preso un compito concreto di analisi su un documento lungo (lo stesso tipo di lavoro per cui i nuovi modelli vengono presentati come più adatti) e lo abbiamo affidato al modello in test, confrontando il risultato con il nostro metodo abituale.",
            "[Da personalizzare con l'esito reale del test del team: dove il modello ha funzionato meglio, dove ha avuto bisogno di una correzione umana, quanto tempo è stato risparmiato o perso davvero — senza inventare cifre o esiti non verificati.]",
            "La lezione non è «questo modello è il migliore», ma «un modello nuovo va testato sul proprio caso d'uso prima di cambiare strumento, non adottato perché vince su un benchmark pubblico».",
        ],
        cta="La vostra azienda ha già testato un modello di nuova generazione su un compito reale, o si affida ancora ai soli benchmark pubblicati? Raccontatecelo 👇",
        hashtags="#IntelligenzaArtificiale #AIBusiness #Esperienza #B2B #Innovazione",
    ),
    dict(
        badge="Prioritario",
        day="Venerdì 16/10",
        format="Divulgativo stile Datapizza",
        title="OpenAI ha appena «firmato» i testi di ChatGPT per l'Europa. Come funziona, in parole *povere*",
        news="textGrain, la filigrana testuale di OpenAI per l'AI Act europeo",
        news_url="https://www.actuia.com/en/news/openai-will-watermark-chatgpt-in-the-eu-but-leaves-the-api-opt-in/",
        hook="Il 5 ottobre OpenAI ha pubblicato textGrain, il sistema che userà per «firmare» i testi di ChatGPT nell'Unione Europea. Non è un timbro visibile, e non è neanche invisibile nel senso che si immagina di solito. Vale la pena capire come funziona davvero.",
        points=[
            "Un testo scritto da ChatGPT sembra identico a uno scritto da una persona, ma a ogni parola il modello sceglie, tra le alternative possibili, quella leggermente favorita da un calcolo statistico legato a una chiave segreta e alle parole precedenti.",
            "Chi ha quella chiave può rileggere il testo e misurare se quel pattern statistico c'è: non serve nessun carattere nascosto o invisibile, serve solo rifare lo stesso calcolo e confrontarlo.",
            "Il limite è proprio nella sua natura statistica: su un testo lungo e non modificato il rilevamento è alto (95% su 400 token in inglese), ma scende sotto editing leggero — sostituire un quarto delle parole con sinonimi lo fa crollare al 17% — e varia molto da una lingua europea all'altra.",
        ],
        cta="Ti sembra una soluzione tecnica solida per sapere cosa è stato scritto da un'AI, o un primo passo ancora facile da aggirare? Dicci la tua 👇",
        hashtags="#AI #TechExplained #AIAct #B2B #Compliance",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Carosello dati — il divario AI tra grandi imprese e PMI italiane",
        title="Le grandi imprese italiane adottano l'AI quattro volte più delle *PMI*",
        news="Dati Osservatorio IIA su adozione AI nelle imprese italiane (giugno 2026)",
        news_url="https://www.tecnoandroid.it/news/osservatorio-iia-l836-delle-pmi-italiane-e-ancora-senza-ai-1908305/",
        hook="I dati dell'Osservatorio IIA, presentati a giugno 2026, fotografano un'Italia a due velocità sull'adozione dell'AI nelle imprese. Non sono dati della settimana, ma il divario che descrivono si sta allargando, non riducendo.",
        points=[
            "16,4% — la quota di imprese italiane che usa l'AI nel 2025, quasi raddoppiata rispetto all'8,2% del 2024 secondo l'Osservatorio IIA.",
            "53,1% — la quota di grandi imprese italiane che ha già adottato l'AI, contro il 15,7% delle PMI: un divario di 37,4 punti percentuali, salito dai 20 punti del 2023.",
            "58,6% — la quota di PMI italiane che indica la mancanza di competenze interne come primo ostacolo all'adozione dell'AI.",
            "Le PMI rappresentano oltre il 96% del tessuto produttivo italiano: un divario che cresce tra chi è già avanti e chi non ha ancora iniziato non resta un problema di poche aziende, diventa un problema di competitività del Paese.",
        ],
        closing="Il divario non si chiude da solo, e non si chiude comprando uno strumento in più: le PMI che lo stanno colmando lo fanno con formazione mirata e un metodo di adozione graduale — non con un rollout generale a tutta l'azienda dall'oggi al domani.",
        cta="Nella tua azienda, il principale ostacolo all'adozione dell'AI è la mancanza di competenze, di tempo, o di un metodo per iniziare? 👇",
        hashtags="#IntelligenzaArtificiale #PMI #DigitalTransformation #B2B #Formazione",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    dict(
        badge="Riserva",
        day="Banca contenuti (settimana corrente o successiva)",
        format="Riflessione di chiusura settimana / lista community",
        title="5 cose che questa settimana ci dice sulla corsa all'*AI*",
        news="Sintesi dei trend della settimana 1 - 9 ottobre 2026",
        news_url="https://www.infoworld.com/article/4229615/google-makes-gemini-4-ai-model-available-to-a-trusted-few.html",
        hook="Chiudiamo la settimana con quello che ci portiamo a casa dalle notizie AI degli ultimi giorni.",
        points=[
            "Google torna competitivo con Gemini 4 Argon, ma non vince su ogni benchmark: la corsa alla frontiera non ha più un solo leader indiscusso su tutto.",
            "Anthropic apre l'accesso ridotto ai propri modelli e rende pubblico un numero enorme — 129.000 vulnerabilità trovate dal progetto Glasswing — che dice quanto lavoro di sicurezza ci sia ancora da fare sul codice che gira nelle aziende.",
            "OpenAI prova a rispettare l'AI Act europeo con una filigrana nei testi, ma i suoi stessi dati mostrano che un editing leggero la rende quasi inutile: la conformità dichiarata da un fornitore non va data per scontata.",
            "Un agente AI cinese, Manus, cerca una valutazione da 4 miliardi di dollari nello stesso periodo in cui la fiducia negli agenti resta un tema aperto in tutto il settore.",
            "Nessuno di questi punti richiede di inseguire il prossimo modello. Tutti richiedono lo stesso lavoro: testare prima di adottare, verificare prima di fidarsi, misurare il risultato invece del benchmark.",
        ],
        closing="Una settimana di correzioni, più che di rivoluzioni: i laboratori rispondono ai problemi emersi nelle settimane scorse con prodotti concreti, ma nessuno di questi prodotti sostituisce la verifica che un'azienda deve comunque fare per conto proprio.",
        cta="Qual è la notizia di questa settimana che ti ha fatto riflettere di più? 👇",
        hashtags="#AINews #WeeklyRecap #Tech #IntelligenzaArtificiale #B2B",
        carousel_note="Idea di riserva: gli asset non vengono generati salvo attivazione.",
    ),
    # Idea 8, extra: aggiunta su richiesta esplicita di Ramona (9/10) sul tema
    # del risparmio economico delle aziende grazie all'AI. Sesto post
    # Prioritario della settimana, oltre ai 5 dello schema standard: eccezione
    # dichiarata, non un cambio della cadenza di default a 5/settimana. Angolo
    # diverso dall'idea 8 della settimana scorsa (risparmio di TEMPO per le
    # PMI italiane, studio OpenAI/Opinium): qui il tema e' il risparmio
    # economico a livello enterprise, con dati PwC/ISG/Gartner che mostrano
    # quanto sia raro, oggi, vederlo misurato davvero.
    dict(
        badge="Prioritario",
        day="Venerdì 16/10 (extra della settimana, su richiesta)",
        format="Carosello dati (mito da sfatare — l'AI fa risparmiare automaticamente)",
        title="L'AI fa risparmiare in automatico sui costi aziendali? Solo per il 12% delle *aziende*",
        news="PwC Global CEO Survey 2026 + dati ISG e Gartner sulla spesa AI",
        news_url="https://italia-informa.com/ai-piu-economica-imprese-costi-in-aumento.aspx",
        hook="🔥 Il mito: adottare l'AI in azienda si traduce quasi automaticamente in un risparmio sui costi, prima o poi.",
        no_hashtags=True,
        is_myth=True,
        myth_body="I dati del PwC Global CEO Survey 2026 e di altre due ricerche indipendenti raccontano una storia più lenta e più selettiva.",
        points=[
            "12% — la quota di CEO che dichiara sia ricavi più alti sia costi più bassi grazie all'AI, secondo il PwC Global CEO Survey 2026 (4.454 CEO intervistati in 95 paesi): la combinazione che ci si aspetta, oggi raggiunta solo da una minoranza.",
            "56% — la quota di CEO che non ha ancora visto benefici finanziari significativi dall'AI, nello stesso sondaggio.",
            "31% — la quota dei 1.200 casi d'uso AI analizzati da ISG (Information Services Group) arrivata in piena produzione; di questi, solo uno su quattro ha raggiunto il ritorno economico atteso.",
            "La spesa globale in AI prevista da Gartner per il 2026 sale comunque a 2.520 miliardi di dollari (+44% sull'anno precedente), oltre la metà destinata a infrastruttura — chip, server, data center — non a progetti che generano risparmio diretto.",
        ],
        myth_closing="Il prezzo per usare l'AI continua a scendere, ma la spesa delle aziende sale lo stesso: più richieste, documenti più lunghi, agenti che fanno più chiamate in sequenza. Il risparmio non arriva da solo con l'adozione — arriva da un progetto misurato, su un caso d'uso specifico, con un metodo per sapere se sta funzionando. È la differenza tra sperare in un risparmio e costruirlo.",
        cta="Nella tua azienda, il risparmio ottenuto grazie all'AI viene misurato con un metodo, o si dà per scontato che ci sia? 👇",
        hashtags="",
    ),
    # Idea 9, extra: debutto, su richiesta esplicita di Ramona (9/10), di una
    # rubrica settimanale su F-hack AI (fhack.ai), la piattaforma/evento di
    # hackathon AI di Digitiamo stessa. A differenza di tutte le altre idee
    # della settimana, qui la fonte e' Digitiamo in prima persona (fhack.ai),
    # non una notizia di settore esterna, ed e' l'unico post della settimana
    # con un messaggio apertamente promozionale: coerente con la natura della
    # rubrica, non con la regola "nessun post vende prima di giovedi'" pensata
    # per i contenuti di curation editoriale. Finche' Ramona non conferma se
    # questo sostituisce uno dei 5 slot standard o resta un'aggiunta fissa,
    # resta un'eccezione dichiarata come le altre idee extra di questa
    # settimana.
    dict(
        badge="Prioritario",
        day="Martedì 13/10, ore 17:00 (extra della settimana, su richiesta — rubrica F-hack AI)",
        format="Carosello / documento LinkedIn — F-hack AI (rubrica settimanale)",
        title="Niente slide, solo un prototipo che funziona entro sera: dentro F-hack AI *01*",
        news="F-hack AI 01 (18/9/2026, Talent Garden Milano) + F-hack AI 02, challenge aperte",
        news_url="https://www.fhack.ai",
        hook="Il 18 settembre abbiamo portato F-hack AI 01 a Talent Garden Milano: il nostro format di hackathon dove un'azienda porta un problema vero, e più team AI-first lo risolvono in parallelo, nello stesso giorno, con un prototipo che funziona davvero — non uno slide deck.",
        points=[
            "4 aziende, 4 challenge reali in altrettanti ambiti diversi — dalla sicurezza dei modelli linguistici ai media generativi, passando per impatto urbano e gestione dei dati — e 5 team AI-first al lavoro in parallelo sullo stesso tipo di problema.",
            "Ogni team aveva le stesse KPI, definite prima dell'evento, e sono state le aziende stesse a valutare i prototipi finali: non una giuria esterna, non una presentazione, un confronto diretto sul risultato.",
            "Il principio alla base è lo stesso di sempre: l'AI non si impara, si costruisce. Per questo l'evento si chiude con una demo dal vivo, non con delle slide.",
            "Le challenge per F-hack AI 02 sono aperte da ora: la data dell'evento dal vivo è ancora da annunciare, ma c'è anche il F-hack Lab, sempre attivo, per chi ha un problema reale da mettere alla prova senza aspettare la prossima edizione.",
        ],
        closing="Se la tua azienda ha un caso d'uso AI che vuole vedere costruito — non solo raccontato in una proposta — le challenge per F-hack AI 02 sono aperte, e il F-hack Lab non ha scadenze.",
        cta="Hai un problema in azienda che vorresti vedere risolto da un prototipo AI reale, costruito in un giorno? Raccontacelo nei commenti o scrivi a info@fhack.ai 👇",
        hashtags="#FhackAI #IntelligenzaArtificiale #Innovazione #B2B #Hackathon",
    ),
]

# ---------------------------------------------------------------------------
# SUGGERIMENTI DI PUBBLICAZIONE
# ---------------------------------------------------------------------------
publishing = [
    dict(
        day="Lunedì 12/10",
        time="08:00",
        format="Thought leadership",
        reason="Apertura settimana, finestra mattutina 7:30-9:30: massimo traffico professionale, ideale per un post di respiro ampio che dà il tono alla settimana senza chiedere nulla.",
    ),
    dict(
        day="Martedì 13/10",
        time="12:15",
        format="Mito da sfatare (sicurezza del codice generato/controllato dall'AI)",
        reason="Finestra pausa pranzo 12:00-13:00, giorno a massimo traffico B2B. Formato diretto e polarizzante, pensato per generare commenti più che reach — e prepara il terreno al carosello del giorno dopo sullo stesso filo (fidarsi di un modello perché è nuovo o perché vince un benchmark).",
    ),
    dict(
        day="Mercoledì 14/10",
        time="12:15",
        format="Carosello dati / mito da sfatare (benchmark e prezzi dei nuovi modelli)",
        reason="Seconda finestra pausa pranzo B2B, distanziata di un giorno dal primo mito ma sullo stesso filo narrativo. Il formato documento/carosello ha oggi il tasso di engagement più alto su LinkedIn, e i dati su benchmark e prezzi sono densi abbastanza da meritare uno spazio proprio.",
    ),
    dict(
        day="Giovedì 15/10",
        time="08:30",
        format="Esperienza diretta (test interno su un modello di nuova generazione)",
        reason="Segue narrativamente il carosello del giorno prima, nella finestra mattutina. Reach tipicamente più basso di un carosello, ma è il formato che storicamente genera più commenti e messaggi diretti da decision maker — va mantenuto in calendario anche se il reach atteso è minore.",
    ),
    dict(
        day="Venerdì 16/10",
        time="08:00",
        format="Divulgativo (Datapizza style)",
        reason="Contenuto divulgativo a bassa frizione, adatto a chiusura settimana lavorativa quando i decision maker scorrono il feed con più calma; nessuna CTA commerciale.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 1 — Carosello «il divario AI tra grandi imprese e PMI italiane»",
        reason="Banca contenuti: utile come secondo documento se questa settimana c'è margine di pubblicazione, o come apertura della settimana successiva su un tema a lungo termine per il pubblico B2B italiano. Non promossa a Prioritario questa settimana: i 5 slot fissi dello schema (apertura, due miti, esperienza diretta, divulgativo) sono già tutti occupati dal filo narrativo su modelli e sicurezza.",
    ),
    dict(
        day="Da programmare",
        time="—",
        format="Riserva 2 — Riflessione di chiusura",
        reason="Chiude l'arco della settimana. Utile nel weekend se il traffico lo giustifica, o come richiamo della settimana successiva.",
    ),
    dict(
        day="Venerdì 16/10",
        time="12:15",
        format="Carosello dati — l'AI fa risparmiare in automatico? (extra, su richiesta)",
        reason="Settimo post della settimana, aggiunto su richiesta dopo l'approvazione del piano standard: non rientra nello schema 5 Prioritario + 2 Riserva. Finestra pausa pranzo B2B, nello stesso giorno del divulgativo mattutino ma distanziata di oltre 4 ore; formato documento/carosello per dati densi (PwC, ISG, Gartner) e un angolo diverso dal risparmio di tempo già trattato nella settimana del 5/10 (qui: risparmio economico misurato, non percepito).",
    ),
    dict(
        day="Martedì 13/10",
        time="17:00",
        format="Carosello / documento — rubrica F-hack AI (extra, su richiesta, debutto)",
        reason="Ottavo post della settimana: debutto della rubrica settimanale su F-hack AI richiesta da Ramona. Orario di fine giornata lavorativa come secondo post del martedì, distanziato di oltre 4 ore dal mito della pausa pranzo per non competere sullo stesso pubblico nello stesso momento. È l'unico post della settimana con fonte interna (fhack.ai) e messaggio apertamente promozionale — coerente con la natura della rubrica, non con la regola di non vendere nei primi giorni pensata per la curation editoriale. Il giorno fisso della rubrica (e se sostituire uno dei 5 slot standard o restare un'aggiunta) va confermato da Ramona per le settimane successive.",
    ),
]
