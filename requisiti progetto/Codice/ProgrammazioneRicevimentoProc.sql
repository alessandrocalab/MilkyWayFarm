--%%%%%   PROGRAMMAZIONE RICEVIMENTO, lanciabile dall'utente DOCENTE
CREATE OR REPLACE PROCEDURE prog_ric 
	(data DATE, durata_in ricevimento.durata%TYPE) 
IS
--DECLARE
durata 						NUMBER :=durata_in;
sabato_fascista		EXCEPTION;
BEGIN
IF TO_CHAR(data,'D')=6 OR TO_CHAR(data,'D')=7 THEN
	RAISE 	sabato_fascista; 
END IF;
IF durata<30 THEN
	DBMS_OUTPUT.PUT_LINE('Il ricevimento dura minimo 30 minuti');
	durata:=30;
ELSIF durata>200 THEN
	DBMS_OUTPUT.PUT_LINE('Il ricevimento dura massimo 200 minuti');
	durata:=200;
ELSE
	durata:=ROUND(durata/10)*10;
	DBMS_OUTPUT.PUT_LINE('La durata prevista e'' di '|| durata ||' minuti');
END IF;
INSERT INTO ricevimento VALUES(data,durata);
FOR i IN 1..(durata/10) LOOP 
	INSERT INTO prenotazione VALUES(data,i,NULL,NULL,NULL,NULL);
END LOOP;
/*il ciclo FOR si puo' sostituire con un unico INSERT usando una query gerarchica*/
EXCEPTION
WHEN sabato_fascista THEN
	RAISE_APPLICATION_ERROR(-20002,'Non e'' possibile fissare i ricevimenti il sabato o la domenica.');
END;
