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
def prova(nome):
    def deco(f):
        ok.append((nome, f))
        return f
    return deco


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
@prova("i nomi degli asset e gli URL su Buffer coincidono")
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
@prova("il ciclo con l'umano: ripetibile, e rifa' un post solo")
def _rifacimento():
    import names, plan, render, week
    from playwright.async_api import async_playwright

    tmp = tempfile.mkdtemp(prefix="ped-test-")
    vecchio_out, vecchio_redo = render.OUT_DIR, dict(getattr(week, "REDO", {}) or {})
    render.OUT_DIR = tmp

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
    for nome, f in ok:
        try:
            print("  ok    %-58s %s" % (nome, f() or ""))
        except Exception as e:
            falliti += 1
            print("  FALLITO %-56s %s: %s" % (nome, type(e).__name__, e))
    print()
    if falliti:
        raise SystemExit("%d prove fallite su %d." % (falliti, len(ok)))
    print("Tutte le %d prove passate." % len(ok))
