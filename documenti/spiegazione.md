# Il nuovo software Messina, spiegato passo per passo

<p class="by">19 ottobre 2026</p>

## Perché lo facciamo

Vogliamo un programma nostro che faccia da solo il lavoro ripetitivo, così le persone si occupano solo delle cose che contano. Oggi molte operazioni si fanno a mano: si copiano i dati dalle mail nelle bolle, si preparano i giri su carta, si ricontrollano le fatture una per una.

Il nuovo programma legge, prepara e propone. Una persona guarda e conferma con un tasto. Nessuno perde il posto: si toglie il lavoro noioso, non le persone.

Ci sono due società e quindi **due programmi separati**, uno per Messina Autotrasporti e uno per Messina Corporation. Non si mescolano: ognuno ha i suoi dati, le sue schermate e le sue persone.

Questo documento spiega cosa abbiamo progettato, un passaggio alla volta. In fondo trovate come provare la versione cliccabile. Le domande per voi sono in un documento a parte.

## Com'è fatto, in una pagina

Il progetto ha sette pezzi: due programmi per l'ufficio e cinque app semplici.

| Pezzo | Società | Chi lo usa | A cosa serve |
| --- | --- | --- | --- |
| Gestionale Autotrasporti | Messina Autotrasporti | Ufficio bolle, traffico, amministrazione, Direzione | Dalla mail d'ordine fino alla fattura |
| App autisti | Messina Autotrasporti | Autisti, sul telefono | Le consegne del giorno, la firma e la foto della bolla |
| App magazzino | Messina Autotrasporti | Magazzinieri | Entrata, uscita, spostamenti e inventario, tutto scansionato |
| App presenze | Tutti i dipendenti | Ognuno sul suo telefono | Il badge virtuale per timbrare entrata e uscita |
| Gestionale Corporation | Messina Corporation | Matteo, Pier, Simone, Manuel | Lotti di computer, magazzino, vendite, stage |
| App Corporation | Messina Corporation | Chi mette computer e telefoni in magazzino | Entrate: foto del seriale, scheda e bancale |
| Negozio online | Messina Corporation | I clienti, da internet | Comprare i nostri computer usati |

I due programmi usano la stessa tecnologia di base, ma i dati restano separati. Tutto è intestato a Messina: le società restano proprietarie dei dati e del programma.

C'è anche quello che chiamiamo **secondo cervello**. È un archivio di tutto quello che sa l'azienda: clienti, tariffe, regole, eccezioni, chi fa cosa. Il programma lo consulta prima di ogni proposta, come farebbe un dipendente esperto.

Lo stile è lo stesso ovunque: bianco e nero, pochi tasti, niente manuali. Funziona su computer, tablet e su qualsiasi telefono.

## Messina Autotrasporti, passo per passo

Ogni ordine che arriva diventa una spedizione e attraversa sei fasi, dalla mail del cliente alla fattura. Il programma segue ogni spedizione e sa sempre a che punto è.

### Il percorso di una spedizione

1. **Arriva la mail.** Il cliente scrive come oggi. Il programma legge la mail e prepara la bolla da solo, con indirizzi, colli, peso e accessori (sponda, piano, fascia oraria). Se manca un dato, il campo è in rosso.
2. **L'ufficio bolle conferma.** Ogni mattina il programma divide le bolle tra Christian, Gabriele e Alberto in base al carico, e fa girare i clienti così tutti sanno gestire tutti. Ognuno trova la sua lista pronta, controlla la bolla già compilata e preme Conferma. Se uno è assente, il suo lavoro va agli altri due.
3. **Il traffico prepara i giri.** Il programma prepara da solo i giri del giorno dopo, mezzo per mezzo. Mauro e Nelson aprono il giro che vogliono, cambiano quello che serve (ordine delle fermate, fasce orarie, accessori, una fermata passata a un altro mezzo) e premono «Conferma». Se dopo arriva una spedizione nuova, il programma la inserisce e chiede di nuovo la conferma.
4. **Si carica il mezzo.** Il magazziniere prende i colli dal loro posto e li scansiona mentre salgono sul camion. Se ne manca uno, o se finisce sul camion sbagliato, la spedizione non parte.
5. **L'autista consegna.** Dall'app sul telefono raccoglie la firma e fotografa la bolla firmata. Se la foto è sfocata, la consegna non si chiude finché non la rifà bene. Se la consegna non riesce, indica il motivo e cosa succede alla merce: nuova consegna già fissata, riprova nel giro, oppure rientro in magazzino in giacenza.
6. **Si fattura.** Ogni consegna diventa una riga di fattura con la tariffa giusta del cliente. Angela controlla e approva. Solo dopo la fattura parte verso Fatture in Cloud.

