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


#ANIMALE_ALLERGICO_SOSTANZA:ETICHETTA_ANIMALE NOME_SOSTANZA DATA_ATTESTAZIONE 

ETICHETTA_ANIMALE = []

NOME_SOSTANZA = []

DATA_ATTESTAZIONE = []


theList=list(zip(ETICHETTA_ANIMALE, NOME_SOSTANZA, DATA_ATTESTAZIONE))

keys = ["ETICHETTA_ANIMALE", "NOME_SOSTANZA", "DATA_ATTESTAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, NOME_SOSTANZA, DATA_ATTESTAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE_ALLERGICO_SOSTANZA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/5_animale_allergico_sostanza.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/5_animale_allergico_sostanza.sql", lines)