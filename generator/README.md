# Generatore PED Digitiamo (Piano Editoriale settimanale)

Codice usato per generare in automatico il report PDF settimanale, le immagini
dei post LinkedIn e il carosello dati, e per caricarli come bozze su Buffer.
Le immagini e i PDF gia' generati sono nella cartella superiore di questa
repository; questa cartella (`generator/`) contiene solo il codice sorgente.

## Struttura

- `build_report.py` — contiene tutti i contenuti testuali del report settimanale
  (trend, analisi competitor, le 7 idee di post, calendario pubblicazione) come
  strutture dati Python. **E' il file da modificare ogni settimana** con i nuovi
  contenuti.
- `generate_html.py` — legge `build_report.py` e genera `report.html` (il
  layout HTML/CSS del PDF, con la palette brand Digitiamo).
- `render_pdf.py` — apre `report.html` con Playwright/Chromium e lo stampa in
  PDF (`../PED_Digitiamo_<data>.pdf`).
- `carousel_slides.html` — template HTML delle slide del carosello dati (6
  slide, formato 1080x1350). Da personalizzare con i dati della settimana.
- `render_carousel.py` — screenshot di ogni slide di `carousel_slides.html` →
  PNG, poi da unire in PDF con `img2pdf` (vedi sotto).
- `single_images.html` — template delle 4 immagini di accompagnamento ai post
  prioritari (stesso stile grafico del carosello: navy/blu/bianco, Archivo
  Black, accento verde/blu, palette brand Digitiamo).
- `render_single_images.py` — screenshot delle 4 slide di `single_images.html`
  → PNG.
- `captions.py` — testo finale (caption) di ciascun post, pronto per Buffer.
- `publish_buffer.py` — crea le bozze su Buffer via GraphQL (immagini +
  documento/carosello). Le chiavi API **non sono incluse**: vanno passate come
  variabili d'ambiente (vedi sotto).

## Flusso settimanale

1. Ricerca trend/news della settimana (fuori da questo codice).
2. Aggiornare `build_report.py` con i nuovi trend, competitor, 7 idee di post.
3. `python3 generate_html.py` → produce `report.html`.
4. `python3 render_pdf.py <YYYY-MM-DD>` → produce `../PED_Digitiamo_<data>.pdf`.
5. Aggiornare `carousel_slides.html` e `single_images.html` con i contenuti
   della settimana (titoli, dati, hook).
6. `python3 render_carousel.py <slug> <YYYY-MM-DD>` → produce le 6 PNG del
   carosello nella cartella superiore.
7. Unire le PNG del carosello in un unico PDF con `img2pdf`:
   ```python
   import img2pdf
   files = [f"carosello_<slug>_<data>_slide{i}.png" for i in range(1, 7)]
   with open("carosello_<slug>_<data>.pdf", "wb") as f:
       f.write(img2pdf.convert(files))
   ```
8. `python3 render_single_images.py <YYYY-MM-DD>` → produce le 4 PNG delle
   immagini prioritarie nella cartella superiore.
9. `git add`, `git commit`, `git push` di tutti i nuovi file generati (PDF,
   PNG) — **non riusare mai un nome file gia' usato in settimane precedenti**,
   perche' Buffer scarica il file dall'URL solo al momento della
   pubblicazione effettiva della bozza, che puo' avvenire giorni dopo la
   creazione.
10. Aggiornare `captions.py` con le nuove caption e lanciare
    `publish_buffer.py` (con le variabili d'ambiente impostate) per creare le
    bozze su Buffer.

## Dipendenze

```
pip install playwright img2pdf pypdf --break-system-packages
python3 -m playwright install chromium   # se non gia' presente
```

Negli ambienti dove Chromium e' gia' preinstallato (es. il container usato per
questa automazione), passare `executable_path='/opt/pw-browsers/chromium'` a
`playwright.chromium.launch()` invece di scaricarlo di nuovo (vedi gli script
esistenti).

## Credenziali (MAI hardcodare nel codice — repo pubblica)

`publish_buffer.py` legge le credenziali da variabili d'ambiente:

- `BUFFER_API_KEY` — token Bearer per `api.buffer.com`
- `BUFFER_CHANNEL_ID` — id del canale LinkedIn "digitiamo" (tipo `ChannelId!`
  nello schema GraphQL Buffer, non `String!`)

Il push su GitHub richiede un Personal Access Token fine-grained con permesso
"Contents: Read and write" sulla sola repo `digitiamo-social-assets`, passato
inline nel comando `git push` (mai salvato su file):

```bash
env -u https_proxy -u HTTPS_PROXY -u http_proxy -u HTTP_PROXY \
  git push "https://<TOKEN>@github.com/Ra2287/digitiamo-social-assets.git" main
```

## Nota nota sul carosello/documento Buffer

Buffer accetta la creazione di bozze "documento" via API (asset type
`document`, con `url` + `title` + `thumbnailUrl`), ma al momento della
scrittura di questo README **non genera l'anteprima a pagine sfogliabili**
per documenti allegati via URL esterno (i campi `numPages`/`thumbnails`
restano vuoti anche dopo ore, testato sia con `raw.githubusercontent.com` sia
con un mirror CDN). Il documento resta comunque funzionante e viene scaricato
correttamente da Buffer al momento della pubblicazione effettiva. Per vedere
l'anteprima a pagine prima di approvare, l'unica via nota e' aprire la bozza
nell'editor Buffer e ri-allegare il PDF manualmente da li' (drag & drop).
