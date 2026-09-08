# Prove — 4 post, settimana 7–13 settembre 2026

Contenuti dal **report reale** (`PED_Digitiamo_20260907.pdf`), con la sezione di
origine annotata. Nella v2 sono stati letti **gli articoli**, non i riassunti:
ne sono usciti dati che il report non aveva e una correzione di merito.

Sorgente: `make_week37_demos.py` · anteprime `W37-*.png` · sfogliatore
`python3 preview.py`

| # | Post | Origine | Slide |
|---|---|---|---|
| 1 | Rassegna News AI | trend 01 + 02 + 04 | 4 |
| 2 | Model fatigue | trend 03 | 6 |
| 3 | Agenti AI in produzione | trend 07 · riframato | 6 |
| 4 | EU AI Act | trend 10 · ricostruito | 6 |

## 1. La copertina, e un problema del font che non è mio

La copertina mancava perché non usavo quella vera: `newsai_cover_bg.png` ha
titolo, sottotitolo, icona e wordmark **incorporati nel PNG** (misurati:
y 169-335, 474-593, 701-913, 1344-1415). L'unico campo variabile è il periodo.

Poi è emerso il motivo per cui i font stonavano: **il testo incorporato nella
copertina non è nei font del brand.** Non è Montserrat né Lato — è un grotesque
tipo Roboto, messo da Canva. Qualunque testo si aggiunga in font di brand ci
stona accanto.

Indovinare quel font introdurrebbe un **terzo carattere** nel sistema. Quindi la
soluzione è non competere: il periodo sta in una **pill**, che è un elemento di
brand e si legge come etichetta. La differenza tipografica diventa una gerarchia
voluta invece di una stonatura.

Da segnalare al team design: se la copertina va rifatta, va rifatta con i font
del brand.

## 2. Model fatigue: cosa ho tenuto dell'esperimento e cosa ho buttato

La ruota di huashu aveva dato **10/20, "ritratto computazionale" (Fathom / Ben
Fry)**. Il trapianto integrale dello stile — fondo nero, tipografia propria,
prosa lunga — era **fuori brand e troppo testuale**. Buttato.

Quello che funzionava era **un solo segno**: la densità che nasce dai dati. È
diventato il `kind` `cadence` dentro i template di brand. Due bande, stessa
finestra di sei mesi, 5 tratti contro 17: la differenza si legge senza leggere.

Dagli articoli sono arrivati i dati che il report non aveva:
- **cadenza mediana: 37,5 giorni nel 2023 → 11 nel 2026** — il numero che rende
  il fenomeno misurabile;
- il "da dieci a cinque" ha un autore: **Suresh Vasudevan, CEO di Clockwork
  Systems**, citato da CNBC. Una frase attribuita vale più di un numero anonimo,
  quindi ha un formato proprio (`kind` `quote`) invece di finire schiacciata in
  un corpo di testo.

**Semplificazione dichiarata sulla slide**: i tratti sono la cadenza mediana
documentata, non i singoli rilasci. Inventare quaranta date per fare densità
sarebbe stato un falso.

## 3. Il «76%» è stato tolto

Verificando la fonte: il numero **847 viene da un post su Medium che compare con
due firme diverse allo stesso URL** (`snehal_singh` e `neurominimal`), e la
paternità accademica che alcune riprese attribuiscono — Stanford, MIT, Carnegie
Mellon, Nvidia, "Elloe AI Research Lab" — **non è verificabile**: quel paper non
si trova. Il 91% sul tool-chaining è reale ma viene da una ricerca diversa
(STAC, 483 casi).

Il caveat del report era corretto. Ma un post che apre con "76%" poggia su
qualcosa che un cliente smonta in trenta secondi, ed è contro la voce del brand.

Il post ora sta sul **meccanismo**, documentato e verificabile: rotazione delle
credenziali su cicli di ~90 giorni, fallimenti **silenziosi** (risultato vuoto
letto come «nessun dato», scritture parziali, percorsi di recupero inventati),
**agenti orfani**, e CVE reali (CVE-2025-6514 CVSS 9,6 nel protocollo MCP;
CVE-2025-59536 CVSS 8,7). Titolo: *«Gli agenti non si schiantano. Derivano»*.

Il meccanismo *è* l'argomento del Team Augmentation. Il 76% non lo era.

## 4. AI Act ricostruito

La v1 diceva «obblighi in vigore, regole in movimento»: vero e inutile. Ora ci
sono le date esatte — Allegato III al **2 dicembre 2027**, Allegato I al
**2 agosto 2028**, sandbox al **2 agosto 2027**, watermarking con tolleranza fino
al **2 dicembre 2026** — e il punto che ribalta la lettura corrente: **la
rilevazione dei bias è stata estesa** dai soli sistemi ad alto rischio a tutti i
sistemi AI e ai modelli generalisti, nello stesso pacchetto che ha rinviato le
scadenze.

CTA sull'AI Business Academy, non sul Team Augmentation: è compliance, non
architettura.

## Resta aperto

- **Conflitto di formato.** Queste sono 1200×1500 col sistema di brand; il
  carosello che il bot ha pubblicato lunedì è 1080×1350 e non lo usa. Nello
  stesso feed convivono male.
- **La copertina News AI va rifatta nei font del brand** (vedi §1).
- I marchi di terzi restano in senso editoriale, separati dal marchio Digitiamo.
