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


#VISITA_VETERINARIA:ETICHETTA_ANIMALE DATA_VISITA MATRICOLA_VETERINARIO STATO_SALUTE TIPO_VISITA 
ETICHETTA_ANIMALE = [
    "'0000000001'",
    "'0000000016'",
    "'0000000036'"
]

DATA_VISITA = [
    "DATE '2025-02-26'",
    "DATE '2025-03-22'",
    "DATE '2025-03-10'"
]

MATRICOLA_VETERINARIO = [
    "'0000009001'",
    "'0000009003'",
    "'0000009003'"
]

STATO_SALUTE = [
    "'BUONO'",
    "'BUONO'",
    "'DISCRETO'"
]

TIPO_VISITA = [
    "'INGRESSO'",
    "'ROUTINE'",
    "'BIOSICUREZZA'"
]

theList=list(zip(ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA))

keys = ["ETICHETTA_ANIMALE", "DATA_VISITA", "MATRICOLA_VETERINARIO", "STATO_SALUTE", "TIPO_VISITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, DATA_VISITA, MATRICOLA_VETERINARIO, STATO_SALUTE, TIPO_VISITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("VISITA_VETERINARIA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/7_visita_veterinaria.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/7_visita_veterinaria.sql", lines)