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


#VACCINAZIONE:ETICHETTA_ANIMALE NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA DATA_VACCINAZIONE MATRICOLA_SOMMINISTRATORE 

ETICHETTA_ANIMALE = [
    "'0000000032'",
    "'0000000032'",

    "'0000000007'",
    "'0000000007'",

    "'0000000010'",
    "'0000000010'",

    "'0000000015'",
    "'0000000015'"
]

NOME_VACCINO = [
    "'mixomatosi'",
    "'malattia emorragica'",

    "'clostridiosi'",
    "'enterotossiemia'",

    "'clostridiosi'",
    "'enterotossiemia'",

    "'mal rosso'",
    "'parvovirosi'"
]

NOME_TIPO_ANIMALE = [
    "'Coniglio'",
    "'Coniglio'",

    "'Capra'",
    "'Capra'",

    "'Pecora'",
    "'Pecora'",

    "'Maiale'",
    "'Maiale'"
]

NOME_STADIO_CRESCITA = [
    "'Svezzamento'",
    "'Giovane'",

    "'Svezzamento'",
    "'Giovane'",

    "'Svezzamento'",
    "'Giovane'",

    "'Accrescimento'",
    "'Adulto'"
]

DATA_VACCINAZIONE = [
    "DATE '2025-02-28'",
    "DATE '2025-03-10'",

    "DATE '2025-02-27'",
    "DATE '2025-03-15'",

    "DATE '2025-02-27'",
    "DATE '2025-04-15'",

    "DATE '2025-03-05'",
    "DATE '2025-05-15'"
]

MATRICOLA_SOMMINISTRATORE = [
    "'0000009002'",
    "'0000009002'",

    "'0000009002'",
    "'0000009002'",

    "'0000009002'",
    "'0000009002'",

    "'0000009001'",
    "'0000009001'"
]


theList=list(zip(ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE))

keys = ["ETICHETTA_ANIMALE", "NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "DATA_VACCINAZIONE", "MATRICOLA_SOMMINISTRATORE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA_ANIMALE, NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, DATA_VACCINAZIONE, MATRICOLA_SOMMINISTRATORE\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/6_vaccinazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/6_vaccinazione.sql", lines)