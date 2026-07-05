--Attivato se vengono utilizzati più semi
--di quelli disponibili

CREATE TRIGGER TRG_CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA_DISP_SEMI
AFTER INSERT OR UPDATE ON CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA

DECLARE 
    IS_INVALID NUMBER(2,0);
    SEMI_NEGATIVI EXCEPTION;

BEGIN 

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM SEMI_PRODUZIONE_AGRICOLA_DISPONIBILI
    WHERE SEMI_DISPONIBILI < 0;

    IF IS_INVALID <> 0
        THEN 
            RAISE SEMI_NEGATIVI;
    END IF;

EXCEPTION 
    WHEN SEMI_NEGATIVI
        THEN 
            RAISE_APPLICATION_ERROR(
                -20001,
                'Sono stati selezionati più semi produzione agricola di quelli disponibili'
            );
END;
/


--Attivato se vengono utilizzati 
--semi non compatibili con il tipo
--di coltura selezionato

CREATE TRIGGER TRG_CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA_SEMI_COMP
BEFORE INSERT OR UPDATE ON CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA
FOR EACH ROW 

DECLARE 
    IS_VALID NUMBER(1,0);
    SEMI_INCOMPATIBILI EXCEPTION;

BEGIN
    
    SELECT COUNT(*)
    INTO IS_VALID
    FROM(
        SELECT NOME_SEMI
        FROM TIPO_COLTURA TC 
        WHERE TC.NOME_TIPO_COLTURA=(
            SELECT NOME_TIPO_COLTURA
            FROM CICLO_COLTIVAZIONE CC
            WHERE CC.DATA_INIZIO=:NEW.DATA_INIZIO
            AND CC.CODICE_CELLA_IDR=:NEW.CODICE_CELLA_IDR
            AND CC.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
        )
    )T 
    WHERE T.NOME_SEMI=:NEW.NOME_PRODOTTO;

    IF IS_VALID = 0
        THEN 
            RAISE SEMI_INCOMPATIBILI;
    END IF;

EXCEPTION
    WHEN SEMI_INCOMPATIBILI
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Sono inseriti semi non compatibili
                con il tipo di coltivazione del ciclo'
            );
END;
/



--Attivato se i semi utilizzati
--sono prodotti dopo l'inizio
--del ciclo coltivazione

CREATE TRIGGER TRG_CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA_SEMI_NON_PRODOTTI
BEFORE INSERT OR UPDATE ON CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA
FOR EACH ROW 

DECLARE 
    SEMI_INCOMPATIBILI EXCEPTION;

BEGIN
    
    IF :NEW.DATA_PRODUZIONE_AGRICOLA > :NEW.DATA_INIZIO
        THEN 
            RAISE SEMI_INCOMPATIBILI;
    END IF;

EXCEPTION
    WHEN SEMI_INCOMPATIBILI
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Sono inseriti semi non presenti
                nella data di inizio del ciclo'
            );
END;
/