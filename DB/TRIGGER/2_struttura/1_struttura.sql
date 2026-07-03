--ATTIVATO SE VIENE TERMINATA UNA STRUTTURA 
--CONTENTENTE BLOCCHI ANIMALI O CELLE IDROPONICHE
--NON ANCORA TERMINATE

CREATE TRIGGER TRG_STRUTTURA_CHECK_DATA
BEFORE INSERT OR UPDATE ON STRUTTURA
FOR EACH ROW

DECLARE
    NUMERO_BLOCCHI_ANIMALI_ATTIVI NUMBER(6,0);
    NUMERO_CELLE_IDRO_ATTIVE NUMBER(6,0);

BEGIN 
    IF :NEW.DATA_TERMINAZIONE IS NOT NULL
        THEN 

            IF :NEW.DATA_TERMINAZIONE < :NEW.DATA_ATTIVAZIONE
                THEN

                RAISE_APPLICATION_ERROR(
                    -20004,
                    'Non è possibile inserire una data di terminazione minore di quella di attivazione'
                );

            ELSE

            SELECT COUNT(*)
            INTO NUMERO_BLOCCHI_ANIMALI_ATTIVI
            FROM BLOCCO_ANIMALE BA
            WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND(
                    BA.DATA_SMONTAGGIO IS NULL
                    OR BA.DATA_SMONTAGGIO > :NEW.DATA_TERMINAZIONE
                );

            SELECT COUNT(*)
            INTO NUMERO_CELLE_IDRO_ATTIVE
            FROM CELLA_IDROPONICA CI 
            WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND(
                    CI.DATA_SMONTAGGIO IS NULL
                    OR CI.DATA_SMONTAGGIO > :NEW.DATA_TERMINAZIONE
                ); 

            IF NUMERO_BLOCCHI_ANIMALI_ATTIVI > 0 
                OR NUMERO_CELLE_IDRO_ATTIVE > 0
                THEN

                RAISE_APPLICATION_ERROR(
                    -20003,
                    'Per terminare la struttura è necessario terminare tutti i blocchi animali e le celle idroponiche al suo interno'
                );

                END IF;
            END IF;
        END IF;
   
    END;
/