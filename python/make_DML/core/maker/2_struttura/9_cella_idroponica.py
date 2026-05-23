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


#CELLA_IDROPONICA:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA SISTEMA_IDROPONICO DATA_SMONTAGGIO DATA_MONTAGGIO MAX_COLTURE 

CODICE_CELLA_IDR = [
    "'001A'",
    "'001B'",
    "'001C'",
    "'002A'",
    "'002B'",
    "'002C'",
    "'002D'",
    "'002E'"
]

CODICE_AREA = [
    "'A00A'",
    "'A00A'",
    "'A00A'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'"
]

NOME_STRUTTURA = [
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'"
]

SISTEMA_IDROPONICO = [
    "'NFT'",
    "'DWC'",
    "'Letto a substrato'",
    "'NFT'",
    "'DWC'",
    "'Aeroponica'",
    "'Letto a substrato'",
    "'Flusso e riflusso'"
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
    "DATE '2026-04-02'",
    "DATE '2026-04-02'",
    "DATE '2026-04-03'",
    "DATE '2026-05-24'",
    "DATE '2026-05-24'",
    "DATE '2026-05-25'",
    "DATE '2026-05-25'",
    "DATE '2026-05-26'"
]

MAX_COLTURE = [
    8,
    6,
    5,
    12,
    10,
    8,
    8,
    6
]


theList=list(zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE))

keys = ["CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "SISTEMA_IDROPONICO", "DATA_SMONTAGGIO", "DATA_MONTAGGIO", "MAX_COLTURE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, SISTEMA_IDROPONICO, DATA_SMONTAGGIO, DATA_MONTAGGIO, MAX_COLTURE\n"
for i in range(len(theList)):
  lines+=make_DML_line("CELLA_IDROPONICA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/9_cella_idroponica.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/9_cella_idroponica.sql", lines, "a")