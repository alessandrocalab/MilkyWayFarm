--%%%%%   CALCOLA AUTOMATICAMENTE L'ID DEL RICEVENDO
CREATE OR REPLACE TRIGGER email2hid
BEFORE INSERT ON ricevendo 
FOR EACH ROW
BEGIN
-- calcolo e assegno il valore della funzione hash 
SELECT ORA_HASH(LOWER(:NEW.email),999999) INTO :NEW.hid FROM DUAL;
-- stampo a video il valore di hid
DBMS_OUTPUT.PUT_LINE('L''hash ID di '||:NEW.email|| ' e'' '|| :NEW.hid);
END;
