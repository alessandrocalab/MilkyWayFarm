--%%%%%%%%      TABELLA RICEVENDO
CREATE TABLE ricevendo  (
	hid							CHAR(6)					PRIMARY KEY,
	email   				VARCHAR2(30)    UNIQUE  NOT NULL,
	nome    				VARCHAR2(15)    NOT NULL,
	cognome 				VARCHAR2(15)    NOT NULL,
	matricola       CHAR(9)         UNIQUE,
	dipartimento    VARCHAR2(15),
	qualifica       VARCHAR2(10),    
CONSTRAINT qualifiche_ammesse CHECK(
		LOWER(qualifica) IN
			('dottorando','tesista','studente','altro')),
CONSTRAINT matr_ammesse CHECK(
		SUBSTR(matricola,1,4) IN
			('0123','0124','0108')),
CONSTRAINT dipartimenti_ammessi CHECK(
		INITCAP(dipartimento) IN
			('Mitolalia','Fantascienze','Xenologia')),
CONSTRAINT codici_dip CHECK(
		(SUBSTR(matricola,1,4)='0123' AND
		INITCAP(dipartimento)='Mitolalia')
		OR
		(SUBSTR(matricola,1,4)='0124' AND
		INITCAP(dipartimento)='Fantascienze')
		OR
		(SUBSTR(matricola,1,4)='0108' AND
		INITCAP(dipartimento)='Xenologia')),
CONSTRAINT email_mask CHECK(
		REGEXP_LIKE(email,'^\w+.*@{1}\w+.*$')), 
CONSTRAINT matricola_mask CHECK(
		REGEXP_LIKE(matricola,'^\d{4}[/]\d{4}$'))
                );