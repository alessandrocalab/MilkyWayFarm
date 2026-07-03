--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML
INSERT INTO VACCINO VALUES ('Clostridiosi', 'Bovino', 'Vitello', NULL, NULL, NULL, 1, 6, 2.00);
INSERT INTO VACCINO VALUES ('Mastite', 'Bovino', 'Adulto', 'Clostridiosi', 'Vitello', 'Bovino', 0, 24, 5.00);

INSERT INTO VACCINO VALUES ('Newcastle', 'Gallina', 'Giovane', NULL, NULL, NULL, 1, 2, 0.30);
INSERT INTO VACCINO VALUES ('Bronchite infettiva', 'Gallina', 'Adulto', 'Newcastle', 'Giovane', 'Gallina', 1, 5, 0.25);

INSERT INTO VACCINO VALUES ('Mixomatosi', 'Coniglio', 'Cucciolo', NULL, NULL, NULL, 1, 1, 0.50);
INSERT INTO VACCINO VALUES ('Malattia emorragica', 'Coniglio', 'Giovane', 'Mixomatosi', 'Cucciolo', 'Coniglio', 1, 3, 0.50);

COMMIT;
