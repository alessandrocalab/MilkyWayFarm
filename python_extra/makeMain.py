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
MAIN_VISTE_PATH="./DB/VISTE/main.sql"
MAIN_TRIGGER_PATH="./DB/TRIGGER/main.sql"
MAIN_PROCEDURE_PATH="./DB/PROCEDURE/main.sql"
MAIN_RUOLI_PATH="./DB/RUOLI/main.sql"
MAIN_UTENTI_PATH="./DB/UTENTI/main.sql"
MAIN_SCHEDULER_PATH="./DB/SCHEDULER/main.sql"
MAIN_TOTALE_PATH="./DB/main.sql"

DDL_PATH="./DB/DDL/"
DML_PATH="./DB/DML/"
VISTE_PATH="./DB/VISTE/"
TRIGGER_PATH="./DB/TRIGGER/"
PROCEDURE_PATH="./DB/PROCEDURE/"
RUOLI_PATH="./DB/RUOLI/"
UTENTI_PATH="./DB/UTENTI/"
SCHEDULER_PATH="./DB/SCHEDULER/"


def getNum(nome_file:str):
    return int(nome_file.split("_")[0])


def getSortKey(nome_file:str):
    nome=nome_file.split("_")[0]

    if nome.isdigit():
        return (0, int(nome), nome_file)

    return (1, nome_file.lower())


def getSqlFiles(dir_path:str, dir:str):
    sql_files=[
        sql for sql in os.listdir(dir_path)
        if sql.lower().endswith(".sql") and sql!="main.sql"
    ]
    sql_files=sorted(sql_files, key=getSortKey)

    if dir=="1_prodotto":
        sql_files=sorted(
            sql_files,
            key=lambda sql: (-1, sql) if sql=="3_unita_di_misura.sql" else getSortKey(sql)
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

    sql_files=sorted(tmp_sql_files, key=getSortKey)

    if len(sql_files) != 0:
        nome_sezione=os.path.basename(os.path.normpath(base_path))
        main_text+=f"\n--Sezione: {nome_sezione}\n\n"

        for sql in sql_files:
            num_tabelle+=1
            main_text+=f"@{path_prefix}{sql}\n"

    dirs=sorted(tmp_dirs, key=getSortKey)

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

    main_body, num_tabelle_VISTE=getMainBody(VISTE_PATH, "VISTE/")
    main_text+=main_body

    main_text+="\n--Sezione: TRIGGER\n\n"
    main_body, num_tabelle_TRIGGER=getMainBody(TRIGGER_PATH, "TRIGGER/")
    main_text+=main_body

    main_body, num_tabelle_PROCEDURE=getMainBody(PROCEDURE_PATH, "PROCEDURE/")
    main_text+=main_body

    main_body, num_tabelle_RUOLI=getMainBody(RUOLI_PATH, "RUOLI/")
    main_text+=main_body

    main_body, num_tabelle_UTENTI=getMainBody(UTENTI_PATH, "UTENTI/")
    main_text+=main_body

    main_body, num_tabelle_SCHEDULER=getMainBody(SCHEDULER_PATH, "SCHEDULER/")
    main_text+=main_body

    main_text+=MAIN_END

    with open(MAIN_TOTALE_PATH, "w") as f:
        f.write(main_text)

    return num_tabelle_DDL, num_tabelle_DML, num_tabelle_VISTE, num_tabelle_TRIGGER, num_tabelle_PROCEDURE, num_tabelle_RUOLI, num_tabelle_UTENTI, num_tabelle_SCHEDULER


num_tabelle_DDL=makeMain(DDL_PATH, MAIN_DDL_PATH, "DDL")
num_tabelle_DML=makeMain(DML_PATH, MAIN_DML_PATH, "DML")
num_tabelle_VISTE=makeMain(VISTE_PATH, MAIN_VISTE_PATH, "VISTE")
num_tabelle_TRIGGER=makeMain(TRIGGER_PATH, MAIN_TRIGGER_PATH, "TRIGGER")
num_tabelle_PROCEDURE=makeMain(PROCEDURE_PATH, MAIN_PROCEDURE_PATH, "PROCEDURE")
num_tabelle_RUOLI=makeMain(RUOLI_PATH, MAIN_RUOLI_PATH, "RUOLI")
num_tabelle_UTENTI=makeMain(UTENTI_PATH, MAIN_UTENTI_PATH, "UTENTI")
num_tabelle_SCHEDULER=makeMain(SCHEDULER_PATH, MAIN_SCHEDULER_PATH, "SCHEDULER")
makeMainTotale()

print(f"main DDL creato con successo, {num_tabelle_DDL} tabelle")
print(f"main DML creato con successo, {num_tabelle_DML} tabelle")
print(f"main VISTE creato con successo, {num_tabelle_VISTE} viste")
print(f"main TRIGGER creato con successo, {num_tabelle_TRIGGER} trigger")
print(f"main PROCEDURE creato con successo, {num_tabelle_PROCEDURE} procedure")
print(f"main RUOLI creato con successo, {num_tabelle_RUOLI} ruoli")
print(f"main UTENTI creato con successo, {num_tabelle_UTENTI} utenti")
print(f"main SCHEDULER creato con successo, {num_tabelle_SCHEDULER} scheduler")
print("main totale creato con successo")
