# Uso della cartella DB

Questo documento descrive l'uso dei file attualmente presenti nella cartella `DB`.

## Struttura principale

La cartella e organizzata in sezioni:

- `DDL/`: contiene gli script di creazione delle tabelle e dei vincoli statici;
- `DML/`: contiene gli script di popolamento con dati fittizi;
- `QUERY/`: contiene interrogazioni operative di esempio;
- `PL_SQL/`: contiene package PL/SQL usati per simulazione e test;
- `drop_all.sql`: elimina tutte le tabelle dello schema corrente;
- `view_all.sql`: query di report sui consumi dei cicli di coltivazione;
- `ttest.sql`: script di test rapido.

## Creazione dello schema

Per ricostruire lo schema da zero, posizionarsi nella cartella `DDL` ed eseguire:

```sql
@main.sql
```

Lo script:

1. attiva `SQLBLANKLINES`;
2. richiama `../drop_all.sql`;
3. crea le tabelle nell'ordine corretto;
4. crea chiavi primarie, chiavi esterne e vincoli `CHECK`;
5. termina con `COMMIT`.

Lo script `drop_all.sql` elimina tutte le tabelle presenti nello schema Oracle corrente usando `CASCADE CONSTRAINTS PURGE`.

## Popolamento dei dati

Dopo aver creato lo schema, posizionarsi nella cartella `DML` ed eseguire:

```sql
@main.sql
```

Lo script popola le principali tabelle del database con dati fittizi riguardanti:

- prodotti e sostanze;
- strutture, blocchi, celle e sensori;
- tipi animali, animali, stadi, diete, vaccini, visite e prescrizioni;
- modalita di coltivazione, tipi di coltura e semi missione;
- associazioni tra prodotti, sostanze, diete, colture, blocchi e modalita.

Alcune tabelle operative, come produzioni, registrazioni sensore e cicli di coltivazione, possono essere popolate manualmente, tramite procedure o tramite gli script di simulazione.

## Query disponibili

La cartella `QUERY/` contiene query di esempio per interrogazioni operative:

- `1.sql`: verifica se una cella idroponica ha un ciclo attivo;
- `2.sql`: recupera l'ultimo ciclo di una cella;
- `3.sql`: ricava la durata del ciclo in base ai semi usati;
- `4.sql`: elenca le produzioni possibili per un tipo di coltura;
- `5.sql`: calcola la quantita di semi usata in un ciclo;
- `6.sql`: calcola i semi missione residui;
- `7.sql`: calcola i semi ottenuti da produzione agricola ancora disponibili;
- `8.sql`: ricava il tipo di coltura a partire dal seme;
- `9.sql`: ricava le modalita di coltivazione compatibili con una coltura.

Alcune query contengono valori di esempio da sostituire, come date, codici cella o nomi struttura.

## Package PL/SQL disponibili

La cartella `PL_SQL/` contiene tre package:

### `simulatore.sql`

Crea il package `SIMULATORE`, relativo alla parte agricola.

Procedure principali:

```sql
SIMULATORE.SIMULA_GIORNO(TRUNC(SYSDATE));
SIMULATORE.RUN_SIMULAZIONE(DATE '2026-07-03');
```

Il package puo avviare cicli di coltivazione, chiuderli e generare produzioni agricole dimostrative.

### `simulatore_animale.sql`

Crea il package `SIMULATORE_ANIMALE`, relativo alla produzione animale.

Procedure principali:

```sql
SIMULATORE_ANIMALE.SIMULA_GIORNO(TRUNC(SYSDATE));
SIMULATORE_ANIMALE.RUN_SIMULAZIONE(DATE '2026-07-03');
```

Il package usa animali, allocazioni, stadi di crescita e prodotti stimati per generare produzioni animali dimostrative.

### `simulatore_sensori.sql`

Crea il package `SIMULATORE_SENSORI`, relativo alle registrazioni dei sensori.

Procedure principali:

```sql
SIMULATORE_SENSORI.SIMULA_GIORNO(TRUNC(SYSDATE), 60);
SIMULATORE_SENSORI.RUN_SIMULAZIONE(DATE '2026-07-03', 60);
```

Il secondo parametro indica l'intervallo in minuti tra una registrazione e la successiva. Il valore `60` genera una registrazione ogni ora.

## Script di test

Il file `ttest.sql` compila i tre package PL/SQL e lancia una simulazione sulla data odierna:

```sql
@ttest.sql
```

Lo script:

1. abilita `SERVEROUTPUT`;
2. compila i package agricolo, animale e sensori;
3. esegue le procedure giornaliere sulla data `TRUNC(SYSDATE)`;
4. mostra il numero di righe create nella data odierna per produzioni agricole, produzioni animali e registrazioni sensore.

## Ordine consigliato di esecuzione

Da SQL*Plus o SQLcl:

```sql
cd DDL
@main.sql

cd ../DML
@main.sql

cd ..
@ttest.sql
```

## Note importanti

- Gli script PL/SQL di simulazione sono utili per collaudo e generazione di dati dimostrativi, ma non sostituiscono le operazioni utente e i trigger richiesti dalla consegna.
- Per il progetto d'esame sara opportuno aggiungere script separati per trigger, viste, utenti, privilegi e scheduler.
- Se lo schema Oracle e stato creato prima della correzione del nome `DATA_DEALLOCAZIONE`, potrebbe essere necessario ricrearlo da zero.
