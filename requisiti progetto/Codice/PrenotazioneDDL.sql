--%%%%%%%%      TABELLA PRENOTAZIONE
CREATE TABLE prenotazione       (
	data  					DATE,
	numero 					NUMBER(2) /*inutile CHECK (numero<21)*/,
	classificazione VARCHAR2(11)    
				CHECK (LOWER(classificazione) IN
				('easy','not so easy','uneasy','hard','very hard')),
	data_e_ora_p    DATE,
	data_e_ora_d    DATE,
	hid  CHAR(6)    /*rendendolo obbligatorio 
				si andrebbe in contrasto con la procedura prenota*/,
CONSTRAINT pkp  PRIMARY KEY (data,numero),
CONSTRAINT fkrm FOREIGN KEY (data)  
			REFERENCES ricevimento(data_e_ora_i) ON DELETE CASCADE,
CONSTRAINT fkrv FOREIGN KEY (hid) 
			REFERENCES ricevendo(hid)  ON DELETE SET NULL,
CONSTRAINT fwd_time     CHECK (data_e_ora_d>data_e_ora_p)  
/*la disdetta deve essere successiva alla prenotazione*/
                   		     );

CREATE UNIQUE INDEX no_stalking ON prenotazione 
(CASE WHEN data IS NULL OR hid IS NULL THEN NULL ELSE data END,
 CASE WHEN hid IS NULL OR data IS NULL THEN NULL ELSE hid END);

