--DATA_INIZIO, CODICE_CELLA_IDR, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2024-11-25', '000A', 'Struttura Agricola', DATE '2025-05-24', 'Idro cereali base', 'Grano duro');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-06-01', '000A', 'Struttura Agricola', DATE '2025-09-29', 'Idro cereali base', 'Mais');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-10-10', '000A', 'Struttura Agricola', DATE '2026-04-07', 'Idro cereali base', 'Grano duro');

INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-11-15', '000B', 'Struttura Agricola', DATE '2025-12-30', 'Idro foglia base', 'Lattuga');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-01-05', '000B', 'Struttura Agricola', DATE '2026-04-05', 'Idro frutto concentrata', 'Pomodoro');

INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-10', '000A', 'Struttura Agricola II', DATE '2026-05-25', 'Idro foglia base', 'Lattuga');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-06-01', '000A', 'Struttura Agricola II', NULL, 'Idro cereali base', 'Mais');

INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-20', '000C', 'Struttura Agricola II', NULL, 'Organica letame bovino', 'Soia');

INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-11-25', '000A', 'Struttura Mista', DATE '2026-01-08', 'Idro foglia base', 'Lattuga');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-01-20', '000A', 'Struttura Mista', DATE '2026-04-19', 'Organica letame bovino', 'Pomodoro');

INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-12-10', '000B', 'Struttura Mista', DATE '2026-04-05', 'Idro cereali base', 'Mais');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-15', '000B', 'Struttura Mista', DATE '2026-05-30', 'Idro foglia base', 'Lattuga');

COMMIT;
