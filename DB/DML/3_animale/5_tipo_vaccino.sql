--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML
INSERT INTO VACCINO VALUES ('Clostridiosi', 'Bovino', 'Svezzamento', NULL, NULL, NULL, 1, 6, 2.00);
INSERT INTO VACCINO VALUES ('Mastite', 'Bovino', 'Adulto', 'Clostridiosi', 'Svezzamento', 'Bovino', 0, 24, 5.00);

INSERT INTO VACCINO VALUES ('Newcastle', 'Gallina', 'Giovane', NULL, NULL, NULL, 1, 2, 0.30);
INSERT INTO VACCINO VALUES ('Bronchite infettiva', 'Gallina', 'Ovodeposizione', 'Newcastle', 'Giovane', 'Gallina', 1, 5, 0.25);

INSERT INTO VACCINO VALUES ('Mixomatosi', 'Coniglio', 'Svezzamento', NULL, NULL, NULL, 1, 1, 0.50);
INSERT INTO VACCINO VALUES ('Malattia emorragica', 'Coniglio', 'Giovane', 'Mixomatosi', 'Svezzamento', 'Coniglio', 1, 3, 0.50);

COMMIT;COMMIT;
