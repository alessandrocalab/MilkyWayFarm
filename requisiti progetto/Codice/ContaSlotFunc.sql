--%%%%%   CONTEGGIO DEI POSTI DISPONIBILI
CREATE OR REPLACE FUNCTION conta_slot (data_ricevimento DATE) 
RETURN NUMBER
IS
--DECLARE
data_r 				DATE;
posti_disp		NUMBER(2);
posti_occ			NUMBER(2);
BEGIN
-- controllo che nel giorno scelto ci sia ricevimento
SELECT data_e_ora_i 	INTO  data_r
			FROM ricevimento
			WHERE TRUNC(data_e_ora_i)=TRUNC(data_ricevimento);
-- conto i posti disponibili e occupati
SELECT 	MAX(numero)-COUNT(hid)+COUNT(data_e_ora_d),
				COUNT(hid)-COUNT(data_e_ora_d)	
			INTO posti_disp, posti_occ
			FROM prenotazione 
			WHERE TRUNC(data)=TRUNC(data_r); 
-- restituisco il numero di posti disponibili
RETURN posti_disp;
EXCEPTION
WHEN 	NO_DATA_FOUND	THEN
			RETURN NULL;
END;
