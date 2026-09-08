# -*- coding: utf-8 -*-
"""
Crea le bozze settimanali del PED sul canale LinkedIn "digitiamo" via Buffer GraphQL API.

Le credenziali NON sono incluse in questo file (la repo e' pubblica): vanno passate
come variabili d'ambiente prima di eseguire lo script.

Variabili d'ambiente:
  BUFFER_API_KEY     token Bearer per api.buffer.com (obbligatoria)
  BUFFER_CHANNEL_ID  opzionale: di norma il canale LinkedIn viene ricavato
                     dall'API. Serve solo se all'account sono collegati piu'
                     canali LinkedIn, perche' in quel caso lo script non sceglie
                     per conto suo (tipo GraphQL ChannelId, non String)

Uso:
  export BUFFER_API_KEY="..."
  python3 publish_buffer.py

Caption e URL non si scrivono piu' a mano: vengono da `plan.content()` e
`names.py`, le stesse fonti del renderer.
"""
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

BUFFER_ENDPOINT = "https://api.buffer.com"

# Base degli asset pubblici. La repo fa da CDN: Buffer scarica da qui.
RAW_BASE = os.environ.get(
    "ASSETS_RAW_BASE",
    "https://raw.githubusercontent.com/Ra2287/digitiamo-social-assets/main/",
)

CREATE_IMAGE_POST_QUERY = """
mutation CreateDraftPost($text: String!, $channelId: ChannelId!, $imageUrl: String!) {
  createPost(input: { text: $text, channelId: $channelId, schedulingType: automatic, mode: addToQueue, saveToDraft: true, assets: [{ image: { url: $imageUrl } }] }) {
    ... on PostActionSuccess { post { id text assets { id mimeType } } }
    ... on MutationError { message }
  }
}
"""

CREATE_DOCUMENT_POST_QUERY = """
mutation CreateDraftDocumentPost($text: String!, $channelId: ChannelId!, $docUrl: String!, $docTitle: String!, $thumbUrl: String!) {
  createPost(input: { text: $text, channelId: $channelId, schedulingType: automatic, mode: addToQueue, saveToDraft: true, assets: [{ document: { url: $docUrl, title: $docTitle, thumbnailUrl: $thumbUrl } }] }) {
    ... on PostActionSuccess { post { id text assets { id mimeType } } }
    ... on MutationError { message }
  }
}
"""

DELETE_POST_QUERY = """
mutation DelPost($input: DeletePostInput!) {
  deletePost(input: $input) {
    ... on DeletePostSuccess { id }
    ... on VoidMutationError { message }
  }
}
"""


KEYCHAIN_SERVICE = "digitiamo-buffer"

ISTRUZIONI_TOKEN = """Il token Buffer non e' disponibile.

Sul Mac, salvalo una volta sola nel Keychain (non chiede di incollarlo in un
comando, quindi non finisce nella cronologia della shell):

    security add-generic-password -a "$USER" -s %s -w

(premi invio, poi incolla il token al prompt: non viene mostrato)

Da quel momento qualunque sessione lo trova da sola, anche quando e' Claude a
lanciare lo script. In alternativa, per un uso una volta sola:

    read -rs "KEY?Buffer access token: " && export BUFFER_API_KEY="$KEY" && unset KEY

Il token NON va nel codice ne' in un file della repo: questa repo e' pubblica.""" % KEYCHAIN_SERVICE


