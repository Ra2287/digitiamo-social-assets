# Generatore PED Digitiamo (Piano Editoriale settimanale)

Genera il report PDF settimanale, le grafiche social (carosello + immagini dei
post) e crea le bozze su Buffer. Gli asset già generati stanno nella cartella
superiore, che fa da **CDN pubblica**: Buffer scarica le immagini da
`raw.githubusercontent.com`.

## Come è organizzato

Il principio: **contenuto, layout e brand sono tre cose separate.**

```
brand-spec.md        La verità sul brand: asset, palette, font, formati, divieti.
                     Estratta dai template Canva reali — leggila prima di
                     toccare qualsiasi cosa di visivo.
brand/
  tokens.py          Palette, font, formati, asset come dati. UNICA fonte.
  fonts/*.woff2      Montserrat 700/800 + Lato 400/700 (i font del brand)
  bg/*.png           Gli sfondi Canva reali
  logo/*.png         Wordmark e icone-categoria, con alpha

week.py              ← CONTENUTO della settimana per le grafiche
build_report.py      ← CONTENUTO della settimana per il report
captions.py          ← TESTI dei post per Buffer

templates.py         Layout delle grafiche social (da week.py a HTML)
generate_html.py     Layout del report (da build_report.py a HTML)
render.py            HTML -> PNG/PDF (unico renderer)
publish_buffer.py    Crea le bozze su Buffer, con preflight degli URL
```

Ogni settimana si modificano **solo i tre file di contenuto**. Layout e brand
non si toccano.

## Flusso settimanale

1. **Ricerca** trend/news della settimana (fuori da questo codice).
2. **Contenuti**: aggiorna `build_report.py` (trend, competitor, 7 idee),
   `week.py` (slide del carosello + immagini singole) e `captions.py` (testi
   dei post). In `week.py` imposta la nuova `DATE`.
3. **Genera tutto**:
   ```bash
   python3 render.py all
   ```
   Produce nella cartella superiore: `PED_Digitiamo_<data>.pdf`, le 6 PNG del
   carosello + `carosello_<slug>_<data>.pdf`, e le 4 PNG delle immagini singole.
   (Anche `render.py carousel` / `singles` / `report` singolarmente.)
4. **Controlla le grafiche a occhio.** Il renderer blocca l'esecuzione se un
   testo sfora il suo riquadro, ma non giudica se è *bello*.
5. **Commit e push** dei nuovi asset. Il push deve avvenire **prima** del passo 6.
6. **Bozze su Buffer**:
   ```bash
   export BUFFER_API_KEY="..."
   export BUFFER_CHANNEL_ID="..."
   python3 publish_buffer.py
   ```
   Fa un preflight su ogni URL prima di creare qualsiasi bozza: se un asset non
   è raggiungibile, non crea niente.
7. **Approvazione umana** in Buffer. Lo script crea solo bozze, mai post
   programmati.

## Regola dei nomi file (non negoziabile)

**Non riusare mai un nome file già pubblicato.** Buffer scarica l'asset
dall'URL al momento della pubblicazione effettiva della bozza, che può avvenire
giorni dopo la creazione: sovrascrivere un file cambia in silenzio l'immagine
di un post già approvato. `render.py` si rifiuta di sovrascrivere un file
esistente — se serve rigenerare, cambia `DATE` o lo slug in `week.py`, oppure
cancella a mano l'asset non ancora pubblicato.

## Dipendenze

```bash
pip3 install -r requirements.txt
python3 -m playwright install chromium
```

Se Chromium è già presente nell'ambiente, indicalo invece di riscaricarlo:

```bash
export CHROMIUM_PATH=/opt/pw-browsers/chromium
```

Senza quella variabile si usa il Chromium di Playwright.

## Credenziali (MAI nel codice — la repo è pubblica)

`publish_buffer.py` legge tutto dall'ambiente:

- `BUFFER_API_KEY` — token Bearer per `api.buffer.com`
- `BUFFER_CHANNEL_ID` — id del canale LinkedIn "digitiamo" (tipo `ChannelId!`
  nello schema GraphQL Buffer, non `String!`)
- `ASSETS_RAW_BASE` — opzionale, per puntare a un altro host degli asset

Per il push su GitHub usa un credential helper o `gh auth login`. **Non**
passare il token inline nell'URL di `git push`: resta nella cronologia della
shell.

## Note sul carosello/documento Buffer

Buffer accetta la creazione di bozze "documento" via API (asset type
`document`, con `url` + `title` + `thumbnailUrl`), ma **non genera l'anteprima
a pagine sfogliabili** per documenti allegati via URL esterno: i campi
`numPages`/`thumbnails` restano vuoti anche dopo ore (testato sia con
`raw.githubusercontent.com` sia con un mirror CDN). Il documento resta
funzionante e viene scaricato correttamente alla pubblicazione. Per vedere
l'anteprima prima di approvare, l'unica via nota è aprire la bozza nell'editor
Buffer e ri-allegare il PDF a mano (drag & drop).

Nota collaterale: `raw.githubusercontent.com` serve i PDF come
`application/octet-stream`, non `application/pdf`. È normale e il preflight lo
accetta.

## Da dove viene il brand

Gli asset in `brand/` non sono ricostruzioni: vengono dai template Canva reali
usati in produzione dal renderer del progetto `social-ped`. Provenienza di ogni
singolo valore (incluse le coordinate dei ritagli del logo) in `brand-spec.md`.

Cosa manca ancora, in breve: il logo in **vettoriale** (gli asset sono PNG
ritagliati), la versione **navy del wordmark** per fondi chiari, e le
**icone-categoria** oltre a News AI e Webinar. Dettagli in `brand-spec.md` §8.
