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


#CELLA_IDR_RISPETTA_MOD_COLT:CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA NOME_MOD_COLTIVAZIONE 

CODICE_CELLA_IDR = []

CODICE_AREA = []

NOME_STRUTTURA = []

NOME_MOD_COLTIVAZIONE = []


theList=list(zip(CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE))

keys = ["CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "NOME_MOD_COLTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_MOD_COLTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("CELLA_IDR_RISPETTA_MOD_COLT", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/10_cella_idr_rispetta_mod_colt.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/10_cella_idr_rispetta_mod_colt.sql", lines)