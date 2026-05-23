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


#SERB_RISPETTA_MOD_CONS:NUMERO_SERBATOIO CODICE_AREA NOME_STRUTTURA NOME_CONSERVAZIONE 

NUMERO_SERBATOIO = []

CODICE_AREA = []

NOME_STRUTTURA = []

NOME_CONSERVAZIONE = []


theList=list(zip(NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE))

keys = ["NUMERO_SERBATOIO", "CODICE_AREA", "NOME_STRUTTURA", "NOME_CONSERVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_SERBATOIO, CODICE_AREA, NOME_STRUTTURA, NOME_CONSERVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("SERB_RISPETTA_MOD_CONS", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/14_serb_rispetta_mod_cons.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/14_serb_rispetta_mod_cons.sql", lines)