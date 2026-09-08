# brand-spec.md — Digitiamo

> Gate file del protocollo asset (huashu-design §1.a). Ogni design che porta il
> marchio Digitiamo si basa su questo file. **Nessun valore qui e' inventato**:
> ognuno e' estratto dagli asset Canva reali del brand — la provenienza e'
> annotata voce per voce.
>
> Ultima verifica: 2026-09-07 · Fonte primaria: `/Users/fabiopia/social-ped/renderer/assets`
> (template Canva esportati e usati in produzione dal renderer PED).

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
urlato. Il brand ha un accento verde acido, ma lo usa con parsimonia (vedi §3).

## 2. Asset reali (obbligatori, mai ricostruiti)

Tutti in `generator/brand/`. Estratti dai PNG Canva; il marchio non esisteva come
file standalone, e' stato ricavato dagli sfondi con alpha da luminanza.

| Asset | File | Dim. | Provenienza |
|---|---|---|---|
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

## 3. Palette

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
| `--c-sky-top` | `#d0f0ff` | Gradiente cielo (alto) | `newsai_bg` |
| `--c-sky-mid` | `#d8f2ff` | Gradiente cielo (medio) | `newsai_bg` |
| `--c-sky-bottom` | `#ddf3ff` | Gradiente cielo (basso) | `newsai_bg` |
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

## 4. Tipografia

- **Display: Montserrat** — 800 per titoli e numeri, 700 per etichette/eyebrow.
  Geometrica, larga, maiuscoletto con `letter-spacing` positivo per le eyebrow e
  negativo (−0.5 a −1px) per i titoli grandi.
- **Corpo: Lato** — 400 per il testo corrente, 700 per metadati ed evidenze.
  `line-height` 1.34 sul corpo, 1.04–1.05 sui titoli display.

I quattro `.woff2` sono **incorporati in base64** nei template (`tokens.py::font_face_css`).
Motivo: il rendering headless non deve dipendere dalla rete. Un `@import` a Google
Fonts che fallisce produce PNG in un font di fallback — sbagliati e senza errore.

## 5. Formati

| Formato | Dim. | Uso |
|---|---|---|
| Verticale 4:5 | **1200×1500** | news, carosello, webinar — feed LinkedIn/Instagram |
| Quadrato 1:1 | **1200×1200** | hiring |
| A4 @96dpi | 794×1123 | report PED interno (PDF) |

1200×1500 e' la dimensione dei template Canva reali. E' il formato canonico:
1080×1350 ha lo stesso rapporto ma risoluzione minore, senza motivo.

Dall'8 settembre 2026 non e' piu' solo una convenzione: `render.py::_check_size`
misura ogni PNG prodotto e rifiuta qualunque scostamento, cancellando il file.
Gli asset fino al 31 agosto restano 1080×1350 e non vanno presi a riferimento.

## 6. Limiti di caratteri (tarati sui box reali)

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

## 7. Divieti (violazioni viste in produzione)

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

## 7-bis. Varieta' di colore: il ritmo per tipo di post

Un carosello le cui pagine stanno tutte sullo stesso fondo si legge come una
sola immagine ripetuta. `templates.POST_TYPES` assegna a ogni formato una
**sequenza di superfici** (`rhythm`), che alterna scuro e chiaro per dare
respiro allo swipe. Il ritmo non e' decorativo: le pagine chiare cadono sui
momenti di respiro, non sull'apertura o sulla chiamata all'azione.

Il fondo chiaro e' diventato possibile solo dopo aver derivato le varianti
scure del marchio: con il solo wordmark bianco ogni pagina era **costretta** a
un fondo scuro, ed e' da li' che nasceva la monotonia.

## 8. Cosa manca ancora (onesto)

- **Logo vettoriale ufficiale.** Le varianti navy e blu sono *derivazioni*
  ottenute ricolorando l'alpha del wordmark bianco. Il marchio e' piatto e
  monocromatico in tutti gli asset Canva, quindi la derivazione e' fedele — ma
  se il team design ha l'SVG originale, quello vince.
- **Scale >2× e stampa**: gli asset sono PNG ricavati per ritaglio.
- **Icone-categoria oltre news/webinar**: `Talenti AI`, `Modelli`, `Normativa`,
  `Investimenti`, `Prodotti`, `Ricerca` non hanno un badge dedicato. Da disegnare
  con la grammatica §2 (quadrato arrotondato + spillo/nodo).
- **Nuvola sul fondo chiaro**: `editorial_sky.png` porta il gradiente cielo e la
  filigrana a circuito, ma non la nuvola bianca di `newsai_bg` (estrarla da un
  gradiente non da' un alpha pulito). Se serve, va chiesta come asset separato.
