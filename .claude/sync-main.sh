#!/bin/bash
# Allinea la copia locale a origin/main all'avvio di una sessione Claude Code.
#
# Perche' un hook e non una riga in CLAUDE.md: CLAUDE.md e' un'ISTRUZIONE, che
# Claude legge e di norma segue; questo e' un MECCANISMO, che gira comunque.
# La differenza conta perche' una sessione su codice vecchio non ha plan.py ne'
# names.py e finisce per riscrivere l'HTML da zero — l'errore che il sistema
# esiste per evitare.
#
# Non distrugge mai lavoro locale: se ci sono modifiche non committate, o se il
# ramo e' divergente, si limita a dirlo. Esce sempre 0, perche' un hook che
# fallisce non deve impedire di lavorare.
set -u
cd "$(dirname "$0")/.." 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

if ! git fetch --quiet origin 2>/dev/null; then
  echo "[sync] origin non raggiungibile: si lavora sulla copia locale."
  exit 0
fi

ramo=$(git branch --show-current)
if [ -n "$(git status --porcelain)" ]; then
  echo "[sync] ci sono modifiche non committate: NON allineo. Ramo: ${ramo:-(distaccato)}."
  exit 0
fi

if [ "$ramo" != "main" ]; then
  dietro=$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)
  echo "[sync] ramo '${ramo:-(distaccato)}', non main. origin/main ha $dietro commit che questo ramo non ha."
  exit 0
fi

if git merge --ff-only origin/main >/dev/null 2>&1; then
  echo "[sync] main allineato a origin ($(git rev-parse --short HEAD))."
else
  echo "[sync] main e origin/main sono DIVERGENTI: non allineo da solo."
  echo "[sync] Integra a mano prima di generare: 'git rebase origin/main' (o chiedi)."
fi
exit 0
