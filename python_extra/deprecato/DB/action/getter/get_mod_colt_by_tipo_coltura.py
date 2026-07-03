from python.DB.action.getter.base import get_data_base

def get_mod_colt_by_tipo_coltura(NOME_TIPO_COLTURA):
    return get_data_base(
        "SELECT TC.NOME_MODALITA_COLTIVAZIONE "
        "FROM TIPO_COLT_ACCETTA_MOD_COLT TC "
        f"WHERE UPPER(TC.NOME_TIPO_COLTURA)=UPPER('{NOME_TIPO_COLTURA}')"
    )