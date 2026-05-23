#modulo per parsing e ottenimento nome tabella e nome attributi

def getTableData(path):
    with open(path, "r") as f:
        raw_table=f.read()
    
    table_lines=raw_table.split("\n")
    
    table_name=(table_lines[0].split(" ")[2])[:-1] #eliminiamo la parentesi finale
    table_attr=[]
    table_lines=table_lines[1:] #escludiamo la prima riga con il nome della tabella

    for line in table_lines:
        line=line.strip()

        if not line:
            continue

        if line.startswith("--"):
            break
        
        if line.startswith(")"):
            break

        if line.startswith("CONSTRAINT"):
            continue
        nome=line.split(" ")[0]
        table_attr.append(nome)

    return table_name, table_attr

if __name__=="__main__":
    print(getTableData("./DB/DDL/1_prodotto/1_tipo_prodotto.sql"))