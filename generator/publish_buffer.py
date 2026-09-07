# -*- coding: utf-8 -*-
"""
Crea le bozze settimanali del PED sul canale LinkedIn "digitiamo" via Buffer GraphQL API.

Le credenziali NON sono incluse in questo file (la repo e' pubblica): vanno passate
come variabili d'ambiente prima di eseguire lo script.

Variabili d'ambiente richieste:
  BUFFER_API_KEY     token Bearer per api.buffer.com
  BUFFER_CHANNEL_ID  id del canale LinkedIn "digitiamo" (tipo ChannelId, non String)

Uso tipico (da adattare ogni settimana con le nuove caption/URL immagine):
  export BUFFER_API_KEY="..."
  export BUFFER_CHANNEL_ID="..."
  python3 publish_buffer.py
"""
import json
import os
import ssl
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


def _graphql(api_key, query, variables):
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
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


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


def main():
    api_key = os.environ.get("BUFFER_API_KEY")
    channel_id = os.environ.get("BUFFER_CHANNEL_ID")
    if not api_key or not channel_id:
        raise SystemExit(
            "Imposta BUFFER_API_KEY e BUFFER_CHANNEL_ID come variabili d'ambiente prima di eseguire lo script."
        )

    # Le caption stanno in captions.py, la data e gli slug in week.py: gli URL
    # si derivano da li' invece di essere riscritti a mano ogni settimana.
    import captions
    import week

    posts = []
    for single in week.SINGLES:
        # week.py dice quale caption va con quale immagine: la corrispondenza
        # non e' posizionale (CAPTION_3 e' il carosello, non un'immagine singola).
        name = single["caption"]
        caption = getattr(captions, name, None)
        if caption is None:
            raise SystemExit("captions.py non definisce %s (richiesto da %s)"
                             % (name, single["slug"]))
        posts.append((
            single["slug"],
            caption,
            RAW_BASE + "brandstyle_%s_%s.png" % (single["slug"], week.DATE),
        ))

    preflight([url for _, _, url in posts])

    for label, text, img_url in posts:
        _check_result(create_image_post(api_key, channel_id, text, img_url), label)

    print("\nFatto: %d bozze create su Buffer (da approvare a mano)." % len(posts))


if __name__ == "__main__":
    main()
