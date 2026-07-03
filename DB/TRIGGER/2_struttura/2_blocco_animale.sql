--ATTIVATO SE VIENE TERMINATO UN BLOCCO ANIMALE
--CON ANIMALI ALL'INTERNO OPPURE PRIMA
--DELLA SUA DATA DI ATTIVAZIONE

--ATTIVATO SE OCCUPA PIU SUPERFICIÈ DI QUELLA DISPONIBILE NELLA STRUTTURA

CREATE TRIGGER TRG_BLOCCO_ANIMALE_CHECK_DATA_SMONTAGGIO
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE
FOR EACH ROW

DECLARE
    NUMERO_ANIMALI NUMBER(6,0);
    SUPERFICIE_STRUTTURA NUMBER(8,2);

BEGIN 
    SELECT SUPERFICIE_MQ
    INTO SUPERFICIE_STRUTTURA
    FROM STRUTTURA S
    WHERE S.NOME_STRUTTURA=:NEW.NOME_STRUTTURA;

    IF :NEW.SUPERFICIE_MQ > SUPERFICIE_STRUTTURA
        THEN

            RAISE_APPLICATION_ERROR(
                    -20001,
                    'La superficie del blocco animale supera quella della struttura in cui è contenuto'
                );

    ELSE IF :NEW.DATA_SMONTAGGIO IS NOT NULL --CONTROLLO SU DATA SMONTAGGIO
        THEN 

            IF :NEW.DATA_SMONTAGGIO < :NEW.DATA_MONTAGGIO
                THEN

                RAISE_APPLICATION_ERROR(
                    -20004,
                    'Non è possibile inserire una data di terminazione minore di quella di attivazione'
                );

            ELSE

            SELECT COUNT(*)
            INTO NUMERO_ANIMALI
            FROM ANIMALE_ALLOCATO_BLOCCO AAB
            WHERE AAB.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
            AND AAB.NUMERO_BLOCCO=:NEW.NUMERO_BLOCCO
                AND(
                    AAB.DATA_DEALLOCAZIONE IS NULL
                    OR AAB.DATA_DEALLOCAZIONE > :NEW.DATA_SMONTAGGIO
                );

           

            IF NUMERO_ANIMALI > 0 
                THEN

                RAISE_APPLICATION_ERROR(
                    -20003,
                    'Per terminare un blocco animale è necessario rimuovere gli animali al suo interno'
                );

                END IF;
            END IF;
        END IF;
    END IF;
   
    END;
/