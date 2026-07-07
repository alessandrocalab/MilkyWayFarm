--%%%%%%%%      TABELLA RICEVIMENTO
CREATE TABLE ricevimento        (
	data_e_ora_i    DATE    		PRIMARY KEY,
	durata          NUMBER(3) 	/* in minuti */,
CONSTRAINT  ore_ufficio CHECK 
		(TO_CHAR(data_e_ora_i,'HH24') BETWEEN 8 AND 17)
															);

CREATE UNIQUE INDEX data_univoca 
						ON ricevimento (TRUNC(data_e_ora_i));