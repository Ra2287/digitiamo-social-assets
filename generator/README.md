# Generatore PED Digitiamo (Piano Editoriale settimanale)

Genera il report PDF settimanale, le grafiche social (carosello + immagini dei
post) e crea le bozze su Buffer. Gli asset finiscono in `settimane/<data>/`,
**una cartella per settimana**, che fa da **CDN pubblica**: Buffer scarica le
immagini da `raw.githubusercontent.com`.

I percorsi li costruisce `names.py`. Un asset già pubblicato **non si sposta e
non si rinomina**: il suo URL è dentro una bozza, e cambiarlo la rompe senza
errori visibili fino al giorno della pubblicazione.

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

build_report.py      ← CONTENUTO della settimana (idee, trend, competitor)
captions.py          ← TESTI dei post per Buffer
week.py              la data, i rifacimenti (REDO), le correzioni a mano

plan.py              Dal report alle slide: sceglie il template dal campo `format`
names.py             I nomi dei file degli asset. UNICA fonte (renderer + Buffer)
templates.py         Layout delle grafiche social (da plan/week a HTML)
generate_html.py     Layout del report (da build_report.py a HTML)
render.py            HTML -> PNG/PDF (unico renderer)
publish_buffer.py    Crea le bozze su Buffer, con preflight degli URL
```

Ogni settimana si modificano **solo i file di contenuto**. Layout, brand e
scelta dei template non si toccano: `plan.py` deriva le slide dal report.

## Flusso settimanale

1. **Ricerca** trend/news della settimana (fuori da questo codice).
2. **Contenuti**: aggiorna `build_report.py` (trend, competitor, 7 idee) e
   `captions.py` (testi dei post). In `week.py` imposta la nuova `DATE`.
   Le slide **non** si scrivono a mano: le deriva `plan.py` dal report.
3. **Controlla la scelta dei template**: `python3 plan.py` stampa quale tipo di
   post è stato dedotto per ogni idea. Se un formato non è riconosciuto si
   ferma, e va aggiunta una regola o allineata la dicitura nel report.
4. **Genera tutto**:
   ```bash
   python3 render.py all
   ```
   Produce in `settimane/<data>/`: `PED_Digitiamo_<data>.pdf`, le PNG dei
   caroselli + `carosello_<slug>_<data>.pdf`, e le PNG delle immagini singole.
   I post già generati vengono saltati: si può rilanciare senza doppioni.
   (Anche `render.py carousel` / `singles` / `report` singolarmente.)
5. **Controlla le grafiche a occhio.** Il renderer blocca l'esecuzione se un
   testo sfora il suo riquadro, ma non giudica se è *bello*.
6. **Commit e push** dei nuovi asset. Il push deve avvenire **prima** del passo 7.
7. **Bozze su Buffer**:
   ```bash
   export BUFFER_API_KEY="..."
   python3 publish_buffer.py
   ```
   Il canale viene ricavato dall'API (`--canali` per elencarli): niente id da
   copiare a mano.
   Fa un preflight su ogni URL prima di creare qualsiasi bozza: se un asset non
   è raggiungibile, non crea niente.
8. **Approvazione umana** in Buffer. Lo script crea solo bozze, mai post
   programmati.

## Regola dei nomi file (non negoziabile)

**Non riusare mai un nome file già pubblicato.** Buffer scarica l'asset
dall'URL al momento della pubblicazione effettiva della bozza, che può avvenire
giorni dopo la creazione: sovrascrivere un file cambia in silenzio l'immagine
di un post già approvato.

Perciò `render.py` **salta** i post già generati: rilanciarlo è sicuro. I nomi
stanno tutti in `names.py`, unica fonte anche per gli URL che finiscono su
Buffer — quando erano scritti in due posti, bastava cambiarne uno perché la
bozza puntasse a un URL inesistente, con l'errore visibile solo giorni dopo.

## Rifare un post dopo la revisione umana

Il flusso è human-in-the-loop: il lunedì viene generato tutto, poi una persona
chiede modifiche. Rifare significa dare al post un **URL nuovo**, perché la
bozza esistente punta a quello vecchio.

1. Correggi il contenuto (`build_report.py`, `captions.py`, o la slide in
   `week.CAROUSELS`/`SINGLES`).
2. Segna il post in `week.REDO` — gli slug li stampa `python3 plan.py`:
   `REDO = {"idea2-la-sicurezza-dell-ai": 1}`
3. `python3 render.py all` rigenera solo quel post, con suffisso `-r1`.
4. Commit, push, `python3 publish_buffer.py`: crea la bozza nuova e segnala
   quella obsoleta. `python3 publish_buffer.py --elimina-obsolete` la elimina.

La revisione è per post: rifare l'idea 2 non tocca le altre. Le bozze create
sono registrate in `buffer-drafts.json` — senza quel registro non si saprebbe
quale bozza è diventata obsoleta.

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

- `BUFFER_API_KEY` — token Bearer per `api.buffer.com` (obbligatoria)
- `BUFFER_CHANNEL_ID` — **opzionale**: di norma il canale LinkedIn viene ricavato
  dall'API. Serve solo se all'account sono collegati più canali LinkedIn, caso in
  cui lo script si ferma invece di indovinare (tipo `ChannelId!` nello schema
  GraphQL Buffer, non `String!`)
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
