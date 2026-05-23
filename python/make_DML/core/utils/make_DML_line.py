#modulo per la costruzione di una riga DML 

def make_DML_line(table_name:str, values:list):
    DML_txt:str=f"INSERT INTO {table_name} VALUES ("

    for val in values:
        DML_txt+=f"{val}, "

    DML_txt=DML_txt[:-2] #togliamo gli ultimi due caratteri
    DML_txt+=");" #e terminaniamo con una parentesi di chiusura

    return DML_txt  


if __name__=="__main__":
    print(make_DML_line("TIPO_PRODOTTO",["latte", 23, "ml"]))