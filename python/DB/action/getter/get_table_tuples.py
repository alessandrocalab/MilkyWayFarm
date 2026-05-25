from python.DB.action.getter.base import get_data_base

def get_table_data(table):
    return get_data_base(f"SELECT * FROM {table}") #tutorial SQL injection:


