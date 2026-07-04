--Attivato se la visita veterinaria non ricade
--in un periodo in cui l'animale è allocato


CREATE TRIGGER TRG_VISITA_VETERINARIA
BEFORE INSERT OR UPDATE ON VISITA_VETERINARIA
FOR EACH ROW

DECLARE
    IS_ALLOCATO NUMBER(1,0);
    ANIMALE_NON_ALLOCATO EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_ALLOCATO
    FROM ANIMALE_ALLOCATO_BLOCCO AAB
    WHERE AAB.ETICHETTA_ANIMALE=:NEW.ETICHETTA_ANIMALE
    AND AAB.DATA_ALLOCAZIONE <= :NEW.DATA_VISITA
    AND (
        AAB.DATA_DEALLOCAZIONE IS NULL
        OR AAB.DATA_DEALLOCAZIONE > :NEW.DATA_VISITA
    );

    IF IS_ALLOCATO = 0
        THEN
            RAISE ANIMALE_NON_ALLOCATO;
    END IF;

EXCEPTION
    WHEN ANIMALE_NON_ALLOCATO
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'La visita è effettuata in una data dove l''animale non è allocato in nessun blocco'
            );

END;
/