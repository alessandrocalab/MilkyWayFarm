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


#PRODOTTO_DA_STADIO_CRESCITA:NOME_PRODOTTO NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE 

NOME_PRODOTTO = [
    # BOVINO
    "'Latte bovino'",
    "'Carne bovina'",
    "'Pelle bovina'",
    "'Letame bovino'",

    # CAPRA
    "'Latte caprino'",
    "'Carne caprina'",

    # PECORA
    "'Latte ovino'",
    "'Carne ovina'",
    "'Lana ovina'",
    "'Letame ovino'",

    # MAIALE
    "'Carne suina'",
    "'Letame suino'",

    # GALLINA
    "'Uova di gallina'",
    "'Carne di pollo'",
    "'Pollina'",
    "'Piume di pollame'",

    # TACCHINO
    "'Carne di tacchino'",
    "'Pollina'",
    "'Piume di pollame'",

    # CONIGLIO
    "'Carne di coniglio'"
]

NOME_STADIO_CRESCITA = [
    # BOVINO
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",

    # CAPRA
    "'Adulto'",
    "'Adulto'",

    # PECORA
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",

    # MAIALE
    "'Adulto'",
    "'Adulto'",

    # GALLINA
    "'Ovodeposizione'",
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",

    # TACCHINO
    "'Adulto'",
    "'Adulto'",
    "'Adulto'",

    # CONIGLIO
    "'Adulto'"
]

NOME_TIPO_ANIMALE = [
    # BOVINO
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",

    # CAPRA
    "'Capra'",
    "'Capra'",

    # PECORA
    "'Pecora'",
    "'Pecora'",
    "'Pecora'",
    "'Pecora'",

    # MAIALE
    "'Maiale'",
    "'Maiale'",

    # GALLINA
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",

    # TACCHINO
    "'Tacchino'",
    "'Tacchino'",
    "'Tacchino'",

    # CONIGLIO
    "'Coniglio'"
]

theList=list(zip(NOME_PRODOTTO, NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE))

keys = ["NOME_PRODOTTO", "NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_DA_STADIO_CRESCITA", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/7_prodotto_da_stadio_crescita.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/7_prodotto_da_stadio_crescita.sql", lines)