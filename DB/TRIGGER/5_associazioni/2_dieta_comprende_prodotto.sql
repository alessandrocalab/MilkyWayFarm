--Attivato se aggiungo a una dieta già
--assegnata a uno stadio crescita un
--prodotto che contiene sostanze che 
--generano intolleranze

CREATE TRIGGER TRG_DIETA_COMPRENDE_PRODOTTO_INTOLLERANTE
BEFORE INSERT OR UPDATE ON DIETA_COMPRENDE_PRODOTTO
FOR EACH ROW

DECLARE
    IS_INVALID NUMBER(6,0);
    INTOLLERANTE EXCEPTION;

BEGIN 

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM STADIO_CRESCITA_PREVEDE_DIETA SCPD
    JOIN STADIO_CRESCITA_INTOLLERANTE_SOSTANZA SCIC 
    ON SCIC.NOME_STADIO_CRESCITA=SCPD.NOME_STADIO_CRESCITA
    AND SCIC.NOME_TIPO_ANIMALE=SCPD.NOME_TIPO_ANIMALE
    WHERE SCPD.NOME_DIETA=:NEW.NOME_DIETA 
    AND SCIC.NOME_SOSTANZA IN(
        SELECT NOME_SOSTANZA
        FROM PRODOTTO_CONTIENE_SOSTANZA
        WHERE NOME_PRODOTTO=:NEW.NOME_PRODOTTO
    );

    IF IS_INVALID <> 0
        THEN 
            RAISE INTOLLERANTE;
    END IF;

EXCEPTION 
    WHEN INTOLLERANTE
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Tentativo di aggiungere un prodotto a una dieta
                assegnata a uno stadio crescita che presenta
                intolleranze a sostanze contenute nel prodotto'
            );
END;
/


--Attivato se il prodotto non è edibile

CREATE TRIGGER TRG_DIETA_COMPRENDE_PRODOTTO_NON_EDIBILE
BEFORE INSERT OR UPDATE ON DIETA_COMPRENDE_PRODOTTO
FOR EACH ROW

DECLARE
    IS_VALID NUMBER(1,0);
    NO_EDIBILE EXCEPTION;

BEGIN

    SELECT IS_EDIBILE
    INTO IS_VALID
    FROM TIPO_PRODOTTO
    WHERE TIPO_PRODOTTO.NOME_PRODOTTO=:NEW.NOME_PRODOTTO;

    IF IS_VALID = 0
        THEN 
            RAISE NO_EDIBILE;
    END IF;

EXCEPTION 
    WHEN NO_EDIBILE
        THEN 
            RAISE_APPLICATION_ERROR(
                -20001,
                'Il prodotto aggiunto alla dieta non è edibile'
            );
END;
/