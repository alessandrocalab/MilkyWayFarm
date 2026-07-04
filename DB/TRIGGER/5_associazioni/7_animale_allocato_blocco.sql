--Attivato se l'animale è allocato
--in un blocco non compatibile con
--il tipo di animale

CREATE TRIGGER TRG_ANIMALE_ALLOCATO_BLOCCO_COMPATIBILE
BEFORE INSERT OR UPDATE ON ANIMALE_ALLOCATO_BLOCCO 
FOR EACH ROW 


--Attivaso se non vi è spazio disponibile
--all'interno del blocco

--Attivato se vi sono incompatibilità
--sulle date di allocazione

--Attivato se l'allocazione non è
--la più recente per l'animale (greedy choice)