import os


MAIN_START=(
        "SET SQLBLANKLINES ON \n--senza interpreta male le righe vuote\n\n"
    )

MAIN_DELETE=(
        "--Eliminazione schema precedente"
        "\n\n@../drop_all.sql\n\n"
    )
MAIN_DELETE_TOTALE=(
        "--Eliminazione schema precedente"
        "\n\n@drop_all.sql\n\n"
    )
MAIN_END="\n\nCOMMIT;\n"

MAIN_DDL_PATH="./DB/DDL/main.sql"
MAIN_DML_PATH="./DB/DML/main.sql"
MAIN_VISTA_PATH="./DB/VISTA/main.sql"
MAIN_TRIGGER_PATH="./DB/TRIGGER/main.sql"
MAIN_TOTALE_PATH="./DB/main.sql"

DDL_PATH="./DB/DDL/"
DML_PATH="./DB/DML/"
VISTA_PATH="./DB/VISTA/"
TRIGGER_PATH="./DB/TRIGGER/"


def getNum(nome_file:str):
    return int(nome_file.split("_")[0])


def getSqlFiles(dir_path:str, dir:str):
    sql_files=os.listdir(dir_path)
    sql_files=sorted(sql_files, key=getNum)

    if dir=="1_prodotto":
        sql_files=sorted(
            sql_files,
            key=lambda sql: 0 if sql=="3_unita_di_misura.sql" else getNum(sql)
        )

    return sql_files


def getMainBody(base_path:str, path_prefix:str=""):
    main_text=""
    num_tabelle=0

    dirs=os.listdir(base_path)

    tmp_dirs=[]
    tmp_sql_files=[]

    for dir in dirs:
        dir_path=base_path+dir

        if os.path.isfile(dir_path) and dir.lower().endswith(".sql") and dir!="main.sql":
            tmp_sql_files.append(dir)
            continue

        if not os.path.isdir(dir_path):
            continue

        tmp_dirs.append(dir)

    sql_files=sorted(tmp_sql_files, key=getNum)

    if len(sql_files) != 0:
        nome_sezione=os.path.basename(os.path.normpath(base_path))
        main_text+=f"\n--Sezione: {nome_sezione}\n\n"

        for sql in sql_files:
            num_tabelle+=1
            main_text+=f"@{path_prefix}{sql}\n"

    dirs=sorted(tmp_dirs, key=getNum)

    for dir in dirs:
        if dir=="main.sql":
            continue

        dir_path=base_path+dir

        if not os.path.isdir(dir_path):
            continue

        sql_files=getSqlFiles(dir_path, dir)

        main_text+=f"\n--Sezione: {dir}\n\n"

        for sql in sql_files:
            if not sql.lower().endswith(".sql"):
                continue

            num_tabelle+=1
            main_text+=f"@{path_prefix}{dir}/{sql}\n"

    return main_text, num_tabelle


def makeMain(base_path:str, main_path:str, tipo:str, path_prefix:str=""):
    main_text=MAIN_START
    if tipo=="DDL":
        main_text+=MAIN_DELETE

    main_body, num_tabelle=getMainBody(base_path, path_prefix)
    main_text+=main_body
    main_text+=MAIN_END

    with open(main_path, "w") as f:
        f.write(main_text)

    return num_tabelle


def makeMainTotale():
    main_text=MAIN_START+MAIN_DELETE_TOTALE

    main_text+="\n--Sezione: DDL\n\n"
    main_body, num_tabelle_DDL=getMainBody(DDL_PATH, "DDL/")
    main_text+=main_body

    main_text+="\n--Sezione: DML\n\n"
    main_body, num_tabelle_DML=getMainBody(DML_PATH, "DML/")
    main_text+=main_body

    main_body, num_tabelle_VISTA=getMainBody(VISTA_PATH, "VISTA/")
    main_text+=main_body

    main_text+="\n--Sezione: TRIGGER\n\n"
    main_body, num_tabelle_TRIGGER=getMainBody(TRIGGER_PATH, "TRIGGER/")
    main_text+=main_body

    main_text+=MAIN_END

    with open(MAIN_TOTALE_PATH, "w") as f:
        f.write(main_text)

    return num_tabelle_DDL, num_tabelle_DML, num_tabelle_VISTA, num_tabelle_TRIGGER


num_tabelle_DDL=makeMain(DDL_PATH, MAIN_DDL_PATH, "DDL")
num_tabelle_DML=makeMain(DML_PATH, MAIN_DML_PATH, "DML")
num_tabelle_VISTA=makeMain(VISTA_PATH, MAIN_VISTA_PATH, "VISTA")
num_tabelle_TRIGGER=makeMain(TRIGGER_PATH, MAIN_TRIGGER_PATH, "TRIGGER")
makeMainTotale()

print(f"main DDL creato con successo, {num_tabelle_DDL} tabelle")
print(f"main DML creato con successo, {num_tabelle_DML} tabelle")
print(f"main VISTA creato con successo, {num_tabelle_VISTA} viste")
print(f"main TRIGGER creato con successo, {num_tabelle_TRIGGER} trigger")
print("main totale creato con successo")
