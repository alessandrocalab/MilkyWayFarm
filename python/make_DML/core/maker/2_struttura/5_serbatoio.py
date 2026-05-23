import os
import sys
import json

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

from python.make_DML.core.utils.make_DML_line import make_DML_line
from python.make_DML.core.utils.make_DML import make_DML


#SERBATOIO:NUMERO_SERBATOIO CODICE_AREA NOME_STRUTTURA DATA_SMONTAGGIO DATA_MONTAGGIO PRESSIONE_MAX_PA DIMENSIONE_M3 
NUMERO_SERBATOIO = [
    "'S001'",
    "'S002'",
    "'S003'",
    "'S004'",
    "'S005'",
    "'S006'",
    "'S007'",
    "'S008'"
]

CODICE_AREA = [
    "'A00C'",
    "'A00D'",
    "'A00E'",
    "'A00K'",
    "'A00K'",
    "'A00L'",
    "'A00L'",
    "'A00L'"
]

NOME_STRUTTURA = [
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'"
]

DATA_SMONTAGGIO = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

DATA_MONTAGGIO = [
    "DATE '2023-08-07'",
    "DATE '2023-08-08'",
    "DATE '2023-08-08'",
    "DATE '2023-08-11'",
    "DATE '2023-08-11'",
    "DATE '2023-08-12'",
    "DATE '2023-08-12'",
    "DATE '2023-08-12'"
]

PRESSIONE_MAX_PA = [
    120000,
    130000,
    110000,
    150000,
    150000,
    140000,
    140000,
    130000
]

DIMENSIONE_M3 = [
    2,
    2,
    1,
    4,
    4,
    5,
    5,
    3
]

theList=list(zip(NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3))

keys = ["NUMERO_SERBATOIO", "CODICE_AREA", "NOME_STRUTTURA", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "PRESSIONE_MAX_PA", "DIMENSIONE_M3"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, DATA_SMONTAGGIO, DATA_MONTAGGIO, PRESSIONE_MAX_PA, DIMENSIONE_M3\n"
for i in range(len(theList)):
  lines+=make_DML_line("SERBATOIO", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/5_serbatoio.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/5_serbatoio.sql", lines,"a")