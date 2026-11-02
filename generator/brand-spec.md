# brand-spec.md — Digitiamo

> Gate file del protocollo asset (huashu-design §1.a). Ogni design che porta il
> marchio Digitiamo si basa su questo file. **Nessun valore qui e' inventato**:
> la provenienza e' annotata voce per voce.
>
> **Dal 2 novembre 2026 vale il linguaggio approvato quel giorno** (§2–§7): Sora,
> palette blu/notte/lavanda, un solo gradiente, barratura a mano, marchio
> vettoriale disegnato dal layout. Il sistema precedente — Montserrat + Lato,
> sfondi Canva con marchio e badge incorporati, accento verde — e' **superato**
> e resta descritto in appendice, perche' gli asset gia' pubblicati in
> `settimane/` ne derivano.
>
> Fonte primaria: i 12 post di riferimento approvati il 2/11/2026 (mock HTML
> Main, Mito, Dati, Chiaro, Interna, Citazione, Caso, Chiusura, News, FotoIrca,
> FotoIed, Prodotto) e gli asset del sito `digitiamo-site`.

## 1. Chi e' Digitiamo

Societa' di consulenza tech italiana, B2B. Due linee di offerta:

- **Team Augmentation** — AI Engineer e sviluppatori senior che si integrano nel
  team del cliente (posizionamento: governance di architettura, sicurezza, debito
  tecnico e passaggio in produzione — non "manodopera in piu'").
- **AI Business Academy** — formazione e progetti mirati sui casi d'uso reali
  dell'azienda cliente (posizionamento: non "AI a pioggia").

Pubblico: decision-maker e aziende italiane del software/enterprise. Persone che
usano l'AI ma non fanno ricerca.

Canali: LinkedIn (primario, canale `digitiamo`), Instagram (secondario).
Sito: digitiamo.com · Recruiting: recruiting@digitiamo.com

