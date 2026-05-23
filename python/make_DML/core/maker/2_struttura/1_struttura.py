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


#STRUTTURA:NOME_STRUTTURA DATA_TERMINAZIONE QUOTA LONGITUDINE LATITUDINE VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

NOME_STRUTTURA = ["'Primo Modulo'","'Struttura Agricola'","'Struttura Stoccaggio'","'Struttura Zootecnica'","'Struttura Agricola II'"]

DATA_TERMINAZIONE = ['NULL',"DATE '2026-05-07'",'NULL','NULL','NULL']

QUOTA = [
    1120,
    1122,
    1118,
    1121,
    1119
]

LONGITUDINE = [
    137.441700,
    137.442050,
    137.441320,
    137.442410,
    137.440980
]

LATITUDINE = [
    4.589210,
    4.589430,
    4.589050,
    4.588820,
    4.589650
]

VOLUME_M3 = ["900","200","700","1600","800"]

SUPERFICIE_MQ = ["300","50","200","400","200"]

DATA_ATTIVAZIONE = ["DATE '2023-06-17'","DATE '2023-06-20'","DATE '2023-08-04","DATE '2025-02-23'","DATE '2026-04-01'"]


theList=list(zip(NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["NOME_STRUTTURA", "DATA_TERMINAZIONE", "QUOTA", "LONGITUDINE", "LATITUDINE", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STRUTTURA, DATA_TERMINAZIONE, QUOTA, LONGITUDINE, LATITUDINE, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("STRUTTURA", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/1_struttura.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/1_struttura.sql", lines)