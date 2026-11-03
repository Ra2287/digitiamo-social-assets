# -*- coding: utf-8 -*-
"""Le verifiche della pipeline. Nessuna rete, nessun asset pubblicato toccato.

    python3 test_pipeline.py

Gira anche in CI, prima del render: una regressione qui costa un job rosso,
non una settimana di post sbagliati.

Perche' esiste: queste prove sono nate a mano durante la ricostruzione del
generatore, in una cartella temporanea. Un test che vive fuori dalla repo
marcisce — e due di essi erano gia' diventati stantii perche' riferivano slug
di una settimana passata. Qui i bersagli si ricavano dal piano corrente.
"""
import asyncio
import contextlib
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ok = []
def prova(nome, titoli_di_prova=False):
    def deco(f):
        ok.append((nome, f, titoli_di_prova))
        return f
    return deco


@contextlib.contextmanager
def _titoli_di_prova():
    """Le prove su nomi e rifacimenti girano sul report VERO, che puo' non
    avere ancora `titolo_post` (dal 2/11/2026 un titolo oltre 60 caratteri
    ferma il piano: e' giusto, ma non e' cio' che queste prove controllano).
    Qui, solo per la durata della prova, un titolo segnaposto; il report non
    viene toccato su disco."""
    import build_report, plan
    added = []
    for idea in build_report.ideas:
        if (not idea.get("titolo_post")
                and len((idea.get("title") or "").replace("*", "")) > plan.BUDGET["titolo"]):
            idea["titolo_post"] = "Titolo di prova della slide"
            added.append(idea)
    try:
        yield
    finally:
        for idea in added:
            del idea["titolo_post"]


# ---------------------------------------------------------------------------
@prova("plan.py scegle il template giusto per ogni formato del report")
def _template():
    import plan
    # Diciture reali, prese dai report esistenti: la scelta e' per parole
    # chiave proprio perche' cambiano fra un'esecuzione e l'altra.
    casi = [
        ("Carosello / rassegna news della settimana",
         "Tre lanci in una settimana", "news_roundup"),
        ("Carosello/documento LinkedIn (data-point multipli)",
         "News AI: le notizie della settimana", "news_roundup"),
        ("Carosello / documento dati",
         "L'AI nelle aziende italiane: i numeri", "data_carousel"),
        ("Carosello",
         "EU AI Act: obblighi di trasparenza in vigore", "compliance_carousel"),
        ("Carosello",
         "Cos'e' il reward hacking, spiegato semplice", "explainer_carousel"),
        ("Mito da sfatare (stile Talent Garden)",
         "La sicurezza dell'AI", "myth"),
        ("Thought leadership / grande quadro di settore",
         "Anthropic ha fermato il training", "thought_leadership"),
        ("Esperienza diretta (template)",
         "Come guardiamo la configurazione", "direct_experience"),
        ("Divulgativo stile Datapizza",
         "Cos'e' un endpoint", "mini_lesson"),
    ]
    for fmt, titolo, atteso in casi:
        got = plan.post_type_for(dict(format=fmt, title=titolo, badge="Prioritario"))
        assert got == atteso, "%r + %r -> %s invece di %s" % (fmt, titolo, got, atteso)
    # E un formato ignoto deve FERMARE, non tirare a indovinare.
    try:
        plan.post_type_for(dict(format="Formato che non esiste", title="x"))
    except plan.PlanError:
        pass
    else:
        raise AssertionError("un formato ignoto e' passato: indovinerebbe il template")
    return "%d formati + il rifiuto di un formato ignoto" % len(casi)


