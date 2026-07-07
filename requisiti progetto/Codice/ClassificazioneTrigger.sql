--%%%%%   IMPOSTA AUTOMATICAMENTE IL LIVELLO DI DIFFICOLTA'
CREATE OR REPLACE TRIGGER pop_classificazione
BEFORE UPDATE OF hid ON prenotazione 
FOR EACH ROW
DECLARE
punti_qualifica		NUMBER(1);
punti_turno				NUMBER(1);
BEGIN
-- calcolo i punti per la qualifica del ricevendo
SELECT DECODE(LOWER(qualifica),'dottorando',4,'tesista',3,'studente',2,'altro',1) INTO  punti_qualifica
		FROM ricevendo
		WHERE hid=:NEW.hid;
-- calcolo i punti per il turno
SELECT CEIL(:NEW.numero/4) INTO punti_turno FROM DUAL;
-- assegno il livello di difficolta'
SELECT DECODE(CEIL(punti_qualifica*punti_turno/4),1,'easy',2,'not so easy',3,'uneasy',4,'hard',5,'very hard') 
	INTO :NEW.classificazione FROM DUAL; 
EXCEPTION
WHEN 	NO_DATA_FOUND	THEN
		RAISE_APPLICATION_ERROR(-20001,'hid insistente');
END;
