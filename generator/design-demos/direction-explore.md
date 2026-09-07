# Esplorazione — tre strade nuove per il carosello

**Stato: IN ATTESA DI SCELTA.**

Non sono varianti del sistema attuale: sono tre linguaggi diversi, ognuno con un
riferimento reale dichiarato. Tutti richiamano il brand (palette, Montserrat/Lato,
marchio, motivo a circuito) ma nessuno assomiglia a quello che c'è adesso.

Sorgente: `make_explore_demos.py` · anteprime: `X-*_{1,2}.png` · confronto:
`_esplorazione.png` · nel browser: `python3 review.py --dir <cartella>`

## Le tre logiche di huashu, applicate davvero

| | Strada | Logica | Riferimento |
|---|---|---|---|
| **A** | Businessweek | riferimento reale | Bloomberg Businessweek, pagina dati, era Richard Turley (2010-2014) |
| **B** | Lupi / Data Humanism | miglior designer per *questo* cliente | Giorgia Lupi, partner Pentagram, manifesto Data Humanism |
| **C** | Holmes / Explanation Graphics | ruota dei secondi → **2/20** partizione infografica | Nigel Holmes, direttore grafico di TIME 1978-1994 |

**Perché B non è una scelta casuale.** Lupi è italiana come il cliente, e il suo
metodo — inventare un alfabeto di simboli per il contenuto specifico, più una
legenda obbligatoria — combacia con un marchio che **è già un circuito con nodi**.
Il glifo dei dati è il nodo del logo: l'alfabeto nasce dall'identità invece di
esserle appiccicato sopra.

## Il materiale fotografico è stato procurato PRIMA di disegnare

È il gate che avevo saltato nei giri precedenti (huashu Phase 3.5): un contenuto
che ha bisogno di un'immagine non si risolve con un blocco di colore.

- **`brand/photo/nasa-columbia-supercomputer.jpg`** — pubblico dominio (NASA).
  Test di onestà superato: la slide parla di "89 miliardi dal segmento data
  center", e la fotografia rende fisico un segmento contabile astratto.
- **`brand/third-party/nvidia-wordmark-*.svg`** — logo ufficiale, da svgl.app.
  **Non è decorazione**: il protocollo asset impone che un prodotto nominato
  mostri il proprio marchio, altrimenti la grafica parla di un'azienda senza
  mostrarla. È il punto in cui questi caroselli erano incompleti fin dall'inizio.

### Scartate, e perché

- **ASUS GeForce 210 / 7600** — schede di consumo del 2009. Illustrare i ricavi
  data center del 2026 con hardware consumer di quindici anni prima è
  **fuorviante**: è la "foto d'archivio vagamente a tema" che il protocollo vieta.
- **Foto CC BY-SA** (BalticServers, UNC, Virginia Tech) — attribuzione *e*
  share-alike su un post commerciale sono un rischio evitabile, dato che esistono
  equivalenti in pubblico dominio con lo stesso contenuto.

## Vincoli emersi, non previsti

1. **Due verdi non convivono.** Il verde NVIDIA è `#76b900`, quello Digitiamo
   `#43ef84`. Un logo di terzi **non si ricolora**, quindi dove appare NVIDIA
   l'accento Digitiamo passa al blu.
