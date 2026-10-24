# Allineamento al mockup · STATO

Aggiornato: 23 ottobre 2026, dopo il collaudo indipendente (COLLAUDO.md).
Commit: messina-sistema `1b39177` (secondo collaudo, sopra `6ff5ff7`, `8e956a7`, `f211ff0`), messina-prova. `ae19e6a` (sopra `2e54d8e`, `bb796eb`).
Ramo `allineamento-mockup` in tutti e due, su GitHub. main non toccato, niente pubblicato (parte solo ci.yml: test e build).
60 schermate × 3 larghezze (390, 820, 1280) = 180 immagini affiancate (mockup a sinistra, codice a destra), `<nome>-<larghezza>.png` in questa cartella.
**Nessuno scorrimento orizzontale** in nessuna (misurato dallo script su tutte e 180).
Controlli: build e tsc di gestionale, app, portale, negozio senza errori; `bash supabase/tests/run.sh` → «OK: migrazioni, seed e test passati»; `codice/index.html` ricostruito.

**Come le ho guardate.** Tutte e 180 aperte da me (affiancate a gruppi). Le schermate toccate dopo il primo giro di foto
(Fatturazione, Telecamere, Autisti, Telepass, giro, Portale, App autisti lista, Inventario, Schede, Telecamere Corporation, Negozio)
le ho rifatte e riguardate alle tre larghezze. Quando una tabella esce dal riquadro ho misurato larghezza minima e scorrimento
interno nel mockup e nel codice: dove dico «scorre come nel mockup» i numeri coincidono.
«Identica» = stessa impaginazione, ordine, etichette, testi, grafica. Restano diversi i **dati** (il mockup ha numeri scritti a mano,
il codice quelli del database di prova) e la data in alto.

## Come è montata la struttura del mockup (scelte tecniche, da rivedere)

- **Quattro app dallo stesso codice** (`apps/app`): la parte si sceglie con `window.MESSINA.parte`
  (`autisti`, `magazzino`, `presenze`, `corporation`) oppure con l'indirizzo (`?parte=autisti` o una cartella `/autisti/`).
  Con la parte fissata l'app apre direttamente quella schermata, senza barra in basso e senza scelta del profilo.
  Senza parte resta l'app unica di prima (barra Consegne · Magazzino · Entrate · Badge). È la strada che tocca meno logica:
  stessa build, stesso service worker, stesse funzioni. **Non ho cambiato `_pubblica.yml`**: per mettere online quattro app
  servono 4 progetti Cloudflare con il loro `config.js` (`parte: ...`) oppure 4 cartelle nello stesso progetto (vedi Da decidere).
- **Portale dentro Autotrasporti**: voce «Portale» del menu (stessa posizione del mockup). Dentro c'è il portale vero
  (`apps/portale`) rivestito come `portaleBody()` del mockup (barra «Area clienti» con Home, Spedizioni, Magazzino, Giacenze,
  Fatture). In Prova gira in una cornice con il cliente scelto (Snam / Econocom); online si apre l'indirizzo `portaleUrl`.
  Il programma `apps/portale` per i clienti veri resta com'era come accesso (login, password dimenticata).
- **J7** nel menu (ultima voce, solo Direzione): stessa impaginazione del mockup (Importa, Confronto, Parallelo) ma
  l'importazione da J7 nel codice vero non esiste ancora: «Importa» resta spento (Da decidere 42).
- **Prova** (`sorgenti/pagina.html`): stesso CSS del mockup, 10 voci con gli stessi nomi e ordine, Introduzione identica
  (stesso testo e stessi tasti, che aprono i programmi veri). Ogni parte entra da sola con un utente di esempio
  (`entraInProva`, vale solo senza chiavi): Autotrasporti = Direzione, Corporation = Direzione Corporation (profilo di prova
  nuovo `u-dirc`), App autisti = Autista 1, App magazzino = Magazziniere 1, App presenze = Christian (profilo di prova nuovo
  `u-chr`, collegato al dipendente Christian), App Corporation = Vendite. Le app stanno nel telefono con il riquadro
  spiegazione del mockup. Il «Da provare» del mockup cambia con la sezione aperta.
- In prova la Direzione ha anche il permesso dei riepiloghi presenze (come nel mockup, dove vede Presenze). Solo prova.

