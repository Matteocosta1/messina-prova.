#!/usr/bin/env bash
# Ricostruisce codice/index.html («Prova programma Messina») dal codice VERO di messina-sistema.
# Costruisce gestionale, app, portale e negozio (modalità Prova, senza config.js), genera i due siti,
# poi li mette tutti dentro sorgenti/pagina.html.
# Uso: bash sorgenti/costruisci.sh /percorso/di/messina-sistema
# Serve Node con esbuild e react installati in messina-sistema (npm install).
set -euo pipefail
QUI="$(cd "$(dirname "$0")" && pwd)"; SIS="$(cd "${1:?serve il percorso di messina-sistema}" && pwd)"
for a in gestionale app portale negozio; do
  if [ -f "$SIS/apps/$a/config.js" ]; then echo "C'è apps/$a/config.js: toglilo, la prova va costruita senza chiavi" >&2; exit 1; fi
done
( cd "$SIS" && node siti/genera.mjs >/dev/null )
for a in gestionale app portale negozio; do ( cd "$SIS" && node "apps/$a/build.mjs" >/dev/null 2>&1 ) || { echo "Build di $a non riuscita" >&2; exit 1; }; done
python3 -I "$QUI/componi.py" "$SIS" "$QUI/../codice/index.html"
echo "Codice: messina-sistema $(git -C "$SIS" rev-parse --short HEAD)$(git -C "$SIS" diff --quiet || echo ' con modifiche non ancora su GitHub')"
