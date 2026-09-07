# -*- coding: utf-8 -*-
"""CONTENUTO della settimana per le grafiche social. **E' il file da modificare
ogni settimana** insieme a build_report.py (report) e captions.py (testi post).

Qui c'e' solo contenuto: nessun HTML, nessun colore, nessuna misura. Il layout
sta in templates.py, il brand in brand/tokens.py. Prima questo contenuto era
scritto a mano dentro il markup di carousel_slides.html / single_images.html,
il che fondeva contenuto, layout e brand in un unico file riscritto ogni volta.

Convenzione di markup nei testi: `*parola*` rende la parola in colore accento.
Nessun altro HTML e' ammesso — i testi vengono escapati.

Limiti di caratteri: vedi brand-spec.md §6. L'auto-fit e' una rete di sicurezza,
non un permesso a sforare.
"""

DATE = "2026-08-31"
WEEK_LABEL = "31 agosto – 4 settembre 2026"

# ---------------------------------------------------------------------------
# CAROSELLO — documento LinkedIn sfogliabile
# ---------------------------------------------------------------------------
# Ogni voce ha un `kind` che seleziona il layout in templates.py:
#   hook      apertura: eyebrow + titolone + sottotitolo
#   data      dato secco: numero/data gigante + spiegazione + nota
#   checklist elenco numerato di obblighi/punti
#   statement affermazione forte: titolone + corpo + nota
#   cta       chiusura: titolone + box con offerta
# `surface` codifica il REGISTRO del contenuto, non l'estetica (vedi templates.py):
#   navy = argomentazione (apertura, tesi, chiusura)
#   blue = fatto verificabile (dati, date, elenchi di obblighi)
AI_ACT = dict(
    slug="ai-act",
    post_type="compliance_carousel",   # il ritmo di colore viene da qui
    category="News AI",      # badge icona-categoria (vedi brand-spec.md §2)
    slides=[
        dict(
            kind="hook",
            eyebrow="Analisi settimanale",
            title="L'AI Act non è più una *promessa*",
            subtitle="È entrato in vigore il 2 agosto 2026. Ecco cosa cambia "
                     "davvero per chi fa software in Italia — in 5 numeri.",
        ),
        dict(
            kind="data",
            eyebrow="Data chiave",
            datanum="2 agosto 2026",
            explain="Il giorno in cui gli obblighi dell'AI Act sono passati "
                    "dalla teoria alla pratica in tutta l'Unione Europea.",
            note="Non è più una scadenza futura da tenere d'occhio: da questa "
                 "data, le regole si applicano.",
            source="Commissione Europea, Axios",
        ),
        dict(
            kind="checklist",
            eyebrow="Cosa è già attivo",
            title="3 obblighi già in *vigore*",
            items=[
                "Trasparenza sui contenuti generati da AI, chatbot inclusi",
                "Notifica obbligatoria agli utenti quando interagiscono con "
                "materiale creato dall'AI",
                "Watermarking per tracciare l'origine dei contenuti generati",
            ],
            source="digital-strategy.ec.europa.eu",
        ),
        dict(
            kind="data",
            eyebrow="Cosa manca ancora",
            datanum="Dic 2027 → Ago 2028",
            explain="Le regole più severe, per i sistemi AI ad alto rischio, "
                    "arrivano in due tappe successive.",
            note="Non tutto è già in vigore — ma chi aspetta l'ultima scadenza "
                 "per organizzarsi parte già in ritardo.",
            source="artificialintelligenceact.eu",
        ),
        dict(
            kind="statement",
            eyebrow="Il punto debole",
            title="L'EU AI Office può già chiedere *accesso e dati*",
            body="Anche senza multe già codificate in questa fase, l'Autorità "
                 "europea ha ora il potere di richiedere informazioni e accesso "
                 "ai modelli usati in azienda.",
            note="Tradotto: se non sai ancora dove e come la tua azienda usa "
                 "l'AI, è il momento di scoprirlo — prima che te lo chiedano loro.",
            source="digital-strategy.ec.europa.eu",
        ),
        dict(
            kind="cta",
            title="Governare l'AI non è un'opzione, *è il lavoro*",
            cta_title="Scrivici adesso ↗",
            cta_sub="Team Augmentation Digitiamo: professionisti AI Engineer & Dev "
                    "che si integrano nel tuo team per governare compliance, "
                    "architettura e produzione — senza costi di recruiting.",
        ),
    ],
)


