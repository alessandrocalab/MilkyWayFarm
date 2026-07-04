--ATTIVATO SE VIENE TERMINATO UN BLOCCO ANIMALE
--CON ANIMALI ALL'INTERNO OPPURE PRIMA
--DELLA SUA DATA DI ATTIVAZIONE

--ATTIVATO SE OCCUPA PIU SUPERFICIE DI QUELLA DISPONIBILE NELLA STRUTTURA

--ATTIVATO SE LA DATA DI MONTAGGIO È PIU VECCHIA DI QUELLA PIÙ RECENTE DI UN ALTRO BLOCCO/CELLA
--NELLA STESSA STRUTTURA

--ATTIVATO SE LA DATA DI MONTAGGIO È MENO RECENTE
--DI QUELLA DI ATTIVAZIONE DELLA STRUTTURA

CREATE TRIGGER TRG_BLOCCO_ANIMALE
BEFORE INSERT OR UPDATE ON BLOCCO_ANIMALE
FOR EACH ROW

DECLARE
    NUMERO_ANIMALI NUMBER(6,0);
    SUPERFICIE_STRUTTURA_DISPONIBILE NUMBER(8,2);
    DATA_ULTIMO_BLOCCO DATE;
    DATA_ATTIVAZIONE_STRUTTURA DATE;

BEGIN
    --Controllo data struttura
    SELECT DATA_ATTIVAZIONE
    INTO DATA_ATTIVAZIONE_STRUTTURA
    FROM STRUTTURA
    WHERE STRUTTURA.NOME=:NEW.NOME_STRUTTURA;

    IF   :NEW.DATA_MONTAGGIO < DATA_ATTIVAZIONE_STRUTTURA
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Non è possibile inserire una data di montaggio meno recente di quella di attivazione della struttura ospitante'
            );
    END IF;



    --Controllo data blocco/cella più recente
    SELECT MAX(DATA_MONTAGGIO)
    INTO DATA_ULTIMO_BLOCCO 
    FROM(
        SELECT MAX(DATA_MONTAGGIO)
        FROM CELLA_IDROPONICA CI
        WHERE CI.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
        
        UNION 

        SELECT MAX(DATA_MONTAGGIO)
        FROM BLOCCO_ANIMALE BA
        WHERE BA.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
        AND BA.NUMERO_BLOCCO<>:NEW.NUMERO_BLOCCO
    );

    IF DATA_ULTIMO_BLOCCO IS NOT NULL 
        AND :NEW.DATA_MONTAGGIO < DATA_ULTIMO_BLOCCO 
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Non è possibile inserire una data di montaggio meno recente dell’ultimo blocco nella stessa struttura'
            );
    END IF;


    --Controllo superficie
    SELECT S.SUPERFICIE_MQ - NVL((
        SELECT SUM(SUPERFICIE_MQ)
            FROM (
                SELECT SUPERFICIE_MQ
                FROM BLOCCO_ANIMALE BA
                WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND NUMERO_BLOCCO<>:NEW.NUMERO_BLOCCO
                AND BA.DATA_MONTAGGIO <= :NEW.DATA_MONTAGGIO
                AND (
                    BA.DATA_SMONTAGGIO IS NULL
                    OR BA.DATA_SMONTAGGIO >= :NEW.DATA_MONTAGGIO
                )

                UNION ALL

                SELECT SUPERFICIE_MQ
                FROM CELLA_IDROPONICA CI
                WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND CI.DATA_MONTAGGIO <= :NEW.DATA_MONTAGGIO
                AND (
                    CI.DATA_SMONTAGGIO IS NULL
                    OR CI.DATA_SMONTAGGIO >= :NEW.DATA_MONTAGGIO
                )

            )
        ), 0)
    INTO SUPERFICIE_STRUTTURA_DISPONIBILE
    FROM STRUTTURA S
    WHERE S.NOME_STRUTTURA=:NEW.NOME_STRUTTURA;

    IF :NEW.SUPERFICIE_MQ > SUPERFICIE_STRUTTURA_DISPONIBILE
        THEN

            RAISE_APPLICATION_ERROR(
                    -20001,
                    'La superficie del blocco animale supera quella disponibile della struttura in cui è contenuto'
                );
    END IF;




    
    IF :NEW.DATA_SMONTAGGIO IS NOT NULL --CONTROLLO SU DATA SMONTAGGIO
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
   
END;
/