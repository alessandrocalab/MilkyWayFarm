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


#DEALLOC_PROD_BLOCCO_ANIMALE_SERB:DATE_MIN NOME_PRODOTTO NUMERO_SERB CODICE_AREA_SERB NOME_STRUTTURA_SERB NUMERO_BLOCCO CODICE_AREA_BLOCCO NOME_STRUTTURA_BLOCCO QUANTITA_DEALLOCATA 

DATE_MIN = []

NOME_PRODOTTO = []

NUMERO_SERB = []

CODICE_AREA_SERB = []

NOME_STRUTTURA_SERB = []

NUMERO_BLOCCO = []

CODICE_AREA_BLOCCO = []

NOME_STRUTTURA_BLOCCO = []

QUANTITA_DEALLOCATA = []


theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SERB", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "NUMERO_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_STRUTTURA_BLOCCO", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, NUMERO_BLOCCO, CODICE_AREA_BLOCCO, NOME_STRUTTURA_BLOCCO, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_BLOCCO_ANIMALE_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/23_dealloc_prod_blocco_animale_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/23_dealloc_prod_blocco_animale_serb.sql", lines)