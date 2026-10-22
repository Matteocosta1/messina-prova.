#!/usr/bin/env bash
# Ricostruisce index.html della prova: base.html + le modifiche in ordine (mod9 → mod12).
# I due siti vetrina dentro la prova vengono da messina-sistema: prima lì «node siti/genera.mjs».
# Uso: bash sorgenti/costruisci.sh /percorso/di/messina-sistema
set -euo pipefail
QUI="$(cd "$(dirname "$0")" && pwd)"; SIS="${1:?serve il percorso di messina-sistema}"
TMP="$(mktemp)"; cp "$QUI/base.html" "$TMP"
python3 "$QUI/mod9.py"  "$TMP" "$SIS/apps/sito-trasporti/anteprima.html" "$SIS/apps/sito-corporation/anteprima.html"
python3 "$QUI/mod10.py" "$TMP"
python3 "$QUI/mod11.py" "$TMP"
python3 "$QUI/mod12.py" "$TMP"
{ cat "$QUI/testa.html"; cat "$TMP"; echo '</html>'; } > "$QUI/../index.html"
rm "$TMP"; echo "index.html ricostruito"
