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
                     Linguaggio approvato il 2/11/2026 — leggila prima di
                     toccare qualsiasi cosa di visivo.
brand/
  tokens.py          Palette, gradiente, font, formati, asset come dati. UNICA fonte.
  fonts/*.woff2      Sora 400/600/700 (latin + latin-ext, OFL) — più i
                     Montserrat/Lato legacy del solo report interno
  logo/              Marchio vettoriale (sorgente) + PNG legacy
  strike/            La barratura a mano del sito
  bg/*.png           Sfondi Canva del sistema precedente: SUPERATI, conservati
                     perché gli asset pubblicati ne derivano

build_report.py      ← CONTENUTO della settimana (idee, trend, competitor)
captions.py          ← TESTI dei post per Buffer
week.py              la data, i rifacimenti (REDO), le correzioni a mano

plan.py              Dal report alle slide: il tipo dal campo `format`, il
                     layout dalla forma del contenuto (vedi sotto)
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

## Il layout segue il contenuto

`plan.py` sceglie il **tipo** di post dal campo `format` (si ferma se non lo
riconosce) e il **layout** dalla forma del contenuto. Regole deterministiche,
stampate idea per idea da `python3 plan.py`:

```
  2. Il tuo editor di AI coding gira in myth   single · 1 slide
     layout single · barrato 'sicuro' · cifra — · superficie light
```

| Se l'idea ha… | succede | se il dato non regge |
|---|---|---|
| `citazione` + `autore` (+ `ruolo`) | singola: layout citazione; carosello: slide citazione dopo la copertina | citazione senza autore → si ferma |
| `immagine` (file nella repo, percorso dalla radice; `credito`, `immagine_alt` opzionali) | foto vera con velatura: la singola o la copertina | URL, file mancante o fuori repo → si ferma |
| `barrato` | quella parola del titolo viene barrata a mano | non nel titolo, con cifre, o maiuscola fuori dalla prima parola (nome proprio) → si ferma |
| un mito (`myth` o `is_myth`) senza `barrato` | barrata la parola dopo «quindi è»/«quindi», o l'unica `*parola*` accentata | se non è univoca: nessuna barratura |
| cifre in apertura dei punti («42% …», «800.000 — …») | carosello dati non-mito: la prima fa la **copertina dati**; ≥3 restanti → scorecard, 1–2 → slide cifra | — (nelle singole il titolo resta il post) |
| una cifra con segno e argomento di guadagno («−12 ore…», «+18% di ricavi»), o `positivo` | quella cifra/parola in verde, slide scura | `positivo` che non compare → si ferma |

**Chiaro/scuro**: fra i post della settimana si alternano scuro e chiaro (i
caroselli, le foto e le citazioni contano come scuri); dentro un carosello
argomentazione scura, fatti ed elenchi chiari, prima e ultima pagina scure.

**Demo o prove fuori dalla CDN**: `PED_OUT_DIR=/una/cartella python3 render.py
carousel` scrive lì dentro invece che nella repo, così non nasce nessun nome
pubblicato in `settimane/`.

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

- `BUFFER_API_KEY` — token Bearer per `api.buffer.com`. **Opzionale**: lo script
  cerca il token nell'ambiente, poi nel Keychain di macOS (servizio
  `digitiamo-buffer`), poi in `~/.config/digitiamo/buffer-token`. L'ambiente è
  la via per le esecuzioni automatiche (secret di CI); il file è per Linux e
  Windows, e sta **fuori dalla repo** di proposito — un file nell'albero di
  lavoro è a un `git add -A` dall'essere pubblicato, e questa repo è pubblica.
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

Dal 2 novembre 2026 il linguaggio è quello approvato quel giorno (12 post di
riferimento): Sora, palette blu `#3E00EA` / quasi nero / lavanda, un solo
gradiente, barratura a mano, marchio vettoriale disegnato dal layout, verde
solo per i guadagni. Provenienza di ogni valore in `brand-spec.md`; il sistema
precedente (template Canva di `social-ped`) è descritto lì in appendice.