**Tono di voce** (da `social-ped/agent/system-prompt.md`, il brief dell'agente PED):
sempre in italiano; amichevole e accessibile, "un collega competente, non un
comunicato stampa"; frasi brevi e concrete; nessun corporate-ese, nessun
entusiasmo finto; diretto e onesto — se un contenuto e' debole si dice, non si
riempie lo spazio. **Niente sensazionalismo.** Meglio un post in meno che un post
sbagliato.

Implicazione per il design: il registro visivo e' **sobrio e sicuro di se'**, non
urlato. Il verde esiste, ma solo per i segnali positivi (vedi §3).

## 2. Asset (obbligatori, mai ricostruiti)

| Asset | File | Provenienza |
|---|---|---|
| **Marchio vettoriale** | `brand/logo/digitiamo-wordmark.svg` (viewBox 620×250) | team design, 8/9/2026. **Unica sorgente del marchio nei post**: `tokens.wordmark_uri(colore)` toglie lo `<style>` interno e scrive il fill come attributo (un SVG in `<img>` non eredita il CSS della pagina) |
| Font | `brand/fonts/sora-{latin,latin-ext}-{400,600,700}-normal.woff2` | `@fontsource/sora` 5.2.8 (jsDelivr), scaricati il 2/11/2026. Licenza SIL OFL 1.1 in `brand/fonts/Sora-OFL.txt`. SHA-256 latin-700: `c3337a67…3cfac2` |
| Barratura a mano | `brand/strike/barratura.svg` | copia di `digitiamo-site/assets/barratura-manuale-blu.svg` (tratto `#60A5FA`) con `preserveAspectRatio="none"`, per stirarsi sulla parola |
| Loghi di terzi | `brand/third-party/*.svg` | vedi il README di quella cartella: uso editoriale, mai ricolorati |
| Foto | `brand/photo/` + campo `immagine` delle idee | foto vere con provenienza (`PROVENANCE.md`), mai immagini generate |

Il marchio si disegna **bianco** su scuro e foto, **blu `#3E00EA`** su chiaro,
230×64 (`object-fit:contain`) in basso a sinistra; 300×84 in alto nella CTA.

## 3. Palette

`brand/tokens.py::COLORS` e' l'unica fonte in codice.

| Token | Hex | Ruolo |
|---|---|---|
| `primary` | `#3E00EA` | blu Digitiamo: accento su chiaro, testa del gradiente, marchio su chiaro |
| `ink` | `#070011` | quasi nero: testo su chiaro, coda del gradiente, testo del bottone CTA |
| `night` | `#1C073A` | notte: superfici scure piene |
| `lavender` | `#717FFE` | accento su scuro (`*parola*`), virgolette delle citazioni, tinta dati su scuro |
| `mist` | `#EBEEFC` | occhielli e testo secondario su scuro |
| `paper` | `#F4F5FA` | fondo chiaro; testo principale su scuro |
| `green` | `#00DC93` | **solo** segnali positivi (un guadagno) e il bottone CTA |
| `body_light` / `muted_light` | `#3A3550` / `#5B5670` | corpo e note su chiaro (mock Chiaro, Interna) |

**Il verde non e' un accento.** Si usa solo per una cifra o parola che e' un
guadagno (§7-ter) e per il bottone CTA. Mai per default. Su `#F4F5FA` il verde
non si legge, quindi una slide con un guadagno e' sempre scura.

**Un solo gradiente**: `linear-gradient(180deg,#3E00EA 0%,#070011 100%)`
(`tokens.GRADIENT`) per i post scuri. Variante chiara: fondo `#F4F5FA`, testo
`#070011`, accenti `#3E00EA`. Post con foto: foto vera a tutta pagina con
velatura `rgba(62,0,234,.82) → rgba(62,0,234,.55) 40% → rgba(7,0,17,.92) 80% →
#070011` (mock FotoIrca); nelle notizie la foto va in bianco e nero,
moltiplicata sul blu e sfumata nel quasi nero (mock News).

## 4. Tipografia

**Sora sola**, 400 / 600 / 700, incorporata in base64 (`tokens.font_face_css`)
con i due sottoinsiemi `latin` e `latin-ext` e il loro `unicode-range`. Mai
caricata dalla rete: un `@import` che fallisce produce PNG in un font di
ripiego, sbagliati e senza errore.

| Ruolo | Specifica (dai mock) |
|---|---|
| Occhiello | 30px, 600, maiuscolo, `letter-spacing:4px`, in alto a sinistra; `#EBEEFC` su scuro, `#3E00EA` su chiaro |
| Titolo | 700, ~92–112px (auto-fit con tetto 108px), interlinea 1.05, spaziatura −0.03em |
| Supporto | una frase, 40px, 400, interlinea 1.35 |
| Piede | 30px: `digitiamo.com` (singole) o il contapagine `01 / 06` (caroselli) |

Sora **non ha il glifo «↗»**: per questo i bottoni CTA non hanno la freccia.

## 5. Formati e geometria

| Formato | Dim. | Uso |
|---|---|---|
| Verticale 4:5 | **1200×1500** | tutti i post — imposto da `render.py::_check_size` |
| A4 @96dpi | 794×1123 | report PED interno (PDF) |

Padding dei mock: 104 sopra, 96 ai lati, 88 sotto. Occhiello a y=104; zona di
contenuto y 200–1300 (auto-fit, centrata); piede y 1348–1412. Niente piu' zone
"cotte" negli sfondi: la geometria la decide solo `templates.py`.

## 6. La barratura a mano

Una parola per titolo, al massimo. La parola resta **leggibile**: il tratto le
passa sopra (`span.strike` relativo, `img` assoluta `left:-4% top:30%
width:108% height:50%`). Se il titolo ha una barratura, l'accento di colore
`*parola*` si spegne: un solo segno per titolo. Non si barrano mai **nomi di
clienti, cifre o dati**. Quale parola: §7-ter.

## 7. Divieti

1. **Mai rendere il marchio come testo.** Si usa il vettoriale.
2. **Mai un font diverso da Sora** nelle grafiche, mai caricato dalla rete.
3. **Niente badge di categoria e niente filigrana a circuito**: tolti di
   proposito dall'utente con il linguaggio del 2/11/2026.
4. **Niente verde come decorazione** (§3).
5. **Niente emoji dentro le slide** (nelle caption va bene): `plan.py` toglie
   quelle degli hook del report.
6. **Mai foto generate o "a tema"**: una foto vera e con provenienza, oppure la
   grafica tipografica.
7. **Non riutilizzare mai un nome file** gia' pubblicato (Buffer scarica
   l'asset alla pubblicazione effettiva).

## 7-bis. Chiaro e scuro

- **Fra i post della settimana** (ordine del report) si alternano scuro e
  chiaro; i caroselli contano come scuri (copertina sempre scura), le foto e le
  citazioni pure. Due post vicini non sembrano uguali.
- **Dentro un carosello** il fondo segue il registro: argomentazione (apertura,
  tesi, citazione, sintesi, CTA) scura; fatti da leggere (cifre, scorecard,
  elenchi, notizie) chiari. Prima e ultima pagina scure.
  (`templates.surface_for`.)

## 7-ter. Scelte guidate dal contenuto

Le regole complete, con l'ordine di precedenza, sono nel docstring di
`plan.py` e in `README.md`. In breve: citazione (`citazione` + `autore`) →
layout citazione; `immagine` → foto; `barrato` o, per i miti, la parola dopo
«quindi è» / l'unica parola accentata → barratura; cifre in apertura dei punti
→ copertina dati e scorecard; segno + argomento di guadagno (o `positivo`) →
verde.

## 8. Cosa manca ancora (onesto)

- **Il report PDF interno** (`generate_html.py`) e le pagine di servizio
  (`preview.py`, `review.py`, `build_artifact.py`) non sono stati ridisegnati:
  restano in Montserrat/Lato e palette precedente (`tokens.LEGACY_*`). Non sono
  post pubblicati.
- **Icone per tipo di post**: non servono piu' (niente badge), ma i mock
  avevano badge disegnati; se tornassero, vanno approvati.
- **Foto**: l'unica foto con provenienza in repo e' quella NASA. Le foto dei
  casi cliente (Irca, IED…) sono nei mock ma non nella repo: vanno aggiunte con
  la loro provenienza prima di usarle.

---

# Appendice — il sistema precedente (superato il 2 novembre 2026)

Descrive gli asset da cui derivano i post pubblicati fino a quella data. Gli
sfondi in `brand/bg/`, i wordmark PNG e `make_editorial_bg.py` **restano nella
repo** per questo: la storia deve restare ricostruibile. Nessun layout li usa
piu'.

### 2. Asset reali (obbligatori, mai ricostruiti)

Tutti in `generator/brand/`. Estratti dai PNG Canva; il marchio non esisteva come
file standalone, e' stato ricavato dagli sfondi con alpha da luminanza.

| Asset | File | Dim. | Provenienza |
|---|---|---|---|
| **Marchio vettoriale** | `logo/digitiamo-wordmark.svg` | viewBox 620×250 | **fornito dal team design l'8 settembre 2026.** E' la sorgente ufficiale: un file per tutti i colori (il fill si sovrascrive via CSS). Non ancora usato dal renderer — vedi §8 |
| Wordmark bianco | `logo/digitiamo-wordmark-white.png` | 245×78 | ritagliato da `webinar_bg.png` (142,143)-(375,209), bianco su navy |
| Icona "News AI" | `logo/icon-news-white.png` | 200×181 | ritagliata da `newsai_cover_bg.png` (506,169)-(694,338), bianco su blu |
| Icona "Webinar" | `logo/icon-webinar-white.png` | 154×104 | ritagliata da `webinar_bg.png` (937,130)-(1079,222) |
| Sfondo news | `bg/newsai_bg.png` | 1200×1500 | template Canva `EAHN8F_sKuA` |
| Sfondo cover news | `bg/newsai_cover_bg.png` | 1200×1500 | idem |
| Sfondo webinar | `bg/webinar_bg.png` | 1200×1500 | template Canva `EAHBgIbKc_s` |
| Sfondo hiring | `bg/hiring_bg.png` | 1200×1200 | template Canva `EAGtUUjl0y0` |
| Campo editoriale navy | `bg/editorial_navy.png` | 1200×1500 | derivato da `webinar_bg` — icona videocamera rimossa, badge News AI al suo posto (`make_editorial_bg.py`) |
| Campo editoriale blu | `bg/editorial_blue.png` | 1200×1500 | come sopra, con le tinte navy rimappate su blu |
| Campo editoriale cielo | `bg/editorial_sky.png` | 1200×1500 | gradiente cielo campionato da `newsai_bg` + filigrana a circuito estratta da `webinar_bg`. **Non ha marchio né badge incorporati** |
| Wordmark navy / blu | `logo/digitiamo-wordmark-{navy,blue}.png` | 245×78 | ricolorazione dell'alpha di quello bianco |
| Badge News AI navy / blu | `logo/icon-news-{navy,blue}.png` | 200×181 | idem |
| Font display | `fonts/Montserrat-{700,800}.woff2` | — | font del brand, dai template Canva |
| Font corpo | `fonts/Lato-{400,700}.woff2` | — | idem |

### Anatomia del marchio

Il wordmark e' "**digitiamo**" in minuscolo, dove la **d** iniziale e' un glifo a
**tracce di circuito**: linee parallele che terminano in nodi circolari, disegnate
dentro la sagoma della lettera. E' l'elemento distintivo del brand — la fusione
"tecnologia + parola italiana".

**Il motivo circuito e' anche la filigrana decorativa** del sistema: la stessa
sagoma della `d`, ingrandita a tutta altezza, in una tinta piu' chiara del fondo
(`--c-blue-tint` su blu, `--c-navy-tint` su navy), ancorata a sinistra e tagliata
dal bordo. E' la firma visiva riconoscibile a distanza.

### Sistema di icone-categoria

Le icone non sono decorazione: sono **badge di categoria**, costruiti sullo stesso
schema — quadrato con angoli arrotondati, bianco pieno, con il motivo **spillo/nodo**
(un cerchio con foro + asta verticale) inserito nel simbolo del formato:

- libro aperto + spillo → **News AI**
- videocamera + spillo → **Webinar / Evento**

Lo spillo e' il nodo del circuito, ripreso dalla `d`. Un nuovo tipo di post
richiede una nuova icona **costruita con questa grammatica**, non un'icona
generica presa da una libreria.

### 3. Palette

Estratta per conteggio pixel dominanti sui PNG di sfondo. `brand/tokens.py` e'
l'unica fonte di verita' in codice; qui c'e' il ragionamento.

| Token | Hex | Ruolo | Provenienza |
|---|---|---|---|
| `--c-blue` | `#4a3aff` | **Primario.** Fondo dei pannelli editoriali | 44.8% di `newsai_bg`, 81.8% di `newsai_cover_bg` |
| `--c-navy` | `#0e0a48` | Fondo autorevole/serio (webinar, hiring) | 85.3% di `webinar_bg` |
| `--c-green` | `#43ef84` | **Accento, uso parsimonioso** | 4.1% di `hiring_bg` |
| `--c-white` | `#ffffff` | Testo su fondi saturi, marchio, nuvola | — |
| `--c-blue-tint` | `#6052ff` | Filigrana circuito su blu | 12.3% di `newsai_bg` |
| `--c-navy-tint` | `#2c285e` | Filigrana circuito su navy | 13.3% di `webinar_bg` |
| `--c-sky-ink` | `#d0f0ff` | Azzurro pallido come **inchiostro** su fondo scuro (accento di testo su navy e blu) | `newsai_bg`, famiglia cielo |
| `--c-text-on-blue` | `#eef0ff` | Corpo su pannello blu | `social-ped/renderer/server.js` |
| `--c-text-muted-navy` | `#b9c0f5` | Metadati su navy | idem |
| `--c-text-muted-soft` | `#c7ccf0` | Ruoli/didascalie su navy | idem |
| `--c-accent-ring` | `#2e7bf0` | Anello avatar, accento secondario | idem |
| `--c-tint` | `#ebeefc` | Superfici tenui su bianco (report PDF) | report PED |

**Uso del verde.** Negli asset Canva originali il verde appare **solo** nel
contesto hiring. Con la direzione B (2026-09-07) e' stato esteso al contesto
editoriale. I limiti sono stati **misurati**, non stimati, con il validator
della skill dataviz:

| Tinta | Su navy | Su blu | Su cielo |
|---|---|---|---|
| `--c-green` `#43ef84` | PASS ≥3:1 | PASS ≥3:1 | **1,2:1 — inutilizzabile** |
| `--c-blue` `#4a3aff` | — | — | PASS ≥3:1 |
| `--c-sky-top` `#d0f0ff` | ok come TESTO | ok come TESTO | — |

Nota: `#d0f0ff` **fallisce il chroma floor** (0.039, "reads gray"), quindi non
puo' codificare un dato: va bene come colore di testo, non come tinta di un
marchio numerico o di una barra.

### Due ruoli distinti: tinta dati e accento di testo

Confonderli e' stato un errore reale in fase di implementazione (il verde era
fissato nel codice e finiva su fondo chiaro a 1,2:1). Ora ogni superficie
dichiara entrambi:

