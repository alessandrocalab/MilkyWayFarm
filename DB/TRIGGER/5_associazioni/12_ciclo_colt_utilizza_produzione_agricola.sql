--Attivato se vengono utilizzati più semi
--di quelli disponibili

CREATE TRIGGER TRG_CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA
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