def _from_keychain():
    """Il token dal Keychain di macOS. None se non c'e', non e' leggibile, o
    non siamo su un Mac.

    La prima volta macOS puo' chiedere l'autorizzazione con una finestra: si
    concede una volta ("Consenti sempre").
    """
    if sys.platform != "darwin":
        return None
    try:
        out = subprocess.run(
            ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() or None if out.returncode == 0 else None


def token_file():
    """Il percorso del file con il token, FUORI dalla cartella della repo.

    Perche' fuori e non un `.env` accanto al codice: questa repo e' pubblica, e
    un file dentro l'albero di lavoro e' a un `git add -A` di distanza
    dall'essere pubblicato per sempre. Il `.gitignore` protegge fino al primo
    errore; una cartella diversa protegge sempre.

    Segue XDG dove definito, cosi' funziona su Linux, macOS e Windows.
    """
    base = os.environ.get("XDG_CONFIG_HOME") or os.path.join(
        os.path.expanduser("~"), ".config")
    return os.path.join(base, "digitiamo", "buffer-token")


def _from_file():
    """Il token dal file di configurazione. None se non c'e'."""
    path = token_file()
    try:
        with open(path, encoding="utf-8") as f:
            token = f.read().strip()
    except (IOError, OSError, UnicodeDecodeError):
        return None
    if not token:
        return None

    # Su POSIX un file di segreti leggibile da altri utenti e' un problema:
    # lo si segnala, ma non si rifiuta il token — bloccare la pubblicazione
    # per i permessi sarebbe peggio del rischio che si vuole evitare.
    if os.name == "posix":
        mode = os.stat(path).st_mode & 0o077
        if mode:
            print("AVVISO: %s e' leggibile da altri utenti.\n"
                  "        Restringilo con:  chmod 600 %s" % (path, path))
    return token


def api_key():
    """Il token Buffer, dalla prima fonte che ce l'ha.

    Ordine: ambiente, Keychain (solo macOS), file di configurazione. L'ambiente
    per primo perche' e' quello che usa un'esecuzione automatica in CI, dove il
    token arriva da un secret e non deve essere scritto da nessuna parte.
    """
    return ((os.environ.get("BUFFER_API_KEY") or "").strip()
            or _from_keychain()
            or _from_file()
            or _exit_senza_token())


def _exit_senza_token():
    mac = """Sul Mac, nel Keychain (la via migliore: non e' un file):

    security add-generic-password -a "$USER" -s %s -w

(premi invio, poi incolla il token al prompt: non viene mostrato)""" % KEYCHAIN_SERVICE

    raise SystemExit("""Il token Buffer non e' disponibile. Tre modi, in ordine di preferenza.

1. In un'esecuzione automatica (GitHub Actions e simili): la variabile
   d'ambiente BUFFER_API_KEY, da un secret. Non va scritta su disco.

2. %s

3. Su Linux e Windows, in un file FUORI dalla repo:

    %s

   Crealo con la sola riga del token, poi restringi i permessi:
    mkdir -p "%s" && chmod 600 "%s"

   Fuori dalla repo di proposito: questa repo e' PUBBLICA, e un file dentro
   l'albero di lavoro e' a un `git add -A` dall'essere pubblicato per sempre.

Per un uso una volta sola, senza scrivere niente:

    read -rs "KEY?Buffer access token: " && export BUFFER_API_KEY="$KEY" && unset KEY

Il token NON va nel codice, in un file della repo, o in una chat: se e'
finito in una conversazione, va rigenerato su Buffer.""" % (
        mac, token_file(), os.path.dirname(token_file()), token_file()))


def _graphql(api_key, query, variables):
    if not isinstance(api_key, str):
        # Succede se si passa per sbaglio la FUNZIONE api_key invece del token
        # che restituisce: l'header diventa "Bearer <function ...>" e Buffer
        # risponde 401, cioe' un errore che incolpa la chiave invece del codice.
        raise TypeError(
            "il token deve essere una stringa, non %s: probabilmente e' stata "
            "passata la funzione api_key invece di api_key()"
            % type(api_key).__name__)
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        BUFFER_ENDPOINT,
        data=payload,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    # Il contesto TLS esplicito serve anche qui, non solo nel preflight: senza,
    # su un Python che non trova la CA di sistema ogni chiamata a Buffer
    # fallirebbe con CERTIFICATE_VERIFY_FAILED.
    try:
        with urllib.request.urlopen(req, timeout=30, context=_ssl_context()) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Un traceback di quindici righe non dice a nessuno cosa fare. Gli errori
        # di autenticazione sono di gran lunga i piu' frequenti, e la causa e'
        # quasi sempre la chiave: vale la pena dirlo.
        body = ""
        try:
            body = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            pass
        if e.code in (401, 403):
            raise SystemExit(
                "Buffer ha risposto %d %s: la chiave non e' valida.\n"
                "  - BUFFER_API_KEY deve essere un **access token personale** di "
                "Buffer (una stringa lunga), non un codice licenza o un id.\n"
                "  - Si genera dalle impostazioni sviluppatore dell'account "
                "Buffer, e va rigenerato se e' stato condiviso.\n"
                "  - Controlla che la variabile sia esportata in QUESTA shell: "
                "`echo ${BUFFER_API_KEY:+impostata}`.\n"
                "%s" % (e.code, e.reason, ("  Risposta: %s" % body) if body else "")
            )
        raise SystemExit("Buffer ha risposto %d %s.%s"
                         % (e.code, e.reason, ("\n  Risposta: %s" % body) if body else ""))
    except urllib.error.URLError as e:
        raise SystemExit("Buffer non raggiungibile: %s" % e.reason)


def create_image_post(api_key, channel_id, text, image_url):
    """Crea una bozza con immagine allegata (asset type: image)."""
    result = _graphql(
        api_key,
        CREATE_IMAGE_POST_QUERY,
        {"text": text, "channelId": channel_id, "imageUrl": image_url},
    )
    return result


def create_document_post(api_key, channel_id, text, doc_url, doc_title, thumb_url):
    """Crea una bozza con documento/carosello allegato (asset type: document).

    NOTA: al momento della scrittura, Buffer non genera l'anteprima a pagine
    sfogliabili per i documenti allegati via URL esterno tramite questa API
    (numPages/thumbnails restano vuoti anche dopo ore) - e' un limite noto
    della piattaforma, non un problema del PDF sorgente. Il documento resta
    comunque funzionante: Buffer lo scarica correttamente al momento della
    pubblicazione effettiva della bozza.
    """
    result = _graphql(
        api_key,
        CREATE_DOCUMENT_POST_QUERY,
        {
            "text": text,
            "channelId": channel_id,
            "docUrl": doc_url,
            "docTitle": doc_title,
            "thumbUrl": thumb_url,
        },
    )
    return result


def delete_post(api_key, post_id):
    result = _graphql(api_key, DELETE_POST_QUERY, {"input": {"id": post_id}})
    return result


CHANNELS_QUERY = """
query Channels($organizationId: OrganizationId!) {
  channels(input: { organizationId: $organizationId }) {
    id
    name
    displayName
    service
  }
}
"""

ORGS_QUERY = "query { account { organizations { id name } } }"


def channels(api_key):
    """Tutti i canali collegati, su tutte le organizzazioni dell'account."""
    res = _graphql(api_key, ORGS_QUERY, {})
    if res.get("errors"):
        raise SystemExit("Buffer ha rifiutato la richiesta: %s"
                         % json.dumps(res["errors"], ensure_ascii=False)[:300])
    orgs = (((res.get("data") or {}).get("account") or {}).get("organizations")) or []
    if not orgs:
        raise SystemExit("Nessuna organizzazione per questo token: la chiave e' valida?")

    out = []
    for org in orgs:
        got = _graphql(api_key, CHANNELS_QUERY, {"organizationId": org["id"]})
        for ch in ((got.get("data") or {}).get("channels")) or []:
            out.append(dict(ch, organization=org.get("name")))
    return out


def resolve_channel(api_key, service="linkedin"):
    """Il canale su cui pubblicare, ricavato dall'API invece che configurato.

    `social-ped` fa cosi' e ha ragione: un id copiato a mano in una variabile
    d'ambiente e' un passaggio in piu' per chiunque installi il progetto, e un
    id sbagliato pubblica sul canale di qualcun altro.

    Differenza voluta rispetto a social-ped: se i canali che corrispondono sono
    piu' di uno **non ne sceglie uno**. Scegliere il primo significherebbe
    poter pubblicare sulla pagina sbagliata senza che nessuno lo noti; meglio
    fermarsi e farsi dire quale, con BUFFER_CHANNEL_ID.
    """
    found = channels(api_key)
    match = [c for c in found if service in (c.get("service") or "").lower()]
    if not match:
        raise SystemExit(
            "Nessun canale '%s' collegato a Buffer.\nCanali disponibili: %s"
            % (service, ", ".join("%s:%s" % (c.get("service"),
                                             c.get("displayName") or c.get("name"))
                                  for c in found) or "nessuno"))
    if len(match) > 1:
        raise SystemExit(
            "Ci sono %d canali '%s' collegati, non scelgo io su quale pubblicare.\n"
            "Imposta BUFFER_CHANNEL_ID con quello giusto:\n%s"
            % (len(match), service,
               "\n".join("  %s  %s (%s)" % (c["id"], c.get("displayName") or c.get("name"),
                                            c.get("organization")) for c in match)))
    ch = match[0]
    print("Canale: %s (%s, %s)" % (ch.get("displayName") or ch.get("name"),
                                   ch.get("service"), ch.get("organization")))
    return ch["id"]


def _ssl_context():
    """Contesto TLS che funziona anche dove OpenSSL non trova la CA di sistema.

    Su macOS il Python di python.org spesso ha `ssl.get_default_verify_paths()`
    che punta a un cert.pem inesistente: senza questo, ogni verifica fallirebbe
    con CERTIFICATE_VERIFY_FAILED e il preflight bocciherebbe URL validi —
    peggio che non averlo. Si usa il bundle di certifi quando disponibile.
    """
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


# Esiti distinti: un problema di trasporto locale (TLS, DNS, timeout) NON e' la
# stessa cosa di un asset mancante, e non va trattato come tale.
OK, MISSING, UNKNOWN = "ok", "missing", "unknown"


def check_url(url):
    """Verifica che l'asset esista DAVVERO e sia servito come immagine/PDF.

    Perche' serve: Buffer scarica l'asset dall'URL al momento della
    pubblicazione effettiva della bozza, non alla creazione. Un URL sbagliato
    (typo nel nome file, push dimenticato) produce una bozza accettata senza
    errori che fallisce giorni dopo, quando nessuno sta piu' guardando.

    Ritorna (esito, dettaglio) con esito in {OK, MISSING, UNKNOWN}.
    """
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "digitiamo-ped/1"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=_ssl_context()) as resp:
            ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
            length = int(resp.headers.get("Content-Length") or 0)
    except urllib.error.HTTPError as e:
        # Il server ha risposto: qui l'asset manca per davvero.
        return MISSING, "HTTP %s" % e.code
    except Exception as e:
        # Non siamo riusciti a chiedere: non sappiamo se l'asset esista.
        return UNKNOWN, "%s: %s" % (type(e).__name__, e)
    # raw.githubusercontent.com serve i PDF come application/octet-stream, non
    # come application/pdf: va accettato (Buffer li scarica correttamente).
    # Quello che va respinto e' il text/html della pagina 404 di GitHub.
    if ctype.startswith("text/"):
        return MISSING, "il server ha risposto HTML, non un asset (%s)" % ctype
    if not (ctype.startswith("image/") or ctype in ("application/pdf", "application/octet-stream")):
        return MISSING, "Content-Type inatteso: %s" % (ctype or "assente")
    if length and length < 1024:
        return MISSING, "file troppo piccolo (%d byte)" % length
    return OK, "%s, %d KB" % (ctype, length // 1024)


def preflight(urls, strict=True):
    """Controlla tutti gli URL. Interrompe se un asset manca davvero.

    Gli esiti UNKNOWN (rete/TLS locale) non bloccano: vengono segnalati come
    avviso, perche' bocciare un asset valido per un problema di trasporto
    locale fermerebbe la pubblicazione senza motivo. Con strict=False anche i
    MISSING diventano avvisi.
    """
    print("Preflight di %d URL:" % len(urls))
    missing, unknown = [], []
    for u in urls:
        outcome, detail = check_url(u)
        tag = {OK: "OK   ", MISSING: "MANCA", UNKNOWN: "?    "}[outcome]
        print("  %s %s  (%s)" % (tag, u.rsplit("/", 1)[-1], detail))
        if outcome == MISSING:
            missing.append((u, detail))
        elif outcome == UNKNOWN:
            unknown.append((u, detail))

    if unknown:
        print("\nAVVISO: %d URL non verificabili da questa macchina (rete/TLS)."
              "\n        Non e' detto che manchino: verifica a mano prima di approvare le bozze."
              % len(unknown))
    if missing and strict:
        raise SystemExit(
            "\n%d asset non raggiungibili: nessuna bozza creata.\n"
            "Controlla di aver committato E pushato gli asset prima di pubblicare."
            % len(missing)
        )
    if not missing and not unknown:
        print("Tutti gli URL sono raggiungibili.")
    print()


def _check_result(res, label):
    """Solleva un errore sui fallimenti GraphQL invece di limitarsi a stamparli.

    Prima un MutationError su uno dei 4 post veniva stampato e ignorato: il
    ciclo continuava e l'esecuzione terminava con successo apparente.
    """
    if res.get("errors"):
        raise SystemExit("[%s] errore GraphQL: %s" % (label, json.dumps(res["errors"], ensure_ascii=False)))
    payload = (res.get("data") or {}).get("createPost") or {}
    if payload.get("message"):
        raise SystemExit("[%s] Buffer ha rifiutato la bozza: %s" % (label, payload["message"]))
    post = payload.get("post") or {}
    if not post.get("id"):
        raise SystemExit("[%s] risposta inattesa: %s" % (label, json.dumps(res, ensure_ascii=False)[:400]))
    print("[%s] bozza creata: %s" % (label, post["id"]))
    return post


LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "buffer-drafts.json")


