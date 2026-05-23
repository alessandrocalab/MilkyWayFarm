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


#PRODOTTO_MISSIONE_ALLOC_SERB:NOME_PRODOTTO NOME_MISSIONE NUMERO_SERBATOIO CODICE_AREA_SERB NOME_STRUTTURA_SERB QUANTITA_ALLOCATA 

NOME_PRODOTTO = []

NOME_MISSIONE = []

NUMERO_SERBATOIO = []

CODICE_AREA_SERB = []

NOME_STRUTTURA_SERB = []

QUANTITA_ALLOCATA = []


theList=list(zip(NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA))

keys = ["NOME_PRODOTTO", "NOME_MISSIONE", "NUMERO_SERBATOIO", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_MISSIONE, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_MISSIONE_ALLOC_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/19_prodotto_missione_alloc_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/19_prodotto_missione_alloc_serb.sql", lines)