| Superficie | Testo | Accento (testo) | Tinta dati (cifre, barre) |
|---|---|---|---|
| navy | bianco | verde | verde |
| blu | bianco | cielo | verde |
| cielo | navy | blu | blu |

### 4. Tipografia

- **Display: Montserrat** — 800 per titoli e numeri, 700 per etichette/eyebrow.
  Geometrica, larga, maiuscoletto con `letter-spacing` positivo per le eyebrow e
  negativo (−0.5 a −1px) per i titoli grandi.
- **Corpo: Lato** — 400 per il testo corrente, 700 per metadati ed evidenze.
  `line-height` 1.34 sul corpo, 1.04–1.05 sui titoli display.

I quattro `.woff2` sono **incorporati in base64** nei template (`tokens.py::font_face_css`).
Motivo: il rendering headless non deve dipendere dalla rete. Un `@import` a Google
Fonts che fallisce produce PNG in un font di fallback — sbagliati e senza errore.

### 5. Formati

| Formato | Dim. | Uso |
|---|---|---|
| Verticale 4:5 | **1200×1500** | news, carosello, webinar — feed LinkedIn/Instagram |
| Quadrato 1:1 | **1200×1200** | hiring |
| A4 @96dpi | 794×1123 | report PED interno (PDF) |

1200×1500 e' la dimensione dei template Canva reali. E' il formato canonico:
1080×1350 ha lo stesso rapporto ma risoluzione minore, senza motivo.

