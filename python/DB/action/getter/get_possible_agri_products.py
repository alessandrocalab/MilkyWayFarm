from python.DB.action.getter.base import get_data_base

def get_possible_agri_products(NOME_TIPO_COLTURA):
    return get_data_base(
        "SELECT NOME_PRODOTTO,QUANTITA_STIMATE_PER_KG_SEMI "
        "FROM TIPO_COLTURA_TIPO_PRODOTTO "
        f"WHERE NOME_TIPO_COLTURA='{NOME_TIPO_COLTURA}'"
    )