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


#ANIMALE:ETICHETTA DATA_USCITA ETICHETTA_GENITORE SESSO MESE_NASCITA ANNO_NASCITA DATA_INGRESSO NOME_TIPO_ANIMALE 

ETICHETTA = [
    "'0000000001'",
    "'0000000002'",
    "'0000000003'",
    "'0000000004'",

    "'0000000005'",
    "'0000000006'",
    "'0000000007'",

    "'0000000008'",
    "'0000000009'",
    "'0000000010'",

    "'0000000011'",
    "'0000000012'",
    "'0000000013'",
    "'0000000014'",
    "'0000000015'",

    "'0000000016'",
    "'0000000017'",
    "'0000000018'",
    "'0000000019'",
    "'0000000020'",
    "'0000000021'",
    "'0000000022'",
    "'0000000023'",

    "'0000000024'",
    "'0000000025'",
    "'0000000026'",
    "'0000000027'",

    "'0000000028'",
    "'0000000029'",
    "'0000000030'",
    "'0000000031'",
    "'0000000032'",
    "'0000000033'",

    "'0000000034'",
    "'0000000035'",

    "'0000000036'",
    "'0000000037'",
    "'0000000038'",
    "'0000000039'",

    "'0000000040'",
    "'0000000041'",
    "'0000000042'",
    "'0000000043'"
]

DATA_USCITA = [
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",

    "DATE '2025-03-18'",
    "DATE '2025-03-18'",
    "DATE '2025-03-19'",
    "DATE '2025-03-19'",

    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

ETICHETTA_GENITORE = [
    "NULL",
    "NULL",
    "'0000000001'",
    "'0000000001'",

    "NULL",
    "NULL",
    "'0000000005'",

    "NULL",
    "NULL",
    "'0000000008'",

    "NULL",
    "NULL",
    "'0000000011'",
    "'0000000011'",
    "'0000000011'",

    "NULL",
    "NULL",
    "'0000000016'",
    "'0000000016'",
    "'0000000016'",
    "'0000000016'",
    "'0000000016'",
    "'0000000016'",

    "NULL",
    "NULL",
    "'0000000024'",
    "'0000000024'",

    "NULL",
    "NULL",
    "'0000000028'",
    "'0000000028'",
    "'0000000028'",
    "'0000000028'",

    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL",

    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

SESSO = [
    "'F'",
    "'M'",
    "'F'",
    "'M'",

    "'F'",
    "'M'",
    "'F'",

    "'F'",
    "'M'",
    "'F'",

    "'F'",
    "'M'",
    "'F'",
    "'M'",
    "'F'",

    "'F'",
    "'M'",
    "'F'",
    "'F'",
    "'F'",
    "'F'",
    "'M'",
    "'F'",

    "'F'",
    "'M'",
    "'F'",
    "'M'",

    "'F'",
    "'M'",
    "'F'",
    "'M'",
    "'F'",
    "'M'",

    "'F'",
    "'M'",

    "'F'",
    "'F'",
    "'M'",
    "'F'",

    "'F'",
    "'F'",
    "'F'",
    "'M'"
]


MESE_NASCITA = [
    6,
    8,
    1,
    2,

    5,
    4,
    9,

    3,
    7,
    10,

    11,
    1,
    8,
    8,
    9,

    4,
    5,
    9,
    9,
    10,
    10,
    11,
    11,

    3,
    4,
    10,
    10,

    2,
    6,
    12,
    12,
    1,
    1,

    12,
    9,

    1,
    5,
    7,
    6,

    2,
    3,
    1,
    1
]

ANNO_NASCITA = [
    2019,
    2020,
    2024,
    2024,

    2021,
    2022,
    2024,

    2021,
    2021,
    2024,

    2021,
    2022,
    2024,
    2024,
    2024,

    2023,
    2023,
    2024,
    2024,
    2024,
    2024,
    2024,
    2024,

    2023,
    2023,
    2024,
    2024,

    2023,
    2023,
    2024,
    2024,
    2025,
    2025,

    2022,
    2023,

    2024,
    2024,
    2024,
    2023,

    2024,
    2024,
    2024,
    2024
]

DATA_INGRESSO = [
    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",

    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",

    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",

    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",

    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    "DATE '2025-02-24'",
    "DATE '2025-02-24'",

    "DATE '2025-02-26'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-28'",

    "DATE '2025-05-04'",
    "DATE '2025-05-04'",
    "DATE '2025-05-05'",
    "DATE '2025-05-05'"
]


NOME_TIPO_ANIMALE = [
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",
    "'Bovino'",

    "'Capra'",
    "'Capra'",
    "'Capra'",

    "'Pecora'",
    "'Pecora'",
    "'Pecora'",

    "'Maiale'",
    "'Maiale'",
    "'Maiale'",
    "'Maiale'",
    "'Maiale'",

    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",
    "'Gallina'",

    "'Tacchino'",
    "'Tacchino'",
    "'Tacchino'",
    "'Tacchino'",

    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",
    "'Coniglio'",

    "'Capra'",
    "'Coniglio'",

    "'Gallina'",
    "'Coniglio'",
    "'Maiale'",
    "'Pecora'",

    "'Gallina'",
    "'Gallina'",
    "'Coniglio'",
    "'Coniglio'"
]

theList=list(zip(ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE))

keys = ["ETICHETTA", "DATA_USCITA", "ETICHETTA_GENITORE", "SESSO", "MESE_NASCITA", "ANNO_NASCITA", "DATA_INGRESSO", "NOME_TIPO_ANIMALE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE", theList[i])+"\n"

os.makedirs("make_DML/data/3_animale", exist_ok=True)
with open("make_DML/data/3_animale/2_animale.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/3_animale/2_animale.sql", lines)