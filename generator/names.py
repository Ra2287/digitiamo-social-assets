# -*- coding: utf-8 -*-
"""I nomi dei file degli asset. Unica fonte, per render.py e publish_buffer.py.

Prima il formato dei nomi era scritto in due posti: `render.py` li generava e
`publish_buffer.py` li ricostruiva per comporre gli URL. Bastava cambiarne uno
perche' Buffer puntasse a URL inesistenti — e l'errore si sarebbe visto solo
alla pubblicazione effettiva della bozza, giorni dopo.

## Le revisioni servono al ciclo human-in-the-loop

Il flusso reale e': il lunedi' l'automazione genera report, asset e bozze
Buffer; se qualcosa non va, un umano chiede di rifarlo.

Rifare **non** puo' voler dire sovrascrivere: la bozza Buffer punta a quell'URL
e Buffer scarica l'asset alla pubblicazione, non alla creazione. Sovrascrivere
cambierebbe in silenzio l'immagine di una bozza gia' vista. Ma non puo' nemmeno
voler dire cambiare data o slug: la settimana e il post sono gli stessi.

Quindi si segna il post in `week.REDO`: stessa settimana, stesso post, **URL
nuovo**. La bozza va rifatta puntando al nuovo URL — che e' esattamente cio' che
serve, perche' e' stato chiesto un contenuto diverso.

La revisione e' **per post**, non per settimana: se va rifatto un post solo, gli
altri quattro restano quelli approvati, con le loro bozze intatte.

## Perche' i nomi sono percorsi e non solo nomi di file

Gli asset di ogni settimana stanno in `settimane/<data>/`. Qui le funzioni
restituiscono il **percorso relativo alla radice della CDN**, non il solo nome:
cosi' `render.py` scrive nella cartella giusta e `publish_buffer.py` compone
l'URL giusto senza che nessuno dei due sappia come sono organizzate le cartelle.

La data resta anche nel nome del file, pur essendo gia' nella cartella: un PDF
scaricato o allegato viaggia da solo, e la data e' l'unica cosa che lo rende
riconoscibile fuori dal suo contesto.
"""
import posixpath

import week


def revision(slug):
    """La revisione di un singolo post. 0 = prima generazione del lunedi'."""
    redo = getattr(week, "REDO", None) or {}
    if not isinstance(redo, dict):
        raise SystemExit(
            "week.REDO deve essere un dizionario slug -> numero di revisione, "
            "non %s." % type(redo).__name__)
    n = redo.get(slug, 0)
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise SystemExit(
            "week.REDO[%r] deve essere un intero >= 0, non %r." % (slug, n))
    return n


def _suffix(slug):
    n = revision(slug)
    return "-r%d" % n if n else ""


def week_dir(date=None):
    """La cartella della settimana, relativa alla radice della CDN.

    Separatori POSIX perche' questa stringa e' sia un pezzo di percorso su disco
    (dove `/` funziona anche su Windows) sia un pezzo di URL.
    """
    return posixpath.join("settimane", date or week.DATE)


def _in_week(name):
    return posixpath.join(week_dir(), name)


def carousel_slide(slug, index):
    """La slide n-esima di un carosello.

    L'indice parte da 1 e corrisponde al `data-slug` che templates.py assegna
    alle slide (`slide1`, `slide2`, ...): e' cosi' che publish_buffer riesce a
    puntare alla prima slide come anteprima del documento.
    """
    return carousel_slide_name(slug)("slide%d" % index)


def carousel_slide_name(slug):
    """Fabbrica di nomi per render.py, che passa lo slug della slide dal DOM."""
    def make(slide_slug):
        return _in_week("carosello_%s_%s%s_%s.png"
                        % (slug, week.DATE, _suffix(slug), slide_slug))
    return make


def carousel_pdf(slug):
    return _in_week("carosello_%s_%s%s.pdf" % (slug, week.DATE, _suffix(slug)))


def single(slug):
    return _in_week("brandstyle_%s_%s%s.png" % (slug, week.DATE, _suffix(slug)))


def report_pdf():
    # Il report e' interno e non tracciato: qui la revisione non serve, un
    # documento consegnato si rigenera sopra senza conseguenze esterne.
    return _in_week("PED_Digitiamo_%s.pdf" % week.DATE)
