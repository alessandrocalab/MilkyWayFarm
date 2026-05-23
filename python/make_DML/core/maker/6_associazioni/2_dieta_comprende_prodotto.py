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


#DIETA_COMPRENDE_PRODOTTO:NOME_PRODOTTO NOME_DIETA QUANTITA_GRAMMI 

NOME_PRODOTTO = []

NOME_DIETA = []

QUANTITA_GRAMMI = []


theList=list(zip(NOME_PRODOTTO, NOME_DIETA, QUANTITA_GRAMMI))

keys = ["NOME_PRODOTTO", "NOME_DIETA", "QUANTITA_GRAMMI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_DIETA, QUANTITA_GRAMMI\n"
for i in range(len(theList)):
  lines+=make_DML_line("DIETA_COMPRENDE_PRODOTTO", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/2_dieta_comprende_prodotto.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/2_dieta_comprende_prodotto.sql", lines)