### Il gradiente cielo NON e' un token

E' cotto dentro `bg/editorial_sky.png`, e i suoi valori vivono in un solo
posto: `brand/make_editorial_bg.py`, che quel PNG lo genera.

| | Valore | Da dove |
|---|---|---|
| `SKY_TOP` | `#c5ebff` | campionato su `newsai_bg.png`, colonna x=40 (fuori dalla nuvola) |
| `SKY_BOTTOM` | `#dbf3ff` | idem |

Misurato sul PNG prodotto: y=0 `#c5ebff`, y=1499 `#dbf3ff` — corrispondono.

Fino all'8 settembre 2026 `tokens.py` dichiarava *anche* un gradiente, con
`sky_top #d0f0ff`, `sky_mid` e `sky_bottom` — valori diversi da quelli reali, e
gli ultimi due mai usati. Il render legge l'immagine e non i token, quindi le
slide erano corrette; ma la discrepanza ha portato una revisione esterna a
diagnosticare un refuso inesistente sul fondo di una slide. Ora `sky_ink` e'
solo un colore di testo e dice cosa e'.

**Regola generale**: un colore che finisce dentro un asset non va dichiarato
una seconda volta come token. Il posto dove nasce e' l'unica fonte.

Dall'8 settembre 2026 non e' piu' solo una convenzione: `render.py::_check_size`
misura ogni PNG prodotto e rifiuta qualunque scostamento, cancellando il file.
Gli asset fino al 31 agosto restano 1080×1350 e non vanno presi a riferimento.

