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
report**: scrivi le idee in `generator/build_report.py` e `plan.py` sceglie il
template dal campo `format` e il layout dalla forma del contenuto (citazione,
foto, cifre, parola da barrare). Non serve scegliere nulla a mano.

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

**Ogni idea Prioritario ha anche i testi brevi per le slide** (regola di
Fabio, 2/11/2026: «non usare troppo testo nelle slide»). I campi lunghi
(`title`, `hook`, `points`) restano per il report e le caption; le slide usano
prima questi:

- `titolo_post` — il titolo a manifesto, **≤ 60 caratteri**, 3–8 parole,
  corto e incisivo, fedele all'idea (nessun fatto nuovo). **Obbligatorio se
  `title` supera 60 caratteri: senza, `plan.py` si ferma**;
- `sottotitolo_post` — una sola frase di supporto, ≤ 110 caratteri;
- `barrato` — la parola del titolo da barrare, **scelta di proposito** (mai
  un nome di cliente, una cifra o un dato);
- `punti_post` — facoltativo: versioni brevi dei punti (≤ 80 caratteri; per
  le cifre «9 — piattaforme violate in un mese»).

Senza i campi brevi, supporto, elenchi e sintesi vengono tagliati da soli al
primo confine naturale (e `python3 plan.py` lo segnala), ma un testo scritto
corto è sempre meglio di uno tagliato. Budget completi in
`generator/brand-spec.md` §6.

`generator/performance.py` **non** è tra questi: è codice, non contenuto
settimanale. Calcola da sé, a ogni generazione del report, il bilancio della
settimana precedente da Buffer — vedi «Il report si apre con "Come sono
andati i post"» più sotto. Non va mai toccato per scrivere il report di una
singola settimana.

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

Poi, in locale, per vedere cosa esce:

```bash
cd generator
python3 test_pipeline.py     # le prove della pipeline: nessuna rete, niente toccato
python3 plan.py              # per ogni idea: template, layout, testi usati e lunghezza/budget
python3 render.py all        # tutto in settimane/<data>/: report PDF, caroselli, singole
python3 preview.py           # sfoglia le slide nel browser, come su LinkedIn
```

## Pubblicare: `[pubblica]` nel messaggio dell'ultimo commit

Gli asset e le bozze Buffer **non** li produci a mano. Li fa un workflow
(`.github/workflows/ped.yml`), e parte solo quando glielo dici:

```bash
git add generator/build_report.py generator/captions.py generator/week.py
git commit -m "PED <data>: contenuti della settimana [pubblica]"
git push
```

Committa quante volte vuoi mentre lavori: **il marcatore va solo sull'ultimo**.
Senza `[pubblica]`, il push non avvia niente.

Perché non parte da sé a ogni push: la sessione del lunedì fa più commit mentre
scrive, e un push di `build_report.py` fatto prima di `captions.py` avvierebbe
una corsa che arriva a Buffer e si ferma su una caption mancante. Job rosso e
mail, per del lavoro a metà. Dopo tre mail così nessuno le apre più — e quella
mail è l'unica rete di sicurezza di questo sistema. **Un segnale rumoroso è un
segnale spento.**

Il workflow fa, in ordine: prove → `plan.py` → `render.py all` → commit degli
asset → bozze Buffer → commit del registro. Il token arriva da un secret di
GitHub (`BUFFER_API_KEY`), quindi non serve averlo sulla propria macchina. Se
qualcosa si rompe, arriva una mail e il log sta nella tab Actions.

Si può lanciare anche a mano, dalla tab **Actions → Run workflow**: è ripetibile,
salta gli asset già generati e le bozze già create, quindi non fa doppioni.

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

Il `format` decide il **tipo**; la **forma del contenuto** decide il layout
(dal 2/11/2026). `python3 plan.py` stampa, per ogni idea, layout, parola
barrata, cifra e superficie. Le regole, tutte deterministiche:

- `citazione` + `autore` → layout citazione (senza autore si ferma: mai
  citazioni inventate o anonime);
- `immagine` (file nella repo) → foto vera con velatura; altrimenti tipografica;
- `barrato` → quella parola barrata a mano (deve stare nel titolo; mai cifre,
  mai nomi propri); senza `barrato` nessuna barratura, nemmeno nei miti;
- cifre in apertura dei punti: in un carosello dati che non è un mito la prima
  fa la **copertina dati**; tre o più restanti → **scorecard**, una o due →
  slide **cifra**; i punti in prosa → **elenco**;
- verde solo per un guadagno riconosciuto (segno + argomento: «−12 ore»,
  «+18% di ricavi») o marcato con `positivo`;
- chiaro/scuro alternati fra i post della settimana; dentro i caroselli
  argomentazione scura, fatti chiari, prima e ultima pagina scure.

