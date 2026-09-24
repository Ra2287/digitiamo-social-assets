# -*- coding: utf-8 -*-
"""Come sono andati i post della settimana precedente, da Buffer.

Richiesto da Ramona il 24/9/2026: ogni report deve aprire con un bilancio di
cosa e' successo ai post proposti la settimana prima — non solo nuove idee.

## Cosa fa

1. Calcola la settimana precedente a `week.DATE` (lunedi'-domenica).
2. Legge `buffer-drafts.json` per sapere quali bozze erano state create per
   quella settimana (slug, id Buffer, e — dai registri scritti da questo
   punto in poi — titolo e formato dell'idea).
3. Interroga l'API GraphQL di Buffer per lo stato e le metriche (impression,
   reach, reazioni, commenti, condivisioni, tasso di engagement) di QUEI
   post specifici sul canale LinkedIn, filtrando per intervallo di date.
4. Confronta le due liste: quali bozze sono state pubblicate (`sent`), quali
   sono rimaste in sospeso (bozza mai approvata, o approvata ma non ancora
   uscita) — un dato utile quanto le metriche stesse.

## Perche' non e' contenuto scritto da Claude

A differenza di `trends`/`competitors`/`ideas` in `build_report.py`, questa
sezione e' calcolata da dati live ad ogni generazione del report: non va mai
scritta a mano, e non va "aggiustata" se i numeri sono deludenti. Se Buffer
non e' raggiungibile o manca il token, la sezione lo dice chiaramente invece
di restare vuota senza spiegazione o mostrare numeri vecchi.

## Il fallback via git

I registri scritti PRIMA di questo modulo (settimane fino al 2026-09-21) non
hanno i campi `title`/`format`: per quelle si recupera `build_report.ideas`
dal commit che ha chiuso quella settimana (`git show <sha>:generator/build_report.py`,
cercando l'ultimo commit con "PED <data>" nel messaggio). Richiede una clone
non superficiale (vedi `fetch-depth: 0` in ped.yml) — se anche questo fallisce,
l'etichetta ricade sullo slug reso leggibile: mai un titolo indovinato.
"""
import datetime
import json
import os
import subprocess

RAW_LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "buffer-drafts.json")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

METRIC_ORDER = ["impressions", "reach", "reactions", "comments", "shares", "engagementRate"]
METRIC_LABELS = {
    "impressions": "Impression",
    "reach": "Reach",
    "reactions": "Reazioni",
    "comments": "Commenti",
    "shares": "Condivisioni",
    "engagementRate": "Tasso di engagement",
}


# ---------------------------------------------------------------------------
# Funzioni pure: date, formattazione, confronto registro/Buffer. Nessuna rete,
# testabili da test_pipeline.py.
# ---------------------------------------------------------------------------
def previous_week(date_str):
    """(lunedi', domenica_esclusiva, etichetta) della settimana prima di `date_str`.

    `date_str` e' il lunedi' della settimana del report corrente (`week.DATE`).
    Ritorna il lunedi' di 7 giorni prima e il lunedi' successivo a quello
    (limite esclusivo, comodo per un filtro `dueAt: {start, end}`).
    """
    monday = datetime.date.fromisoformat(date_str)
    prev_monday = monday - datetime.timedelta(days=7)
    prev_sunday = monday - datetime.timedelta(days=1)
    label = "%s – %s" % (prev_monday.strftime("%d/%m"), prev_sunday.strftime("%d/%m/%Y"))
    return prev_monday.isoformat(), monday.isoformat(), label


def fmt_metric(mtype, value):
    """Un valore di metrica Buffer, formattato per la tabella del report."""
    if mtype == "engagementRate":
        return "%.1f%%" % value
    if value == int(value):
        return "{:,}".format(int(value)).replace(",", ".")
    return "%.1f" % value


def registry_entries_for(date_str, ledger_path=None):
    """Le voci di buffer-drafts.json per la settimana `date_str`."""
    path = ledger_path or RAW_LEDGER
    try:
        with open(path, encoding="utf-8") as f:
            ledger = json.load(f)
    except (IOError, ValueError):
        return []
    return [e for e in ledger if e.get("date") == date_str]


def _slugify_label(slug):
    """Ultima risorsa: uno slug come 'idea4-il-gap-ai-delle' diventa
    'Il gap ai delle...' — mai un titolo inventato, solo lo slug leggibile."""
    parts = slug.split("-")
    if parts and parts[0].startswith("idea"):
        parts = parts[1:]
    text = " ".join(parts)
    return (text[:1].upper() + text[1:]) if text else slug


