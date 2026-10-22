# Prova del programma Messina

La prova di tutto il sistema Messina, fatta con il **programma vero** di `messina-sistema` in modalità Prova:
gestionali Autotrasporti e Corporation, app (autisti, magazzino, Entrate, badge), portale clienti, negozio online
e siti di Messina Autotrasporti e Messina Corporation. Dati di esempio: niente arriva a clienti o colleghi.

- **Aprirla:** https://matteocosta1.github.io/messina-prova./ (oppure l'artifact «Prova programma Messina»): è il mockup approvato.
- **Un solo database simulato per tutti i pannelli.** Ogni programma, dopo una modifica, manda i dati alla pagina,
  che li gira agli altri: una consegna fatta nell'app si vede nel gestionale e nel portale, un acquisto del negozio
  arriva in Corporation › Ordini, un modulo del sito arriva nella Mail. «Ricomincia» (Introduzione) riparte da capo.
- **Servizi simulati come se fossero collegati:** mail Outlook, «Crea bolla» da una mail, Fatture in Cloud (numero
  e invio allo SdI), pagamento Stripe (ordine, vendita, computer venduto), moduli dei siti, etichetta, lettore presenze.
  Il codice delle simulazioni è in `messina-sistema/packages/dati/src/prova*.ts` e vale solo senza chiavi.
- **`index.html` è il mockup approvato** (identico ad `archivio/prova-mockup-22-ottobre.html`): è quello che si apre dal link e si mostra in azienda. Dal 23 ottobre comanda lui: il programma vero deve avere le stesse sezioni, la stessa divisione e la stessa grafica.
- **`codice/index.html`**: la prova costruita dal codice vero di `messina-sistema` (un solo database simulato). Non si modifica a mano:

      bash sorgenti/costruisci.sh /percorso/di/messina-sistema

  Lo script costruisce i quattro programmi e i due siti (serve `npm install` in `messina-sistema`) e li mette dentro
  `sorgenti/pagina.html` con `sorgenti/componi.py`. Si rifiuta di partire se un programma ha un `config.js` con le chiavi.
  Online: https://matteocosta1.github.io/messina-prova./codice/
- **`archivio/`**: la prova precedente, scritta a mano sul mockup approvato (`prova-mockup-22-ottobre.html`), con i
  suoi sorgenti (`base.html` + `mod9.py` → `mod12.py`). Non si aggiorna più: resta come riferimento.
- **`documenti/`**: Spiegazione del progetto, Domande per papà e mamma, Informativa presenze (testi `.md` e PDF)
  e il PDF del Dossier. PDF: `python3 documenti/build.py documenti spiegazione` poi
  `node documenti/pdf.js "$PWD/documenti" spiegazione "Messina - Spiegazione del progetto.pdf"` (serve Playwright).
