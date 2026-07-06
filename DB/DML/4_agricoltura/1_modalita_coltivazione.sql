--NOME_MODALITA_COLTIVAZIONE, NOME_PRODOTTO, PH_MIN, PH_MAX, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, IMPOLLINAZIONE, SISTEMA_ILLUMINAZIONE, ACQUA_ORA, ORE_LUCE_GIORNO, QUANTITA_SOLUZIONE_ORA
INSERT INTO MODALITA_COLTIVAZIONE VALUES (
    'Idro foglia base',
    'Soluzione nutritiva idroponica base',
    5.8,
    6.5,
    289,
    296,
    60,
    85,
    0,
    'LED_BIANCO',
    0.035,
    14,
    0.003
);

INSERT INTO MODALITA_COLTIVAZIONE VALUES (
    'Idro frutto concentrata',
    'Soluzione nutritiva concentrata',
    5.8,
    6.8,
    293,
    302,
    60,
    80,
    1,
    'LED_FULL',
    0.070,
    16,
    0.007
);

INSERT INTO MODALITA_COLTIVAZIONE VALUES (
    'Idro cereali base',
    'Soluzione nutritiva idroponica base',
    6.0,
    7.0,
    291,
    298,
    55,
    75,
    0,
    'LED_FULL',
    0.045,
    14,
    0.004
);

INSERT INTO MODALITA_COLTIVAZIONE VALUES (
    'Organica letame bovino',
    'Letame bovino',
    6.2,
    7.2,
    290,
    298,
    55,
    80,
    0,
    'LED_BIANCO',
    0.040,
    13,
    0.020
);

INSERT INTO MODALITA_COLTIVAZIONE VALUES (
    'Organica letame ovino',
    'Letame ovino',
    6.2,
    7.2,
    290,
    297,
    55,
    78,
    0,
    'LED_BIANCO',
    0.038,
    13,
    0.015
);

COMMIT;
