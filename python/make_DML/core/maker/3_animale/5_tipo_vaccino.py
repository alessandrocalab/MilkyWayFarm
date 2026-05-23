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


#VACCINO:NOME_VACCINO NOME_TIPO_ANIMALE NOME_STADIO_CRESCITA NOME_VACCINO_PROPEDEUTICO NOME_STADIO_CRESCITA_PROPEDEUTICO NOME_TIPO_ANIMALE_PROPEDEUTICO IS_VACCINO_OBBLIGATORIO ETA_MINIMA_MESI DOSE_ML 

NOME_VACCINO = [
    "'Newcastle'",
    "'bronchite infettiva'",
    "'coccidiosi'",

    "'mixomatosi'",
    "'malattia emorragica'",

    "'clostridiosi'",
    "'enterotossiemia'",

    "'clostridiosi'",
    "'enterotossiemia'",

    "'mal rosso'",
    "'parvovirosi'",

    "'respiratorio'",
    "'clostridiosi'",
    "'mastite'",

    "'Newcastle'",
    "'coccidiosi'"
]

NOME_TIPO_ANIMALE = [
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",

    "'Coniglio'",
    "'Coniglio'",

    "'Capra'",
    "'Capra'",

    "'Pecora'",
    "'Pecora'",

    "'Maiale'",
    "'Maiale'",

    "'Bovino'",
    "'Bovino'",
    "'Bovino'",

    "'Tacchino'",
    "'Tacchino'"
]

NOME_STADIO_CRESCITA = [
    "'Pulcino'",
    "'Giovane'",
    "'Pulcino'",

    "'Svezzamento'",
    "'Giovane'",

    "'Svezzamento'",
    "'Giovane'",

    "'Svezzamento'",
    "'Giovane'",

    "'Accrescimento'",
    "'Adulto'",

    "'Svezzamento'",
    "'Giovane'",
    "'Adulto'",

    "'Pulcino'",
    "'Giovane'"
]

NOME_VACCINO_PROPEDEUTICO = [
    "NULL",
    "'Vaccino pollame Newcastle'",
    "NULL",

    "NULL",
    "'Vaccino conigli mixomatosi'",

    "NULL",
    "'Vaccino ovicaprini clostridiosi'",

    "NULL",
    "'Vaccino ovicaprini clostridiosi'",

    "NULL",
    "'Vaccino suini mal rosso'",

    "NULL",
    "'Vaccino bovini respiratorio'",
    "'Vaccino bovini clostridiosi'",

    "NULL",
    "'Vaccino pollame Newcastle'"
]

NOME_STADIO_CRESCITA_PROPEDEUTICO = [
    "NULL",
    "'Pulcino'",
    "NULL",

    "NULL",
    "'Svezzamento'",

    "NULL",
    "'Svezzamento'",

    "NULL",
    "'Svezzamento'",

    "NULL",
    "'Accrescimento'",

    "NULL",
    "'Svezzamento'",
    "'Giovane'",

    "NULL",
    "'Pulcino'"
]

NOME_TIPO_ANIMALE_PROPEDEUTICO = [
    "NULL",
    "'Gallina'",
    "NULL",

    "NULL",
    "'Coniglio'",

    "NULL",
    "'Capra'",

    "NULL",
    "'Pecora'",

    "NULL",
    "'Maiale'",

    "NULL",
    "'Bovino'",
    "'Bovino'",

    "NULL",
    "'Tacchino'"
]

IS_VACCINO_OBBLIGATORIO = [
    1,
    1,
    0,

    1,
    1,

    1,
    1,

    1,
    1,

    1,
    1,

    1,
    1,
    0,

    1,
    0
]

ETA_MINIMA_MESI = [
    0,
    1,
    0,

    1,
    2,

    3,
    6,

    3,
    6,

    3,
    8,

    3,
    12,
    24,

    0,
    2
]

DOSE_ML = [
    0.05,
    0.05,
    0.05,

    0.50,
    0.50,

    2.00,
    2.00,

    2.00,
    2.00,

    2.00,
    2.00,

    2.00,
    2.00,
    2.00,

    0.05,
    0.05
]

theList=list(zip(NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML))

keys = ["NOME_VACCINO", "NOME_TIPO_ANIMALE", "NOME_STADIO_CRESCITA", "NOME_VACCINO_PROPEDEUTICO", "NOME_STADIO_CRESCITA_PROPEDEUTICO", "NOME_TIPO_ANIMALE_PROPEDEUTICO", "IS_VACCINO_OBBLIGATORIO", "ETA_MINIMA_MESI", "DOSE_ML"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_VACCINO, NOME_TIPO_ANIMALE, NOME_STADIO_CRESCITA, NOME_VACCINO_PROPEDEUTICO, NOME_STADIO_CRESCITA_PROPEDEUTICO, NOME_TIPO_ANIMALE_PROPEDEUTICO, IS_VACCINO_OBBLIGATORIO, ETA_MINIMA_MESI, DOSE_ML\n"
for i in range(len(theList)):
  lines+=make_DML_line("VACCINO", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/5_tipo_vaccino.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/5_tipo_vaccino.sql", lines)