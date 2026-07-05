--Attivato se la data di montaggio sensore
--non è compatibile con quella di montaggio blocco
CREATE TRIGGER TRG_BLOCCO_ANIMALE_CONTIENE_SENSORE_VALIDITA_DATA
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE_CONTIENE_SENSORE
FOR EACH ROW

DECLARE
    IS_VALID NUMBER(1,0);
    DATA_NON_COMPATIBILE EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_VALID
    FROM BLOCCO_ANIMALE BA
    WHERE BA.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
    AND BA.NUMERO_BLOCCO=:NEW.NUMERO_BLOCCO
    AND BA.DATA_MONTAGGIO <= :NEW.DATA_MONTAGGIO
    AND(
        BA.DATA_SMONTAGGIO IS NULL 
        OR BA.DATA_SMONTAGGIO > :NEW.DATA_MONTAGGIO
    )
    AND(
        :NEW.DATA_SMONTAGGIO IS NULL 
        OR BA.DATA_SMONTAGGIO IS NULL
        OR :NEW.DATA_SMONTAGGIO <= BA.DATA_SMONTAGGIO
    );

    IF IS_VALID = 0
        THEN
            RAISE DATA_NON_COMPATIBILE;
    END IF;

EXCEPTION
    WHEN DATA_NON_COMPATIBILE
        THEN 
            RAISE_APPLICATION_ERROR(
                -20003,
                'Le date di montaggio/smontaggio del sensore non
                sono compatibili con quelle del blocco animale'
            );
END;
/


--Attivato se un sensore è già montato in un altro
--blocco o cella idroponica

CREATE TRIGGER TRG_BLOCCO_ANIMALE_CONTIENE_SENSORE_DUPLICATO
AFTER INSERT OR UPDATE ON BLOCCO_ANIMALE_CONTIENE_SENSORE

DECLARE
    IS_INVALID NUMBER(1,0);
    SENSORE_DUPLICATO EXCEPTION;

BEGIN 

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM ALLOCAZIONI_SENSORI AS1
    JOIN ALLOCAZIONI_SENSORI AS2
    ON AS1.NOME_PRODUTTORE=AS2.NOME_PRODUTTORE
    AND AS1.NOME_MODELLO=AS2.NOME_MODELLO
    AND AS1.SERIALE=AS2.SERIALE

    WHERE AS1.DATA_MONTAGGIO < AS2.DATA_MONTAGGIO
    AND(
        AS1.DATA_SMONTAGGIO IS NULL
        OR AS1.DATA_SMONTAGGIO > AS2.DATA_MONTAGGIO
    );

    IF IS_INVALID <> 0
        THEN 
            RAISE SENSORE_DUPLICATO;
    END IF;

EXCEPTION
    WHEN SENSORE_DUPLICATO
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Il sensore inserito è gia presente in un altro blocco animale
                o cella idroponica nello stesso intervallo di tempo'
            );
END;
/


--Attivato se la data di smontaggio
--è precedente a quella di montaggio

CREATE TRIGGER TRG_BLOCCO_ANIMALE_CONTIENE_SENSORE_DATA_SMNT
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE_CONTIENE_SENSORE
FOR EACH ROW 

BEGIN
    IF :NEW.DATA_MONTAGGIO > :NEW.DATA_SMONTAGGIO
        THEN 
            RAISE_APPLICATION_ERROR(
                -20004,
                'La data di smontaggio è
                precedente a quella di montaggio'
            );
    END IF;
END;
/