def _load_ledger():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (IOError, ValueError):
        return []


def _record(entries):
    """Registra le bozze create: (settimana, revisione, slug, id, url).

    Serve al ciclo di rifacimento. Quando un post viene rifatto, la revisione
    sale e l'asset prende un URL nuovo: la bozza vecchia resta su Buffer,
    puntata all'immagine vecchia. Senza questo registro nessuno sa piu' quale
    bozza sia — e a fine settimana ne vengono pubblicate due.
    """
    ledger = _load_ledger()
    ledger.extend(entries)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Registrate in %s." % os.path.basename(LEDGER))


def _entries_for(slugs):
    """Le bozze registrate per questa settimana, sui post indicati."""
    import week
    return [e for e in _load_ledger()
            if e.get("date") == week.DATE and e.get("slug") in slugs]


def _split(posts):
    """Divide i post in: bozza da creare, bozza gia' creata, bozza obsoleta.

    La revisione e' per post (`week.REDO`), quindi il confronto va fatto post
    per post: rifare l'idea 2 non rende obsolete le bozze delle altre.
    """
    import names
    known = _entries_for({p["slug"] for p in posts})
    todo, done, stale = [], [], []
    for p in posts:
        rev = names.revision(p["slug"])
        mine = [e for e in known if e.get("slug") == p["slug"]]
        if any((e.get("revision") or 0) == rev for e in mine):
            done.append(p["slug"])
        else:
            todo.append(p)
        stale += [e for e in mine if (e.get("revision") or 0) < rev]
    return todo, done, stale


