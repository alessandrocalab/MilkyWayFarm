--Attivato se la data di montaggio
--del blocco animale è precedente a quella
--di attivazione della struttura

CREATE TRIGGER TRG_BLOCCO_ANIMALE_DATA_STRUTTURA
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE
FOR EACH ROW

DECLARE 
    IS_VALID NUMBER(1,0);
    DATA_NON_COMPATIBILE EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_VALID
    FROM STRUTTURA S
    WHERE S.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
    AND S.DATA_ATTIVAZIONE <= :NEW.DATA_MONTAGGIO
    AND(
        S.DATA_TERMINAZIONE IS NULL 
        OR S.DATA_TERMINAZIONE > :NEW.DATA_MONTAGGIO
    )
    AND(
        S.DATA_TERMINAZIONE IS NULL 
        OR :NEW.DATA_SMONTAGGIO IS NULL
        OR S.DATA_TERMINAZIONE >= :NEW.DATA_SMONTAGGIO
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
                'Non è possibile inserire una data di montaggio meno recente di quella di attivazione della struttura ospitante'
            );
END;
/


--Attivato se il blocco animale
--occupa più superficie di quella
--disponibile nella struttura

CREATE TRIGGER TRG_BLOCCO_ANIMALE_SUPERFICIE_DISP
AFTER INSERT OR UPDATE ON BLOCCO_ANIMALE

DECLARE
    IS_INVALID NUMBER(9,0);
    SUPERFICIE_INSUFFICIENTE EXCEPTION;

BEGIN

    SELECT COUNT(*)
    INTO IS_INVALID
    FROM STRUTTURA S 
    JOIN(
        SELECT 
            CI2.NOME_STRUTTURA,
            CI2.DATA_MONTAGGIO AS ISTANTE,
            SUM(CI.SUPERFICIE_MQ) AS SUPERFICIE_OCCUPATA

        FROM ELEMENTI_PRODUTTIVI CI
        JOIN ELEMENTI_PRODUTTIVI CI2
        ON CI.NOME_STRUTTURA=CI2.NOME_STRUTTURA
        WHERE CI.DATA_MONTAGGIO <= CI2.DATA_MONTAGGIO
        AND(
            CI.DATA_SMONTAGGIO IS NULL 
            OR CI.DATA_SMONTAGGIO > CI2.DATA_MONTAGGIO
        )
        GROUP BY 
            CI2.NOME_STRUTTURA,
            CI2.DATA_MONTAGGIO
    ) T
    ON S.NOME_STRUTTURA=T.NOME_STRUTTURA
    WHERE S.SUPERFICIE_MQ<T.SUPERFICIE_OCCUPATA;

    IF IS_INVALID <> 0
        THEN 
            RAISE SUPERFICIE_INSUFFICIENTE;
    END IF;

EXCEPTION
    WHEN SUPERFICIE_INSUFFICIENTE
        THEN 
            RAISE_APPLICATION_ERROR(
                -20001,
                'La superficie del blocco animale supera quella disponibile della struttura in cui è contenuto'
            );
END;
/


--Attivato se la data di smontaggio
--è precedente a quella di montaggio

CREATE TRIGGER TRG_BLOCCO_ANIMALE_DATA_SMONTAGGIO
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE
FOR EACH ROW

DECLARE
    DATA_SMONTAGGIO_NON_VALIDA EXCEPTION;

BEGIN

    IF :NEW.DATA_SMONTAGGIO IS NOT NULL
        AND :NEW.DATA_SMONTAGGIO < :NEW.DATA_MONTAGGIO
        THEN 
            RAISE DATA_SMONTAGGIO_NON_VALIDA;
    END IF;

EXCEPTION
    WHEN DATA_SMONTAGGIO_NON_VALIDA
        THEN 
            RAISE_APPLICATION_ERROR(
                -20004,
                'Non è possibile inserire una data di smontaggio precedente a quella di montaggio'
            );
END;
/


--Attivato se viene smontato
--un blocco animale con animali
--ancora al suo interno

CREATE TRIGGER TRG_BLOCCO_ANIMALE_ANIMALI_PRESENTI
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE
FOR EACH ROW

DECLARE
    IS_INVALID NUMBER(6,0);
    ANIMALI_PRESENTI EXCEPTION;

BEGIN

    IF :NEW.DATA_SMONTAGGIO IS NOT NULL
        THEN

            SELECT COUNT(*)
            INTO IS_INVALID
            FROM ANIMALE_ALLOCATO_BLOCCO AAB
            WHERE AAB.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
            AND AAB.NUMERO_BLOCCO=:NEW.NUMERO_BLOCCO
            AND(
                AAB.DATA_DEALLOCAZIONE IS NULL
                OR AAB.DATA_DEALLOCAZIONE > :NEW.DATA_SMONTAGGIO
            );

            IF IS_INVALID <> 0
                THEN 
                    RAISE ANIMALI_PRESENTI;
            END IF;

    END IF;

EXCEPTION
    WHEN ANIMALI_PRESENTI
        THEN 
            RAISE_APPLICATION_ERROR(
                -20003,
                'Per terminare un blocco animale è necessario rimuovere gli animali al suo interno'
            );
END;
/
