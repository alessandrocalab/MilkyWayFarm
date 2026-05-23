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


#TIPO_COLT_ACCETTA_MOD_COLT:NOME_TIPO_COLTURA NOME_MODALITA_COLTIVAZIONE 

NOME_TIPO_COLTURA = []

NOME_MODALITA_COLTIVAZIONE = []


theList=list(zip(NOME_TIPO_COLTURA, NOME_MODALITA_COLTIVAZIONE))

keys = ["NOME_TIPO_COLTURA", "NOME_MODALITA_COLTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_TIPO_COLTURA, NOME_MODALITA_COLTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_COLT_ACCETTA_MOD_COLT", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/11_tipo_colt_accetta_mod_colt.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/11_tipo_colt_accetta_mod_colt.sql", lines)