- **Cornici della prova come la pagina** (`sorgenti/pagina.html`, `comeLaPagina`): nel mockup telefono e portale stanno dentro la pagina,
  quindi le regole CSS «max-width» guardano la larghezza della finestra. Le cornici vere sono strette: la prova cancella dalle cornici
  (app e portale dentro Autotrasporti) le regole max-width che alla larghezza della finestra non valgono. Così a 820/1280 il telefono
  non usa più le regole da telefono vero (titoli, margini) e a 390 il portale ha la griglia 2×2. Solo prova, il programma non cambia.
- **Menu in alto della prova**: non scorre più da solo fino alla voce attiva (tolto `scrollIntoView`), come nel mockup.
- **Dati di prova completati** (solo `packages/dati/src/prova*.ts`): due Sprinter; zone a terra con bancali; missione S07 con gli articoli
  del mockup; Econocom indicato nei posti; bolla di entrata Snam da 4 colli; scansioni con foto delle telecamere; timbrature di tutto il mese
  (Ottobre e Riepiloghi), ferie/permessi l'anno (26 gg, 72 h, di esempio); due modifiche a mano di oggi; mese scorso chiuso (Fatturazione).
  **Finti, da sapere**: i km dei giri di domani sono scritti a mano come se li avesse calcolati l'ottimizzatore (che non è collegato), e
  in Fatturazione le «Consegne» delle fatture senza bolle collegate si contano dalle righe della tariffa base.
- **Correzioni del programma vero emerse dal collaudo** (valgono anche online): colonna Cliente dei Movimenti (il database scrive
  `dettagli.cliente_id`, il codice cercava il nome); «Modifiche a mano» contate sul giorno italiano e non UTC; Inventario «Tutti» senza
  venduti e smontati; tabelle Telepass e Satellitare in ordine di autista; foto delle telecamere che non si caricano mostrate come riquadro scuro.

## Esito per schermata (390 / 820 / 1280, guardate tutte)

