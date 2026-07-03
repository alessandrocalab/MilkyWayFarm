from python.DB.action.insert.base import insert_base

def insert_cycle_use_agri_production(
    DATA_INIZIO,
    CODICE_CELLA_IDR,
    NOME_STRUTTURA,
    DATA_PRODUZIONE_AGRICOLA,
    DATA_INIZIO_CICLO_COLTIVAZIONE,
    CODICE_CELLA_IDR_PROD_AGR,
    NOME_STRUTTURA_PROD_AGR,
    NOME_PRODOTTO,
    QUANTITA
):
    if hasattr(DATA_INIZIO,"strftime"):
        DATA_INIZIO=DATA_INIZIO.strftime("%Y-%m-%d")

    if hasattr(DATA_PRODUZIONE_AGRICOLA,"strftime"):
        DATA_PRODUZIONE_AGRICOLA=DATA_PRODUZIONE_AGRICOLA.strftime("%Y-%m-%d")

    if hasattr(DATA_INIZIO_CICLO_COLTIVAZIONE,"strftime"):
        DATA_INIZIO_CICLO_COLTIVAZIONE=DATA_INIZIO_CICLO_COLTIVAZIONE.strftime("%Y-%m-%d")

    insert_base(
        "INSERT INTO CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA VALUES ("
        f"DATE '{DATA_INIZIO}',"
        f"'{CODICE_CELLA_IDR}',"
        f"'{NOME_STRUTTURA}',"
        f"DATE '{DATA_PRODUZIONE_AGRICOLA}',"
        f"DATE '{DATA_INIZIO_CICLO_COLTIVAZIONE}',"
        f"'{CODICE_CELLA_IDR_PROD_AGR}',"
        f"'{NOME_STRUTTURA_PROD_AGR}',"
        f"'{NOME_PRODOTTO}',"
        f"{QUANTITA}"
        ")"
    )