2. **La foto va trattata in duotone.** A colori pieni porta dentro grigi neutri
   (e nell'altra candidata un murale arancione) che sfondano il sistema cromatico.
   Il duotone conserva la struttura — cioè l'informazione — e riporta l'immagine
   nella palette.

## Degradazione dichiarata su C

L'anima dello stile Holmes è **l'illustrazione disegnata a mano**, e la scheda di
stile lo dice esplicitamente (resa 76% in puro HTML). Non ho capacità di
generazione immagini confermata, e disegnare finte illustrazioni in SVG è
esattamente ciò che il protocollo anti-slop vieta. Quindi C usa la fotografia
reale come elemento pittorico più forme piatte contornate: **il registro c'è, il
tratto a mano no.** Se serve C per davvero, servono illustrazioni vere — o da un
illustratore, o da un modello di generazione immagini con il tuo via libera.

## Revisione 2 — "troppo flat" e la strip del logo

Feedback: *"sono tutti un po' troppo flat e la strip blue in cui c'è il logo non
mi convince"*. Entrambe le cose erano giuste.

**La strip.** In B era una fascia colorata il cui unico contenuto era il logo:
non faceva nulla, e si vedeva. Rimossa. Il marchio sta ora nella composizione,
in basso, accanto alla legenda che gli appartiene. Anche in C la fascia in testa
è diventata un'etichetta che sta nel layout.

**Il flat.** Un campo di colore piatto con del testo sopra resta piatto per
quanto bene sia composto. La profondità ora viene da quattro cose, tutte
ancorate al brand e nessuna decorativa:

1. **Fotografia a piena pagina** (in duotone) come fondo, non come francobollo
   in mezzo alla pagina. In A la foto *è* la pagina.
2. **Stratificazione**: il testo scavalca il bordo dell'immagine, l'inserto
   bianco entra nella fotografia, la cifra `92,5%` esce dal margine destro. La
   profondità viene dalla sovrapposizione dei piani, non da un'ombra applicata.
3. **Motivo a circuito a grande scala** come strato tonale. È la firma del
   marchio, quindi usarlo come elemento di profondità è legittimo — e in B fondo
   e primo piano diventano la stessa forma a due scale diverse.
4. **Grana di stampa** all'5,5% in multiply: materialità senza gradienti finti.

Il gradiente c'è solo dove il brand lo ha davvero (il cielo di `newsai_bg`), non
come effetto aggiunto. In C le ombre sono **dure e a registro** — quelle dei
blocchi tipografici stampati con la lastra fuori registro, che è il linguaggio
di stampa dell'epoca di Holmes, non un `box-shadow` morbido da interfaccia.

### Due errori miei in questa revisione

- **Ho violato la mia stessa regola sui due verdi.** La prima versione con
  profondità metteva l'accento Digitiamo `#43ef84` sulla stessa pagina del logo
  NVIDIA `#76b900`. Corretto: in questi caroselli l'accento è il cielo sui fondi
  scuri e il blu sui chiari. Il verde cede il campo perché un logo di terzi non
  si ricolora.
- **Il circuito era grigio neutro.** L'avevo portato a nero con
  `filter: brightness(0) saturate(0)` e abbassato di opacità: risultato, macchie
  grigie fuori palette. Ora è tinto col blu del brand tramite maschera CSS.

### Un falso positivo del mio controllo

Il controllo di sforamento segnalava B e C come rotte. Non lo erano: gli strati
di circuito **escono dal bordo di proposito** e sono già tagliati da
`overflow:hidden`. Il controllo ora esclude gli strati decorativi e misura solo
il contenuto. Da tenere a mente se si portano gli strati a sanguinare anche in
`templates.py`: la stessa verifica in `render.py` darebbe lo stesso falso allarme.

## Difetti trovati guardando i render (revisione 1)

Il controllo automatico non li ha visti: sono sovrapposizioni, non sforamenti —
la stessa zona cieca già incontrata sulla scorecard.

1. **A**: `line-height` sotto 1 con uno sfondo su `<em>` inline faceva
   sovrapporre gli evidenziati alla riga sopra. Corretto a 1.12 +
   `box-decoration-break: clone`.
2. **B**: 96 nodi su 13 colonne = 8 righe, che sforavano e finivano sotto la
   legenda. Portati a 16 colonne (6 righe) e legenda riposizionata.
3. **B**: etichette dei glifi a 17/14px su tela 1200 — sotto la soglia di
   leggibilità che avevo fissato io stesso. Portate a 29/19px, e àncorate al
   bordo superiore del nodo invece che allo stelo (a due righe gli finivano sopra).