| Schermata | Esito | Differenze che restano (non dati) |
|---|---|---|
| Introduzione | identica | |
| Autotrasporti · Home, Anomalie, sezione, Mail, Bolle | identiche | |
| Traffico | diversa | tolti dallo schermo «Gasolio stimato» e «Risparmio −14%»; nel riquadro nero tolta la frase «e ha messo le fermate … nell’ordine più corto per un camion (356 km invece di 412)»; «3 mezzi» senza «negli esempi»: Da decidere 43 |
| Pagina del giro | identica | Sposta attivo, km nella riga, «In magazzino» |
| Magazzino · Pianta, Controllo, Movimenti, Missioni, Storico | identiche | Controllo a 820: tabella da 820 px che scorre dentro il riquadro come nel mockup. Missioni: tolti Bloccati/Sblocca (Da decidere 19), «Apri l'app magazzino» e «Lancia» attivi |
| Giacenze | identica | |
| Clienti, scheda cliente | identiche | |
| Portale | identica | a 390 griglia 2×2 |
| Fatturazione | identica | «Invia» presente e attivo |
| Mezzi, Autisti, Telepass | identiche | Telepass e Satellitare in ordine di autista come nel mockup |
| Satellitare | diversa | tolto il riquadro «Gasolio a ottobre» (il mockup lo vuole in euro, il dato c'è solo in litri): Da decidere 47. «Litri/100 km» calcolato in tabella |
| Presenze · Oggi, Correzioni, Allarmi, Riepiloghi, Ferie, Ottobre | identiche | Ferie e Allarmi a 820/390 scorrono dentro il riquadro come nel mockup (900 e 980 px) |
| Telecamere (Autotrasporti e Corporation) | identiche | ordine e avvisi come nel mockup; tabella Foto scorre come nel mockup |
| J7 | diversa | «Importa» spento e senza «· N righe»: Da decidere 42 |
| App autisti · lista, fermata, Bolla, Non consegnato 1 e 2 | identiche | |
| App magazzino · home, Entrata, Uscita, Trasferisci, Missioni | identiche | Uscita apre direttamente la spedizione (scelta: Da decidere 38); Entrata con «Bolla Snam … · 4 colli», barra e «0 di 4 messi a posto» |
| App presenze · Badge | diversa | manca «Simula: un collega prova con il mio badge» e la guida della prova non lo cita più: Da decidere 39. QR con margine di 2 moduli come il mockup |
| App Corporation · Foto, Scheda | identiche | seriale letto, «Verificato su Lenovo», Nel DDT/Lavorato da noi, Cancellazione Certus, Batteria dal report |
| App Corporation · Grado | diversa | testo «Scegli il grado con un tocco.» invece di «Il programma propone B dal report…» e nessun difetto preselezionato (il servizio che legge il seriale non restituisce difetti: preselezionarne uno sarebbe inventato): Da decidere 44 |
| Corporation · Home, Mail, Lotti, Inventario (Tabella e Schede), Ordini, Stage Computer, Stage Cellulari | identiche | Inventario: icona telefono sulle schede dei telefoni (Da decidere 45) |
| Corporation · Ricambi | diversa (1 etichetta) | titolo «Computer smontati» (nel codice non esiste «da smontare»); sottotesto come il mockup, «non funzionanti, dischi già cancellati», calcolato: se un disco non ha il rapporto dice «dischi da cancellare» |
| Negozio · vetrina, prodotto, ricambi, carrello | identiche | |
| Sito Autotrasporti, Sito Corporation | identici | stesso HTML |
| Menu in alto, telefono finto (G1, G2) | identici | |

## Da decidere

(cosa · perché serve · proposta di posizione nel mockup)

### Struttura
1. **Da dove entrano i clienti veri nel Portale.** Il gestionale sta dietro Zero Trust ed è solo per i dipendenti; il Portale nel
   mockup è dentro Autotrasporti. Oggi il programma `apps/portale` ha il suo indirizzo e il suo login (con «Password dimenticata»).
   Proposta: i clienti continuano a entrare da `portale.[dominio]` (fuori da Zero Trust), con l'aspetto identico a quello che
   vede la Direzione dentro Autotrasporti; la voce «Portale» del gestionale apre lo stesso programma.
2. **Come la Direzione vede il portale «con gli occhi» di un cliente fuori dalla prova.** In prova si sceglie Snam o Econocom
   ed entra l'utente di esempio. Online serve una funzione nuova (vista del portale per un cliente scelto, senza la sua password).
   Proposta: chip Snam / Econocom come nel mockup + una RPC «portale come» solo per Direzione e Commerciale.
3. **Quattro app online**: 4 progetti Cloudflare (messina-app-autisti, -magazzino, -presenze, -corporation) con `config.js`
   `parte: ...`, oppure un progetto con 4 cartelle. Va cambiato `_pubblica.yml` (non toccato).
4. **Passaggio tra le due società** (rpc `mie_aziende`/`cambia_azienda`) per chi lavora in tutte e due: il mockup non ha il tasto.
   Proposta: chip «Autotrasporti / Corporation» sotto «MESSINA» nel menu laterale.
5. **«Esci»** dei gestionali e del portale: il mockup non lo ha. Proposta: ultima voce del menu laterale, dopo J7 / Telecamere.
6. **« · Prova»** nella data in alto: tolto (non c'è nel mockup).

### Sezioni e sotto-schede che il codice ha e il mockup no (raggiungibili solo da link)
7. **Preventivi** (Autotrasporti): preventivi del commerciale con approvazione della Direzione. Proposta: voce di menu dopo Clienti.
8. **Richieste** (Corporation): richieste delle aziende dal negozio («Per aziende»). Proposta: voce dopo Ordini.
9. **Presenze** (Corporation): presenze dei dipendenti della Corporation. Proposta: voce dopo Ricambi.
10. **Magazzino › Asset** (IMEI · cespite · utente, abbinamento dall'Excel, spedizione con bolla). Proposta: sotto-scheda dopo Missioni.
11. **Presenze › Telefoni** (approvazione del telefono del badge). Proposta: sotto-scheda dopo Ferie.

### Tasti, riquadri e colonne tolti dallo schermo (la funzione resta nel codice)
12. **Bolle › Completa**: campo per scrivere il dato mancante quando il cliente risponde. Serve per sbloccare la bolla senza Mail.
    Proposta: sotto il riquadro rosso «Manca», al posto del testo.
13. **Bolle › Non consegnate**: rimettere nei giri le spedizioni ferme (rpc `rimetti_in_giro`). Proposta: in Traffico, nel riquadro «Da assegnare».
14. **Bolle › Peso, Contrassegno, Valore della merce** nei dati della bolla. Proposta: altre caselle nella griglia della bolla.
15. **Bolle › prezzo voce per voce** (righe_bolla). Oggi si vede solo il totale come nel mockup. Proposta: aprire il totale con un tocco.
16. **Traffico › scelta del giorno** (Oggi / Domani / giorno lavorativo). Oggi si mostra il giorno dei giri pronti. Proposta: chip sopra la riga «Domani».
17. **Traffico pagina del giro › Chiudi d'ufficio** (consegnata / mancata senza l'app). È visibile solo a giro partito; c'era già prima. Proposta: lasciarlo dov'è (riga dei tasti della fermata) — da confermare.
18. **Magazzino › Missioni: campo per scrivere quale zona/scaffale/cliente.** Oggi «Lancia» rilancia la missione con lo stesso filtro di quella in corso (S07): per sceglierne un altro serve il campo. Proposta: campo «Cerca» piccolo accanto ai chip.
19. **Magazzino › Missioni › riquadro «Bloccati», riquadro rosso del posto bloccato (Manca / In più / Cosa è successo / Sblocca) e Rettifica.** Tolti dallo schermo (non sono nel mockup). Servono all'ufficio per chiudere i posti dove il magazzino non torna: senza, un posto bloccato resta bloccato. Le funzioni (`sblocca_posto`, `rettifica_posto`) restano. Proposta: sotto «Missione in corso», un riquadro rosso «Bloccati N» come gli altri avvisi del mockup; toccandolo si apre il posto con Manca / In più, campo «Cosa è successo» e i tasti «Sblocca» e «Rettifica».
20. **Clienti › Listino** base (lo cambia la Direzione). Proposta: tasto «Listino» a destra di «Nuovo cliente».
21. **Clienti › Anagrafica per la fattura** (P.IVA, PEC, codice destinatario, IVA, split payment, asset). Senza, la fattura elettronica viene scartata. Proposta: riquadro tra le quattro schede e «Tariffa base», più tasto «Anagrafica» accanto a «Contratto PDF».
22. **Fatturazione › Chiudi mese, scelta del mese, Esiti SdI, colonne Mese/Bolle/Imponibile/IVA/SdI.** «Chiudi mese» prepara le fatture dalle bolle: senza il tasto le fatture del mese non nascono. **Bloccante**. Proposta: «Chiudi mese» accanto a «Invia» e «Nuova»; colonna SdI dopo Stato.
23. **Mezzi › Portata** (kg e bancali, usata dai vincoli del giro). Proposta: colonna dopo Sponda.
24. **Telepass › Visto** sui passaggi da controllare. Proposta: tasto piccolo nella colonna Nota.
25. **Satellitare e Telecamere › riquadro dell'accordo art. 4 e della conservazione** (Permesso). Per legge, senza accordo non si raccoglie niente; qui la Direzione lo scrive. Proposta: riquadro sotto le quattro schede numeriche.
26. **Satellitare › Vista** e **Telecamere › Visto** sugli avvisi. Proposta: tasto piccolo accanto alla pill rossa.
27. **Presenze › Ferie › «L'anno» e «Cambia»** (quanto spetta l'anno e data di assunzione). Proposta: tasto «Cambia» in fondo alla riga.
28. **Corporation › Lotti: Nuovo lotto, riquadro del lotto (quadratura, documenti, Chiudi), colonne Caricati e Stato.** Senza «Nuovo» non si apre un lotto e l'app non sa dove caricare. **Bloccante**. Proposta: «Nuovo» accanto a «Carica fattura d'acquisto e DDT»; riquadro del lotto aprendo una riga.
29. **Corporation › Inventario: filtri per stato** (Disponibile, Da confermare, Resi, Fermo, Venduto) e **scheda del PC** (grado, prezzo, siti, Conferma, Vendi, Rimetti, Fermo). La scheda si apre toccando una riga (non visibile finché non si tocca). Proposta: filtri in una seconda riga di chip.
30. **Corporation › Ordini: Spedito (tracking) e Reso.** Proposta: nella colonna finale dopo «Etichetta spedizione».
31. **Corporation › Ricambi: Smonta un computer, Metti in vendita, Venduto.** Proposta: «Smonta» sopra la tabella; tasti nella colonna finale.
32. **Corporation › Stage Cellulari: tasti Fatto / Fatta / Chiudi** per segnare reset, sblocco e ticket. Proposta: nelle celle, come prima.
33. **Negozio › piede** con P.IVA, Privacy, Termini, Resi (obbligatorio per legge su un negozio online). Proposta: in fondo alla pagina, sotto i prodotti.
34. **Negozio › «Per aziende»** (modulo richiesta) apre una pagina che il mockup non ha (il mockup ha il tasto ma non la pagina).

### Blocco 7
35. (chiuso) **Bolle assegnate in automatico**: fatto dal coordinatore in `f211ff0` (a chi ne ha meno da confermare, regola nel database e nella prova).
36. **Etichette di una parola**: fatte dove il mockup ha una parola. Restano più parole dove il mockup stesso le ha
    (es. «Crea bolla da questa mail», «Prenota la riconsegna»).

### Altro trovato nelle app
37. **App autisti › Riserva** (consegna con riserva: collo mancante, danneggiato, in più) — c'era già. Non è nel mockup. Proposta: lasciarla dov'è, chip piccolo sotto la fotocamera.
38. **App magazzino › Uscita: scelta della spedizione.** Ora, come nel mockup, si apre direttamente la prima spedizione di oggi non ancora caricata. L'elenco delle spedizioni (c'era prima) è nel codice ma non si vede. Nel lavoro vero le spedizioni sono più di una: senza scelta il magazziniere carica nell'ordine del programma. Proposta: titolo «Spedizione Snam · Motrice …» toccabile, che apre l'elenco; oppure aprire da sola la spedizione del mezzo in baia.
39. **App presenze › «Simula: un collega prova con il mio badge».** Nel codice non c'è: il controllo vero lo fa il lettore all'ingresso (rpc `timbra_lettore`, che rifiuta e registra l'allarme). In un'app vera il tasto non ha senso; serve solo nella prova. Proposta: solo nella prova, tasto «Simula» sotto Entrata/Uscita che chiama `timbra_lettore` con il badge di Christian da un telefono non registrato (così l'allarme compare in Presenze › Allarmi).
40. **App Corporation › scelta del lotto** (più lotti aperti) e **PC / Telefono**. Proposta: chip sotto le icone dei passi.
41. (chiuso) Bolle assegnate in automatico: fatto dal coordinatore (`f211ff0`, migrazione `20261023000100`).

### Aggiunti dopo il collaudo del 23 ottobre
42. **J7 › Importa.** Nel mockup è nero e attivo, con «· N righe» nelle schede dei file. Nel codice l'importazione dei file di J7 non esiste: il tasto resta spento e le schede dicono «Da fare». Serve per portare clienti, inventario, bolle aperte e storico nel sistema nuovo. Proposta: dove è nel mockup; va scritta la funzione (caricamento file → tabelle di appoggio → controllo → copia), prima su un progetto di prova.
43. **Traffico › ottimizzatore per camion: Gasolio stimato e Risparmio.** Il codice ha la colonna `km_previsti` (la scrive l'ottimizzatore, HERE o TomTom, non ancora collegato). In prova i km dei giri di domani sono scritti a mano come se l'ottimizzatore li avesse calcolati, così si vedono «Ottimizzati per camion», Km totali e i km di ogni giro. **Gasolio stimato** resta «—» (serve un prezzo del gasolio e un consumo per mezzo, che non ci sono) e **Risparmio −14%** non c'è (serve il confronto con il percorso non ottimizzato, che solo l'ottimizzatore dà). Proposta: dove sono nel mockup, quando c'è l'ottimizzatore.
44. **App Corporation › grado proposto dal report.** Il mockup dice «Il programma propone B dal report. Cambialo con un tocco.» e preseleziona «Graffi sul coperchio». Nel codice nessuna funzione propone il grado: il grado parte da B e i difetti da vuoti. Il testo del mockup oggi direbbe il falso, quindi resta «Scegli il grado con un tocco.». Proposta: regola semplice (batteria dal report sotto 80% → C; altrimenti B) scritta nel database, poi il testo del mockup.
46. **App magazzino › Uscita › tasto «Bancale»** (merce in deposito che esce a bancale intero, rpc `esci_bancale`). Tolto: non è nel mockup. La funzione resta: il bancale si può leggere con «Scansiona il collo» o con la pistola. Proposta: chip «Collo / Bancale» sopra «Scansiona il collo», come in Entrata.
47. **Satellitare › «Gasolio a ottobre» in euro.** Nel mockup è in euro; nel database c'è solo il numero di litri delle carte carburante (colonna `litri`), non l'importo. Il riquadro è tolto dallo schermo. Proposta: dove è nel mockup, quando l'importazione delle carte carburante porta anche l'importo (o con un prezzo al litro scritto dalla Direzione).
48. **Corporation › Home › «Richieste» in «Da guardare oggi».** Le richieste delle aziende (dal negozio, «Per aziende») hanno una sezione che il menu del mockup non ha (vedi 8), quindi la voce è tolta. Proposta: tornano quando si decide il punto 8.
49. **Segnaposto del programma vero diventati «—»** dove il dato manca: tariffe delle giacenze, date del contratto, fatturazione del cliente. Restano i segnaposto che il mockup ha nello stesso punto: «[sconti, minimi, accordi particolari…]» (Eccezioni), «Garanzia [mesi]» e «Reso entro [giorni]» (negozio), «[n. ticket]», «[Cliente]» e «[dominio]» nelle mail, «[nome da comunicare]» del satellitare, il Resoconto del mattino, «i numeri qui sono di esempio» (Ferie) e la frase «è una prova» dell'Introduzione. Tolto «Spediamo entro [giorni]» dalla pagina di grazie del negozio (il mockup non ce l'ha). Da decidere: i valori veri di garanzia, reso e tempi di spedizione.
50. **QR del badge con margine di 2 moduli** come nel mockup (lo standard ne chiede 4). La maggior parte dei lettori lo legge lo stesso, ma va provato con il lettore vero all'ingresso; se non legge si torna a 4.
45. **Corporation › Inventario: icona del telefono.** Il mockup ha solo portatili; il codice può avere anche telefoni. Ho messo un'icona del telefono con lo stesso tratto di quella del portatile, solo sulle schede dei telefoni. Nella prova non ci sono più telefoni in inventario (come il mockup), quindi l'icona non si vede. Da confermare o togliere.


## Secondo collaudo (COLLAUDO2.md): schermate cambiate

Rifatte e guardate alle tre larghezze: t-traffico, t-satellitare, t-telecamere, c-telecamere, t-mag-controllo, t-mag-mov, t-portale,
t-giacenze, t-clienti, t-cliente, t-home, b-badge, m-home, k-grado, c-home, c-inv, c-inv-schede, c-stageTel, c-ricambi, n-home, n-prod.
- Traffico: riquadro nero con il testo del mockup (tolta la frase sull'ordine più corto), «Gasolio stimato» tolto.
- Satellitare: riquadro del gasolio in litri tolto.
- Telecamere (tutte e due): «Trasferisci»; nella colonna Posto il posto d'arrivo; in prova la foto della telecamera è un riquadro scuro come nel mockup; a 1280 la tabella è larga come nel mockup (655 px nel riquadro di 587, colonna Telecamera intera).
- Magazzino › Controllo: sotto 900 px il numero di bolla va a capo come «[n. bolla]» del mockup, così Esito resta leggibile (misurato: finisce a 806 px con il riquadro a 804; il mockup a 815).
- Movimenti: «Da → a» con partenza e arrivo nei dati di prova.
- Portale: 30 px sotto «Area clienti» come nel mockup.
- Badge: guida senza «Simula»; QR con il margine del mockup.
- App magazzino: riquadro Missione con il carattere del mockup (stessa altezza).
- Corporation Home: tolta la voce «Richieste».
- Stage Cellulari: i telefoni di prova sono ricevuti oggi (Ricevuti oggi 5).
- Ricambi: sottotesto del mockup, calcolato.
- Inventario e negozio: niente iPhone nei dati di prova.
- Segnaposto: vedi Da decidere 49.

## Non fatto e perché
- **J7 Importa**, **ottimizzatore** (Gasolio, Risparmio), **Simula** del badge, **grado proposto dal report**: le funzioni non esistono nel codice vero (Da decidere 39, 42, 43, 44).
- **Ricambi › «Computer da smontare»**: nel codice non c'è uno stato «da smontare» (si smonta e basta); il testo del mockup direbbe il falso.
- **Online**: `_pubblica.yml` pubblica ancora un'app sola e il portale a sé; per le 4 app serve decidere il punto 3.
- Dati: il mockup ha numeri finti scritti a mano; il codice mostra i dati del database di prova.
