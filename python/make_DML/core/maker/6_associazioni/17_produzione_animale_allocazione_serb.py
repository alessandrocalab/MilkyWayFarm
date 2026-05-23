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


#PRODUZIONE_ANIMALE_ALLOC_SERB:DATA_PRODUZIONE NUMERO_BLOCCO NOME_STRUTTURA_BLOCCO CODICE_AREA_BLOCCO NOME_PRODOTTO NUMERO_SERBATOIO CODICE_AREA_SERB NOME_STRUTTURA_SERB QUANTITA_ALLOCATA 

DATA_PRODUZIONE = []

NUMERO_BLOCCO = []

NOME_STRUTTURA_BLOCCO = []

CODICE_AREA_BLOCCO = []

NOME_PRODOTTO = []

NUMERO_SERBATOIO = []

CODICE_AREA_SERB = []

NOME_STRUTTURA_SERB = []

QUANTITA_ALLOCATA = []


theList=list(zip(DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA))

keys = ["DATA_PRODUZIONE", "NUMERO_BLOCCO", "NOME_STRUTTURA_BLOCCO", "CODICE_AREA_BLOCCO", "NOME_PRODOTTO", "NUMERO_SERBATOIO", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA_BLOCCO, CODICE_AREA_BLOCCO, NOME_PRODOTTO, NUMERO_SERBATOIO, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_ANIMALE_ALLOC_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/17_produzione_animale_allocazione_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/17_produzione_animale_allocazione_serb.sql", lines)