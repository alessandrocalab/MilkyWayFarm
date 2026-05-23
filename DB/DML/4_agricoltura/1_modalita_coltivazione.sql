--NOME_MODALITA_COLTIVAZIONE, NOME_PRODOTTO, PH_MIN, PH_MAX, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, IMPOLLINAZIONE, SISTEMA_ILLUMINAZIONE, ACQUA_ML_ORA, ORE_LUCE_GIORNO, QUANTITA_SOLUZIONE_ML_ORA
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro cereali base', 'Soluzione nutritiva idroponica base', 6.0, 7.0, 291, 297, 55, 75, 0, 'LED_FULL', 45.0, 14, 4.0);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro pomodoro standard', 'Soluzione nutritiva idroponica base', 5.8, 6.8, 293, 300, 60, 80, 1, 'LED_FULL', 70.0, 16, 6.0);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro pomodoro intensivo', 'Soluzione nutritiva concentrata', 5.8, 6.8, 295, 303, 65, 85, 1, 'LED_VIOLA', 85.0, 18, 7.5);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro lattuga rapida', 'Soluzione nutritiva idroponica base', 5.8, 6.5, 289, 295, 65, 85, 0, 'LED_BIANCO', 35.0, 14, 3.0);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro cucurbitacee', 'Soluzione nutritiva concentrata', 5.8, 6.8, 294, 301, 60, 80, 1, 'LED_FULL', 75.0, 16, 6.5);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro legumi base', 'Biofertilizzante microbico', 6.0, 7.0, 291, 298, 55, 75, 1, 'LED_FULL', 55.0, 14, 4.5);
INSERT INTO MODALITA_COLTIVAZIONE VALUES ('Idro soia nutriente', 'Soluzione nutritiva concentrata', 6.0, 7.0, 292, 300, 55, 75, 1, 'LED_FULL', 60.0, 14, 5.0);

COMMIT;