def _posts():
    """Le bozze da creare, derivate dal report (immagini singole + caroselli)."""
    import captions
    import names
    import plan
    import week

    def text_for(item):
        name = item.get("caption")
        text = getattr(captions, name, None) if name else None
        if text is None:
            raise SystemExit(
                "captions.py non definisce %s, richiesto da %s.\n"
                "Convenzione: il testo di un post derivato dal report si chiama "
                "CAPTION_<numero dell'idea nel report>, quindi qui serve %s.\n"
                "Un post dichiarato a mano in week.py usa invece il nome che "
                "scrive nel suo campo `caption`.\n"
                "Ogni post prioritario ha bisogno del suo testo: `python3 "
                "plan.py` elenca quali servono."
                % (name, item["slug"], name))
        return text

    carousels, singles = plan.content()
    posts = []

    for item in carousels:
        # Il carosello e' un post con documento allegato, e Buffer vuole la
        # prima slide come anteprima.
        pdf = RAW_BASE + names.carousel_pdf(item["slug"])
        thumb = RAW_BASE + names.carousel_slide(item["slug"], 1)
        posts.append(dict(kind="document", slug=item["slug"], text=text_for(item),
                          doc_url=pdf, thumb_url=thumb,
                          title=item.get("title") or item["slug"],
                          urls=[pdf, thumb]))

    for item in singles:
        img = RAW_BASE + names.single(item["slug"])
        posts.append(dict(kind="image", slug=item["slug"], text=text_for(item),
                          image_url=img, urls=[img]))
    return posts


