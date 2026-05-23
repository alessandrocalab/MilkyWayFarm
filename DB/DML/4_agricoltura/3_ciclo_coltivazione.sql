--DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, QUANTITA_SEMI, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2023-07-01', '000A', 'A00A', 'Struttura Agricola', DATE '2023-12-28', 0.6, 'Idro cereali base', 'Grano duro');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2024-03-01', '000A', 'A00A', 'Struttura Agricola', DATE '2024-05-30', 0.3, 'Idro pomodoro standard', 'Pomodoro');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-06-01', '000A', 'A00A', 'Struttura Agricola', DATE '2025-09-29', 0.4, 'Idro cereali base', 'Mais');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2023-07-05', '000B', 'A00A', 'Struttura Agricola', DATE '2023-11-02', 0.5, 'Idro cereali base', 'Mais');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2024-01-15', '000B', 'A00A', 'Struttura Agricola', DATE '2024-05-14', 0.35, 'Idro soia nutriente', 'Soia');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-01-10', '000B', 'A00A', 'Struttura Agricola', DATE '2025-02-24', 0.2, 'Idro lattuga rapida', 'Lattuga');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2023-08-01', '000C', 'A00B', 'Struttura Agricola', DATE '2023-10-27', 0.3, 'Idro pomodoro intensivo', 'Pomodoro');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2024-04-01', '000C', 'A00B', 'Struttura Agricola', DATE '2024-06-28', 0.2, 'Idro legumi base', 'Fagiolo');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2023-07-10', '000D', 'A00C', 'Struttura Agricola', DATE '2023-10-18', 0.2, 'Idro tuberi substrato', 'Patata');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2024-02-01', '000D', 'A00C', 'Struttura Agricola', DATE '2024-04-21', 0.8, 'Idro radici substrato', 'Carota');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2025-05-10', '000D', 'A00C', 'Struttura Agricola', DATE '2025-07-04', 0.4, 'Idro cucurbitacee', 'Zucchina');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-05', '001A', 'A00A', 'Struttura Agricola II', DATE '2026-05-20', 0.3, 'Idro lattuga rapida', 'Lattuga');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-05-21', '001A', 'A00A', 'Struttura Agricola II', NULL, 0.3, 'Idro legumi base', 'Fagiolo');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-05', '001B', 'A00A', 'Struttura Agricola II', NULL, 0.5, 'Idro cereali base', 'Mais');
INSERT INTO CICLO_COLTIVAZIONE VALUES (DATE '2026-04-04', '001C', 'A00A', 'Struttura Agricola II', NULL, 0.2, 'Idro tuberi substrato', 'Patata');

COMMIT;