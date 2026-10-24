# Collaudo: mockup approvato vs programma

Data: 23/10/2026. Collaudatore indipendente: ho guardato solo le immagini, non ho modificato file e non ho letto STATO.md.
Regola: contano solo le differenze che NON sono dati (numeri, nomi, data in alto, lunghezza delle liste).

## Differenze comuni a più schermate

- **G1 – Menu in alto (390 e 820):** nel programma il menu scorre fino alla voce attiva (es. «Negozio online», «App magazzino»), mentre nel mockup resta fermo su «Introduzione». A 820 la prima voce visibile risulta tagliata («uzione», «:orporation»). Il problema c'è in tutte le schermate App/Corporation/Negozio/Siti.
- **G2 – Telefono finto (app autisti, magazzino, presenze, Corporation):** a 390 nel mockup l'area del telefono ha un bordo sottile arrotondato, nel programma no. A 820 e 1280 il contenuto parte circa 10 px più in alto e alcuni titoli dentro il telefono sono più piccoli.

## 1. Tabella

| Schermata | 390 | 820 | 1280 | Esito | Differenze (cosa, dove) |
|---|---|---|---|---|---|
| intro | ✓ | ✓ | ✓ | Identica | — |
| a-bolla | ✓ | ✓ | ✓ | Differenze | Solo G2 |
| a-fermata | ✓ | ✓ | ✓ | Differenze | «entro le 12» diventa «Entro le 12» (maiuscola). A 820/1280 sotto Firma si vede in più «Tocca e fai firmare il cliente». G2 |
| a-lista | ✓ | ✓ | ✓ | Differenze | Solo G2 |
| a-mancata | ✓ | ✓ | ✓ | Differenze | A 820/1280 il titolo «Perché non è stata consegnata?» sta su 1 riga con un carattere più piccolo (nel mockup 2 righe). G2 |
| a-merce | ✓ | ✓ | ✓ | Differenze | Solo G2 |
| b-badge | ✓ | ✓ | ✓ | Differenze | Entrata/Uscita: nel mockup 2 tasti neri pieni, nel programma Entrata è grigia disattivata e Uscita bianca con contorno. **Manca il tasto «Simula: un collega prova con il mio badge»**, anche se la guida lo cita ancora. Testo sotto il QR cambiato: «Avvicina il telefono al lettore… iPhone di Christian» diventa «Premi Entrata o Uscita e avvicina… questo dispositivo di Christian». G1 |
| c-home | ✓ | ✓ | ✓ | Differenze | Sottotitolo di Incassato: «al netto delle commissioni» diventa «netto di commissioni, spese, IVA e resi». G1 |
| c-inv | ✓ | ✓ | ✓ | Differenze | Nella riga iPhone 13 i valori finiscono nelle colonne sbagliate («128 GB · Blu» sotto Processore, «Batteria 89%» sotto RAM). Alcune righe hanno il Grado vuoto. G1 |
| c-inv-schede | ✓ | ✓ | ✓ | Differenze (minori) | La scheda iPhone mostra l'icona del portatile. Alcune schede sono senza grado e altre hanno «— · —» e «€ —» |
| c-lotti | ✓ | ✓ | ✓ | Identica | Solo G1 |
| c-mail | ✓ | ✓ | ✓ | Identica | Solo G1 |
| c-ordini | ✓ | ✓ | ✓ | Identica | Solo G1 |
| c-ricambi | ✓ | ✓ | ✓ | Differenze | Etichetta del 3° riquadro: «Computer da smontare / non funzionanti, dischi già cancellati» diventa «Computer smontati / non si vendono più interi». Nuovo stato «Da vendere» |
| c-stage | ✓ | ✓ | ✓ | Identica | — |
| c-stageTel | ✓ | ✓ | ✓ | Identica | — |
| c-telecamere | ✓ | ✓ | ✓ | Differenze | Telecamere in ordine alfabetico (Baie, Corsia S03, Corsia S07, Ingresso, Piazzale, Stage) invece dell'ordine del mockup (Ingresso, Piazzale, Baie…). Avvisi della notte in ordine inverso. Tabella Foto delle scansioni: a 390 si vedono solo Cosa/Posto, a 820 mancano Telecamera e miniatura, a 1280 si vedono solo Cosa/Posto/Movimento (Chi, Ora, Telecamera e miniatura fuori dal riquadro, «C» tagliata) |
| k-scan | ✓ | ✓ | ✓ | Differenze | Nel mirino manca il riquadro bianco con l'etichetta «MTM… / S/N PF3XXXXX / 20V» |
| k-scheda | ✓ | ✓ | ✓ | **Diversa** | Mockup: «Letto dalla foto PF3XXXXX», «Verificato su Lenovo», chip «Nel DDT/Lavorato da noi», titolo modello, tabella Processore/RAM/Disco/Schermo/**Cancellazione Certus/Batteria dal report**, Avanti nero. Programma: campo «Seriale» vuoto, elenco vuoto Marca/Modello/Processore/RAM/Disco/Schermo/**Scheda video**, Avanti grigio disattivato |
| k-grado | ✓ | ✓ | ✓ | Differenze | Testo guida: «Il programma propone B dal report. Cambialo con un tocco.» diventa «Scegli il grado con un tocco.». Nessun difetto preselezionato (nel mockup «Graffi sul coperchio» è attivo) |
| m-home | ✓ | ✓ | ✓ | Identica | Solo G2 |
| m-entrata | ✓ | ✓ | ✓ | Differenze | Mancano la riga «Bolla Snam [n. bolla] · 4 bancali» (sostituita da «Scansiona il primo bancale o collo»), la **barra di avanzamento** e «0 di 4 messi a posto» |
| m-uscita | ✓ | ✓ | ✓ | **Diversa** | Mockup: dettaglio della spedizione («Spedizione Snam · Motrice · Autista 2», Collo 1…4 di 4 «prendi da S03-…», etichetta «Adesso», tasti «Scansiona il collo» e «Non parte finché mancano colli»). Programma: elenco di spedizioni numerate con «0 di 4 / 12 di 12», testo «Merce in deposito…», **nessun tasto** |
| m-sposta | ✓ | ✓ | ✓ | Identica | Solo G2 |
| m-missioni | ✓ | ✓ | ✓ | Differenze | Nelle righe dei posti manca «· Econocom». La nota «Se arriva un camion puoi uscire…» non si vede (lista tagliata in fondo al telefono, l'ultima riga è tagliata a metà) |
| n-home | ✓ | ✓ | ✓ | Differenze | **Filtri marchio in ordine diverso**: mockup Tutti/Lenovo/HP/Dell/Apple, programma Tutti/Apple/Dell/HP/Lenovo. Nel negozio portatili compare un iPhone 13 con icona portatile e senza riga specifiche (scheda più bassa, righe disallineate) |
| n-prod | ✓ | ✓ | ✓ | Differenze | Opzioni Memoria invertite (16 GB prima di 8 GB). Gradi «Esaurito» grigi; **a 820 la scritta "Esaurito" esce dai bordi dei tasti grado** |
| n-carrello | ✓ | ✓ | ✓ | Identica | Solo G1 |
| n-ricambi | ✓ | ✓ | ✓ | Identica | Solo dati (la provenienza riporta anche la marca, «Da Dell Latitude 5420») |
| sitoC | ✓ | ✓ | ✓ | Identica | La percentuale animata è stata catturata in un momento diverso |
| sitoT | ✓ | ✓ | ✓ | Identica | Solo G1 |
| t-home | ✓ | ✓ | ✓ | Identica | Solo dati |
| t-anomalie | ✓ | ✓ | ✓ | Identica | — |
| t-anomalie-sez | ✓ | ✓ | ✓ | Identica | — |
| t-mail | ✓ | ✓ | ✓ | Identica | — |
| t-bolle | ✓ | ✓ | ✓ | Identica | Solo dati |
| t-traffico | ✓ | ✓ | ✓ | Differenze | Mancano l'etichetta verde **«Ottimizzati per camion»** e il riquadro **«Risparmio −14%»**. Km totali e Gasolio stimato mostrano «—». La mappa è un disegno fisso (4/3/3 punti) che non corrisponde ai giri mostrati (2/2/1 fermate) |
| t-giro | ✓ | ✓ | ✓ | Differenze | Tasto **«Sposta» grigio disattivato** su tutte le fermate (nel mockup è attivo). Riga info senza i km |
| t-mag-pianta | ✓ | ✓ | ✓ | Differenze | Zone a terra (Ricevimento, Passaggio Apple, Giacenze, Resi) sostituite da «Nessuna zona a terra registrata.». Testo guida cambiato («il suo contenuto» diventa «i suoi articoli») |
| t-mag-controllo | ✓ | ✓ | ✓ | Differenze | A 820 la colonna Esito è tagliata al bordo («Manca 1 collo rispett…»). Ora «—» su molte righe |
| t-mag-mov | ✓ | ✓ | ✓ | Identica | Solo dati (Cliente «B-0155» su uno spostamento: dato sbagliato) |
| t-mag-inv (Missioni) | ✓ | ✓ | ✓ | Differenze | **Manca il tasto «Apri l'app magazzino»**, sostituito dal riquadro rosso «Bloccati 1». **«Lancia» grigio disattivato.** In più c'è un riquadro rosso grande «S07-2-2 Bloccato / Manca / In più / Cosa è successo / Sblocca» che non è nel mockup. Il titolo perde «(Econocom)» |
| t-mag-storico | ✓ | ✓ | ✓ | Identica | Manca il 2° riquadro anomalia «Modifiche a mano» (dipende dai dati) |
| t-giacenze | ✓ | ✓ | ✓ | Differenze | Lista «Cosa paga il cliente»: a 390 la colonna prezzi non si vede, a 820 i prezzi sono troncati («€ 9,00 a coll», «[tariffa da ins»). Testo «[tariffa da inserire in Clienti]» |
| t-clienti | ✓ | ✓ | ✓ | Identica | — |
| t-cliente | ✓ | ✓ | ✓ | Identica | Solo dati |
| t-portale | ✓ | ✓ | ✓ | Differenze | A 390 i 4 riquadri numeri sono in una colonna a tutta larghezza invece della griglia 2×2 del mockup |
| t-fatture | ✓ | ✓ | ✓ | Differenze | **Manca il tasto nero «Invia»** (resta solo «Nuova»), anche se la guida dice «premi Invia». Colonna Consegne sempre «—» |
| t-mezzi | ✓ | ✓ | ✓ | Differenze | Con il filtro predefinito «Sprinter» la tabella è vuota («Nessun mezzo di questo tipo.»): in demo si vede una tabella vuota |
| t-autisti | ✓ | ✓ | ✓ | Identica | — |
| t-telepass | ✓ | ✓ | ✓ | Identica | — |
| t-satellitare | ✓ | ✓ | ✓ | Differenze | Intestazione «Litri/100 km» diventa «Litri». Mappa senza strade di sfondo e senza il quadratino nero del mezzo |
| t-pres-oggi | ✓ | ✓ | ✓ | Differenze | Lo stato «Ritardo · N min» è un'etichetta rossa con bordo invece del testo semplice del mockup |
| t-pres-fix | ✓ | ✓ | ✓ | Identica | — |
| t-pres-allarmi | ✓ | ✓ | ✓ | Identica | — |
| t-pres-riep | ✓ | ✓ | ✓ | Identica | — |
| t-pres-ferie | ✓ | ✓ | ✓ | Differenze | A 390 la colonna «Restano» sparisce fuori dal riquadro. A 820/1280 la colonna «Da guardare» è tagliata («Manca quanto spetta l'anno (cont…») invece di andare a capo. Il testo della nota sotto la tabella è stato riscritto |
| t-pres-mese | ✓ | ✓ | ✓ | Differenze | A 820 la colonna «Assenze» è tagliata al bordo destro |
| t-telecamere | ✓ | ✓ | ✓ | Differenze | Come c-telecamere: ordine delle telecamere e degli avvisi diverso, colonne della tabella Foto tagliate (a 390 solo Cosa/Posto) |
| t-j7 | ✓ | ✓ | ✓ | Differenze | **«Importa» grigio disattivato** (nel mockup è nero attivo). Mancano le righe «· N righe» nelle schede file |

## 2. Differenze per gravità (quelle che il cliente noterebbe in azienda)

1. **App Corporation › Scheda (k-scheda):** la schermata è diversa dal mockup. Il form è vuoto, Avanti è disattivato e mancano «Verificato su Lenovo», Cancellazione Certus e Batteria.
2. **App magazzino › Uscita (m-uscita):** la schermata è diversa. Al posto del dettaglio colli c'è un elenco di spedizioni e mancano i tasti «Scansiona il collo» / «Non parte finché mancano colli».
3. **Tasti mancanti o disattivati che nel mockup sono attivi:** «Invia» in Fatturazione (manca), «Simula» nel Badge (manca), «Apri l'app magazzino» in Missioni (manca), «Lancia» in Missioni (grigio), «Importa» in J7 (grigio), «Sposta» nel Giro (grigio), Entrata/Uscita del Badge (stile diverso, Entrata grigia).
4. **Elementi in più non approvati:** riquadro rosso «S07-2-2 Bloccato / Sblocca» e «Bloccati 1» in Magazzino › Missioni.
5. **Traffico:** mancano «Ottimizzati per camion» e «Risparmio −14%», Km e Gasolio mostrano «—» e la mappa non corrisponde ai giri.
6. **App magazzino › Entrata:** mancano la barra di avanzamento e «0 di 4 messi a posto».
7. **Colonne e testi tagliati:** Telecamere › Foto delle scansioni (colonne fuori a tutte le larghezze), Giacenze (prezzi spariti a 390, troncati a 820), Presenze › Ferie («Restano» sparita a 390, «Da guardare» tagliata a 820/1280), Presenze › Ottobre a 820 («Assenze»), Magazzino › Controllo a 820 («Esito»), Negozio › Prodotto a 820 («Esaurito» fuori dai tasti).
8. **Ordine diverso:** filtri marchio del Negozio (alfabetico invece di Lenovo/HP/Dell/Apple), ordine di telecamere e avvisi, opzioni Memoria invertite.
9. **Etichette e testi cambiati:** sottotitolo di Incassato (c-home), 3° riquadro di c-ricambi, «Litri/100 km» diventato «Litri», testo guida di k-grado, testo istruzione del Badge, «Entro le 12», nota di Ferie, «· Econocom» assente in Missioni.
10. **Grafica:** manca l'etichetta S/N nel mirino di k-scan, la mappa del Satellitare è senza strade e senza mezzo, Portale a 390 ha i riquadri in una colonna invece che 2×2, lo stato Ritardo in Presenze è un'etichetta rossa.
11. **Contenuti vuoti in demo** (dati, ma ben visibili): Mezzi › Sprinter con tabella vuota, Pianta senza zone a terra, riga iPhone di c-inv con le colonne sfasate (questo è un difetto di mappatura, non solo un dato).
12. **Minori e generali:** il menu in alto scorre sulla voce attiva (G1); il telefono finto ha un bordo e un'altezza del contenuto diversi (G2).

## 3. Immagini aperte

- Nella cartella ci sono **180 immagini** (60 schermate × 3 larghezze), non 183. Esclusi STATO.md e i file «_». Ogni schermata ha tutte e tre le larghezze: nessuna manca e nessuna risultava illeggibile.
- Le ho aperte **tutte e 180**. Durante il primo giro molte sono state trattenute per il limite di richieste del visualizzatore, quindi ho riaperto una per una tutte quelle che non avevo visto chiaramente. Le immagini 390 molto alte (c-inv-schede, n-prod, n-ricambi) le ho controllate anche ritagliate, per leggerle bene.
- Le schermate «Identica» possono comunque avere G1/G2, cioè le differenze generali del menu e del telefono.
