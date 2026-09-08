# digitiamo-social-assets — istruzioni per Claude Code

Questa repo ha **due ruoli insieme**, ed è la cosa da capire prima di toccarla:

1. `generator/` è il **codice** che produce report, caroselli e immagini dei post.
2. `settimane/<data>/` è una **CDN pubblica**: i PNG e i PDF lì dentro vengono
   scaricati da Buffer via `raw.githubusercontent.com` **al momento della
   pubblicazione effettiva del post**, che può avvenire giorni dopo la creazione
   della bozza.

Una cartella per settimana, creata da `render.py`. I percorsi li costruisce
`names.py`, unica fonte sia per il renderer sia per gli URL su Buffer.

```
settimane/2026-08-31/   la settimana del bot: 1080×1350, già pubblicata
settimane/2026-09-07/   ↑ il formato corrente, 1200×1500
archivio/               10 PNG del 28 agosto, senza data né slug nel nome
generator/              il codice
```

**Un asset già pubblicato non si sposta e non si rinomina**: il suo URL è dentro
una bozza o un post, e cambiarlo lo rompe senza alcun errore visibile fino alla
pubblicazione. I 25 file che stavano nella radice sono stati spostati l'8
settembre 2026, dopo aver verificato in Buffer che nessuna bozza pendente li
usasse. Da qui in avanti niente nasce fuori dalla sua cartella, quindi non
serve più spostare nulla.

## Le tre regole che non si violano

**1. Non riusare mai un nome file già pubblicato, e non sovrascriverne uno.**
Buffer scarica l'asset dall'URL alla pubblicazione, non alla creazione della
bozza. Sovrascrivere un file cambia in silenzio l'immagine di un post già
approvato. Quindi `render.py` **salta** i post già generati invece di rifarli:
rilanciarlo è sicuro e non produce doppioni. Per rifare un post c'è
`week.REDO` — vedi «Rifare un post», qui sotto. Non cancellare a mano un asset
già pubblicato, e non cambiare `DATE`: la settimana è quella che è.

**2. Non scrivere HTML/CSS nuovo per le slide.** Le grafiche si **derivano dal
report**: scrivi le idee in `generator/build_report.py` e `plan.py` scegli il
template e la sequenza di slide leggendo il campo `format` di ogni idea. Non
serve scegliere nulla a mano.

Questa regola esiste per un motivo preciso: le esecuzioni del 31 agosto e del
7 settembre hanno prodotto **due design diversi** perché ognuna ha riscritto
l'HTML da zero. Il 7 settembre il marchio è finito reso come testo
«DIGITIAMO» con le ultime quattro lettere in verde — cosa che non esiste nel
brand. È l'errore che il sistema evita.

**3. Il brand non si indovina: sta in `generator/brand-spec.md`.** Leggilo prima
di qualunque lavoro visivo. Contiene palette, font, formati, asset e i divieti,
con la provenienza di ogni valore.

## Il formato è 1200×1500, e non si negozia

Verticale 4:5, come i template Canva reali. Viene da `brand/tokens.py`
(`FORMATS["portrait"]`) e `render.py` **verifica ogni PNG prodotto**: se la
dimensione non corrisponde, cancella il file e si ferma.

Il controllo esiste per un motivo specifico. Gli asset generati fino al
31 agosto — quelli sparsi nella radice e in `settimane/2026-08-31/` — sono
**1080×1350**: stesso rapporto 4:5, risoluzione minore senza motivo. Sono lì e
si vedono, e la deriva tipica è adeguarsi a quello che c'è già. Non farlo: quei
file sono storia, non il riferimento.

Perché serviva un controllo e non una nota: una dimensione sbagliata non produce
nessun errore. LinkedIn riscala, il post esce un po' più sgranato, e nessuno lo
attribuisce al codice.

## Flusso settimanale

Ogni settimana si modificano **solo i file di contenuto**:

