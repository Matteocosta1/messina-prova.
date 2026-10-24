# Passaggio di consegne · Programma Messina (mockup, codice, Home)

Aggiornato: 25 ottobre 2026, fine della chat precedente.
Questa cartella `lavori/` sta solo sul ramo `allineamento-mockup` di messina-prova.: niente è online.
Il Manuale Messina e gli agenti si fanno in un'altra chat («Manuale Messina»), non qui.

## Regole di Alessandro (valgono sempre)

- Fare solo quello che chiede. Le proposte si fanno, ma si aspetta il sì. Niente iniziative su grafica e suoni.
- Il design e la divisione in sezioni del **mockup approvato** non si cambiano. Un tasto o un riquadro nuovo: prima dire dove va e aspettare il sì.
- Ogni scelta tecnica o di struttura va chiesta e approvata da lui e da Matteo. Il programma vero deve essere identico al mockup.
- Prima di modificare il codice: dire cosa si fa e aspettare il sì. Una correzione semplice: solo quella.
- Mai togliere voci, sezioni o funzioni senza chiedere. Se un'istruzione si capisce in più modi, chiedere.
- Controllare che le cose funzionino davvero prima di dirle o scriverle. Gli errori si trovano da soli: lui non fa il collaudatore.
- Ogni schermata ottimizzata per telefoni, tablet e computer: controllare a 390, 820 e 1280 px.
- Etichette e titoli di una parola. Le caselle di ricerca dicono solo «Cerca».
- Diciture chiare, senza ripetizioni, capibili da tutti i lavoratori. Numeri e conti scritti a schermo.
- Non dargli ragione di riflesso: difendere le scelte o ammettere l'errore.
- Prima di aprire un servizio: dire se è gratis, a pagamento o in prova (e per quanto). Link diretti.
- Le chiavi segrete non passano mai in chat (solo l'URL di Supabase e la chiave `sb_publishable_`).
- **Per ora niente online**: si lavora sul ramo. main e la prova pubblicata non si toccano senza il suo ok.
- Quando si cambia il programma: codice in messina-sistema → ricostruire la prova → aggiornare i documenti (Dossier, Spiegazione, Domande e i loro PDF).
- «Non abbiamo limiti di tempo, vogliamo solo la scelta migliore.» «Massima competenza.»

## Dove sono le cose

| Cosa | Dove |
|---|---|
| **Mockup approvato** (il riferimento per tutto) | messina-prova. `main`: `index.html`, identico ad `archivio/prova-mockup-22-ottobre.html`. Online come artifact `https://claude.ai/artifact/Y4UwLkyLdWhNzY4MJBK3dz` |
| Codice del programma | messina-sistema, ramo `allineamento-mockup` (ultimo commit `1b39177`) |
| Prova costruita dal codice | messina-prova. ramo `allineamento-mockup`: `codice/index.html`, si rifà con `bash sorgenti/costruisci.sh /percorso/messina-sistema` |
| Dossier (Decisioni, Agenti, Manuale, Domande, Costi…) | Claude Docs `https://claude.ai/artifact/Q15pfUfX7VB7b3abed45da` |
| Stato dell'allineamento al mockup e «Da decidere» 1–50 | `lavori/collaudo/STATO.md` (più `COLLAUDO.md` e `COLLAUDO2.md`) |
| Prova dal codice vestita sul mockup (file mandato ad Alessandro) | `lavori/collaudo/prova-dal-codice.html` |
| **Esempio Home con Costi, Margine, Scadenze, Resoconto, Priorità** | `lavori/home/esempio-home.html`; versioni precedenti in `lavori/home/versioni/` (per tornare indietro) |
| Simulazione «JARVIS Messina» (giornata degli agenti) | `lavori/jarvis/jarvis-messina.html`, artifact `https://claude.ai/artifact/6tziRNr4tNSnBqMZPAh5fH` |
| PDF «JARVIS e agenti» e «Organizzazione e gestione» con i sorgenti HTML | `lavori/documenti/` |

## Esempio Home: dove siamo

È un esempio costruito sopra il mockup approvato, **non ancora approvato**. Contiene:
- **Conti**: costi del giorno e del mese (costi mensili divisi per i giorni lavorativi; data del mockup 19 ottobre), Margine di oggi e del mese calcolato sul fatturato, con tutti i conti scritti a schermo. Li vedono solo Direzione e Amministrazione.
- **Scadenze**: scadenzario delle fatture d'acquisto mese per mese (Ottobre dal 20 al 31, Novembre, Dicembre, Gennaio) con accanto gli incassi attesi; tasti Dettagli/Chiudi.
- **Resoconto**: elenco per reparto con «Da sistemare», «Da guardare», «Tutto a posto», calcolato dai problemi; «Dettagli» porta ai problemi del reparto.
- **Priorità**: pallini di urgenza con legenda e tasto «Apri».

Domande ancora aperte per Alessandro e Matteo:
- Scadenze su 4 o 6 mesi?
- Come dividere affitto e luce tra le due società?
- Gasolio del giorno reale (da dove arriva il dato)?
- Livelli di urgenza delle Priorità; titolo «Priorità» o «Urgenze»?
- Resoconto anche nella Home Corporation?

## Altre risposte che aspettiamo

- Voci della scheda **Decisioni** del Dossier (bloccanti: Chiudi mese, Nuovo lotto, Anagrafica fattura; Gasolio/Risparmio senza ottimizzatore; J7 Importa; badge «Simula»; proposta di grado).
- Elenco delle persone per gli **accessi** (login per persona: Matteo e Pier vedono tutto, Gianluca solo il commerciale…) e dove mettere la schermata «Accessi». Si imposta quando c'è il progetto Supabase.
- Anna e Luxiona: a chi assegnarle. Magazzino Trasporti che legge i lotti: sì o no.
- Le 17 domande sui preventivi.
- Data a scelta in Traffico (nascosta, Decisioni 16).

## Decisioni già prese da ricordare

- App per i dipendenti in **Swift** su iPhone (24 ottobre).
- **JARVIS Messina** coordina gli agenti: separato dal JARVIS personale di Alessandro, stesse funzioni, login per persona con credenziali create da un amministratore. La parte agenti la decide Alessandro.
- Bolle divise in automatico nell'ufficio bolle a chi ne ha meno da confermare (migrazione `20261023000100_bolle_assegnate.sql` con test `99f`).

## Controlli prima di consegnare

- `npm` build e `tsc` di gestionale, app, portale, negozio.
- Test del database: `bash supabase/tests/run.sh` su un Postgres 16 locale (socket `/tmp/pgtest`, porta 54329; in un contenitore nuovo va installato e avviato prima).
- Schermate a 390, 820 e 1280 px affiancate al mockup, nessuno scorrimento orizzontale.
- Workflow: `ci.yml` gira a ogni push (solo test e build); `prova.yml` solo su main (pubblica); `produzione.yml` e `backup.yml` a mano o programmati.
