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


#PRODOTTO_CONTIENE_SOSTANZA:NOME_PRODOTTO NOME_SOSTANZA LIVELLO_PRESENZA 

NOME_PRODOTTO = []

NOME_SOSTANZA = []

LIVELLO_PRESENZA = []


theList=list(zip(NOME_PRODOTTO, NOME_SOSTANZA, LIVELLO_PRESENZA))

keys = ["NOME_PRODOTTO", "NOME_SOSTANZA", "LIVELLO_PRESENZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_SOSTANZA, LIVELLO_PRESENZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_CONTIENE_SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/3_prodotto_contiene_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/3_prodotto_contiene_sostanza.sql", lines)