# ---------------------------------------------------------------------------
@prova("il layout segue il contenuto: barratura, cifre, citazione, foto, alternanza")
def _selezione():
    import plan, templates

    def errore(f):
        try:
            f()
        except plan.PlanError:
            return True
        return False

    # Barratura: solo con `barrato` scelto di proposito, anche nei miti.
    mito = dict(format="Mito da sfatare", badge="Prioritario",
                title="Il tuo editor gira in una sandbox, quindi è *sicuro*")
    assert plan.strike_word(mito, "myth") is None
    assert plan.strike_word(dict(mito, title="Se non la uso non mi *riguarda*"), "myth") is None
    assert plan.strike_word(dict(mito, barrato="sicuro"), "myth") == "sicuro"
    tl = dict(format="Thought leadership", title="OpenAI dice di aver risolto 3 problemi")
    assert plan.strike_word(dict(tl, barrato="risolto"), "thought_leadership") == "risolto"
    assert errore(lambda: plan.strike_word(dict(tl, barrato="assente"), "thought_leadership"))
    assert errore(lambda: plan.strike_word(dict(tl, barrato="3"), "thought_leadership"))
    assert errore(lambda: plan.strike_word(dict(tl, title="Il caso Irca", barrato="Irca"),
                                           "thought_leadership"))   # nome proprio

    # Cifre e segnale positivo: il segno da solo non basta.
    assert plan.is_gain("−12 ore", "a settimana di inserimento manuale")
    assert plan.is_gain("+18%", "di ricavi nel trimestre")
    assert not plan.is_gain("+117%", "di attacchi anno su anno")
    assert not plan.is_gain("800.000", "chiamate con una chiave rubata")
    dati = dict(format="Carosello / documento dati", badge="Prioritario", title="I conti",
                points=["16,3 miliardi di dollari — i ricavi.", "637 miliardi — gli impegni.",
                        "80,7 miliardi — la perdita.", "Una frase senza cifre."])
    kinds = [s["kind"] for s in plan.slides_for(dati, "data_carousel")]
    assert kinds[:3] == ["data_cover", "figure", "figure"], kinds
    kinds = [s["kind"] for s in plan.slides_for(dict(dati, points=dati["points"] + ["9 — altro."]),
                                                "data_carousel")]
    assert kinds[:2] == ["data_cover", "scorecard"], kinds
    kinds = [s["kind"] for s in plan.slides_for(dict(dati, is_myth=True), "data_carousel")]
    assert kinds[0] == "hook", "un mito apre col titolo barrato, non con la cifra"

    # Citazione: mai senza autore. Foto: solo un file locale dentro la repo.
    q = dict(format="Thought leadership", title="x", citazione="Una frase vera.")
    assert errore(lambda: plan.slides_for(q, "thought_leadership"))
    assert plan.slides_for(dict(q, autore="Nome"), "thought_leadership")[0]["kind"] == "quote"
    foto = dict(format="Esperienza diretta", title="x",
                immagine="generator/brand/photo/nasa-columbia-supercomputer.jpg")
    assert plan.slides_for(foto, "direct_experience")[0]["photo"].startswith("data:image/jpeg")
    assert errore(lambda: plan.decide(dict(foto, immagine="manca.jpg"), "direct_experience"))
    assert errore(lambda: plan.decide(dict(foto, immagine="https://x/y.jpg"), "direct_experience"))
    assert errore(lambda: plan.decide(dict(foto, immagine="../../etc/hosts"), "direct_experience"))

    # Alternanza: singole tipografiche scuro/chiaro, il carosello conta scuro;
    # dentro il carosello prima e ultima scure, i fatti chiari.
    idee = [dict(badge="Prioritario", format="Thought leadership", title="Uno a"),
            dict(badge="Prioritario", format="Mito da sfatare", title="Due b"),
            dict(dati, title="Tre c"),
            dict(badge="Prioritario", format="Esperienza diretta", title="Quattro d")]
    cs, ss, _ = plan.build(idee)
    assert [x["surface"] for x in ss] == ["dark", "light", "light"], [x["surface"] for x in ss]
    surf = [s["surface"] for s in cs[0]["slides"]]
    assert surf[0] == surf[-1] == "dark" and surf[1] == "light", surf
    assert templates.surface_for(dict(kind="figure", gain=True), 1, 4) == "dark"
    return "barratura, cifre/verde, citazione, foto e alternanza verificate"


