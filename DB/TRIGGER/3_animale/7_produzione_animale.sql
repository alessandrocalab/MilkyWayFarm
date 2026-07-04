--Attivato se la data di produzione 
--non è valida, che dunque non vi è in quella data
--un animale capace di produrre quel prodotto

CREATE TRIGGER TRG_PRODUZIONE_ANIMALE
BEFORE INSERT OR UPDATE ON PRODUZIONE_ANIMALE
FOR EACH ROW

DECLARE
    IS_VALID NUMBER(6,0);
    DATA_INVALIDA EXCEPTION;

BEGIN 

    SELECT COUNT(*)
    INTO IS_VALID
    FROM ANIMALE_ALLOCATO_BLOCCO AAB
    JOIN ANIMALE A
    ON A.ETICHETTA=AAB.ETICHETTA_ANIMALE
    JOIN STADIO_CRESCITA SC
    ON SC.NOME_TIPO_ANIMALE=A.NOME_TIPO_ANIMALE
    JOIN PRODOTTO_DA_STADIO_CRESCITA PDSC 
    ON A.NOME_TIPO_ANIMALE=PDSC.NOME_TIPO_ANIMALE
    AND SC.NOME_STADIO_CRESCITA=PDSC.NOME_STADIO_CRESCITA

    WHERE AAB.NUMERO_BLOCCO=:NEW.NUMERO_BLOCCO
    AND AAB.NOME_STRUTTURA=:NEW.NOME_STRUTTURA
    AND AAB.DATA_ALLOCAZIONE <= :NEW.DATA_PRODUZIONE
    AND(
        AAB.DATA_DEALLOCAZIONE IS NULL 
        OR AAB.DATA_DEALLOCAZIONE > :NEW.DATA_PRODUZIONE
    )
    AND PDSC.NOME_PRODOTTO=:NEW.NOME_PRODOTTO
    AND (((EXTRACT(YEAR FROM :NEW.DATA_PRODUZIONE)-A.ANNO_NASCITA)*12)+
        ((EXTRACT(MONTH FROM :NEW.DATA_PRODUZIONE))-A.MESE_NASCITA)) 
        >= SC.ETA_MINIMA_MESI;
    --Assumiamo che i stadi crescita successivi incorporano i possibili prodotti
    --dei stadi crescita precedenti (quindi un adulto produce sempre almeno quello
    --che produce un cucciolo (di solito i cuccioli producono solo letame quindi non
    --si crea alcun problema)), in questo modo rendiamo la query molto più efficente

    IF IS_VALID = 0
        THEN 
            RAISE DATA_INVALIDA;
    END IF;

EXCEPTION

    WHEN DATA_INVALIDA
        THEN 
            RAISE_APPLICATION_ERROR(
                -20001,
                'Non vi è alcun animale nel blocco capace di produrre quel prodotto nella data inserita'
            );
END;
/