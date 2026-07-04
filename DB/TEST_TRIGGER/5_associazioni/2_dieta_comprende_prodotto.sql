--Deve essere bloccato perchè il Fagiolo contiene sostanze
--a cui lo stadio Vitello Bovino è intollerante
INSERT INTO DIETA_COMPRENDE_PRODOTTO VALUES (
    'Fagiolo',
    'Dieta Bovino Vitello',
    1.00
);


--Deve essere bloccato perchè il prodotto non è edibile
INSERT INTO DIETA_COMPRENDE_PRODOTTO VALUES (
    'Letame bovino',
    'Dieta Bovino Adulto',
    1.00
);