Dettagli in `generator/README.md` («Il layout segue il contenuto») e nel
docstring di `plan.py`.

### Cosa rileggere sempre dopo la generazione

Due cose sono **default automatici**, non scelte redazionali:

- **L'accento sul titolo.** `plan.py` evidenzia l'ultima parola. Spesso è quella
  giusta, a volte no («…riguarda anche *te*» è debole). Si corregge scrivendo
  `*parola*` nel titolo dell'idea. Se il titolo ha una barratura, l'accento si
  spegne.
- **La barratura.** Si usa poco e solo di proposito: scrivi `barrato` nell'idea
  quando una parola dell'affermazione è davvero quella smentita. Senza
  `barrato` non si barra nulla, e la `*parola*` accentata resta in colore.
- **I testi tagliati.** `python3 plan.py` segna con `<- tagliato` ogni testo
  accorciato da solo: se il taglio non regge, scrivi il campo breve.
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

## Il report si apre con «Come sono andati i post» (dal 24/9/2026)

Richiesto da Ramona: ogni report apre con un bilancio della settimana
**precedente**, non solo con le idee nuove. È la sezione **01** (le altre sono
scalate di uno: trend → 02, competitor → 03, idee → 04, pubblicazione → 05).

Calcolata da `generator/performance.py`, **a runtime, da dati live** — non è
contenuto che si scrive nel report come trend/competitor/idee. Fa tre cose:

1. Legge `generator/buffer-drafts.json` per sapere quali bozze erano state
   create per la settimana precedente a `week.DATE`.
2. Interroga l'API GraphQL di Buffer (`posts`, filtrato per canale, stato
   `sent` e intervallo di date) per le metriche reali di quei post —
   impression, reach, reazioni, commenti, condivisioni, tasso di engagement.
3. Confronta le due liste: quali bozze sono uscite (con le metriche) e quali
   sono rimaste **in sospeso** — mai approvate, o approvate ma non ancora
   pubblicate. Questo secondo dato conta quanto il primo: se la maggior parte
   delle bozze di una settimana non è mai stata approvata, il report lo dice.

**Implicazioni pratiche per chi genera il report:**

- **Serve `BUFFER_API_KEY` anche per generare il report**, non solo per
  pubblicare le bozze — vedi sotto per dove lo cerca. Se manca o Buffer non
  risponde, la sezione lo dice chiaramente nel PDF (mai un numero vecchio o
  indovinato) e il resto del report si genera comunque: non è un errore
  bloccante.
- **Serve una clone non superficiale** (`fetch-depth: 0` in CI, già impostato
  in `ped.yml`): per le settimane registrate prima del 24/9/2026 — quando
  `buffer-drafts.json` non aveva ancora titolo e formato per ogni bozza — il
  modulo li recupera da `git show <sha>:generator/build_report.py`, cercando
  l'ultimo commit "PED <data>" di quella settimana. Dal 24/9/2026 in poi
  `publish_buffer.py` scrive titolo e formato direttamente nel registro alla
  creazione della bozza, quindi il fallback via git serve sempre meno.
- **Non richiede nessuna azione manuale settimanale**: si rigenera da sé a
  ogni `render.py report`. Non va scritta a mano, non va "aggiustata" se i
  numeri di una settimana sono deludenti — quella è esattamente l'informazione
  che la sezione deve dare.

Le prove pure (calcolo della settimana precedente, formattazione, confronto
registro/Buffer con revisioni) sono in `test_pipeline.py`, senza rete — vedi
`## Le prove` più sotto.

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

## Le prove

`python3 generator/test_pipeline.py` — sette prove, nessuna rete, nessun
asset pubblicato toccato. Girano anche in CI **prima** del render:

1. **La scelta del template** su nove diciture reali, più il rifiuto di un
   formato ignoto: indovinare un template significa pubblicare un post
   sbagliato. E **le scelte guidate dal contenuto**: barratura (ricavata e
   rifiutata), cifre e verde, citazione senza autore, foto fuori repo,
   alternanza chiaro/scuro. E **i budget di testo**: titolo lungo che ferma il
   piano, tagli ai confini, voci in più tolte, citazione mai tagliata.
2. **I nomi degli asset e gli URL su Buffer coincidono** — il bug la cui unica
   manifestazione sarebbe una bozza che punta a un URL inesistente, visibile
   giorni dopo, alla pubblicazione.
3. **Il formato è imposto**, non solo documentato: 1080×1350 e anche un pixel
   di scarto vengono respinti, e il file fuori misura rimosso.
4. **Il ciclo con l'umano**: che un rilancio non tocchi niente, e che un
   rifacimento rigeneri **solo** quel post lasciando intatti gli asset a cui
   puntano le bozze già viste.
