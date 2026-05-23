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


#STADIO_CRESCITA:NOME_STADIO_CRESCITA NOME_TIPO_ANIMALE LIVELLO_BIOSICUREZZA_MINIMO ETA_MINIMA_MESI 

NOME_STADIO_CRESCITA = [
    # GALLINA
    "'Pulcino'",
    "'Giovane'",
    "'Ovodeposizione'",
    "'Adulto'",

    # CONIGLIO
    "'Cucciolo'",
    "'Svezzamento'",
    "'Giovane'",
    "'Adulto'",

    # CAPRA
    "'Capretto'",
    "'Svezzamento'",
    "'Giovane'",
    "'Adulto'",

    # PECORA
    "'Agnello'",
    "'Svezzamento'",
    "'Giovane'",
    "'Adulto'",

    # MAIALE
    "'Suinetto'",
    "'Svezzamento'",
    "'Accrescimento'",
    "'Adulto'",

    # BOVINO
    "'Vitello'",
    "'Svezzamento'",
    "'Giovane'",
    "'Adulto'",

    # TACCHINO
    "'Pulcino'",
    "'Giovane'",
    "'Ingrasso'",
    "'Adulto'"
]

NOME_TIPO_ANIMALE = [
    # GALLINA
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",

    # CONIGLIO
    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",

    # CAPRA
    "'Capra'",
    "'Capra'",
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
    "'Maiale'",
    "'Maiale'",

    # BOVINO
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",

    # TACCHINO
    "'Tacchino'",
    "'Tacchino'",
    "'Tacchino'",
    "'Tacchino'"
]

LIVELLO_BIOSICUREZZA_MINIMO = [
    # GALLINA
    "'ALTO'",
    "'MEDIO'",
    "'MEDIO'",
    "'BASSO'",

    # CONIGLIO
    "'ALTO'",
    "'ALTO'",
    "'MEDIO'",
    "'BASSO'",

    # CAPRA
    "'ALTO'",
    "'MEDIO'",
    "'MEDIO'",
    "'BASSO'",

    # PECORA
    "'ALTO'",
    "'MEDIO'",
    "'MEDIO'",
    "'BASSO'",

    # MAIALE
    "'ALTO'",
    "'ALTO'",
    "'MEDIO'",
    "'BASSO'",

    # BOVINO
    "'ALTO'",
    "'MEDIO'",
    "'MEDIO'",
    "'BASSO'",

    # TACCHINO
    "'ALTO'",
    "'MEDIO'",
    "'MEDIO'",
    "'BASSO'"
]

ETA_MINIMA_MESI = [
    # GALLINA
    0,   # pulcino
    1,   # giovane
    5,   # ovodeposizione
    12,  # adulto

    # CONIGLIO
    0,   # cucciolo
    1,   # svezzamento
    2,   # giovane
    5,   # adulto

    # CAPRA
    0,   # capretto
    3,   # svezzamento
    6,   # giovane
    12,  # adulto

    # PECORA
    0,   # agnello
    3,   # svezzamento
    6,   # giovane
    12,  # adulto

    # MAIALE
    0,   # suinetto
    1,   # svezzamento
    3,   # accrescimento
    8,   # adulto

    # BOVINO
    0,   # vitello
    3,   # svezzamento
    12,  # giovane
    24,  # adulto

    # TACCHINO
    0,   # pulcino
    2,   # giovane
    4,   # ingrasso
    7    # adulto
]




theList=list(zip(NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI))

keys = ["NOME_STADIO_CRESCITA", "NOME_TIPO_ANIMALE", "LIVELLO_BIOSICUREZZA_MINIMO", "ETA_MINIMA_MESI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_STADIO_CRESCITA, NOME_TIPO_ANIMALE, LIVELLO_BIOSICUREZZA_MINIMO, ETA_MINIMA_MESI\n"
for i in range(len(theList)):
  lines+=make_DML_line("STADIO_CRESCITA", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/3_stadio_crescita.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/3_stadio_crescita.sql", lines)