### Le schermate del programma

A sinistra c'è un menu con tredici voci, sempre nello stesso ordine.

**Regola per tutte le chiusure:** niente si chiude se i numeri non tornano. Una bolla con un dato mancante non si conferma, un posto della missione con pezzi mancanti o in più resta bloccato, i conteggi del mese non partono finché ci sono uscite da correggere. Ogni blocco manda un avviso all'ufficio e lo sblocca solo chi deve, scrivendo cosa è successo.

| Voce | Cosa si trova |
| --- | --- |
| Home | I numeri del giorno e il resoconto del mattino: consegne fatte, problemi, cose da guardare. Tre cifre di soldi: fatturato oggi (dalle bolle del giorno per le tariffe), fatturato del mese e incassato, che sale solo quando in Fatturazione si segna che il cliente ha pagato |
| Anomalie | Tutte le cose che non tornano, da ogni sezione, in un solo elenco: cosa, chi deve risolverla e un tasto per andare dove si risolve. In alto il totale, sotto una scheda per sezione (Magazzino, Missioni, Bolle, Presenze, Fatturazione, Telepass) con il suo numero: si entra e si risolvono una per una. È una prova: se non serve si toglie |
| Mail | La posta aziendale dentro il programma. Da ogni mail si può creare la bolla, rispondere con una bozza già scritta, inoltrare o passarla a un collega |
| Bolle | Le bolle da confermare, già divise tra Christian, Gabriele e Alberto |
| Traffico | I giri del giorno dopo, già pronti; ogni giro si apre grande e si modifica; un solo tasto «Conferma» |
| Magazzino | La pianta del capannone con ogni posto, la ricerca della merce, il controllo del giorno tra bolle e scansioni, entrate, uscite e inventari |
| Giacenze | La merce non consegnata tornata in magazzino: motivo, giorni di giacenza, riconsegna da prenotare o già prenotata |
| Clienti | L'elenco dei clienti. Dentro ogni cliente ci sono le tariffe voce per voce |
| Fatturazione | Le fatture pronte e quelle da controllare. Nessuna parte senza approvazione: si preme "Invia". Con "Nuova" se ne fa una a mano, senza aprire Fatture in Cloud. Quando il cliente paga si preme "Pagata" |
| Mezzi | I mezzi divisi per tipo (Sprinter, Furgoni, Motrici, Tre assi, Bilici), con sponda sì o no, autista, Telepass e scadenze |
| Autisti | Ogni autista cercabile per nome: mezzo e giro di oggi, orario di entrata, scadenze di patente e CQC. Stato: Partito, Rientrato o Assente |
| Telepass | Quanto spende ogni autista con il Telepass, giorno per giorno e mese per mese, con tutti i passaggi |
| Presenze | Chi è presente, ritardi, ferie, uscite non timbrate e i conteggi del mese per gli stipendi |

### Le tariffe dei clienti

Nella scheda di ogni cliente le tariffe sono divise in tre parti, ognuna con la data da cui vale.

- **Base:** a collo, a peso, a bancale, per zona, a viaggio o a giornata.
- **Accessori ed extra:** sponda, consegna al piano, attesa, fascia oraria, sabato, giacenza, riconsegna, stoccaggio.
- **Eccezioni:** sconti, minimi e accordi particolari che oggi conosce solo la Direzione.

