SET SERVEROUTPUT ON

--Test procedura INIZIA_CICLO_COLTIVAZIONE_SEMI_ATUOMATICI


--Pulizia eventuale test precedente

DELETE FROM CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';

DELETE FROM CICLO_COLT_UTILIZZA_SEMI_MISSIONE
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';

DELETE FROM CICLO_COLTIVAZIONE
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';

COMMIT;


--Deve andare perche la cella e montata,
--il tipo coltura accetta la modalita,
--la cella rispetta la modalita e i semi sono disponibili

BEGIN
    INIZIA_CICLO_COLTIVAZIONE_SEMI_ATUOMATICI(
        DATE '2026-04-08',
        '000A',
        'Struttura Agricola',
        'Idro cereali base',
        'Grano duro',
        4.50
    );
END;
/


--Verifica ciclo inserito

SELECT *
FROM CICLO_COLTIVAZIONE
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';


--Verifica semi missione utilizzati

SELECT *
FROM CICLO_COLT_UTILIZZA_SEMI_MISSIONE
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';


--Verifica semi da produzione agricola utilizzati

SELECT *
FROM CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA
WHERE DATA_INIZIO=DATE '2026-04-08'
AND CODICE_CELLA_IDR='000A'
AND NOME_STRUTTURA='Struttura Agricola';


--Deve essere bloccato perche la quantita semi non e positiva

BEGIN
    INIZIA_CICLO_COLTIVAZIONE_SEMI_ATUOMATICI(
        DATE '2026-04-09',
        '000A',
        'Struttura Agricola',
        'Idro cereali base',
        'Grano duro',
        0
    );

    DBMS_OUTPUT.PUT_LINE('ERRORE: la quantita semi non positiva non e stata bloccata');

EXCEPTION
    WHEN OTHERS
        THEN
            DBMS_OUTPUT.PUT_LINE('Errore atteso: ' || SQLERRM);
END;
/


--Deve essere bloccato perche i semi richiesti non sono disponibili

BEGIN
    INIZIA_CICLO_COLTIVAZIONE_SEMI_ATUOMATICI(
        DATE '2026-04-09',
        '000A',
        'Struttura Agricola',
        'Idro cereali base',
        'Grano duro',
        9999
    );

    DBMS_OUTPUT.PUT_LINE('ERRORE: la quantita semi non disponibile non e stata bloccata');

EXCEPTION
    WHEN OTHERS
        THEN
            DBMS_OUTPUT.PUT_LINE('Errore atteso: ' || SQLERRM);
END;
/
