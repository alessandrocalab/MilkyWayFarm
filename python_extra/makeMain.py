import os


MAIN_START=(
        "SET SQLBLANKLINES ON \n--senza interpreta male le righe vuote\n\n"
    )

MAIN_DELETE=(
        "--Eliminazione schema precedente"
        "\n\n@../drop_all.sql\n\n"
    )
MAIN_END="\n\nCOMMIT;"

MAIN_DDL_PATH="./DB/DDL/main.sql"
MAIN_DML_PATH="./DB/DML/main.sql"

DDL_PATH="./DB/DDL/"
DML_PATH="./DB/DML/"


def getNum(nome_file:str):
    return int(nome_file.split("_")[0])


def makeMain(base_path:str, main_path:str, tipo:str):
    main_text=MAIN_START
    if tipo=="DDL":
        main_text+=MAIN_DELETE
    num_tabelle=0

    dirs=os.listdir(base_path)

    tmp_dirs=[]

    for dir in dirs:
        dir_path=base_path+dir

        if not os.path.isdir(dir_path):
            continue

        tmp_dirs.append(dir)

    dirs=sorted(tmp_dirs, key=getNum)

    for dir in dirs:
        if dir=="main.sql":
            continue

        dir_path=base_path+dir

        if not os.path.isdir(dir_path):
            continue

        sql_files=os.listdir(dir_path)
        sql_files=sorted(sql_files, key=getNum)

        main_text+=f"\n--Sezione: {dir}\n\n"

        for sql in sql_files:
            if not sql.lower().endswith(".sql"):
                continue

            num_tabelle+=1
            main_text+=f"@{dir}/{sql}\n"

    main_text+=MAIN_END

    with open(main_path, "w") as f:
        f.write(main_text)

    return num_tabelle


num_tabelle_DDL=makeMain(DDL_PATH, MAIN_DDL_PATH, "DDL")
num_tabelle_DML=makeMain(DML_PATH, MAIN_DML_PATH, "DML")

print(f"main DDL creato con successo, {num_tabelle_DDL} tabelle")
print(f"main DML creato con successo, {num_tabelle_DML} tabelle")
