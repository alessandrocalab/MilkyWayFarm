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


#STADIO_CRESCITA_INTOLLERANTE_SOSTANZA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE NOME_SOSTANZA 

NOME_STADIO_CRESCITA = []

NOME_TIPO_ANIMALE = []

NOME_SOSTANZA = []


theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "NOME_SOSTANZA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, NOME_SOSTANZA\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA_INTOLLERANTE_SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/4_stadio_crescita_intollerante_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/4_stadio_crescita_intollerante_sostanza.sql", lines)