Così il programma calcola la fattura giusta da solo, anche per i clienti con accordi speciali.

### Le giacenze

Quando una consegna non riesce e la merce torna a Lacchiarella, va in **giacenza**. Per noi la giacenza è un servizio a pagamento: il cliente paga la consegna tentata, il deposito e la nuova consegna quando la prenota.

1. L'autista, dall'app, sceglie "Torna in magazzino: giacenza" e scansiona i colli quando rientra.
2. In ufficio la spedizione compare nella voce **Giacenze**, con il motivo e i giorni passati in magazzino.
3. Da lì si chiede al cliente la data per la riconsegna, con una mail già pronta che avvisa anche del costo, oppure si prenota direttamente.
4. Consegna tentata, giacenza e riconsegna vanno da sole in fattura, con la tariffa di quel cliente.

I costi della giacenza li inseriamo appena avremo le vostre tabelle.

### Il Telepass

Nella voce **Telepass** si vede quanto spende ogni autista con il Telepass, giorno per giorno e mese per mese, e l'elenco di tutti i suoi passaggi: giorno, ora, tratta e importo. Ogni apparato è legato al suo mezzo, e dal giro del giorno il programma sa chi guidava.

I passaggi fuori orario o in giorni senza giro sono segnati in rosso, così si vede subito se qualcuno usa il Telepass per motivi suoi. La spesa va da sola nei costi dei mezzi. Prima di usarlo per valutare gli autisti va scritto nell'informativa e fatto vedere al consulente del lavoro.

### Il resoconto del mattino

Ogni mattina il programma prepara un riassunto della giornata prima: quante consegne, quante non riuscite, quanto si è fatturato, cosa è in ritardo. Funziona come un piccolo commercialista interno. Riporta anche le presenze del giorno prima.

## L'app per gli autisti

Ogni autista ha sul telefono un'app semplicissima, a prova di chi non è pratico: vede solo le sue consegne e pochi tasti grandi, tutti della stessa misura. La prima pagina di ogni fermata si legge dall'alto in basso, in tre blocchi numerati: **1 Colli**, **2 Accessori**, **3 Firma**, ognuno con il suo tasto «Conferma». Ogni blocco si accende quando è confermato quello sopra, e quelli fatti diventano verdi con la spunta. In fondo ci sono «Avanti», che porta alla pagina **4 Bolla**, e «Non Consegnato», sempre attivo: se la merce non scende dal camion non serve scansionare niente. Accanto all'indirizzo c'è una piccola icona per aprire il navigatore per camion.

1. **La mattina** apre l'app e trova l'elenco delle fermate del giorno, in ordine.
2. **A ogni fermata** vede indirizzo, cliente, colli e accessori già previsti dalla bolla, per esempio la sponda o la consegna al piano.
3. **Se serve un accessorio in più** all'ultimo momento, lo aggiunge con un tasto. Finisce da solo in fattura.
4. **Scansiona i colli** che scarica con il tasto della fotocamera, così nessuno resta sul camion per errore, e preme «Conferma». Negli accessori vede quelli della bolla e preme «Conferma».
5. **Fa firmare il cliente** sul telefono, con il dito, e preme «Conferma». Con «Avanti» passa alla pagina Bolla: prima fotografa la bolla, poi preme «Consegnato». Dopo la firma «Non Consegnato» non c'è più: se il cliente ha firmato, la merce l'ha presa. Si apre la fotocamera del telefono alla massima qualità e il programma misura davvero quanto è nitida la foto: se è mossa, sfocata o troppo scura la rifiuta e la consegna non si chiude finché l'autista non la rifà. La severità del controllo la regola l'ufficio: si parte morbidi e la si tara con le vostre bolle vere, così una foto fatta bene passa sempre. Nel programma vero controllerà anche che il numero della bolla sia quello giusto e che ci sia la firma.
6. **Se la consegna non riesce** preme «Non Consegnato» e sceglie il motivo con un tocco (cliente assente, indirizzo sbagliato, merce rifiutata). Poi dice cosa succede alla merce: c'è già una nuova consegna fissata, riprova più tardi nello stesso giro, oppure torna in magazzino in giacenza.

