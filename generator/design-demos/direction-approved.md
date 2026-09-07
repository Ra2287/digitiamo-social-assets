# Direzione di design — carosello editoriale

**Stato: APPROVATA — Direzione B "Pannello pieno"**
Scelta dell'utente il 2026-09-07, parole esatte: «ok B».
Implementata in `templates.py` (`SURFACES`) + `week.py` (assegnazione superfici).

## Problema affrontato

`brand/bg/newsai_bg.png` nasce per i post "News AI", dove la fascia cielo
(y 0-628, il **42%** dell'immagine) ospita la **foto dell'articolo**. Il carosello
editoriale non ha foto: quella fascia restava un gradiente vuoto e il contenuto
si schiacciava nella metà inferiore.

## Bozze presentate (2026-09-07)

Contenuto identico nelle tre, solo asset reali di brand. Sorgente: `make_demos.py`,
confronto affiancato in `_confronto.png`.

| | Direzione | Idea | Esito |
|---|---|---|---|
| A | Dato nel cielo | Il cielo diventa la zona della cifra (navy su cielo), il pannello blu porta il significato. | scartata |
| **B** | **Pannello pieno** | **Via il cielo: campo pieno, contenuto centrato. Nessuno spazio morto, un solo layout per ogni tipo di slide.** | **scelta** |
| C | Attraverso il taglio | Un blocco tipografico attraversa il confine: navy sopra, bianco sotto. | scartata |

## Come è stata implementata

I due caveat che B aveva alla presentazione sono stati risolti così:

1. **Sfondo con l'icona sbagliata** → creati `bg/editorial_navy.png` e
   `bg/editorial_blue.png` con `brand/make_editorial_bg.py`: parte da
   `webinar_bg.png`, cancella l'icona videocamera (l'area attorno è navy piatto,
   verificato a pixel) e incolla il badge **News AI** corretto. Wordmark e
   filigrana a circuito restano intatti. La variante blu rimappa le due tinte
   navy sulle due tinte blu del brand.

2. **Verde fuori dal contesto hiring** → il verde resta come accento **solo sul
   campo navy**. Sul campo blu due saturi complementari vibrerebbero, quindi
   l'accento è `--c-sky-top`. Vedi `brand-spec.md` §3, aggiornato di conseguenza.

Inoltre, le due superfici **codificano il registro del contenuto**, non decorano:

- **navy** = argomentazione (apertura, tesi, chiusura) — accento verde
- **blue** = fatto verificabile (dati, date, elenchi di obblighi) — accento cielo

L'assegnazione per slide è in `week.py` (`surface=`).

## Nota sull'auto-grow

B promette "zero spazio morto", ma l'auto-fit originale solo rimpiccioliva: una
slide con poco testo restava un blocchetto sospeso. `render.py` ora **ingrandisce
anche**, fino a riempire il 90% del riquadro, con un tetto a
`MAX_CONTAINER_FS = 128`. Il tetto è deliberato: senza, due righe diventerebbero
un cartellone. Sulle slide davvero povere di testo resta quindi dell'aria — è il
compromesso accettato, non una dimenticanza.

## Ancora aperto

- Il **wordmark navy su fondo chiaro** e il **logo vettoriale** non esistono:
  gli asset sono PNG ritagliati dagli sfondi. Da chiedere al team design.
- Le **icone-categoria** oltre a News AI e Webinar (`Talenti AI`, `Modelli`,
  `Normativa`, `Investimenti`, `Prodotti`, `Ricerca`) vanno disegnate con la
  grammatica di `brand-spec.md` §2.