### 6. Limiti di caratteri (tarati sui box reali)

Da `social-ped/config/template-registry.json` — misurati sui box dei template a
1200×1500, non stimati:

| Campo | Max | Note |
|---|---|---|
| `periodo` (cover) | 20 | es. "Giugno 2026" |
| `categoria` | 18 | enum, vedi sotto |
| `titolo` | 48 | un titolo corto che colpisce batte uno lungo che si taglia |
| `corpo` | 200 | |
| `titolo` (webinar) | 60 | |
| `data_ora` (webinar) | 40 | |
| `relatore` (webinar) | 40 | |
| `ruolo_1/2` (hiring) | 30 | |

Enum categorie News AI: `Talenti AI`, `Modelli`, `Normativa`, `Investimenti`,
`Prodotti`, `Ricerca`. Regola editoriale: **mescolare** le categorie in un
carosello, non cinque notizie tutte sui modelli.

Il layout applica auto-fit (`.fit` + `data-maxh`) come rete di sicurezza per
piccoli sforamenti, ma il testo va scritto per rientrare: l'auto-fit corregge,
non autorizza. `render.py` impone anche una **soglia di leggibilita'**
(`MIN_CONTAINER_FS = 72`, cioe' testo minimo ~17px su tela 1200px): se l'auto-fit
dovesse scendere sotto quella soglia il rendering si interrompe, perche' un
testo che "sta" solo perche' rimpicciolito a microcarattere non e' pubblicabile.

### 7. Divieti (violazioni viste in produzione)

1. **Mai rendere il marchio come testo.** `<div>Digitiamo</div>` in un font
   qualsiasi non e' il logo: perde il glifo a circuito, cioe' l'unica cosa
   distintiva. Usare `logo/digitiamo-wordmark-white.png`.
   *(Questo era il comportamento di `carousel_slides.html` e `single_images.html`.)*
2. **Mai sostituire i font del brand.** Il brand e' Montserrat + Lato. Manrope +
   Archivo Black era un'approssimazione — palette giusta, tipografia sbagliata.
3. **Mai fondi piatti al posto degli sfondi di brand.** Il gradiente cielo, la
   nuvola e la filigrana circuito **sono** il brand. Un `background: #4a3aff`
   piatto ha il colore giusto e zero identita'.
4. **Mai caricare font dalla rete al momento del rendering.** Solo base64.
5. **Niente emoji come elemento grafico** dentro le slide (nelle caption va bene).
   Un pill "🔥 Mito da sfatare" e' il segnale piu' riconoscibile di grafica
   generata da AI, e il sistema di icone-categoria (§2) esiste proprio per questo.
6. **Niente verde fuori dal contesto hiring** (§3).
7. **Non riutilizzare mai un nome file** gia' pubblicato: Buffer scarica l'asset
   dall'URL al momento della pubblicazione effettiva, che puo' avvenire giorni
   dopo la creazione della bozza. Sovrascrivere un file cambia in silenzio
   l'immagine di un post gia' approvato.

### 7-bis. Varieta' di colore: il ritmo per tipo di post

Un carosello le cui pagine stanno tutte sullo stesso fondo si legge come una
sola immagine ripetuta. `templates.POST_TYPES` assegna a ogni formato una
**sequenza di superfici** (`rhythm`), che alterna scuro e chiaro per dare
respiro allo swipe. Il ritmo non e' decorativo: le pagine chiare cadono sui
momenti di respiro, non sull'apertura o sulla chiamata all'azione.

Il fondo chiaro e' diventato possibile solo dopo aver derivato le varianti
scure del marchio: con il solo wordmark bianco ogni pagina era **costretta** a
un fondo scuro, ed e' da li' che nasceva la monotonia.

### 8. Cosa manca ancora (onesto)

- ~~**Logo vettoriale ufficiale.**~~ **Arrivato l'8 settembre 2026**:
  `logo/digitiamo-wordmark.svg`. Non ancora in uso dal renderer, per un motivo
  spiegato in fondo a questo documento. Le varianti navy e blu restano
  *derivazioni* dall'alpha del wordmark bianco finche' gli sfondi non vengono
  rigenerati dal vettore.
- **Scale >2× e stampa**: gli asset in uso sono ancora i PNG ricavati per
  ritaglio. Il vettore le risolve, quando verra' adottato.
- **Icone-categoria oltre news/webinar**: `Talenti AI`, `Modelli`, `Normativa`,
  `Investimenti`, `Prodotti`, `Ricerca` non hanno un badge dedicato. Da disegnare
  con la grammatica §2 (quadrato arrotondato + spillo/nodo).
- **Nuvola sul fondo chiaro**: `editorial_sky.png` porta il gradiente cielo e la
  filigrana a circuito, ma non la nuvola bianca di `newsai_bg` (estrarla da un
  gradiente non da' un alpha pulito). Se serve, va chiesta come asset separato.


### Il marchio vettoriale (dall'8 settembre 2026)

`logo/digitiamo-wordmark.svg` — viewBox 620×250, fornito dal team design. E' la
**sorgente**: i PNG in `logo/` erano stati *estratti* dagli sfondi rasterizzati
ricavando l'alpha dalla luminanza, quindi portano l'antialiasing dello sfondo.

Verificato che sia lo stesso marchio, non una variante: ritagliati
sull'inchiostro i rapporti sono 3.561 (PNG) e 3.508 (SVG) — 1,5% di scarto — e
le sagome si sovrappongono al **91,2%**, con soli 97 pixel presenti nel PNG e
assenti nel vettore.

Un solo file serve tutti i colori: il fill sta nella classe `.cls-1` e si
sovrascrive via CSS. Non serve una variante per fondo.

**Non e' ancora usato dal renderer, ed e' deliberato.** Il marchio e' **cotto
dentro** gli sfondi editoriali (`editorial_navy.png`, `editorial_blue.png`), non
disegnato dal layout: solo la superficie `sky` lo sovrappone. Passare al vettore
significa rigenerare gli sfondi con `make_editorial_bg.py`, e quindi cambiare
l'aspetto di **ogni** slide. Va fatto come lavoro voluto, con il confronto dei
pixel prima e dopo — non come effetto collaterale di un commit su altro. Gli
asset gia' pubblicati non devono cambiare: una bozza Buffer punta a quei file.
