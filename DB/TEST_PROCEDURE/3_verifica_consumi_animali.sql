SET SERVEROUTPUT ON

--Test procedura VERIFICA_CONSUMI_ANIMALI


--Deve andare perche nell'intervallo ci sono animali allocati,
--diete attive e prescrizioni veterinarie attive

BEGIN
    VERIFICA_CONSUMI_ANIMALI(
        DATE '2028-01-20',
        DATE '2036-01-22'
    );
END;
/