# ---------------------------------------------------------------------------
@prova("poco testo sulle slide: budget, tagli ai confini, stop sul titolo")
def _budget():
    import plan, templates
    B = plan.BUDGET

    # Il titolo non si taglia mai: troppo lungo e senza titolo_post -> stop.
    lungo = dict(format="Thought leadership", badge="Prioritario",
                 title="Un titolo da report lunghissimo che spiega tutto per filo e per segno")
    try:
        plan.build([lungo])
    except plan.PlanError as e:
        assert "titolo_post" in str(e) and "Un titolo da report" in str(e), e
    else:
        raise AssertionError("un titolo oltre %d caratteri e' passato" % B["titolo"])
    breve = dict(lungo, titolo_post="Un titolo *breve*")
    assert plan.slides_for(breve, "thought_leadership")[0]["title"] == "Un titolo *breve*"
    for campo, val in (("titolo_post", "x" * 61), ("sottotitolo_post", "x" * 111)):
        try:
            plan.slides_for(dict(breve, **{campo: val}), "thought_leadership")
        except plan.PlanError:
            pass
        else:
            raise AssertionError("%s oltre budget e' passato" % campo)

    # Supporto: una frase, tagliata a un confine, mai a meta' parola.
    t, n = plan.fit("Prima frase breve. Seconda frase che non serve.", B["supporto"], True)
    assert t == "Prima frase breve." and n, (t, n)
    lunga = ("Il mito: le violazioni dei tool di sviluppo AI riguardano solo chi le "
             "subisce direttamente — se la tua azienda non ha un account, nulla.")
    t, n = plan.fit(lunga, B["supporto"], True)
    assert len(t) <= B["supporto"] and t.endswith("direttamente."), t
    t, n = plan.fit("parola " * 40, 60)
    assert len(t) <= 60 and t.endswith("parola…"), t
    assert plan.fit("Corta.", 60) == ("Corta.", "")

    # Elenco: al massimo 3 voci entro 80, le altre si tolgono (non si rimpicciolisce).
    idea = dict(format="Riflessione di chiusura", badge="Prioritario", title="Cinque cose brevi",
                points=["Voce numero %d, abbastanza lunga da dover essere tagliata a un "
                        "confine: qui finisce la parte utile e comincia il resto." % i
                        for i in range(5)], closing="x " * 200)
    sl = plan.slides_for(idea, "closing_list")
    liste = [s_ for s_ in sl if s_["kind"] == "checklist"]
    assert len(liste) == 1 and len(liste[0]["items"]) == B["voci"], liste
    assert all(len(v) <= B["voce"] for v in liste[0]["items"]), liste[0]["items"]
    sintesi = next(s_ for s_ in sl if s_["kind"] == "statement")
    assert len(sintesi["body"]) <= B["corpo"], len(sintesi["body"])

    # Scorecard, citazione, CTA, occhielli.
    dati = dict(format="Carosello dati", badge="Prioritario", title="I conti", is_myth=True,
                points=["%d — una descrizione decisamente troppo lunga per una riga di "
                        "scorecard, che deve stare in sessanta caratteri." % i for i in (1, 2, 3)])
    righe = next(s_ for s_ in plan.slides_for(dati, "data_carousel") if s_["kind"] == "scorecard")["rows"]
    assert all(len(d_) <= B["scorecard"] for _, d_ in righe), righe
    try:
        plan.quote_for(dict(title="x", citazione="x" * 141, autore="Nome"))
    except plan.PlanError:
        pass
    else:
        raise AssertionError("una citazione oltre budget e' passata: non si taglia")
    for pt in ("data_carousel", "compliance_carousel"):
        cta = plan._cta_for({}, pt)
        assert len(cta["cta_sub"]) <= B["cta"], cta["cta_sub"]
    occhielli = [v["label"] for v in templates.POST_TYPES.values()] + [
        "I numeri", "Il dato", "I punti", "In sintesi", "Chi l'ha detto"]
    assert all(len(o) <= B["occhiello"] for o in occhielli), [o for o in occhielli if len(o) > B["occhiello"]]
    return "titolo fermato, supporto/voci/sintesi/scorecard entro budget, citazione non tagliata"


# ---------------------------------------------------------------------------
@prova("i nomi degli asset e gli URL su Buffer coincidono", titoli_di_prova=True)
def _nomi():
    import names, plan, publish_buffer as pb, week

    # Il bug che questo test coglie: i nomi erano generati in render.py e
    # ricostruiti in publish_buffer.py. Bastava cambiarne uno perche' la bozza
    # puntasse a un URL inesistente, e l'errore si vedeva solo giorni dopo,
    # alla pubblicazione effettiva.
    carousels, singles = plan.content()
    attesi = set()
    for c in carousels:
        attesi |= {names.carousel_slide(c["slug"], i + 1)
                   for i in range(len(c["slides"]))}
        attesi.add(names.carousel_pdf(c["slug"]))
    attesi |= {names.single(x["slug"]) for x in singles}

    chiesti = {u[len(pb.RAW_BASE):] for p in pb._posts() for u in p["urls"]}
    orfani = chiesti - attesi
    assert not orfani, "Buffer chiederebbe URL che il renderer non produce: %s" % sorted(orfani)
    assert all(u.startswith("settimane/") for u in chiesti), chiesti

    # E con una revisione attiva gli URL devono cambiare, non restare uguali.
    prima = dict(getattr(week, "REDO", {}) or {})
    bersaglio = (carousels + singles)[0]["slug"]
    try:
        week.REDO = dict(prima, **{bersaglio: 1})
        nuovo = {u[len(pb.RAW_BASE):] for p in pb._posts() for u in p["urls"]}
        cambiati = nuovo - chiesti
        assert cambiati and all("-r1" in u for u in cambiati), \
            "una revisione non ha prodotto URL nuovi: %s" % sorted(cambiati)
    finally:
        week.REDO = prima
    return "%d URL, e una revisione ne produce di nuovi" % len(chiesti)


