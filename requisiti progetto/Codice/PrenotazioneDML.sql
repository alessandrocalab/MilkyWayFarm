--%%%%%%%%      AGGIUNTA DI UNA PRENOTAZIONE
INSERT INTO prenotazione VALUES (
TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI'),1,'easy',
TO_DATE('1-mag-2014 13:27','dd-mon-yyyy HH24:MI'),NULL,777256);

INSERT INTO prenotazione VALUES (
TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI'),2,'uneasy',
TO_DATE('2-mag-2014 16:31','dd-mon-yyyy HH24:MI'),NULL,241285);

INSERT INTO prenotazione VALUES (
TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI'),3,'hard',
TO_DATE('4-mag-2014 08:01','dd-mon-yyyy HH24:MI'),NULL,583089);

INSERT INTO prenotazione VALUES (
TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI'),4,'hard',
TO_DATE('2-mag-2014 05:50','dd-mon-yyyy HH24:MI'),NULL,668628);

INSERT INTO prenotazione VALUES (TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI'),5,NULL,NULL,NULL,NULL);

--%%%%%%%%      DISDETTA DI UNA PRENOTAZIONE
UPDATE prenotazione 
SET data_e_ora_d=TO_DATE('3-mag-2014 13:31','dd-mon-yyyy HH24:MI') 
WHERE data=TO_DATE('6-mag-2014 14:30','dd-mon-yyyy HH24:MI') 
AND hid=668628;
