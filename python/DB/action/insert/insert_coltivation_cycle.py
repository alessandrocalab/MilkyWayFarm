from python.DB.action.insert.base import insert_base

def insert_coltivation_cycle(
    DATA_INIZIO,
    CODICE_CELLA_IDR,
    NOME_STRUTTURA,
    DATA_FINE_EFFETTIVA,
    NOME_MOD_COLTIVAZIONE,
    NOME_TIPO_COLTURA
):
    if hasattr(DATA_INIZIO,"strftime"):
        DATA_INIZIO=DATA_INIZIO.strftime("%Y-%m-%d")

    if hasattr(DATA_FINE_EFFETTIVA,"strftime"):
        DATA_FINE_EFFETTIVA=DATA_FINE_EFFETTIVA.strftime("%Y-%m-%d")

    if DATA_FINE_EFFETTIVA is None:
        DATA_FINE_EFFETTIVA_SQL="NULL"
    else:
        DATA_FINE_EFFETTIVA_SQL=f"DATE '{DATA_FINE_EFFETTIVA}'"

    insert_base(
        "INSERT INTO CICLO_COLTIVAZIONE VALUES ("
        f"DATE '{DATA_INIZIO}',"
        f"'{CODICE_CELLA_IDR}',"
        f"'{NOME_STRUTTURA}',"
        f"{DATA_FINE_EFFETTIVA_SQL},"
        f"'{NOME_MOD_COLTIVAZIONE}',"
        f"'{NOME_TIPO_COLTURA}'"
        ")"
    )