In ufficio si vede tutto in tempo reale. Siccome ogni consegna si chiude solo con la bolla fotografata bene, quando l'autista finisce il giro il giro è già chiuso: niente più ora in ufficio a fine giornata, e l'autista torna a casa prima. Il vecchio palmare resta acceso finché l'app non è stata provata bene, così i clienti non perdono il tracciamento.

## Il magazzino e la sua app

Ogni collo e ogni bancale che entra nel capannone viene scansionato e messo in un posto preciso. Se non è scansionato, per il programma non esiste.

### Ogni posto ha un indirizzo

Il capannone viene mappato tutto: ogni scaffale, ogni piano e ogni posizione ha un codice, per esempio **S03-2-1** (scaffale 3, piano 2, posto 1), con un'etichetta QR. A terra ci sono zone fisse: ricevimento, merce di passaggio (quella Apple che entra ed esce in giornata), giacenze, resi e un'area per ogni cliente in deposito.

### L'app magazzino: quattro tasti

1. **Entrata.** Si scansiona il bancale, poi il posto dove lo si mette. Il posto lo propone il programma: quello che esce spesso va in basso e vicino alle baie.
2. **Uscita.** L'app dice cosa prendere e da quale posto. Si scansiona ogni collo mentre sale sul camion. Se il collo è sbagliato suona subito, e la spedizione non può partire finché non ci sono tutti.
3. **Trasferisci.** Si scansiona il pezzo, poi il posto nuovo.
4. **Missioni.** Sono i controlli di uno scaffale o di una zona. Lo lancia l'ufficio e al magazziniere arriva come compito obbligatorio. Quando apre un posto vede l'elenco di quello che dovrebbe esserci e scansiona i pezzi nell'ordine che vuole: ognuno si spunta da solo, e se scansiona qualcosa che non è in elenco compare in rosso come "Extra". Se torna tutto, il posto si chiude da solo. Se manca qualcosa o c'è un pezzo in più il posto non si chiude: preme "Segnala", resta bloccato e va all'ufficio, che lo sblocca solo scrivendo cosa è successo. Tutto resta nello Storico. Ogni scansione si salva subito, quindi se arriva un camion può uscire e poi riprendere da dove era.

### Il magazzino nel gestionale

Nella voce **Magazzino** l'ufficio vede la pianta del capannone con i posti pieni e vuoti, cerca un seriale, una bolla o un cliente e scopre in che posto si trova. Vede anche tutte le entrate e le uscite del giorno, con chi le ha fatte, e gli inventari in corso.

La parte più importante è il **controllo del giorno**: per ogni bolla il programma confronta i colli scritti con quelli scansionati. Se tornano, la riga è verde. Se no, è rossa e dice quale collo manca, in quale bolla e chi l'ha gestita. Così non si perde nulla, e se qualcuno non scansiona bene si vede subito.

Tutto si può filtrare per cliente, e il portale che vedono Snam ed Econocom legge proprio da qui. L'app magazzino è dei Trasporti; la Corporation ha la sua app per i computer, separata.

### Contenuto e Storico

Toccando un posto si vede il **contenuto** del bancale: ogni articolo, la quantità e i codici. Si riempie con la pistola. Chi ha bisogno può correggerlo anche a mano, ma ogni modifica a mano resta segnata in rosso, con chi l'ha fatta e quando.

Nella scheda **Storico** c'è tutto quello che è successo in magazzino: ogni scansione, modifica e cancellazione, con ora, persona e posto. Niente si può cancellare. Se qualcosa non torna, il programma segnala le cose strane, per esempio un collo sparito dopo un certo passaggio o troppe modifiche a mano, e dice chi l'ha toccato per ultimo. Chi ha sbagliato lo decidete voi, dopo averci parlato: spesso è un errore e non una furbata.

