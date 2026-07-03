from python.DB.action.update.base import update_base

def end_cycle(start_date,cell_code,structure,end_date):
    if hasattr(start_date,"strftime"):
        start_date=start_date.strftime("%Y-%m-%d")

    if hasattr(end_date,"strftime"):
        end_date=end_date.strftime("%Y-%m-%d")

    update_base(
        "UPDATE CICLO_COLTIVAZIONE "
        f"SET DATA_FINE_EFFETTIVA=DATE '{end_date}' "
        f"WHERE DATA_INIZIO=DATE '{start_date}' "
        f"AND CODICE_CELLA_IDR='{cell_code}' "
        f"AND NOME_STRUTTURA='{structure}'"
    )