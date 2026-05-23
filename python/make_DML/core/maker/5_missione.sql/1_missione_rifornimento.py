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


#MISSIONE_RIFORNIMENTO:NOME_MISSIONE DATA_LANCIO DATA_ARRIVO_PREVISTO DATA_ARRIVO_EFFETTIVO VOLUME_RIFORNIMENTO_M3 MASSA_RIFORNIMENTO_KG BASE_PARTENZA 

NOME_MISSIONE = [
    "'Ares Supply 01'",
    "'Ares Supply 02'",
    "'Demetra Cargo 01'",
    "'Demetra Cargo 02'",
    "'Hermes BioLab 01'",
    "'Hermes BioLab 02'",
    "'Atlas Storage 01'",
    "'Atlas Storage 02'"
]

DATA_LANCIO = [
    "DATE '2023-06-01'",
    "DATE '2023-08-20'",
    "DATE '2024-01-12'",
    "DATE '2024-07-04'",
    "DATE '2025-02-10'",
    "DATE '2025-09-18'",
    "DATE '2026-01-15'",
    "DATE '2026-03-22'"
]
DATA_ARRIVO_PREVISTO = [
    "DATE '2023-06-16'",
    "DATE '2023-09-04'",
    "DATE '2024-01-27'",
    "DATE '2024-07-19'",
    "DATE '2025-02-25'",
    "DATE '2025-10-03'",
    "DATE '2026-01-30'",
    "DATE '2026-04-06'"
]
DATA_ARRIVO_EFFETTIVO = [
    "DATE '2023-06-17'",
    "DATE '2023-09-04'",
    "DATE '2024-01-29'",
    "DATE '2024-07-18'",
    "DATE '2025-02-26'",
    "DATE '2025-10-04'",
    "DATE '2026-01-31'",
    "DATE '2026-04-07'"
]

VOLUME_RIFORNIMENTO_M3 = [
    45.50,
    52.00,
    38.75,
    60.25,
    28.40,
    34.60,
    70.00,
    64.80
]

MASSA_RIFORNIMENTO_KG = [
    12500.00,
    14800.00,
    9800.00,
    16250.00,
    7200.00,
    8500.00,
    18500.00,
    17100.00
]

BASE_PARTENZA = [
    "'Cape Canaveral'",
    "'Cape Canaveral'",
    "'Spazioporto di Acerra'",
    "'Spazioporto di Acerra'",
    "'Tanegashima'",
    "'Kourou'",
    "'Spazioporto di Acerra'",
    "'Cape Canaveral'"
]


theList=list(zip(NOME_MISSIONE, DATA_LANCIO, DATA_ARRIVO_PREVISTO, DATA_ARRIVO_EFFETTIVO, VOLUME_RIFORNIMENTO_M3, MASSA_RIFORNIMENTO_KG, BASE_PARTENZA))

keys = ["NOME_MISSIONE", "DATA_LANCIO", "DATA_ARRIVO_PREVISTO", "DATA_ARRIVO_EFFETTIVO", "VOLUME_RIFORNIMENTO_M3", "MASSA_RIFORNIMENTO_KG", "BASE_PARTENZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_MISSIONE, DATA_LANCIO, DATA_ARRIVO_PREVISTO, DATA_ARRIVO_EFFETTIVO, VOLUME_RIFORNIMENTO_M3, MASSA_RIFORNIMENTO_KG, BASE_PARTENZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("MISSIONE_RIFORNIMENTO", theList[i])+"\n"

os.makedirs("make_DML/data/5_missione.sql", exist_ok=True)
with open("make_DML/data/5_missione.sql/1_missione_rifornimento.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/5_missione.sql/1_missione_rifornimento.sql", lines)