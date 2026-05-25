from python.DB.action.getter.base import get_data_base

def is_cella_working(CODICE_CELLA_IDR, NOME_STRUTTURA):
    is_working=get_data_base(
        f"SELECT 'True' "
        "FROM CICLO_COLTIVAZIONE CC "
        "WHERE CC.DATA_FINE_EFFETTIVA IS NULL "
        f"AND CC.CODICE_CELLA_IDR='{CODICE_CELLA_IDR}' "
        f"AND CC.NOME_STRUTTURA='{NOME_STRUTTURA}'"
    ) 

    if(is_working):
        return True
    return False
