--Attivato se la data non è compatibile
--con quella di fine del ciclo coltivazione

CREATE TRIGGER TRG_PRODUZIONE_AGRICOLA
BEFORE INSERT OR UPDATE ON PRODUZIONE_AGRICOLA
FOR EACH ROW 

DECLARE
    IS_INVALID NUMBER(1,0);
    DATA_INVALIDA EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM CICLO_COLTIVAZIONE CC 
    WHERE CC.DATA_INIZIO=:NEW.DATA_INIZIO_CICLO_COLTIVAZIONE
    AND CC.CODICE_CELLA_IDR=:NEW.CODICE_CELLA_IDR
    AND CC.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
    AND (
        CC.DATA_FINE_EFFETTIVA IS NULL 
        OR CC.DATA_FINE_EFFETTIVA < :NEW.DATA_PRODUZIONE_AGRICOLA
    );

    IF IS_INVALID <> 0
        THEN
            RAISE DATA_INVALIDA;
    END IF;

EXCEPTION
    WHEN DATA_INVALIDA
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'La data produzione agricola non è valida rispetto quella
                del ciclo coltivazione associato'
            );
END;
/