# ---------------------------------------------------------------------------
# CAROSELLO 2 — idea 6 del PED (Riserva): i numeri di Nvidia
# ---------------------------------------------------------------------------
# Arco: aggancio -> quadro d'insieme -> il totale -> da dove arriva davvero ->
# la lettura -> chiamata all'azione. I tre kind guidati dai dati (`scorecard`,
# `figure`, `share`) non sono alternativi: coprono tre momenti diversi.
# Tutte le slide con cifre stanno sul campo navy, dove il verde e' ammesso come
# tinta dati (vedi templates.py e brand-spec.md §3).
NVIDIA = dict(
    slug="nvidia-q2",
    post_type="data_carousel",         # il ritmo di colore viene da qui
    category="News AI",
    slides=[
        dict(
            kind="hook",
            eyebrow="Numeri della settimana",
            title="96,2 miliardi in un *trimestre*",
            subtitle="Nvidia ha chiuso il trimestre più grande della sua storia. "
                     "Ecco cosa dicono davvero questi numeri sul mercato AI.",
        ),
        dict(
            kind="scorecard",
            eyebrow="I numeri, in fila",
            figure="96,2 mld",
            delta="+106%",
            unit="fatturato trimestrale, anno su anno",
            rows=[
                ("89 mld", "+117%", "dal segmento data center: il vero motore della crescita"),
                ("+9%", "in una seduta", "il titolo, con circa 440 miliardi di capitalizzazione aggiunta in un giorno"),
                ("+70%", "atteso FY2028", "gli analisti scommettono che la domanda di infrastruttura continui a salire"),
            ],
            source="Intellectia.ai / US News",
        ),
        dict(
            kind="figure",
            eyebrow="Il totale",
            figure="96,2",
            unit="miliardi\ndi dollari",
            delta="+106%",
            delta_note="anno su anno",
            say="Il fatturato trimestrale di Nvidia. Più che raddoppiato in dodici mesi.",
            source="Intellectia.ai / US News",
        ),
        dict(
            kind="share",
            eyebrow="Da dove arriva",
            figure="89",
            unit="miliardi\nsu 96,2",
            value=89.0, total=96.2,
            label="Data center", label_rest="Resto",
            say="Quasi tutto il trimestre è un solo segmento, cresciuto del 117% "
                "anno su anno. Non è Nvidia che cresce: è l'infrastruttura AI.",
            source="Intellectia.ai / US News",
        ),
        dict(
            kind="statement",
            eyebrow="La lettura",
            title="Mercato agli inizi o *bolla infrastrutturale?*",
            body="La domanda di infrastruttura AI non rallenta, ma alza l'asticella "
                 "su chi può permettersi di costruire capacità computazionale in proprio.",
            note="Per la maggior parte delle aziende quell'accesso passerà da cloud "
                 "e partner terzi, non da hardware in casa.",
            source="Intellectia.ai / US News",
        ),
        dict(
            kind="cta",
            title="I numeri non dicono *cosa farne*",
            cta_title="Parliamone ↗",
            cta_sub="AI Business Academy Digitiamo: formazione e progetti mirati sui "
                    "casi d'uso reali della tua azienda — non AI a pioggia.",
        ),
    ],
)

# Tutti i caroselli della settimana. render.py li genera tutti.
CAROUSELS = [AI_ACT, NVIDIA]

# ---------------------------------------------------------------------------
# IMMAGINI SINGOLE — una per post prioritario
# ---------------------------------------------------------------------------
# `slug` finisce nel nome file: brandstyle_<slug>_<DATE>.png. Non riusare mai
# uno slug+data già pubblicato (vedi brand-spec.md §7).
# `caption` nomina l'attributo di captions.py da allegare a questa immagine:
# la corrispondenza NON è posizionale (CAPTION_3 è il carosello).
# `post_type` decide la superficie: il registro in templates.py assegna un fondo
# diverso a ciascun formato, così le quattro immagini della settimana non sono
# quattro volte la stessa.
SINGLES = [
    dict(
        slug="idea1-claudeforce",
        caption="CAPTION_1",   # attributo in captions.py
        post_type="thought_leadership",
        eyebrow="Thought leadership",
        title="L'interfaccia del software aziendale sta per *sparire*",
        box="Salesforce + Anthropic lanciano Claudeforce: l'AI diventa "
            "l'interfaccia del CRM.",
    ),
    dict(
        slug="idea2-vibecoding-mito",
        caption="CAPTION_2",   # attributo in captions.py
        post_type="myth",
        eyebrow="Mito da sfatare",
        title="Il vibe coding ha reso inutili gli sviluppatori *senior?*",
        box="Il 35% delle pull request su Cursor arriva già da agenti AI, "
            "non da persone.",
    ),
    dict(
        slug="idea4-esperienza-diretta",
        caption="CAPTION_4",   # attributo in captions.py
        post_type="direct_experience",
        eyebrow="Esperienza diretta",
        title="Abbiamo fatto revisionare del codice *AI* dal nostro team",
        box="Cosa succede davvero quando un agente apre una pull request nel "
            "workflow del team.",
    ),
    dict(
        slug="idea5-rag-datapizza",
        caption="CAPTION_5",   # attributo in captions.py
        post_type="mini_lesson",
        eyebrow="Mini-lezione",
        title="Cos'è il *RAG*, spiegato con gli avvocati",
        box="Google lancia Gemini Enterprise for Legal. Dietro, la tecnica AI "
            "del 2026.",
    ),
]
