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


#DIETA_ANIMALE:NOME_DIETA OBIETTIVO_DIETA 

NOME_DIETA = [
    # GALLINA
    "'Dieta Gallina Pulcino'",
    "'Dieta Gallina Giovane'",
    "'Dieta Gallina Uova'",
    "'Dieta Gallina Adulta'",

    # CONIGLIO
    "'Dieta Coniglio Cucciolo'",
    "'Dieta Coniglio Svezz'",
    "'Dieta Coniglio Giovane'",
    "'Dieta Coniglio Adulto'",

    # CAPRA
    "'Dieta Capra Capretto'",
    "'Dieta Capra Svezz'",
    "'Dieta Capra Giovane'",
    "'Dieta Capra Adulta'",

    # PECORA
    "'Dieta Pecora Agnello'",
    "'Dieta Pecora Svezz'",
    "'Dieta Pecora Giovane'",
    "'Dieta Pecora Adulta'",

    # MAIALE
    "'Dieta Maiale Suinetto'",
    "'Dieta Maiale Svezz'",
    "'Dieta Maiale Ingrasso'",
    "'Dieta Maiale Adulto'",

    # BOVINO
    "'Dieta Bovino Vitello'",
    "'Dieta Bovino Svezz'",
    "'Dieta Bovino Giovane'",
    "'Dieta Bovino Adulto'",

    # TACCHINO
    "'Dieta Tacchino Pulcino'",
    "'Dieta Tacchino Giovane'",
    "'Dieta Tacchino Ingrasso'",
    "'Dieta Tacchino Adulto'"
]

OBIETTIVO_DIETA = []


theList=list(zip(NOME_DIETA, OBIETTIVO_DIETA))

keys = ["NOME_DIETA", "OBIETTIVO_DIETA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_DIETA, OBIETTIVO_DIETA\n"
for i in range(len(theList)):
  lines+=make_DML_line("DIETA_ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/4_dieta_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/4_dieta_animale.sql", lines)