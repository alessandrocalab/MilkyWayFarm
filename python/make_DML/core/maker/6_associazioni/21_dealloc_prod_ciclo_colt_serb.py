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


#DEALLOC_PROD_CICLO_COLT_SERB:DATE_MIN NOME_PRODOTTO NUMERO_SERB CODICE_AREA_SERB NOME_STRUTTURA_SERB DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA QUANTITA_DEALLOCATA 

DATE_MIN = []

NOME_PRODOTTO = []

NUMERO_SERB = []

CODICE_AREA_SERB = []

NOME_STRUTTURA_SERB = []

DATA_INIZIO = []

CODICE_CELLA_IDR = []

CODICE_AREA_CELLA = []

NOME_STRUTTURA_CELLA = []

QUANTITA_DEALLOCATA = []


theList=list(zip(DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA))

keys = ["DATE_MIN", "NOME_PRODOTTO", "NUMERO_SERB", "CODICE_AREA_SERB", "NOME_STRUTTURA_SERB", "DATA_INIZIO", "CODICE_CELLA_IDR", "CODICE_AREA_CELLA", "NOME_STRUTTURA_CELLA", "QUANTITA_DEALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATE_MIN, NOME_PRODOTTO, NUMERO_SERB, CODICE_AREA_SERB, NOME_STRUTTURA_SERB, DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, QUANTITA_DEALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DEALLOC_PROD_CICLO_COLT_SERB", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/21_dealloc_prod_ciclo_colt_serb.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/21_dealloc_prod_ciclo_colt_serb.sql", lines)