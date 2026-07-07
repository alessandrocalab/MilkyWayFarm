--%%%%%   DISDETTA RICEVIMENTO, lanciata dall'utente DISCENTE
CREATE OR REPLACE PROCEDURE disdici (mio_ricevimento DATE, mio_hid ricevendo.hid%TYPE) 
IS
--DECLARE
mio_numero				NUMBER(2);
troppo_tardi			EXCEPTION;
BEGIN
-- controllo che il ricevendo sia effettivamente prenotato
SELECT numero 	INTO  mio_numero
			FROM prenotazione
			WHERE TRUNC(data)=TRUNC(mio_ricevimento)
			AND hid=mio_hid;
-- controllo che la disdetta avvenga al piu' tardi con due giorni di anticipo 
IF TRUNC(mio_ricevimento-3)<TRUNC(SYSDATE) THEN
			RAISE troppo_tardi;
END IF;
-- Disdico
UPDATE prenotazione SET data_e_ora_d=SYSDATE
			WHERE TRUNC(data) = TRUNC(mio_ricevimento)
			AND numero = mio_numero;
-- confermo
COMMIT;
-- stampo a video la conferma 
DBMS_OUTPUT.PUT_LINE('L''appuntamento e'' disdetto.');

EXCEPTION
WHEN 	NO_DATA_FOUND	THEN
		DBMS_OUTPUT.PUT_LINE('Nel giorno che hai scelto non hai un prenotazione.');
WHEN	troppo_tardi		THEN
		DBMS_OUTPUT.PUT_LINE('Non puoi disdire con meno di due giorni di anticipo.');
END;
