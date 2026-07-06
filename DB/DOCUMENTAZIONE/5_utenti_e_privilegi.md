# Utenti e privilegi

## Scopo

Questo documento descrive le categorie di utenti previste per il database MilkyWayFarm.

Le categorie sono definite in base alle responsabilita operative all'interno della biofarm. Ogni utente deve accedere solo ai dati necessari al proprio ruolo e deve eseguire le operazioni di modifica attraverso procedure dedicate, in modo da mantenere controlli, vincoli e transazioni centralizzati.

Gli utenti del DBMS non sono modellati come entita dello schema E/R, ma vengono gestiti tramite utenti Oracle, ruoli, viste e privilegi.

## Categorie individuate

Le categorie individuate sono:

- amministratore;
- veterinario;
- addetto strutture;
- addetto cicli coltivazione;
- addetto animali.

Queste categorie sono sufficienti per separare le principali aree operative del sistema:

- gestione generale;
- gestione sanitaria;
- gestione fisica della struttura;
- gestione agricola;
- gestione zootecnica.

## Amministratore

Nome utente previsto:

```text
MWF_ADMIN
```

L'amministratore gestisce il database nel suo complesso.

Puo consultare tutte le tabelle e tutte le viste del sistema. Puo inoltre eseguire le procedure amministrative necessarie alla manutenzione del database, al popolamento iniziale e alla correzione controllata dei dati.

L'amministratore e l'unico utente che puo avere privilegi diretti ampi sulle tabelle principali.

Operazioni previste:

- consultare lo stato generale della biofarm;
- consultare produzioni, sensori, animali, strutture e cicli;
- gestire dati di riferimento;
- eseguire procedure amministrative;
- creare o aggiornare utenti e privilegi, se previsto dallo script DCL.

## Veterinario

Nome utente previsto:

```text
MWF_VETERINARIO
```

Il veterinario gestisce le informazioni sanitarie degli animali.

Deve poter consultare gli animali, il loro tipo, lo stadio di crescita, le allocazioni nei blocchi, le diete e le eventuali prescrizioni. Deve poter inserire visite veterinarie e prescrizioni, ma non deve modificare direttamente la struttura fisica della biofarm o i cicli di coltivazione.

Operazioni previste:

- consultare gli animali e la loro posizione operativa;
- consultare diete, stadi di crescita e intolleranze;
- inserire visite veterinarie;
- inserire prescrizioni collegate a una visita;
- consultare lo storico sanitario di un animale.

Tabelle principali coinvolte:

- `ANIMALE`;
- `TIPO_ANIMALE`;
- `STADIO_CRESCITA`;
- `ANIMALE_ALLOCATO_BLOCCO`;
- `VISITA_VETERINARIA`;
- `PRESCRIZIONE_ANIMALE`;
- `DIETA_ANIMALE`;
- `STADIO_CRESCITA_PREVEDE_DIETA`.

## Addetto strutture

Nome utente previsto:

```text
MWF_STRUTTURE
```

L'addetto strutture gestisce la parte fisica e tecnica della biofarm.

Si occupa di strutture, blocchi animali, celle idroponiche, sensori e spostamenti dei sensori tra elementi produttivi. Deve poter registrare montaggi e smontaggi, rispettando i vincoli dinamici sulla superficie, sulle date e sulla presenza di animali, cicli o sensori ancora attivi.

Operazioni previste:

- inserire o aggiornare strutture;
- montare o smontare blocchi animali;
- montare o smontare celle idroponiche;
- registrare sensori;
- montare, smontare o spostare sensori;
- consultare le allocazioni dei sensori;
- consultare le registrazioni dei sensori.

Tabelle principali coinvolte:

- `STRUTTURA`;
- `BLOCCO_ANIMALE`;
- `CELLA_IDROPONICA`;
- `TIPO_SENSORE`;
- `SENSORE`;
- `REGISTRAZIONE_SENSORE`;
- `BLOCCO_ANIMALE_CONTIENE_SENSORE`;
- `CELLA_IDR_CONTIENE_SENSORE`.

## Addetto cicli coltivazione

Nome utente previsto:

```text
MWF_COLTIVAZIONE
```

L'addetto cicli coltivazione gestisce la parte agricola della biofarm.

Deve poter consultare celle idroponiche, modalita di coltivazione, tipi di coltura, semi disponibili e cicli agricoli. Deve poter avviare cicli di coltivazione, associare i semi utilizzati, chiudere cicli e registrare la produzione agricola ottenuta.

Operazioni previste:

- consultare le celle idroponiche disponibili;
- consultare semi missione e semi da produzione agricola disponibili;
- avviare un ciclo di coltivazione;
- associare semi a un ciclo;
- chiudere un ciclo di coltivazione;
- registrare produzioni agricole;
- consultare le produzioni agricole e la disponibilita dei semi.

Tabelle principali coinvolte:

- `CELLA_IDROPONICA`;
- `MODALITA_COLTIVAZIONE`;
- `TIPO_COLTURA`;
- `CICLO_COLTIVAZIONE`;
- `SEMI_MISSIONE`;
- `PRODUZIONE_AGRICOLA`;
- `CICLO_COLT_UTILIZZA_SEMI_MISSIONE`;
- `CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA`;
- `TIPO_COLTURA_TIPO_PRODOTTO`.

## Addetto animali

Nome utente previsto:

```text
MWF_ANIMALI
```

L'addetto animali gestisce la parte zootecnica della biofarm.

Deve poter consultare blocchi animali, tipi animali, animali presenti e prodotti generabili dagli stadi di crescita. Deve poter registrare nuovi animali, allocarli nei blocchi, deallocarli e registrare produzioni animali.

Operazioni previste:

- consultare blocchi animali disponibili;
- consultare tipi animali e animali presenti;
- inserire nuovi animali;
- allocare un animale in un blocco;
- deallocare un animale da un blocco;
- registrare produzioni animali;
- consultare lo storico delle allocazioni.

Tabelle principali coinvolte:

- `ANIMALE`;
- `TIPO_ANIMALE`;
- `BLOCCO_ANIMALE`;
- `BLOCCO_AMMETTE_TIPO_ANIMALE`;
- `ANIMALE_ALLOCATO_BLOCCO`;
- `STADIO_CRESCITA`;
- `PRODOTTO_DA_STADIO_CRESCITA`;
- `PRODUZIONE_ANIMALE`.

## Criterio di assegnazione dei privilegi

I privilegi devono essere assegnati secondo il principio del minimo privilegio.

In generale:

- le tabelle principali non dovrebbero essere modificate direttamente dagli utenti operativi;
- gli utenti operativi dovrebbero usare procedure PL/SQL per le operazioni di scrittura;
- le interrogazioni dovrebbero passare, quando utile, attraverso viste dedicate;
- l'amministratore puo avere privilegi piu ampi per manutenzione e collaudo;
- le procedure devono gestire esplicitamente eccezioni, `COMMIT` e `ROLLBACK`.

## Collegamento con le operazioni utente

Le categorie definite in questo documento guidano la scelta delle operazioni utente richieste dal progetto.

Le operazioni principali da implementare come procedure o funzioni PL/SQL sono:

- registrazione di una visita veterinaria con eventuale prescrizione;
- montaggio o spostamento di un sensore;
- avvio di un ciclo di coltivazione con uso di semi;
- chiusura di un ciclo di coltivazione con registrazione della produzione;
- allocazione o deallocazione di un animale in un blocco;
- registrazione di una produzione animale.

Ogni operazione deve coinvolgere piu tabelle e deve rappresentare un'azione reale di una categoria di utenti.