def load_historical_ideas(date_str, repo_root=None):
    """`build_report.ideas` cosi' com'era nell'ultimo commit "PED <date_str>".

    None se non si trova nessun commit per quella settimana (repo troppo
    giovane, o clone superficiale senza la storia). Nessuna modifica al
    working tree: legge il contenuto del commit con `git show`, non fa
    checkout.
    """
    root = repo_root or REPO_ROOT
    try:
        log = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "generator/build_report.py"],
            cwd=root, capture_output=True, text=True, timeout=20, check=True,
        ).stdout
    except (subprocess.SubprocessError, OSError):
        return None
    needle = "PED %s" % date_str
    shas = [line.split(" ", 1)[0] for line in log.splitlines() if needle in line]
    if not shas:
        return None
    sha = shas[0]  # `git log` e' newest-first: il primo trovato e' l'ultimo di quella settimana.
    try:
        content = subprocess.run(
            ["git", "show", "%s:generator/build_report.py" % sha],
            cwd=root, capture_output=True, text=True, timeout=20, check=True,
        ).stdout
    except (subprocess.SubprocessError, OSError):
        return None
    ns = {"__name__": "historical_build_report"}
    try:
        exec(compile(content, "<build_report@%s>" % sha[:8], "exec"), ns)  # noqa: S102
    except Exception:
        return None
    return ns.get("ideas")


def _slug_label_map(date_str, repo_root=None):
    """slug -> (titolo, formato) per la settimana `date_str`, dalla storia git.

    Usa la stessa regola di `plan._slug` per ricavare lo slug da ogni idea,
    cosi' la chiave coincide esattamente con quella scritta nel registro.
    """
    ideas = load_historical_ideas(date_str, repo_root)
    if not ideas:
        return {}
    import plan
    out = {}
    for i, idea in enumerate(ideas, start=1):
        try:
            slug = plan._slug(idea, i)
        except Exception:
            continue
        out[slug] = (idea.get("title") or slug, idea.get("format") or "")
    return out


def label_for(entry, historical_map):
    """Titolo e formato leggibile per una voce del registro.

    Ordine: i campi scritti direttamente nel registro (settimane da questa in
    poi) vincono; poi la storia git; infine lo slug reso leggibile.
    """
    title = entry.get("title")
    fmt = entry.get("format")
    if not title or not fmt:
        hist_title, hist_fmt = historical_map.get(entry.get("slug") or "", (None, None))
        title = title or hist_title
        fmt = fmt or hist_fmt
    return title or _slugify_label(entry.get("slug") or ""), fmt or "—"


def build_summary(registry, sent_posts, historical_map=None):
    """Confronta il registro di una settimana con i post 'sent' trovati su Buffer.

    `registry`: voci di buffer-drafts.json per quella settimana (una lista di
    dict con almeno `slug`, `id`, `revision`).
    `sent_posts`: post da Buffer con almeno `id` e `metrics` (dict tipo->valore).
    `historical_map`: slug -> (titolo, formato), da `_slug_label_map` o {}.

    Ritorna un dict pronto per il template: righe pubblicate (con metriche),
    bozze rimaste in sospeso, e i totali/medie sulle sole righe pubblicate.
    """
    historical_map = historical_map or {}
    by_id = {p["id"]: p for p in sent_posts}

    # Per slug: solo l'ultima revisione registrata conta (le altre sono bozze
    # superate da un rifacimento, non "in sospeso").
    latest_by_slug = {}
    for e in registry:
        slug = e.get("slug")
        if slug is None:
            continue
        cur = latest_by_slug.get(slug)
        if cur is None or (e.get("revision") or 0) >= (cur.get("revision") or 0):
            latest_by_slug[slug] = e

    published, pending = [], []
    for slug, entry in latest_by_slug.items():
        title, fmt = label_for(entry, historical_map)
        post = by_id.get(entry.get("id"))
        if post is None:
            pending.append(dict(slug=slug, title=title, format=fmt))
            continue
        metrics = {m["type"]: m["value"] for m in (post.get("metrics") or [])}
        published.append(dict(slug=slug, title=title, format=fmt, metrics=metrics))

    totals = {}
    for mtype in METRIC_ORDER:
        vals = [p["metrics"][mtype] for p in published if mtype in p["metrics"]]
        if not vals:
            continue
        if mtype == "engagementRate":
            totals[mtype] = sum(vals) / len(vals)  # media, non somma: e' una percentuale
        else:
            totals[mtype] = sum(vals)

    best = None
    ranked = [p for p in published if "engagementRate" in p["metrics"]]
    if ranked:
        best = max(ranked, key=lambda p: p["metrics"]["engagementRate"])

    return dict(published=published, pending=pending, totals=totals, best=best)


