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


#PRODUZIONE_AGRICOLA_ALLOC_SCAFF:DATA_PRODUZIONE_AGRICOLA DATA_INIZIO_CICLO_COLTIVAZIONE CODICE_CELLA_IDR CODICE_AREA_CELLA NOME_STRUTTURA_CELLA NOME_PRODOTTO NUMERO_SCAFFALE CODICE_AREA_SCAFF NOME_STRUTTURA_SCAFF QUANTITA_ALLOCATA 

DATA_PRODUZIONE_AGRICOLA = []

DATA_INIZIO_CICLO_COLTIVAZIONE = []

CODICE_CELLA_IDR = []

CODICE_AREA_CELLA = []

NOME_STRUTTURA_CELLA = []

NOME_PRODOTTO = []

NUMERO_SCAFFALE = []

CODICE_AREA_SCAFF = []

NOME_STRUTTURA_SCAFF = []

QUANTITA_ALLOCATA = []


theList=list(zip(DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA))

keys = ["DATA_PRODUZIONE_AGRICOLA", "DATA_INIZIO_CICLO_COLTIVAZIONE", "CODICE_CELLA_IDR", "CODICE_AREA_CELLA", "NOME_STRUTTURA_CELLA", "NOME_PRODOTTO", "NUMERO_SCAFFALE", "CODICE_AREA_SCAFF", "NOME_STRUTTURA_SCAFF", "QUANTITA_ALLOCATA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA_CELLA, NOME_STRUTTURA_CELLA, NOME_PRODOTTO, NUMERO_SCAFFALE, CODICE_AREA_SCAFF, NOME_STRUTTURA_SCAFF, QUANTITA_ALLOCATA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_AGRICOLA_ALLOC_SCAFF", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/16_produzione_agricola_alloc_scaff.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/16_produzione_agricola_alloc_scaff.sql", lines)