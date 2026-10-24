# COLLAUDO 2: mockup (sinistra) e programma vero (destra)

Collaudo indipendente del 23/10/2026. Non ho modificato niente: ho solo guardato le immagini.
Non conto come differenze i numeri, i nomi, la data in alto, la lunghezza delle liste e lo stato del momento (per esempio un'animazione a metà o una timbratura già fatta).

## 1. Tabella

| Schermata | 390 | 820 | 1280 | Esito | Differenze precise |
|---|---|---|---|---|---|
| intro | ✔ | ✔ | ✔ | Identica | — (resta la frase «Questa è una prova da toccare… i dati sono di esempio») |
| a-bolla | ✔ | ✔ | ✔ | Identica | — |
| a-fermata | ✔ | ✔ | ✔ | Identica* | «4 bancali da scaricare» → «4 colli da scaricare» (probabilmente arriva dalla bolla) |
| a-lista | ✔ | ✔ | ✔ | Identica | — (Motrice → Furgone è un dato) |
| a-mancata | ✔ | ✔ | ✔ | Identica | — |
| a-merce | ✔ | ✔ | ✔ | Identica | — |
| b-badge | ✔ | ✔ | ✔ | **Differenze** | Manca «Simula» (dichiarato). **Non dichiarato:** la guida a sinistra, al punto 3, dice ancora «Prova "Simula: un collega prova con il mio badge"», ma quel tasto non c'è più. Il QR è un po' più piccolo dentro il suo riquadro. |
| k-grado | ✔ | ✔ | ✔ | **Differenze** | Testo guida diverso (dichiarato). **Non dichiarato:** nel mockup il difetto «Graffi sul coperchio» è già selezionato (nero); nel programma non è selezionato nessun difetto. |
| k-scan | ✔ | ✔ | ✔ | Identica | — |
| k-scheda | ✔ | ✔ | ✔ | Identica | — |
| m-home | ✔ | ✔ | ✔ | **Differenze** | Il riquadro rosso «Missione · Scaffale S07» ha il titolo più grande ed è più alto di circa 8 px, quindi i 4 tasti sotto scendono. |
| m-entrata | ✔ | ✔ | ✔ | Identica | — (n. bolla e «colli» sono dati) |
| m-missioni | ✔ | ✔ | ✔ | Identica | — |
| m-sposta | ✔ | ✔ | ✔ | Identica | — |
| m-uscita | ✔ | ✔ | ✔ | Identica | — |
| c-home | ✔ | ✔ | ✔ | Identica* | La lista «Da guardare oggi» ha 8 voci invece di 4 (lunghezza lista). Una voce porta l'etichetta «Richieste», che non è tra le sezioni del menu. |
| c-mail | ✔ | ✔ | ✔ | Identica | — |
| c-lotti | ✔ | ✔ | ✔ | Identica | — |
| c-inv | ✔ | ✔ | ✔ | Identica* | Fra i dati c'è un record di prova «35PROVA00001 · Apple iPhone 13» dentro l'inventario computer. A 820 la tabella finisce pulita su «Disco»: non si vede la colonna tagliata che nel mockup fa capire che si può scorrere. |
| c-inv-schede | ✔ | ✔ | ✔ | Identica* | Si vede la stessa scheda di prova «iPhone 13 · 35PROVA00001». |
| c-ordini | ✔ | ✔ | ✔ | Identica | — («Annullato» è uno stato) |
| c-stage | ✔ | ✔ | ✔ | Identica | — |
| c-stageTel | ✔ | ✔ | ✔ | Identica* | A 1280 c'è scritto «Ricevuti oggi 0» ma la tabella mostra 5 telefoni: i dati non sono coerenti. |
| c-ricambi | ✔ | ✔ | ✔ | **Differenze** | «Computer smontati» (dichiarato). **Non dichiarato:** cambia anche il sottotesto, da «non funzionanti, dischi già cancellati» a «non si vendono più interi». |
| c-telecamere | ✔ | ✔ | ✔ | **Differenze** | Nella colonna Movimento c'è «Trasferimento» invece di «Trasferisci». A 820 le miniature delle foto sono riquadri bianchi vuoti con un trattino invece delle foto scure. A 1280 la tabella «Foto delle scansioni» esce dal riquadro: la colonna Telecamera è tagliata («Telecame», «Baie di c», «Corsia S»), mentre nel mockup si legge intera. |
| n-home | ✔ | ✔ | ✔ | Identica | — (prezzi e specifiche sono dati) |
| n-prod | ✔ | ✔ | ✔ | Identica | — (i valori della scheda tecnica sono più corti, ma sono dati). Sul negozio pubblico restano «Garanzia [mesi]» e «Reso entro [giorni]». |
| n-ricambi | ✔ | ✔ | ✔ | Identica | — |
| n-carrello | ✔ | ✔ | ✔ | Identica | — |
| sitoC | ✔ | ✔ | ✔ | Identica | — (0% contro 100% è solo il momento dell'animazione) |
| sitoT | ✔ | ✔ | ✔ | Identica | — |
| t-home | ✔ | ✔ | ✔ | Identica* | Il «Resoconto del mattino» è lo stesso testo inventato del mockup («Ieri 1.198 consegne…») e non torna con i numeri veri. |
| t-mail | ✔ | ✔ | ✔ | Identica* | Le mail sono quelle finte del mockup, con «[Cliente]», «Officina [nome]» e «[dominio]». |
| t-bolle | ✔ | ✔ | ✔ | Identica | — |
| t-traffico | ✔ | ✔ | ✔ | **Differenze** | Manca «Risparmio» (dichiarato). **Dichiarazione inesatta:** «Gasolio stimato» non è stato tolto, c'è ancora con il valore «—». **Non dichiarato:** il testo fisso del riquadro nero è stato riscritto. Mockup: «…guardando portata, sponda e fasce orarie dei clienti, e ha messo le fermate … nell'ordine più corto per un camion (356 km invece di 412)». Programma: «…alle 03:50: … per zona e … in ordine di fascia oraria (356 km)». Anche «3 mezzi negli esempi» è diventato «3 mezzi». |
| t-giro | ✔ | ✔ | ✔ | Identica | — |
| t-anomalie | ✔ | ✔ | ✔ | Identica | — |
| t-anomalie-sez | ✔ | ✔ | ✔ | Identica | — |
| t-mag-pianta | ✔ | ✔ | ✔ | Identica | — (all'apertura è selezionato S01 invece di S04: è uno stato) |
| t-mag-controllo | ✔ | ✔ | ✔ | **Differenze** | A 820 la colonna «Esito» è tagliata a destra («Manca 1 collo rispett…», «da ricontar…»): la tabella esce dal riquadro, mentre nel mockup si legge intera. |
| t-mag-mov | ✔ | ✔ | ✔ | Identica* | La colonna «Da → a» spesso mostra un solo posto («S03-2-2», «RIC», «—») invece di «partenza → arrivo». |
| t-mag-inv | ✔ | ✔ | ✔ | Identica | — |
| t-mag-storico | ✔ | ✔ | ✔ | Identica | — |
| t-giacenze | ✔ | ✔ | ✔ | Identica* | Restano visibili «€ [tariffa]» per Giacenza e Riconsegna. |
| t-clienti | ✔ | ✔ | ✔ | Identica* | «Contratto fino al [data]» è ancora un segnaposto. |
| t-cliente | ✔ | ✔ | ✔ | Identica* | Resta «[sconti, minimi, accordi particolari…]». |
| t-portale | ✔ | ✔ | ✔ | **Differenze** (lievi) | Lo spazio tra il riquadro «Area clienti» e le schede dei numeri è circa la metà (~14 px contro ~30 px), a tutte le larghezze. |
| t-fatture | ✔ | ✔ | ✔ | Identica | — («Inviata» e il tasto «Pagata» sono stati previsti) |
| t-mezzi | ✔ | ✔ | ✔ | Identica | — |
| t-autisti | ✔ | ✔ | ✔ | Identica | — |
| t-telepass | ✔ | ✔ | ✔ | Identica | — |
| t-satellitare | ✔ | ✔ | ✔ | **Differenze** | «Gasolio a ottobre» mostra «89,7 l» (litri) dove il mockup ha «€ [importo]» (euro): è cambiata l'unità di misura. |
| t-pres-oggi | ✔ | ✔ | ✔ | Identica | — |
| t-pres-mese | ✔ | ✔ | ✔ | Identica | — («Prepara» è spento come nel mockup) |
| t-pres-riep | ✔ | ✔ | ✔ | Identica | — |
| t-pres-allarmi | ✔ | ✔ | ✔ | Identica | — |
| t-pres-ferie | ✔ | ✔ | ✔ | Identica* | Resta la frase «i numeri qui sono di esempio…». |
| t-pres-fix | ✔ | ✔ | ✔ | Identica | — |
| t-telecamere | ✔ | ✔ | ✔ | **Differenze** | Le stesse di c-telecamere: «Trasferimento», miniature vuote a 820, colonna Telecamera tagliata a 1280. |
| t-j7 | ✔ | ✔ | ✔ | Identica (salvo dichiarato) | «Importa» spento (dichiarato) e nient'altro. |

\* Identica: impaginazione uguale al mockup, ma c'è un problema nei contenuti che un cliente noterebbe (vedi punto 2).

**Differenze dichiarate, verificate:**
- **J7:** è vero, cambia solo «Importa» spento.
- **Badge, Grado, Ricambi, Traffico:** il cambio dichiarato c'è, ma non è l'unico (vedi tabella).

## 2. Cosa noterebbe il cliente, dal più grave

1. **Traffico: il riquadro nero con la spiegazione è stato riscritto.** Non dice più «ordine più corto per un camion, 356 km invece di 412» ma «per zona, in ordine di fascia oraria». È un cambio di significato rispetto alla promessa del mockup. In più «Gasolio stimato» resta con «—» e quindi sembra rotto.
2. **Telecamere (Corporation e Trasporti): la tabella «Foto delle scansioni» esce dal riquadro a 1280,** con la colonna Telecamera tagliata. A 820 le foto sono riquadri bianchi vuoti. Si vede subito su un monitor in ufficio.
3. **Badge: la guida dice di provare «Simula»,** ma il tasto non esiste. Chi segue le istruzioni si blocca.
4. **Segnaposto e testi da prova ancora visibili nel programma vero:**
   - «€ [tariffa]» (Giacenze);
   - «Contratto fino al [data]» (Clienti);
   - «Garanzia [mesi]» e «Reso entro [giorni]» (negozio pubblico);
   - le mail finte con «[Cliente]» e «[dominio]»;
   - il «Resoconto del mattino» inventato («1.198 consegne»);
   - «i numeri qui sono di esempio» (Ferie) e la frase «è una prova» (Introduzione).
5. **Dati di prova e dati che non tornano:**
   - un iPhone «35PROVA00001» nell'inventario computer;
   - «Ricevuti oggi 0» con 5 telefoni in tabella (Stage Cellulari a 1280);
   - il gasolio in litri al posto degli euro (Satellitare).
6. **Magazzino › Controllo a 820:** la colonna «Esito» è tagliata.
7. **Testi fissi cambiati senza dichiararlo:**
   - «Trasferisci» → «Trasferimento»;
   - il sottotesto dei Ricambi;
   - «Da → a» con un solo posto nei Movimenti.
8. **Piccole differenze grafiche:**
   - riquadro Missione più alto in App magazzino;
   - spazio più stretto nel Portale;
   - nessun difetto preselezionato in Grado;
   - QR più piccolo nel Badge;
   - in Inventario a 820 non si capisce che la tabella si può scorrere.

## 3. Immagini aperte davvero

**Ho aperto con Read tutte le 180 immagini (60 schermate × 3 larghezze), più un ritaglio della 390 di c-inv-schede,** perché ridotta era illeggibile.

Il visualizzatore più volte ha tolto le immagini dalla conversazione dopo averle mostrate («request limit»). Per questo molte le ho riaperte più volte. Le differenze più gravi le ho ricontrollate su un'immagine mostrata di nuovo, alla fine:
- t-traffico-1280;
- c-telecamere-1280;
- b-badge-1280;
- t-mag-controllo-820;
- k-grado-820 e k-grado-1280;
- m-home ×3.

Limiti di quello che ho visto:
- La 390 di c-inv-schede è alta 7861 px. Rimpicciolita è poco leggibile: nella parte bassa ho controllato solo la struttura delle schede.
- La voce «Richieste» in c-home e il caso «Da → a» in t-mag-mov li ho visti una volta sola e non li ho ricontrollati alla fine.
