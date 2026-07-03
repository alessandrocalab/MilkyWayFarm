--ATTIVATO SE VIENE TERMINATA UNA CELLA IDROPONICA
--CON CICLI DI COLTIVAZIONE ATTIVI OPPURE PRIMA
--DELLA SUA DATA DI ATTIVAZIONE

--ATTIVATO SE OCCUPA PIU SUPERFICIE DI QUELLA DISPONIBILE NELLA STRUTTURA

--ATTIVATO SE LA DATA DI MONTAGGIO È PIU VECCHIA DI QUELLA PIÙ RECENTE DI UN ALTRO BLOCCO/CELLA
--NELLA STESSA STRUTTURA

--ATTIVATO SE LA DATA DI MONTAGGIO È MENO RECENTE
--DI QUELLA DI ATTIVAZIONE DELLA STRUTTURA

CREATE TRIGGER TRG_CELLA_IDROPONICA
BEFORE INSERT OR UPDATE ON CELLA_IDROPONICA
FOR EACH ROW

DECLARE
    NUMERO_CICLI NUMBER(6,0);
    SUPERFICIE_STRUTTURA_DISPONIBILE NUMBER(8,2);
    DATA_ULTIMA_CELLA DATE;
    DATA_ATTIVAZIONE_STRUTTURA DATE;

BEGIN
    --Controllo data struttura
    SELECT DATA_ATTIVAZIONE
    INTO DATA_ATTIVAZIONE_STRUTTURA
    FROM STRUTTURA
    WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA;

    IF :NEW.DATA_MONTAGGIO < DATA_ATTIVAZIONE_STRUTTURA
        THEN
            RAISE_APPLICATION_ERROR(
                -20004,
                'Non è possibile inserire una data di montaggio meno recente di quella di attivazione della struttura ospitante'
            );
    END IF;



    --Controllo data blocco/cella più recente
    SELECT MAX(DATA_MONTAGGIO)
    INTO DATA_ULTIMA_CELLA 
    FROM(
        SELECT MAX(DATA_MONTAGGIO) AS DATA_MONTAGGIO
        FROM BLOCCO_ANIMALE BA
        WHERE BA.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
        
        UNION 

        SELECT MAX(DATA_MONTAGGIO) AS DATA_MONTAGGIO
        FROM CELLA_IDROPONICA CI
        WHERE CI.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
        AND CI.CODICE_CELLA_IDR<>:NEW.CODICE_CELLA_IDR
    );

    IF DATA_ULTIMA_CELLA IS NOT NULL 
        AND :NEW.DATA_MONTAGGIO < DATA_ULTIMA_CELLA 
        THEN
            RAISE_APPLICATION_ERROR(
                -20001,
                'Non è possibile inserire una data di montaggio meno recente dell ultimo blocco o cella nella stessa struttura'
            );
    END IF;


    --Controllo superficie
    SELECT S.SUPERFICIE_MQ - NVL((
        SELECT SUM(SUPERFICIE_MQ)
            FROM (
                SELECT SUPERFICIE_MQ
                FROM BLOCCO_ANIMALE BA
                WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND BA.DATA_MONTAGGIO <= :NEW.DATA_MONTAGGIO
                AND (
                    BA.DATA_SMONTAGGIO IS NULL
                    OR BA.DATA_SMONTAGGIO >= :NEW.DATA_MONTAGGIO
                )

                UNION ALL

                SELECT SUPERFICIE_MQ
                FROM CELLA_IDROPONICA CI
                WHERE NOME_STRUTTURA=:NEW.NOME_STRUTTURA
                AND CODICE_CELLA_IDR<>:NEW.CODICE_CELLA_IDR
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
                    'La superficie della cella idroponica supera quella disponibile della struttura in cui è contenuta'
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
            INTO NUMERO_CICLI
            FROM CICLO_COLTIVAZIONE CC
            WHERE CC.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
            AND CC.CODICE_CELLA_IDR=:NEW.CODICE_CELLA_IDR
                AND(
                    CC.DATA_FINE_EFFETTIVA IS NULL
                    OR CC.DATA_FINE_EFFETTIVA > :NEW.DATA_SMONTAGGIO
                );

           

            IF NUMERO_CICLI > 0 
                THEN

                RAISE_APPLICATION_ERROR(
                    -20003,
                    'Per terminare una cella idroponica è necessario chiudere tutti i cicli di coltivazione al suo interno'
                );

                END IF;
            END IF;
        END IF;
   
END;
/
