from python.DB.action.insert.base import insert_base

def insert_cycle_use_mission_seed(DATA_INIZIO,CODICE_CELLA_IDR,NOME_STRUTTURA,NOME_SEMI,DATA_ARRIVO_SEMI,QUANTITA):
    if hasattr(DATA_INIZIO,"strftime"):
        DATA_INIZIO=DATA_INIZIO.strftime("%Y-%m-%d")

    if hasattr(DATA_ARRIVO_SEMI,"strftime"):
        DATA_ARRIVO_SEMI=DATA_ARRIVO_SEMI.strftime("%Y-%m-%d")

    insert_base(
        "INSERT INTO CICLO_COLT_UTILIZZA_SEMI_MISSIONE VALUES ("
        f"DATE '{DATA_INIZIO}',"
        f"'{CODICE_CELLA_IDR}',"
        f"'{NOME_STRUTTURA}',"
        f"'{NOME_SEMI}',"
        f"DATE '{DATA_ARRIVO_SEMI}',"
        f"{QUANTITA}"
        ")"
    )