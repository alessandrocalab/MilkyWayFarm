--%%%%%%% VISTA DEI RICEVIMENTI DISPONIBILI
CREATE OR REPLACE VIEW ric_disp AS
SELECT DISTINCT data_e_ora_i AS data,
	conta_slot(data_e_ora_i) AS disp 
	FROM ricevimento LEFT OUTER JOIN prenotazione 
										ON data_e_ora_i=data
	WHERE TRUNC(data_e_ora_i)>TRUNC(SYSDATE)
	AND TRUNC(data_e_ora_i)<TRUNC(SYSDATE)+21
	ORDER BY data_e_ora_i;