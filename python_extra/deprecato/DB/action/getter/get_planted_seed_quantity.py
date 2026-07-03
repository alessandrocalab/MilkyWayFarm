from python.DB.action.getter.base import get_data_base

def get_planted_seed_quantity(DATA_INIZIO,CODICE_CELLA_IDR,NOME_STRUTTURA):
    DATA_INIZIO=DATA_INIZIO.strftime("%Y-%m-%d")

    return get_data_base(
        "SELECT "
        "("
            "SELECT NVL(SUM(CCSM.QUANTITA),0) "
            "FROM CICLO_COLT_UTILIZZA_SEMI_MISSIONE CCSM "
            f"WHERE CCSM.DATA_INIZIO=DATE '{DATA_INIZIO}' "
            f"AND CCSM.NOME_STRUTTURA='{NOME_STRUTTURA}' "
            f"AND CCSM.CODICE_CELLA_IDR='{CODICE_CELLA_IDR}'"
        ")"
        "+"
        "("
            "SELECT NVL(SUM(CCPA.QUANTITA),0) "
            "FROM CICLO_COLT_UTILIZZA_PRODUZIONE_AGRICOLA CCPA "
            f"WHERE CCPA.DATA_INIZIO=DATE '{DATA_INIZIO}' "
            f"AND CCPA.NOME_STRUTTURA='{NOME_STRUTTURA}' "
            f"AND CCPA.CODICE_CELLA_IDR='{CODICE_CELLA_IDR}'"
        ") AS QUANTITA "
        "FROM DUAL"
    )