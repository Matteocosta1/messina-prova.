# Prova del programma Messina

La prova cliccabile di tutto il sistema Messina: gestionali Autotrasporti e Corporation, app autisti, magazzino,
presenze e Corporation, negozio online, portale clienti, siti di Messina Autotrasporti e Messina Corporation.
Dati di esempio: niente arriva a clienti o colleghi.

- **Aprirla:** https://matteocosta1.github.io/messina-prova./ (oppure l'artifact «Prova programma Messina»).
- **`index.html`** è la prova pubblicata. Non si modifica a mano: si ricostruisce.
- **`sorgenti/`**: `base.html` (versione del 20 ottobre) più le modifiche in ordine, `mod9.py` → `mod12.py`.
  Una modifica nuova si scrive come `mod13.py` (stesso stile: sostituzioni esatte, si ferma se un testo non c'è),
  si aggiunge a `costruisci.sh` e si ricostruisce:

      bash sorgenti/costruisci.sh /percorso/di/messina-sistema

  I due siti vetrina dentro la prova vengono da `messina-sistema` (`node siti/genera.mjs` lì, prima).
  Verificato il 22 ottobre 2026: la ricostruzione dà un `index.html` identico a quello pubblicato.
- **`documenti/`**: Spiegazione del progetto, Domande per papà e mamma, Informativa presenze (testi `.md` e PDF)
  e il PDF del Dossier. PDF: `python3 documenti/build.py documenti spiegazione` poi
  `node documenti/pdf.js "$PWD/documenti" spiegazione "Messina - Spiegazione del progetto.pdf"` (serve Playwright).