# ---------------------------------------------------------------------------
# Rete: Buffer GraphQL. Isolata qui cosi' le funzioni sopra restano testabili
# senza connessione (vedi test_pipeline.py).
# ---------------------------------------------------------------------------
POSTS_QUERY = """
query WeeklyPosts($input: PostsInput!, $first: Int, $after: String) {
  posts(input: $input, first: $first, after: $after) {
    edges { node { id status dueAt metrics { type value } } }
    pageInfo { hasNextPage endCursor }
  }
}
"""


def resolve_org_and_channel(api_key, service="linkedin"):
    """(organizationId, channelId, displayName) del canale, dall'API.

    Stessa regola di `publish_buffer.resolve_channel`: se ci sono piu' canali
    dello stesso servizio non si sceglie, si solleva un errore — vedi li' il
    perche'.
    """
    import publish_buffer as pb
    res = pb._graphql(api_key, pb.ORGS_QUERY, {})
    orgs = (((res.get("data") or {}).get("account") or {}).get("organizations")) or []
    if not orgs:
        raise SystemExit("Nessuna organizzazione per questo token Buffer.")
    for org in orgs:
        got = pb._graphql(api_key, pb.CHANNELS_QUERY, {"organizationId": org["id"]})
        match = [c for c in ((got.get("data") or {}).get("channels")) or []
                 if service in (c.get("service") or "").lower()]
        if len(match) == 1:
            return org["id"], match[0]["id"], match[0].get("displayName") or match[0].get("name")
        if len(match) > 1:
            raise SystemExit(
                "Ci sono %d canali '%s': imposta BUFFER_CHANNEL_ID, non scelgo io."
                % (len(match), service))
    raise SystemExit("Nessun canale '%s' collegato a Buffer." % service)


def fetch_sent_posts(api_key, org_id, channel_id, start_iso, end_iso):
    """I post 'sent' sul canale, con `dueAt` in [start_iso, end_iso). Pagina da sola."""
    import publish_buffer as pb
    out, after = [], None
    variables = {
        "input": {
            "organizationId": org_id,
            "filter": {
                "channelIds": [channel_id],
                "status": ["sent"],
                "dueAt": {"start": start_iso + "T00:00:00Z", "end": end_iso + "T00:00:00Z"},
            },
        },
        "first": 50,
    }
    while True:
        variables["after"] = after
        res = pb._graphql(api_key, POSTS_QUERY, variables)
        if res.get("errors"):
            raise SystemExit("Buffer ha rifiutato la query dei post: %s"
                             % json.dumps(res["errors"], ensure_ascii=False)[:300])
        payload = (res.get("data") or {}).get("posts") or {}
        for edge in payload.get("edges") or []:
            out.append(edge["node"])
        page = payload.get("pageInfo") or {}
        if not page.get("hasNextPage"):
            break
        after = page.get("endCursor")
    return out


# ---------------------------------------------------------------------------
# Punto di ingresso per generate_html.py
# ---------------------------------------------------------------------------
def gather(date_str=None):
    """Il bilancio della settimana precedente a `date_str` (default week.DATE).

    Non solleva mai per un problema di rete o di token: ritorna sempre un
    dict con `ok` e, se `ok` e' False, `error` da mostrare nel report invece
    di una sezione vuota senza spiegazione.
    """
    import week
    date_str = date_str or week.DATE
    start, end, label = previous_week(date_str)
    registry = registry_entries_for(start)
    result = dict(ok=False, week_start=start, week_end=end, label=label,
                  registry_count=len(set(e.get("slug") for e in registry)))

    if not registry:
        result.update(ok=True, empty=True,
                      note="Nessuna bozza PED risultava creata per la settimana del %s: "
                           "probabilmente e' la prima settimana in cui questa sezione esiste, "
                           "o quella settimana non ha generato asset." % label)
        return result

    try:
        import publish_buffer as pb
        api_key = pb.api_key()
        org_id, channel_id, channel_name = resolve_org_and_channel(api_key)
        sent = fetch_sent_posts(api_key, org_id, channel_id, start, end)
    except SystemExit as e:
        result["error"] = str(e)
        return result
    except Exception as e:  # rete/TLS/timeout: non e' un errore di contenuto
        result["error"] = "%s: %s" % (type(e).__name__, e)
        return result

    historical_map = _slug_label_map(start)
    summary = build_summary(registry, sent, historical_map)
    result.update(ok=True, empty=False, channel=channel_name, **summary)
    return result
