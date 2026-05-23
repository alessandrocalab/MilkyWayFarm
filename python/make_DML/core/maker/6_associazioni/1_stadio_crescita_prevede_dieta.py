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


#STADIO_CRESCITA_PREVEDE_DIETA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE NOME_DIETA DATA_INIZIO DATA_FINE 

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []

NOME_DIETA = []

DATA_INIZIO = []

DATA_FINE = []


theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "NOME_DIETA", "DATA_INIZIO", "DATA_FINE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_DIETA, DATA_INIZIO, DATA_FINE\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA_PREVEDE_DIETA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/1_stadio_crescita_prevede_dieta.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/1_stadio_crescita_prevede_dieta.sql", lines)