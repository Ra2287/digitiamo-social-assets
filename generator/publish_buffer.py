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
import urllib.request

BUFFER_ENDPOINT = "https://api.buffer.com"

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


def main():
    api_key = os.environ.get("BUFFER_API_KEY")
    channel_id = os.environ.get("BUFFER_CHANNEL_ID")
    if not api_key or not channel_id:
        raise SystemExit(
            "Imposta BUFFER_API_KEY e BUFFER_CHANNEL_ID come variabili d'ambiente prima di eseguire lo script."
        )

    # Esempio: personalizzare con le caption/URL della settimana corrente
    # (vedi captions.py per il testo dei post e il repo per gli URL immagine
    # gia' pubblicati su GitHub raw).
    from captions import CAPTION_1, CAPTION_2, CAPTION_4, CAPTION_5  # noqa: E402

    base_img = "https://raw.githubusercontent.com/Ra2287/digitiamo-social-assets/main/"
    posts = [
        (CAPTION_1, base_img + "brandstyle_idea1-claudeforce_2026-08-31.png"),
        (CAPTION_2, base_img + "brandstyle_idea2-vibecoding-mito_2026-08-31.png"),
        (CAPTION_4, base_img + "brandstyle_idea4-esperienza-diretta_2026-08-31.png"),
        (CAPTION_5, base_img + "brandstyle_idea5-rag-datapizza_2026-08-31.png"),
    ]

    for text, img_url in posts:
        res = create_image_post(api_key, channel_id, text, img_url)
        print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
