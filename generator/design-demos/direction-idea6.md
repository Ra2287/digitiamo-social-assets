# Idee di layout — IDEA 6 del PED (carosello dati Nvidia)

**Stato: RISOLTO — tutte e tre implementate come `kind` riusabili.**

## Perché non c'era una scelta da fare

Le avevo presentate come tre direzioni in concorrenza: era un errore di
impostazione. **Per un carosello A, B e C non sono alternative — sono tre tipi
di slide di cui un carosello dati ha bisogno tutti.** La decisione vera non è
"quale layout", è *in che sequenza*.

Sono quindi diventate tre `kind` in `templates.py`:

| kind | Forma | Momento del racconto |
|---|---|---|
| `scorecard` | più indicatori in colonna | quadro d'insieme, presto |
| `figure` | hero number, nessun grafico | la cifra singola che conta |
| `share` | barra parte/tutto | da dove arriva davvero |

Il carosello Nvidia (`week.NVIDIA`) le usa in questa sequenza:
`hook → scorecard → figure → share → statement → cta`.

## Perché questa idea

Delle 7 idee del PED, la 6 — *"96,2 miliardi in un trimestre: cosa ci dicono
davvero i numeri di Nvidia"*, formato Carosello/documento dati, badge Riserva —
è **l'unica ancora senza grafiche**, ed è interamente numeri. È il caso in cui il
layout decide se il post funziona.

Le tre idee stanno **dentro la direzione B "Pannello pieno"** già approvata: il
sistema è deciso, qui si scegli come trattare una slide guidata dai dati.

## Cosa non copre il layout attuale

Il layout `_data` di `templates.py` (occhiello / numero / spiegazione / nota) va
bene per una data secca come "2 agosto 2026". Su una cifra economica perde tre
cose: **l'unità di misura**, **lo scarto percentuale** e **la proporzione**.

## Il colore è stato calcolato, non valutato a occhio

Con `validate_palette.js` della skill dataviz:

- **`#d0f0ff` (cielo brand) FALLISCE il chroma floor** (0.039 — "reads gray"):
  non è una tinta dati, è un neutro. Non può codificare una categoria.
- **`#43ef84` (verde brand) da solo**: chroma PASS, contrasto PASS ≥ 3:1 sia su
  navy sia su blu. L'unico FAIL è la *lightness band*, che è un vincolo per
  palette categoriali multi-serie e non governa un accento a tinta singola.
- Quindi: **una sola tinta dati (verde) + un neutro**. Nessuna palette
  categoriale, quindi nessun rischio di confusione per daltonismo.

### Conseguenza sul brand (una regola precisata, non violata)

`brand-spec.md` §3 riserva il verde al campo navy e assegna al campo blu
l'accento cielo — che però non è una tinta dati. Quindi **le slide con grafico
vanno sul campo navy**. La regola diventa: navy = argomentazione *e* dato
quantificato; blu = affermazione fattuale senza grafico.

## Le tre idee

| | Idea | Forma | Slide necessarie |
|---|---|---|---|
| A | **Cifra e scarto** | hero number, nessun grafico | 1 per cifra |
| B | **Quota** | barra parte/tutto (89 su 96,2) | 1 per proporzione |
| C | **Scorecard** | tre stat tile in colonna | 1 per tutti e tre |

**A · Cifra e scarto** — Una cifra sola non è un grafico: è un titolo che si
legge come un numero. Rende espliciti unità e scarto, che il layout attuale
perde. La più immediata in un feed.

**B · Quota** — L'unica in cui **la forma porta l'informazione**: la barra è
quasi tutta verde, e quello *è* il punto — la crescita è un solo segmento, non
l'azienda intera. Etichette dirette su entrambi i segmenti, nessuna legenda.

**C · Scorecard** — La più densa: una slide invece di tre. Cifre in
`tabular-nums` così le colonne si allineano e i valori si confrontano a colpo
d'occhio.

## Correzioni fatte dopo aver guardato i render

Il validator controlla il colore, non la geometria — quindi le slide vanno viste:

1. **C aveva un difetto di information design**: la colonna centrale significava
   "scarto" nelle righe 1 e 3 ma "seconda cifra assoluta" nella 2. Per questo
   "~440 mld" andava a capo rompendo l'allineamento. Una colonna deve significare
   una cosa sola: ora è sempre il *qualificatore* del dato.
2. **B**: le etichette erano vincolate alla larghezza dei segmenti, e "RESTO"
   (7,5%) sbordava dal proprio contenitore. Ora sono su una riga con
   `space-between` e portano entrambe il valore.
3. Apostrofi ASCII (`e'`, `Piu'`) sostituiti dagli accenti corretti.

## Nota sul mezzo

La skill dataviz vuole un layer di hover per default. Qui il mezzo è un **PNG
pubblicato su LinkedIn**: l'hover non esiste. Tutti i valori stanno quindi come
etichette dirette nel grafico, non in un tooltip.

## Difetti trovati implementando (e come sono stati chiusi)

1. **Colonne della scorecard sovrapposte.** Avevo usato `.62em` come larghezza
   di colonna, ma un `em` sul contenitore della griglia vale ~62px mentre
   "89 mld" a `.40em` ne richiede ~130: le celle si accavallavano. Corretto a
   `1.9em 2.35em 1fr`.
2. **La guardia di render era cieca in orizzontale.** Controllava solo
   `scrollHeight`, quindi la sovrapposizione passava inosservata. Aggiunto un
   controllo di larghezza — che alla **prima versione era un no-op**: guardava
   il contenitore, ma un testo `nowrap` sborda *dentro la cella accanto* senza
   far crescere il contenitore. Ora controlla ogni discendente, ed è stato
   **verificato rompendo la griglia di proposito**: blocca la versione rotta e
   lascia passare i contenuti reali.
3. **Il codice gestiva un solo carosello** (`CAROUSEL` al singolare) mentre il
   PED ne propone due questa settimana (idea 3 e idea 6). Ora `week.CAROUSELS`
   è una lista e `render.py` li genera tutti.
