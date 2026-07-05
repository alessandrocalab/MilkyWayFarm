--Attivato se vengono utilizzati più semi
--di quelli disponibili

CREATE TRIGGER TRG_CICLO_COLTIVAZIONE_UTILIZZA_SEMI_MISSIONE
AFTER INSERT OR UPDATE ON CICLO_COLT_UTILIZZA_SEMI_MISSIONE

DECLARE 
    IS_INVALID NUMBER(2,0);
    SEMI_NEGATIVI EXCEPTION;

BEGIN 

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM SEMI_MISSIONE_DISPONIBILI
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
                'Sono stati selezionati più semi missione di quelli disponibili'
            );
END;
/