# ---------------------------------------------------------------------------
@prova("il formato dichiarato e' imposto, non solo documentato")
def _formato():
    from PIL import Image
    import brand.tokens as tokens
    import render

    w, h = tokens.FORMATS["portrait"]
    d = tempfile.mkdtemp()
    try:
        buono = os.path.join(d, "buono.png")
        Image.new("RGB", (w, h), "white").save(buono)
        render._check_size(buono, w, h)          # non deve sollevare

        for cattivo_size in ((1080, 1350), (w, h - 1)):
            p = os.path.join(d, "cattivo.png")
            Image.new("RGB", cattivo_size, "white").save(p)
            try:
                render._check_size(p, w, h)
            except SystemExit:
                assert not os.path.exists(p), "un asset fuori formato e' rimasto sul disco"
            else:
                raise AssertionError("%dx%d e' passato" % cattivo_size)
    finally:
        shutil.rmtree(d)
    return "%dx%d accettato, 1080x1350 e un pixel di scarto respinti" % (w, h)


# ---------------------------------------------------------------------------
@prova("il ciclo con l'umano: ripetibile, e rifa' un post solo", titoli_di_prova=True)
def _rifacimento():
    import names, plan, render, week
    from playwright.async_api import async_playwright

    tmp = tempfile.mkdtemp(prefix="ped-test-")
    vecchio_out, vecchio_redo = render.OUT_DIR, dict(getattr(week, "REDO", {}) or {})
    render.OUT_DIR = tmp
    # La prova simula il SUO proprio ciclo di rifacimento (REDO = {bersaglio: 1}
    # solo per la seconda genera()). Se in settimana e' gia' in corso un
    # rifacimento vero (week.REDO non vuoto, es. dopo una revisione di Ramona),
    # lasciarlo attivo durante la prima genera() qui sotto renderebbe SUBITO
    # quel post con suffisso -r1 dentro 'prima', e la seconda genera() (con
    # REDO sostituito dal solo bersaglio di prova) lo tratterebbe come "mai
    # fatto" alla revisione 0, generando un secondo file senza -r1: la prova
    # fallirebbe per un'interferenza tra lo stato reale e quello simulato, non
    # per un problema del renderer. Si azzera qui, si ripristina comunque nel
    # finally.
    week.REDO = {}

    async def _genera():
        async with async_playwright() as p:
            b = await p.chromium.launch(**render._launch_kwargs())
            try:
                await render.do_carousel(b)
                await render.do_singles(b)
            finally:
                await b.close()

    def genera():
        # Il renderer stampa una riga per asset: dentro un test diventa rumore
        # che copre l'esito. Si tiene da parte e si mostra solo se fallisce.
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                asyncio.run(_genera())
        except BaseException:
            sys.stdout.write(buf.getvalue())
            raise

    def istantanea():
        out = {}
        for root, _, files in os.walk(tmp):
            for f in files:
                p = os.path.join(root, f)
                out[os.path.relpath(p, tmp)] = os.path.getmtime(p)
        return out

    try:
        genera()
        prima = istantanea()
        assert prima, "non ha generato niente"

        # Ripetibile: un rilancio non deve toccare un asset pubblicato.
        genera()
        assert istantanea() == prima, "un rilancio ha riscritto qualcosa"

        # Rifacimento di UN post: solo quello cambia, gli altri restano.
        carousels, singles = plan.content()
        bersaglio = (singles or carousels)[0]["slug"]
        week.REDO = {bersaglio: 1}
        genera()
        dopo = istantanea()
        nuovi = [f for f in dopo if f not in prima]
        assert nuovi, "il rifacimento non ha prodotto niente"
        assert all("-r1" in f for f in nuovi), nuovi
        assert all(bersaglio in f for f in nuovi), \
            "il rifacimento ha toccato anche altri post: %s" % nuovi
        assert {f: dopo[f] for f in prima} == prima, \
            "ha modificato asset a cui puntano bozze esistenti"
        return "%d asset, rilancio a vuoto, %d rigenerati per '%s'" % (
            len(prima), len(nuovi), bersaglio)
    finally:
        render.OUT_DIR, week.REDO = vecchio_out, vecchio_redo
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
@prova("performance.py: settimana precedente, formattazione e confronto registro/Buffer")
def _performance():
    import performance as perf

    # La settimana precedente a un lunedi' e' il lunedi'-domenica di 7 giorni prima.
    start, end, label = perf.previous_week("2026-09-21")
    assert (start, end) == ("2026-09-14", "2026-09-21"), (start, end)
    assert "14/09" in label and "20/09/2026" in label, label

    # Formattazione: percentuale con un decimale, interi con separatore delle
    # migliaia, mai un valore inventato se manca la chiave.
    assert perf.fmt_metric("engagementRate", 4.5016) == "4.5%"
    assert perf.fmt_metric("impressions", 1234) == "1.234"
    assert perf.fmt_metric("reach", 160) == "160"

    # Il confronto registro/Buffer: un post 'sent' diventa una riga pubblicata
    # con le sue metriche, uno senza corrispondenza in Buffer resta "pending" -
    # mai inventato, mai scartato in silenzio. Una revisione superata (r0 dopo
    # un r1) non genera una riga fantasma.
    registry = [
        dict(slug="idea1-apertura", id="p1", revision=0, title="Apertura", format="Thought leadership"),
        dict(slug="idea2-mito", id="p2", revision=0, title="Mito vecchio", format="Mito da sfatare"),
        dict(slug="idea2-mito", id="p2b", revision=1, title="Mito corretto", format="Mito da sfatare"),
        dict(slug="idea3-mai-approvata", id="p3", revision=0, title="Mai approvata", format="Esperienza diretta"),
    ]
    sent = [
        dict(id="p1", metrics=[
            dict(type="impressions", value=300), dict(type="reactions", value=10),
            dict(type="comments", value=2), dict(type="shares", value=1),
            dict(type="engagementRate", value=5.0),
        ]),
        dict(id="p2b", metrics=[
            dict(type="impressions", value=100), dict(type="reactions", value=1),
            dict(type="comments", value=0), dict(type="shares", value=0),
            dict(type="engagementRate", value=1.0),
        ]),
        # p2 (revisione superata) e' 'sent' ma non deve comparire: e' stata
        # sostituita da p2b, la bozza vecchia va ignorata come un rifacimento.
        dict(id="p2", metrics=[dict(type="impressions", value=9999)]),
    ]
    summary = perf.build_summary(registry, sent)
    slugs_pubblicati = sorted(p["slug"] for p in summary["published"])
    assert slugs_pubblicati == ["idea1-apertura", "idea2-mito"], slugs_pubblicati
    titolo_idea2 = next(p["title"] for p in summary["published"] if p["slug"] == "idea2-mito")
    assert titolo_idea2 == "Mito corretto", titolo_idea2  # la revisione r1 vince, non r0
    assert [p["slug"] for p in summary["pending"]] == ["idea3-mai-approvata"]
    assert summary["totals"]["impressions"] == 400  # 300 + 100, MAI il 9999 della revisione superata
    assert round(summary["totals"]["engagementRate"], 2) == 3.0  # media (5.0+1.0)/2, non somma
    assert summary["best"]["slug"] == "idea1-apertura"  # eng. rate piu' alto

    return "settimana prec. calcolata, %d pubblicati/%d in sospeso, nessuna revisione fantasma" % (
        len(summary["published"]), len(summary["pending"]))


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    falliti = 0
    for nome, f, titoli in ok:
        try:
            with (_titoli_di_prova() if titoli else contextlib.nullcontext()):
                esito = f()
            print("  ok    %-58s %s" % (nome, esito or ""))
        except Exception as e:
            falliti += 1
            print("  FALLITO %-56s %s: %s" % (nome, type(e).__name__, e))
    print()
    if falliti:
        raise SystemExit("%d prove fallite su %d." % (falliti, len(ok)))
    print("Tutte le %d prove passate." % len(ok))