5. **Il bilancio della settimana precedente** (`performance.py`): il calcolo
   della settimana Lun-Dom, la formattazione delle metriche, e che il
   confronto registro/Buffer non inventi righe — una revisione superata da un
   rifacimento non deve comparire come post pubblicato a sé.

I bersagli si ricavano dal piano corrente, non sono scritti a mano: due prove
precedenti erano già diventate stantie perché riferivano gli slug di una
settimana passata.

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

Dal 2 novembre 2026 vale il linguaggio approvato quel giorno (brand-spec.md
§2–§7). Il sistema precedente — Montserrat/Lato, sfondi Canva con marchio e
badge incorporati, verde come accento — è **superato**: i suoi file restano
in `brand/bg/` solo perché gli asset pubblicati ne derivano.

- **Il marchio è un file, non del testo**: il vettoriale
  `brand/logo/digitiamo-wordmark.svg`, disegnato dal layout (bianco su scuro e
  foto, blu `#3E00EA` su chiaro). Gli sfondi non lo incorporano più.
- **Il font è Sora** (400/600/700), incorporato in base64. Mai caricarlo dalla
  rete: un `@import` che fallisce produce PNG in un font di ripiego, sbagliati
  e senza errore. Sora non ha «↗»: niente frecce nei bottoni.
- **Un solo gradiente** (`#3E00EA` → `#070011`) per i post scuri; il chiaro è
  `#F4F5FA`. Niente badge di categoria, niente filigrana a circuito.
- **Il verde `#00DC93` è solo per i guadagni e per il bottone CTA**, mai di
  default, e mai su fondo chiaro (non si legge): una slide con un guadagno è
  scura.
- **La barratura a mano** (una parola per titolo) non tocca mai nomi di
  clienti, cifre o dati.
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

## Revisione e approvazione (obbligatoria, PRIMA delle bozze Buffer)

Dal 3/11/2026, su richiesta esplicita di Ramona: **le bozze Buffer non si
creano più subito dopo `render.py`**, né per i caroselli né per le immagini
singole. Prima deve esserci un giro di revisione/approvazione umano, con la
possibilità di chiedere modifiche — non solo la creazione automatica della
bozza seguita da un rifacimento a posteriori.

Flusso corretto per ogni esecuzione (automatica del lunedì compresa):

1. `python3 test_pipeline.py`, `python3 plan.py`, `python3 render.py all` come
   sempre: generano gli asset in `settimane/<data>/`.
2. **`python3 generator/build_artifact.py`** — genera `artifact.html`: NON
   scrive ne' inventa contenuti, legge solo `plan.content()` (la stessa fonte
   del renderer) e i PNG/PDF che `render.py` ha appena prodotto, per tutte le
   idee Prioritario (caroselli e immagini singole).
3. Pubblicalo con lo strumento Artifact dichiarando
   `capabilities: {artifact: {}}`: la pagina mostra ogni post con le sue
   slide, e chi la apre può segnare **Approvato** o **Da modificare + una
   nota** per ciascuno — le decisioni restano salvate nella pagina stessa
   (capability `artifact`), non in questa sessione.
4. Consegna il PDF del report e il link della pagina di approvazione a
   Ramona, e **fermati qui**: non lanciare `publish_buffer.py` né pushare con
   `[pubblica]` nella stessa esecuzione. Senza un via libera umano non nasce
   nessuna bozza Buffer.
5. Quando Ramona conferma (in chat, o tramite le decisioni salvate nella
   pagina — rileggi l'artifact con `action: "read"` per vederle): per ogni
   post "Da modificare" applica la nota al contenuto (`build_report.py`,
   `captions.py`, o `week.CAROUSELS`/`SINGLES`), segnalo in `week.REDO` (vedi
   «Rifare un post» sopra) e rigenera **solo quello**. Solo a questo punto
   esegui `publish_buffer.py` (o il push con `[pubblica]`) per creare le
   bozze — di tutti i post approvati, non solo di quelli rifatti.

Questo vale per **tutti** i post Prioritario della settimana, caroselli e
immagini singole indifferentemente: non solo per i caroselli.

Altri strumenti di revisione, non sostitutivi di questo passaggio:

- `python3 generator/preview.py` — pagina locale per sfogliare le slide, utile
  mentre si lavora in sessione, ma non condivisibile con Ramona.

## Storia utile

Il 2 novembre 2026 il sistema visivo è stato sostituito dal linguaggio
approvato quel giorno (Sora, gradiente unico, barratura, marchio vettoriale) e
la scelta del layout è diventata guidata dal contenuto. Prima di allora il
brand era stato ricostruito dai template Canva reali del progetto `social-ped`
(renderer di produzione). Il marchio non esisteva come
file ed è stato ricavato dagli sfondi. Cosa manca ancora è annotato in
`generator/brand-spec.md` §8 — in particolare il report PDF interno, che resta
nel sistema precedente.