## Le presenze, senza badge e senza IT

Il timbracartellino con le tessere e il servizio IT a pagamento vengono sostituiti dall'**app presenze**, sul telefono di ogni dipendente.

1. Ognuno ha nell'app il suo badge virtuale: un QR personale.
2. Arrivando preme «Entrata» e passa il telefono sul lettore all'ingresso; uscendo preme «Uscita». Si può entrare e uscire più volte nello stesso giorno.
3. Il QR cambia ogni 30 secondi, così una foto o uno screenshot mandato a un collega non serve a timbrare al posto di un altro.

Nel gestionale, alla voce **Presenze**, l'ufficio vede chi è presente, chi è in ritardo, ferie e malattia. Se qualcuno si dimentica di timbrare l'uscita, il programma suggerisce l'orario guardando l'ultima cosa fatta nelle app (l'ultima consegna, l'ultima scansione) e Angela conferma.

Dentro Presenze ci sono anche tre schede che vedono solo Angela e mamma:

- **Riepiloghi:** per ogni dipendente i ritardi e le uscite anticipate del mese, con i minuti e se sta migliorando o peggiorando. Così non serve controllare ogni mattina chi arriva.
- **Ferie:** ferie maturate, godute e da godere, e permessi spettanti, usati e rimasti. Il programma avvisa se qualcuno rischia di non godere le ferie nei tempi di legge.
- **Allarmi:** ogni badge funziona solo sul telefono del suo dipendente. Se qualcuno prova a timbrare con il badge di un collega da un altro telefono, con uno screenshot o con un badge già chiuso, il lettore non timbra e parte un allarme: di chi era il badge, da quale telefono, quando e a quale ingresso. Da lì si avvisa il dipendente.

Ogni dipendente nell'app vede solo i suoi orari, le sue ferie e i suoi permessi, mai quelli dei colleghi. Chi sa che i suoi orari sono registrati si corregge da solo, senza bisogno di richiami. Prima di partire i dipendenti firmano una breve informativa, che abbiamo già preparato e che va fatta controllare al consulente del lavoro.

A fine mese il programma prepara i conteggi per ognuno, secondo il suo contratto: ore ordinarie, straordinari, notturne, festive, ferie e malattia. Angela e mamma li trovano già pronti. La busta paga ufficiale, con contributi e tasse, resta al consulente del lavoro o al commercialista: decidiamo insieme se il programma deve preparare anche quella parte.

## Satellitare e telecamere

**Satellitare.** I mezzi hanno già il satellitare: il programma si collega a quello, senza montare niente di nuovo. Ogni mezzo ha il suo autista fisso. Ogni giorno il percorso fatto viene confrontato con il giro previsto: una strada parallela lì vicino non conta, una deviazione lontana o una sosta fuori dalle fermate sì, con ora, luogo e durata. Il programma controlla anche gasolio e chilometri, rifornimenti lontani dal giro, motore acceso da fermo e Telepass. Quello che non torna finisce in Anomalie.

**Telecamere.** Una sola voce, uguale nei due programmi, perché il capannone è uno. La vedete solo voi e i vostri figli: il commercialista vede i numeri ma non le immagini. Dentro ci sono le immagini dal vivo, gli avvisi della notte con la foto (che arrivano anche sul telefono) e una foto salvata a ogni scansione del magazzino. Se un collo manca, si apre il movimento e si vede chi l'ha toccato. Le registrazioni restano in azienda, su una rete separata e mai aperta su internet.

## Messina Corporation, passo per passo

Ogni computer passa da sei tappe, da quando arriva per la formattazione a quando viene venduto. Oggi in magazzino ci sono tra 2.000 e 4.000 dispositivi, e il programma serve a sapere sempre dove sono, quanto valgono e quanto ci hanno fatto guadagnare.

### Il percorso di un computer

