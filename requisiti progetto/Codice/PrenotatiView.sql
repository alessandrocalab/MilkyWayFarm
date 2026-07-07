--%%%%%%% VISTA DEI PRENOTATI PER IL PROSSIMO RICEVIMENTO
CREATE OR REPLACE VIEW prenotati AS
SELECT hid,email, data, 
				TO_CHAR(data+(numero-1)*1/144,'HH24:MI') AS ora,
				classificazione AS class  
	FROM ricevendo rdo NATURAL JOIN prenotazione pre
	WHERE pre.data_e_ora_d IS NULL
	AND pre.data>SYSDATE
	AND NOT EXISTS (
		SELECT * FROM ricevimento rto
			WHERE rto.data_e_ora_i <pre.data
			AND rto.data_e_ora_i >SYSDATE);