| File | Cosa contiene |
|---|---|
| `generator/build_report.py` | trend, competitor, 7 idee, calendario — **il contenuto** |
| `generator/week.py` | `DATE`, i rifacimenti (`REDO`) e le eventuali correzioni a mano |
| `generator/captions.py` | i testi dei post per Buffer |

**L'allineamento è automatico.** Un hook `SessionStart`
(`.claude/sync-main.sh`) allinea la copia locale a `origin/main` all'avvio,
perché una sessione su codice vecchio non ha `plan.py` né `names.py` e
riscrive l'HTML da zero — l'errore che questo sistema esiste per evitare.

L'hook **non distrugge mai** lavoro locale: se ci sono modifiche non
committate, o se il ramo è divergente da `origin/main`, si limita a dirlo e non
tocca niente. In quel caso l'integrazione va fatta a mano **prima** di
generare, altrimenti si lavora su una base che non è quella pubblicata:

```bash
git rebase origin/main
```

Leggi sempre la riga `[sync]` all'avvio: dice su che base stai lavorando.

Poi:

```bash
cd generator
python3 plan.py              # mostra quale template è stato scelto per ogni idea
python3 render.py all        # tutto in settimane/<data>/: report PDF, caroselli, singole
python3 preview.py           # sfoglia le slide nel browser, come su LinkedIn
```

### Iniziare una settimana nuova

`week.py` conserva lo stato della settimana **in corso**, comprese le eventuali
correzioni a mano: serve al ciclo di rifacimento, che vive per giorni dopo la
generazione. Quindi all'inizio di una settimana nuova va riportato al punto di
partenza, in quest'ordine:

| Campo | A cosa |
|---|---|
| `DATE`, `WEEK_LABEL` | la settimana nuova |
| `OVERRIDES_FOR` | **la stessa** `DATE` |
| `REDO` | `{}` — i rifacimenti valgono per una settimana sola |
| `CAROUSELS`, `SINGLES` | `[]`, se le grafiche vengono dal report |
| `SOSTITUISCE_IL_PIANO` | `False`, salvo il caso descritto sotto |