1. **Stage.** I computer dei clienti (Accenture, Econocom) vengono cancellati in modo sicuro con Certus, testati e caricati su Arte, a bancali da 70.
2. **Valutazione.** Mentre si lavora ogni computer, si annotano il grado (come è tenuto), i danni e l'etichetta. Si fa anche se il lotto poi lo compra qualcun altro.
3. **Acquisto del lotto.** Quando vinciamo un lotto arrivano fattura e DDT. Il programma confronta i seriali del DDT con quelli che abbiamo già lavorato e segnala cosa manca o non torna.
4. **Carico in magazzino.** Con l'app si fotografa il seriale, il programma trova la scheda del computer sul sito del marchio e propone grado e prezzo. Si stampa un'etichetta Messina con QR. Entra in inventario solo con il via libera di Matteo.
5. **Vendita.** Lo stesso computer viene pubblicato su più siti insieme. Quando si vende su uno, sparisce da tutti gli altri, così non si vende mai due volte.
6. **Spedizione e conti.** L'ordine dice quale computer prendere e da quale scaffale. Ogni vendita aggiorna i conti del suo lotto.

### Le schermate del programma

| Voce | Cosa si trova |
| --- | --- |
| Home | Dispositivi in magazzino, venduti, ordini da spedire, incassato di oggi e del mese, e il resoconto dello stage di oggi e del mese: ricevuti, formattati, in corso, falliti, messi in vendita |
| Mail | La posta divisa in Vendite, Lotti, Stage. Il tasto principale cambia con la mail: carica il DDT, apri l'ordine, manda il riepilogo a Econocom |
| Lotti | Ogni lotto con data, pezzi, costo, pezzi venduti, **euro già incassati** e percentuale recuperata. L'incassato sale a ogni vendita |
| Inventario | Tutti i computer, in una tabella tipo Excel (si apre così) oppure a schede: seriale, marchio, modello, processore, scheda video, memoria, disco, grado, difetti, lotto, bancale, posto, costo, prezzo, stato (Disponibile, Venduto, Fermo, Reso), i siti dove è pubblicato, giorni in magazzino |
| Ordini | Gli ordini da tutti i siti, con colonne separate per marchio, modello e grado, lo scaffale e l'etichetta di spedizione |
| Stage Computer | Il banco da 60 postazioni in tempo reale, computer ricevuti e formattati, interruzioni, licenze Certus |
| Stage Cellulari | Il lavoro di Manuel sui telefoni: IMEI, marchio, modello, cliente, ticket, reset, sblocco su Habble (account iCloud/Google e MDM). Ogni telefono ha uno stato di una parola: Reset, Sblocco, Ticket, Chiuso |

### Come si capisce se un lotto conviene

Oggi un computer ci costa in media circa 60 euro, su lotti grandi e misti. Il programma divide il costo del lotto tra i computer in base al loro valore di mercato. Così si vede, lotto per lotto, quanto abbiamo speso, quanto abbiamo già incassato e quando siamo rientrati.

### Gradi e prezzi

I gradi sono **A, B, C e D**, scritti così anche nel negozio. A, B e C vanno da quasi nuovo a segni evidenti d'uso; il D è un computer che funziona al 100% ma ha la scocca rotta o danni estetici importanti. Tutti e quattro sono testati e garantiti.

I computer che non funzionano non si vendono interi: si smontano e si vendono come **ricambi**, ognuno legato al computer e al lotto da cui viene, così anche quell'incasso conta nel recupero del lotto. Un disco si vende solo dopo la cancellazione certificata. Il programma propone il prezzo guardando il mercato, ma lo decide sempre Matteo. Ogni computer ha un prezzo minimo sotto cui non si scende, che copre commissioni, spedizione, garanzia e resi.

I siti dove vendere sono Back Market, Refurbed, eBay, Amazon, Subito, Vinted e il nostro negozio, tutti collegati allo stesso magazzino.

## L'app per caricare i computer

Sui computer non ci sono più codici a barre, quindi si carica tutto **fotografando l'etichetta del seriale** con il telefono.

