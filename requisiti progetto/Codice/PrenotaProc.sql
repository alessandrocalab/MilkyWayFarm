--%%%%%   PRENOTAZIONE RICEVIMENTO, lanciata dall'utente DISCENTE
CREATE OR REPLACE PROCEDURE prenota (mio_ricevimento DATE, mio_hid ricevendo.hid%TYPE) 
IS
--DECLARE
mia_data 					DATE;
mio_numero				NUMBER(2);
ora_appuntamento	DATE;
troppo_tardi			EXCEPTION;
troppo_presto			EXCEPTION;
tempus_fugit			EXCEPTION;
BEGIN
-- controllo che nel giorno scelto ci sia ricevimento
SELECT data_e_ora_i 	INTO  mia_data
		FROM ricevimento
		WHERE TRUNC(data_e_ora_i)=TRUNC(mio_ricevimento);
-- controllo che la prenotazione avvenga con al massimo tre settimane e minimo un giorno di anticipo 
IF TRUNC(mia_data)=TRUNC(SYSDATE) 	THEN
			RAISE troppo_tardi;
ELSIF mia_data<SYSDATE 		THEN
			RAISE tempus_fugit;
ELSIF mia_data>TRUNC(SYSDATE)+21 	THEN
			RAISE troppo_presto;
END IF;
-- Seleziono il primo slot disponibile e lo blocco, in modo da evitare che venga prenotato da altri
SELECT numero	INTO mio_numero
	FROM prenotazione 
	WHERE data = mia_data
	AND hid IS NULL 
	AND ROWNUM = 1
	ORDER BY numero
	FOR UPDATE WAIT 30; /*questa clausola serve a mettere un lock sulla riga*/
-- prenoto lo slot bloccato in precedenza
UPDATE prenotazione SET data_e_ora_p=SYSDATE, hid=mio_hid
	WHERE data = mia_data AND numero = mio_numero;
-- calcolo l'ora dell'appuntamento
ora_appuntamento:=mia_data+1/144*(mio_numero-1);
-- confermo
COMMIT;
-- stampo a video la conferma e l' ora dell'appuntamento
DBMS_OUTPUT.PUT_LINE('L''appuntamento e'' confermato. Presentati alle ore: ' || TO_CHAR(ora_appuntamento,'HH24:MI'));

EXCEPTION
WHEN 	NO_DATA_FOUND	THEN
		DBMS_OUTPUT.PUT_LINE('Nel giorno che hai scelto non c''e'' ricevimento oppure e'' gia'' saturo. Scegli un altro giorno.');
WHEN	troppo_tardi		THEN
		DBMS_OUTPUT.PUT_LINE('Occorre almeno un giorno di anticipo per prenotarsi. Scegli un altro giorno.');
WHEN	tempus_fugit		THEN
		DBMS_OUTPUT.PUT_LINE('Non e'' possibile prenotarsi per ricevimenti che si sono gia'' tenuti.Scegli un altro giorno.');
WHEN	troppo_presto		THEN
		DBMS_OUTPUT.PUT_LINE('Ci si puo'' prenotare con al massimo tre settimane di anticipo. Scegli un altro giorno.');
END;
