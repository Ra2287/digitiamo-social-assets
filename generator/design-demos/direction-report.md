# Direzione di layout — pagina "Trend del settore" (report PED)

**Stato: IN ATTESA DI SCELTA.**

## Problemi rilevati sul report attuale

1. **Impaginazione rotta (difetto, non estetica).** `trends_page()` impagina a
   `per_page = 5` fisso, ma a 794×1123 ce ne stanno ~3. Misurato:

   | pagina | altezza reale | sforo |
   |---|---|---|
   | 3 | 1743px | +620px |
   | 4 | 1663px | +540px |
   | 5 | 1877px | +754px |
   | 13 | 1384px | +261px |

   Nel PDF le schede si spezzano a metà fra le pagine. È da qui che **13 pagine
   dichiarate diventano 17 pagine stampate**.
2. **Card + bordo colorato a sinistra su ogni blocco** — il pattern più
   riconoscibile della grafica generata da AI.
3. **Gerarchia piatta**: trend, competitor e intuizione hanno lo stesso peso.
4. **"Cosa è successo" e "Perché è rilevante"** hanno la stessa etichettina blu,
   pur essendo un fatto e un'interpretazione.
5. **Nessun linguaggio visivo del brand** oltre a palette e font.

## Le tre direzioni (2026-09-07)

Contenuto reale da `build_report.trends`. Tutte impaginano **per misura**
(`fit_count()`), non per costante. Sorgente: `make_report_demos.py`.

| | Direzione | Trend/pagina | Pagine per 10 trend | File |
|---|---|---|---|---|
| A | Dossier | 4 | 3 | `R-A-dossier.png` |
| B | Spina a circuito | 3 | **4** (la meno efficiente) | `R-B-spina-circuito.png` |
| C | Griglia densa | **6** | **2** (dimezza la sezione) | `R-C-griglia-densa.png` |

## Valutazione onesta

**A · Dossier** — Registro editoriale, nessun contenitore, numeri profilati nel
margine. Il più elegante da leggere in sequenza.
*Ma*: il blocco "perché è rilevante" usa ancora un **bordo verde a sinistra**,
cioè esattamente il pattern che ho criticato al punto 2. È più leggero (2px,
senza card) ma è quello.

**B · Spina a circuito** — La più marcata come identità: fascia navy con marchio
e badge, nodi numerati lungo una spina.
*Ma*: due problemi reali. È la meno efficiente (4 pagine invece di 2-3), e la
spina è **una linea con un anello**, non il motivo del brand — che ha nodi con
foro e tracce parallele. La promessa "motivo a circuito" è mantenuta solo in
parte. Inoltre il "perché" resta un box tinto, quindi un contenitore.

**C · Griglia densa** — L'unica che risolve il problema n.1 in modo netto:
dimezza la sezione trend. La fascia navy di testa dà due livelli reali di
gerarchia (titolo vs corpo vs interpretazione), quindi batte il punto 3.
*Ma*: il corpo scende a 10,6px — leggibile in A4 stampato, ma stretto; e le
tessere della colonna destra hanno altezze diverse, lasciando vuoti.

## Nota

Nessuna delle tre è ancora stata applicata alle altre sezioni (competitor, idee
di post, calendario), che hanno gli stessi cinque problemi. La direzione scelta
va estesa a tutto il report, e `generate_html.py` va convertito
all'impaginazione per misura.