1. Si fotografa il seriale sotto il computer.
2. Il programma cerca il modello sul sito del marchio (per ora Lenovo, HP, Dell e Apple) e riempie la scheda da solo: processore, memoria, disco, schermo.
3. Controlla che quel seriale sia nel DDT del lotto.
4. Si scelgono grado e difetti con pochi tocchi e si scattano le foto per l'annuncio.
5. Il programma propone il prezzo, con il minimo sotto cui non scendere.
6. Si scelgono i siti dove pubblicarlo. Nell'ultima pagina ci sono tre tasti uguali uno sopra l'altro: «Scansiona» per leggere l'etichetta del bancale su cui va, «Nuovo» per crearne uno, e sotto «Conferma», spento finché il bancale non è scelto. Con «Nuovo» si apre una pagina a parte: si stampa l'etichetta del bancale con il QR, lo si porta nel posto libero proposto e si scansiona lo scaffale, così finisce nella pianta del magazzino. Poi si torna indietro e «Conferma» si accende.

Alla fine si preme **Conferma**. In pochi secondi il computer è in magazzino e in vendita, senza scrivere niente a mano: è già nell'inventario e nell'Excel con il suo bancale e il suo posto. L'app si chiama **App Corporation**, la funzione per caricare è **Entrate**, e dentro non ha titoli, solo icone in alto (foto, scheda, grado, prezzo, bancale) che dicono a che punto sei.

Il magazzino è uno solo per tutto il capannone, con gli stessi scaffali. Nel gestionale dei Trasporti la Corporation è un cliente come gli altri; nel gestionale della Corporation si vedono solo i suoi bancali.

## Il negozio online

Il negozio per ora si chiama solo **Messina Corporation**, finché non decidiamo un nome definitivo.

- La pagina principale mostra i computer, con i filtri per marchio: Lenovo, HP, Dell, Apple.
- Aprendo un computer si sceglie il grado (A, B, C, D). Ogni grado ha il suo prezzo, come su Back Market. Sotto c'è la scheda tecnica completa: generazione, processore, scheda grafica, RAM, disco, schermo, batteria e il resto.
- Una sezione a parte, **Ricambi**, vende i pezzi smontati.
- Si aggiunge al carrello e si compra.

I nostri computer sono **usati**, non ricondizionati. Ricondizionato vuol dire rimesso insieme con pezzi di altri computer, e non è il nostro caso. Sul sito non ci sono slogan: solo il nome e i prodotti.

## Le garanzie che ci siamo dati

Abbiamo deciso alcune regole fisse per non correre rischi.

- **J7 non si tocca.** Il nuovo programma lavora accanto a J7 per 1 o 2 mesi. Ogni giorno si confrontano i risultati. J7 si spegne solo quando non ci sono più differenze, e resta comunque consultabile in archivio.
- **Le fatture elettroniche cambiano solo a inizio mese**, con il commercialista avvisato prima, così la numerazione non salta.
- **Il programma non muove mai soldi da solo.** Prepara fatture e conti, ma bonifici e pagamenti restano a voi.
- **All'inizio ogni proposta la controlla una persona.** Solo quando il programma non sbaglia per settimane, i casi normali si confermano da soli. Le persone restano sulle eccezioni.
- **Impara dagli archivi, non dai dipendenti.** Mail, bolle, fatture e listini già esistenti gli insegnano come lavoriamo, senza togliere tempo a nessuno.
- **Sicurezza.** Tutto è intestato a Messina, con copie di sicurezza continue. Le regole sono nel documento "Sicurezza informatica Messina".
- **Si parte dai Trasporti.** Prima bolle, traffico, app autisti e fatturazione, poi la Corporation.

## Come provare la versione cliccabile

Abbiamo preparato una prova che si usa come il programma vero, ma con dati di esempio: potete cliccare tutto senza rompere niente. Si apre da qualsiasi telefono o computer, senza installare nulla.

