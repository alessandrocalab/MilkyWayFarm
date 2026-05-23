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


#SENSORE:SERIALE NOME_PRODUTTORE NOME_MODELLO CODICE_AREA NOME_STRUTTURA 

AREE = [
    # PRIMO MODULO
    ("'A00A'", "'Primo Modulo'"),
    ("'A00B'", "'Primo Modulo'"),

    # STRUTTURA AGRICOLA
    ("'A00A'", "'Struttura Agricola'"),
    ("'A00B'", "'Struttura Agricola'"),
    ("'A00C'", "'Struttura Agricola'"),

    # STRUTTURA STOCCAGGIO
    ("'A00A'", "'Struttura Stoccaggio'"),
    ("'A00B'", "'Struttura Stoccaggio'"),
    ("'A00C'", "'Struttura Stoccaggio'"),
    ("'A00D'", "'Struttura Stoccaggio'"),
    ("'A00E'", "'Struttura Stoccaggio'"),
    ("'A00F'", "'Struttura Stoccaggio'"),
    ("'A00G'", "'Struttura Stoccaggio'"),
    ("'A00H'", "'Struttura Stoccaggio'"),
    ("'A00I'", "'Struttura Stoccaggio'"),
    ("'A00J'", "'Struttura Stoccaggio'"),
    ("'A00K'", "'Struttura Stoccaggio'"),
    ("'A00L'", "'Struttura Stoccaggio'"),

    # STRUTTURA ZOOTECNICA
    ("'A00A'", "'Struttura Zootecnica'"),
    ("'A00B'", "'Struttura Zootecnica'"),
    ("'A00C'", "'Struttura Zootecnica'"),
    ("'A00D'", "'Struttura Zootecnica'"),

    # STRUTTURA AGRICOLA II
    ("'A00A'", "'Struttura Agricola II'"),
    ("'A00B'", "'Struttura Agricola II'")
]


TIPI_SENSORI = [
    {
        "prefisso": "T",
        "produttore": "'EnviroSense'",
        "modello": "'TEMP-K100'"
    },
    {
        "prefisso": "H",
        "produttore": "'EnviroSense'",
        "modello": "'HUM-RH100'"
    },
    {
        "prefisso": "P",
        "produttore": "'PowerGrid Systems'",
        "modello": "'PWR-A5000'"
    }
]


SERIALE = []
NOME_PRODUTTORE = []
NOME_MODELLO = []
CODICE_AREA = []
NOME_STRUTTURA = []


for i, area in enumerate(AREE, start=1):
    codice_area, nome_struttura = area

    for sensore in TIPI_SENSORI:
        SERIALE.append(f"'{sensore['prefisso']}{i:03d}'")
        NOME_PRODUTTORE.append(sensore["produttore"])
        NOME_MODELLO.append(sensore["modello"])
        CODICE_AREA.append(codice_area)
        NOME_STRUTTURA.append(nome_struttura)


theList=list(zip(SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA))

keys = ["SERIALE", "NOME_PRODUTTORE", "NOME_MODELLO", "CODICE_AREA", "NOME_STRUTTURA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, NOME_PRODUTTORE, NOME_MODELLO, CODICE_AREA, NOME_STRUTTURA\n"
for i in range(len(theList)):
  lines+=make_DML_line("SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/7_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/7_sensore.sql", lines)