def main():
    key = api_key()
    # Il canale si ricava dall'API; la variabile serve solo per forzarlo.
    channel_id = os.environ.get("BUFFER_CHANNEL_ID") or resolve_channel(key)

    import names
    import week
    posts = _posts()
    if not posts:
        raise SystemExit(
            "Nessun post da pubblicare: il report non ha idee 'Prioritario'.\n"
            "Controlla build_report.py, oppure `python3 plan.py` per vedere il piano."
        )
    print("Settimana %s: %d post nel piano.\n" % (week.DATE, len(posts)))

    todo, done, stale = _split(posts)
    for slug in done:
        print("  bozza gia' creata, salto: %s" % slug)
    if stale:
        # Non le cancello da solo: sono contenuti che una persona ha gia' visto,
        # e cancellare su un servizio esterno non si annulla.
        print("\nATTENZIONE: %d bozze puntano ad asset di una revisione\n"
              "precedente. Vanno cancellate, altrimenti il post esce due volte:"
              % len(stale))
        for e in stale:
            print("  r%s  %s  (id %s)" % (e.get("revision"), e.get("slug"), e.get("id")))
        print("  Per cancellarle:  python3 publish_buffer.py --elimina-obsolete")
    if not todo:
        print("\nNiente da creare.")
        return
    print()

    preflight([u for p in todo for u in p["urls"]])

    created = []
    for p in todo:
        if p["kind"] == "document":
            res = create_document_post(key, channel_id, p["text"],
                                       p["doc_url"], p["title"], p["thumb_url"])
        else:
            res = create_image_post(key, channel_id, p["text"], p["image_url"])
        post = _check_result(res, p["slug"])
        created.append(dict(date=week.DATE, revision=names.revision(p["slug"]),
                            slug=p["slug"], id=post["id"], url=p["urls"][0]))

    _record(created)
    print("\nFatto: %d bozze create su Buffer (da approvare a mano)." % len(created))


def delete_stale():
    """Cancella le bozze di questa settimana rimaste da revisioni precedenti."""
    key = api_key()
    import week
    _, _, stale = _split(_posts())
    if not stale:
        print("Nessuna bozza obsoleta per la settimana %s." % week.DATE)
        return
    for e in stale:
        print("cancello r%s %s (id %s):" % (e.get("revision"), e.get("slug"), e.get("id")),
              json.dumps(delete_post(key, e["id"]), ensure_ascii=False)[:200])
    ledger = [e for e in _load_ledger() if e not in stale]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)
        f.write("\n")


def list_channels():
    """Stampa i canali collegati. Utile per capire cosa vede la chiave."""
    found = channels(api_key())
    print("%d canali collegati:" % len(found))
    for c in found:
        print("  %-11s %-28s %s" % (c.get("service"),
                                    c.get("displayName") or c.get("name"), c["id"]))


if __name__ == "__main__":
    if "--canali" in sys.argv:
        list_channels()
    elif "--elimina-obsolete" in sys.argv:
        delete_stale()
    else:
        main()