**Link:** [matteocosta1.github.io/messina-prova.](https://matteocosta1.github.io/messina-prova./)

In alto ci sono le schede per passare da un pezzo all'altro. In ogni pagina una riga "Da provare" suggerisce cosa toccare. Vi consigliamo questo giro, una ventina di minuti in tutto:

1. **Autotrasporti.** Aprite Mail e create una bolla da una mail. Andate in Bolle e confermatela. In Clienti aprite un cliente e guardate le sue tariffe. In Giacenze prenotate una riconsegna scegliendo giorno e ora. In Magazzino toccate uno scaffale: per ogni posto vedete gli Articoli e la data di Arrivo. In Traffico leggete cosa ha fatto il programma, aprite un giro e provate a cambiarlo, poi premete «Conferma». Guardate anche **Satellitare** e **Telecamere**. Poi aprite **Portale**: è quello che vedono i clienti di Messina Autotrasporti. Scegliete Snam o Econocom e girate tra Spedizioni, Magazzino, Giacenze e Fatture.
2. **App autisti.** Aprite una fermata e seguite i blocchi dall'alto, ognuno con il suo «Conferma»: colli con la fotocamera, accessori, firma del cliente con il dito. Poi «Avanti» e la foto della bolla: dal telefono si apre la fotocamera vera. Fate una foto mossa e vedrete che viene rifiutata, poi una ferma e premete «Consegnato». Su un'altra fermata premete subito «Non Consegnato» e mandate la merce in giacenza: la ritrovate nel gestionale, in Giacenze.
3. **App magazzino.** Fate un'Entrata: scegliete «Bancale» (bancale e posto) o «Collo» (scatola e bancale su cui va). In Uscita scansionate i colli: il terzo è sbagliato apposta e l'app suona, e la spedizione parte solo a 4 su 4. Poi aprite la missione e un posto: scansionate finché si chiude da solo. Nel quarto posto manca un pezzo e ce n'è uno in più: non si chiude, premete "Segnala". Poi in Autotrasporti › Anomalie lo ritrovate, e in Magazzino › Missioni lo sbloccate scrivendo cosa è successo.
4. **App presenze.** Guardate il QR che cambia ogni 30 secondi e premete «Entrata» e «Uscita». Poi nel gestionale aprite Presenze e guardate Riepiloghi e Ferie.
5. **Corporation.** In Lotti guardate quanto ha incassato ogni lotto. In Inventario passate alla vista tabella. Aprite Ordini, Stage e Ricambi.
6. **App Corporation.** Simulate la foto del seriale, guardate la scheda che si riempie da sola, poi nell'ultima pagina premete «Nuovo»: stampate l'etichetta, scansionate il posto e tornate a «Conferma».
7. **Negozio.** Scegliete un computer, cambiate il grado e guardate come cambia il prezzo; sotto c'è la scheda tecnica. In alto trovate anche Ricambi.
8. **Sito Trasporti.** È il sito pubblico, quello che trova chi vi cerca su internet. In fondo compilate «Chiedi un preventivo» e inviate: la richiesta compare in Autotrasporti › Mail, cartella Clienti, con la risposta già preparata.
9. **Sito Corporation.** Premete «Negozio» in alto: si apre il negozio online. Oppure compilate «Valuta un lotto»: arriva in Corporation › Mail, cartella Lotti.

I nomi e i numeri sono solo di esempio. Servono a far capire come funzionerebbe.

## Cosa succede adesso

Il disegno delle schermate è pronto. Per costruire il programma vero ci servono le vostre risposte e alcuni documenti veri.

1. **Voi** leggete questo documento, provate il link e rispondete alle domande nel documento "Domande per papà e mamma".
2. **Noi** sistemiamo le schermate con le vostre osservazioni.
3. **Si costruisce** il programma vero, partendo dai Trasporti, con le fondamenta e la sicurezza.
4. **Si prova in parallelo** a J7 per 1 o 2 mesi, senza cambiare niente nel lavoro di tutti i giorni.
5. **Si passa al nuovo** solo quando i conti tornano al centesimo.

Se qualcosa non è chiaro, o se vedete qualcosa che nel lavoro vero non funzionerebbe, ditecelo: è proprio quello che ci serve.
