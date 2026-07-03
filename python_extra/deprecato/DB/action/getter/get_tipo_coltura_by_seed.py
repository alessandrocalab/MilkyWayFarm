from python.DB.action.getter.base import get_data_base

def get_tipo_coltura_by_seed(NOME_SEMI):
    return get_data_base(
        "SELECT NOME_TIPO_COLTURA "
        "FROM TIPO_COLTURA_USA_SEMI_DI_TIPO "
        f"WHERE UPPER(NOME_SEMI)=UPPER('{NOME_SEMI}')"
    )