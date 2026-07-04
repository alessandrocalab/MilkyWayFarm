--Attivato se il blocco è di dimensioni minori
--rispetto allo spazio minimo richiesto per 
--il tipo animale


CREATE TRIGGER TRG_BLOCCO_AMMETTE_TIPO_ANIMALE
BEFORE INSERT OR UPDATE ON BLOCCO_AMMETTE_TIPO_ANIMALE
FOR EACH ROW

DECLARE 
    IS_INVALID NUMBER(1,0);
    SPAZIO_INSUFFICENTE EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM BLOCCO_ANIMALE BA
    WHERE BA.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
    AND BA.NUMERO_BLOCCO=:NEW.NUMERO_BLOCCO
    AND BA.SUPERFICIE_MQ<(
        SELECT SPAZIO_MINIMO_MQ
        FROM TIPO_ANIMALE
        WHERE NOME_TIPO_ANIMALE=:NEW.NOME_TIPO_ANIMALE
    );

    IF IS_INVALID <> 0
        THEN 
            RAISE SPAZIO_INSUFFICENTE;
    END IF;

EXCEPTION 
    WHEN SPAZIO_INSUFFICENTE
        THEN 
            RAISE_APPLICATION_ERROR(
                -20001,
                'Il blocco non ha spazio a sufficenza per ammettere il tipo di animale'
            );
END;
/