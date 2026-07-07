--FORNISCE IL BILANCIO DEI PRODOTTI

CREATE PROCEDURE BILANCIO 
AS 

    DATA_PRIMO_ANIMALE DATE;
    DATA_ULTIMA_PRODUZIONE DATE;
    TMP DATE;

    DATI_INSUFFICENTI EXCEPTION;

BEGIN 

    --CALCOLO I CONSUMI ANIMALI A PARTIRE DAL PRIMO 
    --GIORNO IN CUI ENTRA UN ANIMALE FINO ALL'ULTIMO
    --GIORNO DI UNA QUALSIASI PRODUZIONE

    SELECT MIN(DATA_ALLOCAZIONE)
    INTO DATA_PRIMO_ANIMALE
    FROM ANIMALE_ALLOCATO_BLOCCO;

    SELECT MAX(DATA_PRODUZIONE_AGRICOLA)
    INTO DATA_ULTIMA_PRODUZIONE
    FROM PRODUZIONE_AGRICOLA;

    SELECT MAX(DATA_PRODUZIONE)
    INTO TMP 
    FROM PRODUZIONE_ANIMALE;

    IF DATA_ULTIMA_PRODUZIONE IS NULL
        OR TMP > DATA_ULTIMA_PRODUZIONE
        THEN 
            DATA_ULTIMA_PRODUZIONE:=TMP;
    END IF;

    IF DATA_PRIMO_ANIMALE IS NULL
        OR DATA_ULTIMA_PRODUZIONE IS NULL
        OR DATA_ULTIMA_PRODUZIONE < DATA_PRIMO_ANIMALE
        THEN 
            RAISE DATI_INSUFFICENTI;
    END IF;

    DELETE FROM GIORNI_TEMP;

    FOR DELTA IN 0 .. (DATA_ULTIMA_PRODUZIONE-DATA_PRIMO_ANIMALE) LOOP 

        INSERT INTO GIORNI_TEMP VALUES (
            DATA_PRIMO_ANIMALE+DELTA
        );

    END LOOP;

    FOR RW IN(

        SELECT 
            CONSUMI_TOTALI.NOME_PRODOTTO,
            CONSUMI_TOTALI.QUANTITA_CONSUMATA,
            NVL(PAT.QUANTITA_PRODOTTA,0) AS QUANTITA_PRODOTTA,
            NVL(PAT.QUANTITA_PRODOTTA,0)-CONSUMI_TOTALI.QUANTITA_CONSUMATA AS BILANCIO
        FROM(
            SELECT NOME_PRODOTTO, SUM(QUANTITA_CONSUMATA) AS QUANTITA_CONSUMATA
            FROM
                (
                    SELECT *
                    FROM(

                        SELECT DCP.NOME_PRODOTTO, SUM(DCP.QUANTITA) AS QUANTITA_CONSUMATA
                        FROM DIETA_COMPRENDE_PRODOTTO DCP
                        JOIN 
                        ( --CON QUESTA TABELLA PRENDIAMO IN UN DETERMINATO GIORNO
                        --TUTTE LE DIETE SERVITE
                            SELECT 
                                DA.NOME_DIETA
                            FROM GIORNI_TEMP GT
                            
                            JOIN ANIMALE ANM 
                            ON EXISTS(
                                SELECT 1
                                FROM ANIMALE_ALLOCATO_BLOCCO AAB
                                WHERE AAB.ETICHETTA_ANIMALE=ANM.ETICHETTA
                                AND AAB.DATA_ALLOCAZIONE <= GT.DATA_GIORNO
                                AND(
                                    AAB.DATA_DEALLOCAZIONE IS NULL
                                    OR AAB.DATA_DEALLOCAZIONE > GT.DATA_GIORNO
                                )
                            )


                            JOIN STADIO_CRESCITA SC 
                            ON SC.NOME_TIPO_ANIMALE=ANM.NOME_TIPO_ANIMALE
                            AND SC.ETA_MINIMA_MESI=(
                                SELECT MAX(SC2.ETA_MINIMA_MESI)
                                FROM STADIO_CRESCITA SC2
                                WHERE SC2.NOME_TIPO_ANIMALE=ANM.NOME_TIPO_ANIMALE
                                AND SC2.ETA_MINIMA_MESI <=((EXTRACT(YEAR FROM(GT.DATA_GIORNO)))-ANM.ANNO_NASCITA)*12 
                                + ((EXTRACT(MONTH FROM(GT.DATA_GIORNO)))-ANM.MESE_NASCITA)
                            )

                            JOIN STADIO_CRESCITA_PREVEDE_DIETA DA --DIETA ATTIVA
                            ON DA.NOME_STADIO_CRESCITA=SC.NOME_STADIO_CRESCITA
                            AND DA.NOME_TIPO_ANIMALE=ANM.NOME_TIPO_ANIMALE
                            AND DA.DATA_INIZIO <= GT.DATA_GIORNO
                            AND(
                                DA.DATA_FINE IS NULL
                                OR DA.DATA_FINE > GT.DATA_GIORNO
                            )

                        )DS --DIETE SERVITE

                        ON DS.NOME_DIETA=DCP.NOME_DIETA

                        GROUP BY DCP.NOME_PRODOTTO

                        UNION ALL --UNIAMO CON I FARMACI UTILIZZATI

                        SELECT PA.NOME_PRODOTTO, SUM(PA.QUANTITA_GIORNALIERA) AS QUANTITA_CONSUMATA
                        FROM GIORNI_TEMP GT
                        JOIN PRESCRIZIONE_ANIMALE PA
                        ON PA.DATA_VISITA <= GT.DATA_GIORNO
                        AND PA.DATA_VISITA+PA.DURATA_GIORNI >= GT.DATA_GIORNO
                        GROUP BY PA.NOME_PRODOTTO
                    )

                    
            
                    UNION ALL 
                    
                    SELECT *
                    FROM CONSUMO_CICLI_COLTIVAZIONE_2
                )
                GROUP BY NOME_PRODOTTO
        )CONSUMI_TOTALI

        LEFT JOIN (
            SELECT *
            FROM PRODUZIONE_AGRICOLA_TOTALE 

            UNION ALL

            SELECT NOME_PRODOTTO,SUM(QUANTITA) AS QUANTITA_PRODOTTA
            FROM PRODUZIONE_ANIMALE
            GROUP BY NOME_PRODOTTO 
        ) PAT
        ON PAT.NOME_PRODOTTO=CONSUMI_TOTALI.NOME_PRODOTTO
    ) LOOP

        DBMS_OUTPUT.PUT_LINE('nome prodotto: '|| RW.NOME_PRODOTTO);
        DBMS_OUTPUT.PUT_LINE('quantita consumata: '|| RW.QUANTITA_CONSUMATA);
        DBMS_OUTPUT.PUT_LINE('quantita prodotta: '|| RW.QUANTITA_PRODOTTA);
        DBMS_OUTPUT.PUT_LINE('bilancio: '|| RW.BILANCIO);
        DBMS_OUTPUT.PUT_LINE('');

    END LOOP;

    COMMIT; --PER LIBERARE LA TABELLA GIORNI

EXCEPTION
    WHEN DATI_INSUFFICENTI
        THEN 
            ROLLBACK;
            RAISE_APPLICATION_ERROR(
                -20008,
                'Non ci sono dati a sufficenza per
                procedere con il bilancio'
            );

    END;
/
