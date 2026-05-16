import os

MAIN_START=(
        "SET SQLBLANKLINES ON --senza interpreta male le righe vuote\n\n"
        "--Eliminazione schema precedente"
        "\n\n@drop_all.sql\n\n"
    )
MAIN_END="\n\nCOMMIT;"
MAIN_PATH="./DB/main.sql"
DLL_PATH="./DB/DDL/"


main_text=MAIN_START

num_tabelle=0

DDL_dirs=os.listdir(DLL_PATH)
DDL_dirs=sorted(DDL_dirs, key=lambda x: int(x.split("_")[0])) #ordinamento rispetto i numeri prima del primo trattino

for dir in DDL_dirs:
    sql_files=os.listdir(DLL_PATH+dir)
    sql_files=sorted(sql_files, key=lambda x: int(x.split("_")[0]))
    main_text+=f"\n--Sezione: {dir}\n\n"
    for sql in sql_files:
        num_tabelle+=1
        main_text+=f"@DDL/{dir}/{sql}\n"


main_text+=MAIN_END

with open(MAIN_PATH, "w") as f:
    f.write(main_text)

print(f"main creato con successo, {num_tabelle} tabelle")