Non serve ricordarselo a memoria: se resta qualcosa della settimana scorsa,
`render.py` **si ferma** e dice cosa non torna (`OVERRIDES_FOR` diverso da
`DATE`, oppure l'interruttore attivo senza niente dichiarato). Il rischio non è
pubblicare i post sbagliati — è non pubblicare niente finché non si sistema.

Perché `week.py` non si svuota subito dopo la generazione: appena generato, i
post di quella settimana sono bozze in attesa di revisione, e un rifacimento ha
bisogno di trovarli lì. Svuotarlo prima romperebbe proprio il ciclo con
l'umano.

### Quando i post approvati non sono le idee del report

`SOSTITUISCE_IL_PIANO = True` in `week.py` dice: **per questa settimana vale
solo quello che è dichiarato a mano**, il piano derivato dal report non conta.

Serve quando la revisione umana ha cambiato l'insieme dei post — tre trend fusi
in una rassegna, o due idee scartate. L'alternativa sarebbe riscrivere il
report perché produca l'elenco giusto, che significa falsificarlo.

Non è la modalità normale: di norma resta `False` e vale la regola 2.

### Come viene scelto il template

`plan.py` legge il campo `format` di ogni idea e ne deriva il tipo di post, **a
parole chiave** (le diciture cambiano fra un'esecuzione e l'altra):

| Nel `format` c'è… | Tipo di post |
|---|---|
| carosello, documento LinkedIn | `data_carousel`, oppure `compliance_carousel` se parla di normativa, oppure `explainer_carousel` se spiega un concetto |
| mito da sfatare | `myth` (immagine singola) |
| thought leadership | `thought_leadership` (immagine singola) |
| esperienza diretta, case study | `direct_experience` (immagine singola) |
| divulgativo, mini-lezione, Datapizza | `mini_lesson` (immagine singola) |
| lista, riflessione, community, recap | `closing_list` (carosello) |

**Se un formato non corrisponde a nessuna regola, `plan.py` si ferma** e stampa
la stringa esatta. Aggiungi una regola in `plan.FORMAT_RULES` o allinea la
dicitura nel report: un template indovinato diventa un post pubblicato sbagliato.

Dentro un carosello, i punti dell'idea vengono distribuiti così: tre o più punti
che aprono con una cifra diventano **una scorecard**; uno o due diventano slide
**cifra**; i punti in prosa diventano **elenco** (sono frasi intere, non coppie
titolo+corpo, e ricavarne un titolo tagliandole produce frammenti).

### Cosa rileggere sempre dopo la generazione

Due cose sono **default automatici**, non scelte redazionali:

- **L'accento sul titolo.** `plan.py` evidenzia l'ultima parola. Spesso è quella
  giusta, a volte no («…riguarda anche *te*» è debole). Si corregge scrivendo
  `*parola*` nel titolo dell'idea.
- **Il titolo della CTA.** Il report non ha un campo per questo, quindi viene da
  un default per tipo di post (`plan.CTA_TITLES`). È la prima cosa da rileggere.

### Rifare un post (il ciclo con l'umano)

Il flusso è human-in-the-loop: il lunedì l'automazione genera tutto e crea le
bozze, poi una persona guarda e chiede modifiche. Rifare un post significa
**dargli un URL nuovo**, non riscrivere il vecchio file — la bozza esistente
punta a quell'URL, e Buffer scarica l'immagine alla pubblicazione.

1. Correggi il contenuto: il testo dell'idea in `build_report.py`, la caption in
   `captions.py`, oppure la slide in `week.CAROUSELS`/`SINGLES` se serve
   intervenire sul layout.
2. Segna il post in `week.REDO` (gli slug li stampa `python3 plan.py`):

   ```python
   REDO = {"idea2-la-sicurezza-dell-ai": 1}   # poi 2, 3… se si ripete
   ```

3. `python3 render.py all` — rigenera **solo** quel post, con suffisso `-r1`.
   Gli altri restano quelli approvati e li salta.
4. Commit e push, poi `python3 publish_buffer.py`: crea la bozza nuova e
   **segnala quella vecchia**, che punta all'immagine superata. Va eliminata,
   altrimenti il post esce due volte:

   ```bash
   python3 publish_buffer.py --elimina-obsolete
   ```

Le bozze create sono registrate in `generator/buffer-drafts.json` (settimana,
revisione, slug, id Buffer). Serve solo a questo: senza il registro non c'è modo
di sapere quale bozza sia diventata obsoleta. È tracciato su git.

La revisione è **per post**, non per settimana: rifare l'idea 2 non tocca le
altre quattro né le loro bozze.

### Correggere una slide dopo la revisione

Si dichiara in `week.py` con lo **stesso slug** che il piano assegna (lo stampa
`python3 plan.py`): la versione a mano vince su quella derivata. `OVERRIDES_FOR`
deve indicare la settimana corrente, altrimenti `render.py` si ferma — serve a
non riapplicare a una settimana nuova un aggiustamento scritto per la vecchia.

Il report **non** è soggetto a quel controllo: `python3 render.py report`
funziona sempre.

## Pubblicazione su Buffer

```bash
python3 publish_buffer.py
```

**Il token non va chiesto a nessuno**: lo script lo cerca da sé, in tre posti,
nel primo che ce l'ha.

| | Dove | Quando |
|---|---|---|
| 1 | `BUFFER_API_KEY` nell'ambiente | esecuzione automatica (GitHub Actions): il token arriva da un secret e non si scrive su disco |
| 2 | Keychain di macOS, servizio `digitiamo-buffer` | su un Mac, è la via migliore — non è un file |
| 3 | `~/.config/digitiamo/buffer-token` | Linux e Windows |

```bash
# macOS
security add-generic-password -a "$USER" -s digitiamo-buffer -w

# Linux / Windows — il file va FUORI dalla repo
mkdir -p ~/.config/digitiamo && chmod 700 ~/.config/digitiamo
printf '%s' 'IL_TOKEN' > ~/.config/digitiamo/buffer-token
chmod 600 ~/.config/digitiamo/buffer-token
```

Se manca, lo script si ferma e stampa tutte tre le strade con i comandi.

**Perché il file sta fuori dalla repo e non è un `.env` accanto al codice**:
questa repo è pubblica, e un file nell'albero di lavoro è a un `git add -A`
dall'essere pubblicato per sempre. Il `.gitignore` protegge fino al primo
errore; una cartella diversa protegge sempre. (Le regole in `.gitignore` per
`.env` e `*-token` sono solo una rete, non il meccanismo.)

**Mai nel codice né in un file della repo**: questa repo è pubblica. Se un token
è finito in una chat, in un commit o in un log, va rigenerato su Buffer.

**Il canale non va configurato**: lo script lo ricava dall'API cercando quello
LinkedIn (come fa `social-ped`, dove l'id non è memorizzato da nessuna parte).
`python3 publish_buffer.py --canali` elenca quelli collegati alla chiave.

Verificato l'8 settembre 2026 contro l'API: all'account risulta **un solo**
canale LinkedIn, `Digitiamo.ai`. Se un giorno `--canali` ne mostra due, la
risoluzione automatica si ferma di proposito — vedi sotto.

Se all'account risultano **più** canali LinkedIn, lo script **si ferma** invece
di scegliere: pubblicare sulla pagina sbagliata non darebbe alcun errore. In quel
caso serve `BUFFER_CHANNEL_ID` (tipo GraphQL `ChannelId!`, non `String!`).

Crea una bozza per **ogni post prioritario del piano**: immagine singola per i
post singoli, documento allegato (PDF + prima slide come anteprima) per i
caroselli. I contenuti vengono da `plan.content()`, la stessa fonte del
renderer — nessuna lista da aggiornare a mano.

Fa un **preflight su ogni URL prima di creare qualsiasi bozza**: se un asset non
è raggiungibile non crea niente. Quindi **committa e pusha gli asset prima** di
lanciarlo. Come `render.py`, salta i post per cui la bozza esiste già: si può
rilanciare senza creare doppioni. Crea solo bozze, mai post programmati:
l'approvazione umana resta obbligatoria.

## Tornare indietro

Su `main` scrivono **due produttori**: questa automazione e chiunque lavori a
mano sul generatore. Perciò serve saper tornare indietro — con una distinzione
che non va confusa.

**Il codice si può revertire. Un asset pubblicato no.**

- `generator/` è codice: un revert lo riporta a uno stato precedente senza
  conseguenze esterne.
- `settimane/*/` e i `carosello_*` nella radice sono la **CDN**: una bozza
  Buffer può puntare a quei file, e Buffer li scarica al momento della
  pubblicazione effettiva. Rimuoverli con un revert **rompe un post già
  approvato**, e l'errore si vede solo il giorno in cui esce.

Quindi: revert solo del codice, e mai `git push --force` su `main` (altri
hanno già clonato, e i file spariti restano rotti negli URL).

**Punti di ritorno.** Prima di un'integrazione importante si mette un tag
annotato su `main`, che è un nome ricordabile per uno stato pubblicato:

```bash
git tag -a main-prima-di-<cosa> -m "perché questo punto conta" origin/main
git push origin main-prima-di-<cosa>
```

Tag esistenti: `git tag -n`. Per vedere com'era: `git show <tag>`, oppure
`git switch --detach <tag>` per guardarci dentro senza spostare niente.

Per annullare un cambiamento **di codice** già pubblicato:

```bash
git revert --no-commit <sha>..HEAD -- generator/
git commit -m "Torna al generatore di <tag>: <motivo>"
```

`git revert` aggiunge un commit che disfa, invece di riscrivere la storia: è
l'unica forma sicura su una repo pubblica che altri hanno clonato.

## Cosa è tracciato e cosa no

- **Tracciati**: il codice in `generator/`, gli asset di brand, i PNG in
  `settimane/*/`, i `carosello_*.pdf` e `generator/buffer-drafts.json` (il
  registro delle bozze: serve alla sessione della settimana dopo, non solo a
  questa).
- **Non tracciati** (`.gitignore`): il report PDF
  (`settimane/*/PED_Digitiamo_*.pdf`, è un documento interno), `generator/report.html`, `generator/review.html`,
  `generator/preview.html`, `generator/artifact.html` e le anteprime in
  `generator/design-demos/*.png` — tutti rigenerabili.

## Regole visive che sbagliano più spesso

- **Il marchio è un file, non del testo.** `brand/logo/digitiamo-wordmark-*.png`.
  Scriverlo come testo perde il glifo a circuito, che è l'unica cosa distintiva.
- **I font sono Montserrat (display) e Lato (corpo)**, incorporati in base64.
  Mai caricarli dalla rete: un `@import` che fallisce produce PNG in un font di
  fallback, sbagliati e senza errore.
- **Gli sfondi in `brand/bg/` non sono fondi piatti**: hanno marchio e badge già
  incorporati, e zone non utilizzabili. Le misure sono in `templates.py`.
  Ridisegnare il marchio sopra lo duplica.
- **Il verde `#43ef84` non va su fondo chiaro**: contrasto misurato 1,2:1. Su
  navy e blu passa (≥3:1). Sul cielo la tinta dati è il blu brand.
- **I logo di terzi** stanno in `brand/third-party/` con la provenienza. Uso
  editoriale, **mai ricolorati**, e mai accostati al marchio Digitiamo in modo
  che suggerisca una partnership. Se un logo non è reperibile, si dichiara
  l'assenza: non si ridisegna.

## Contenuti: verificare, non riassumere

I post citano notizie reali. Regole dal brief dell'agente PED:

- **Verifica i fatti sulle fonti**, non sui riassunti. Nella settimana del
  7 settembre, leggere gli articoli invece del report ha aggiunto un dato
  mancante (cadenza mediana 37,5 → 11 giorni) e ha smontato un numero: il
  «76% su 847 deployment» viene da un post su Medium che compare con due firme
  diverse allo stesso URL, e la paternità accademica attribuita da alcune
  riprese non è verificabile.
- **Un dato che non regge non va usato come titolo**, nemmeno con un caveat.
- **Niente sensazionalismo**, niente cifre o citazioni inventate, niente claim
  su clienti che non si possono sostanziare.
- Se un dato ha una qualifica (analisi indipendente, non istituzionale), quella
  qualifica va sulla slide.

## Ambiente

```bash
pip3 install -r generator/requirements.txt
python3 -m playwright install chromium
```

Se Chromium è già presente: `export CHROMIUM_PATH=/percorso/chromium`.
Senza quella variabile si usa quello di Playwright.

## Revisione e approvazione

- `python3 generator/preview.py` — pagina locale per sfogliare le slide.
- `python3 generator/build_artifact.py` — genera `artifact.html`, la pagina di
  approvazione condivisibile. Pubblicala con lo strumento Artifact dichiarando
  `capabilities: {artifact: {}}`: così le decisioni (approvato / da modificare
  + nota) restano salvate nella pagina per chi la apre dopo.

## Storia utile

Il brand non era in questa repo: è stato ricostruito dai template Canva reali
del progetto `social-ped` (renderer di produzione). Il marchio non esisteva come
file ed è stato ricavato dagli sfondi. Cosa manca ancora è annotato in
`generator/brand-spec.md` §8 — in particolare il **logo vettoriale ufficiale** e
la copertina News AI, il cui testo incorporato nel PNG non è nei font del brand.
