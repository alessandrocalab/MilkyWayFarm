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


#PRODUZIONE_AGRICOLA:DATA_PRODUZIONE_AGRICOLA DATA_INIZIO_CICLO_COLTIVAZIONE CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA NOME_PRODOTTO QUANTITA 

DATA_PRODUZIONE_AGRICOLA = [
    "DATE '2023-12-28'",
    "DATE '2023-12-28'",

    "DATE '2024-05-30'",
    "DATE '2024-05-30'",

    "DATE '2025-09-29'",
    "DATE '2025-09-29'",

    "DATE '2023-11-02'",
    "DATE '2023-11-02'",

    "DATE '2024-05-14'",
    "DATE '2024-05-14'",

    "DATE '2025-02-24'",
    "DATE '2025-02-24'",

    "DATE '2023-10-27'",
    "DATE '2023-10-27'",

    "DATE '2024-06-28'",
    "DATE '2024-06-28'",

    "DATE '2023-10-18'",
    "DATE '2023-10-18'",

    "DATE '2024-04-21'",
    "DATE '2024-04-21'",

    "DATE '2025-07-04'",
    "DATE '2025-07-04'",

    "DATE '2026-05-20'",
    "DATE '2026-05-20'"
]
DATA_INIZIO_CICLO_COLTIVAZIONE = [
    "DATE '2023-07-01'",
    "DATE '2023-07-01'",

    "DATE '2024-03-01'",
    "DATE '2024-03-01'",

    "DATE '2025-06-01'",
    "DATE '2025-06-01'",

    "DATE '2023-07-05'",
    "DATE '2023-07-05'",

    "DATE '2024-01-15'",
    "DATE '2024-01-15'",

    "DATE '2025-01-10'",
    "DATE '2025-01-10'",

    "DATE '2023-08-01'",
    "DATE '2023-08-01'",

    "DATE '2024-04-01'",
    "DATE '2024-04-01'",

    "DATE '2023-07-10'",
    "DATE '2023-07-10'",

    "DATE '2024-02-01'",
    "DATE '2024-02-01'",

    "DATE '2025-05-10'",
    "DATE '2025-05-10'",

    "DATE '2026-04-05'",
    "DATE '2026-04-05'"
]
CODICE_CELLA_IDR = [
    "'000A'", "'000A'",
    "'000A'", "'000A'",
    "'000A'", "'000A'",

    "'000B'", "'000B'",
    "'000B'", "'000B'",
    "'000B'", "'000B'",

    "'000C'", "'000C'",
    "'000C'", "'000C'",

    "'000D'", "'000D'",
    "'000D'", "'000D'",
    "'000D'", "'000D'",

    "'001A'", "'001A'"
]
CODICE_AREA = [
    "'A00A'", "'A00A'",
    "'A00A'", "'A00A'",
    "'A00A'", "'A00A'",

    "'A00A'", "'A00A'",
    "'A00A'", "'A00A'",
    "'A00A'", "'A00A'",

    "'A00B'", "'A00B'",
    "'A00B'", "'A00B'",

    "'A00C'", "'A00C'",
    "'A00C'", "'A00C'",
    "'A00C'", "'A00C'",

    "'A00A'", "'A00A'"
]
NOME_STRUTTURA = [
    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",

    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",

    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",

    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",
    "'Struttura Agricola'", "'Struttura Agricola'",

    "'Struttura Agricola II'", "'Struttura Agricola II'"
]
NOME_PRODOTTO = [
    "'Grano duro'",
    "'Semi di grano duro'",

    "'Pomodoro'",
    "'Semi di pomodoro'",

    "'Mais'",
    "'Semi di mais'",

    "'Mais'",
    "'Semi di mais'",

    "'Soia'",
    "'Semi di soia'",

    "'Lattuga'",
    "'Semi di lattuga'",

    "'Pomodoro'",
    "'Semi di pomodoro'",

    "'Fagiolo'",
    "'Semi di fagiolo'",

    "'Patata'",
    "'Talee di patata'",

    "'Carota'",
    "'Semi di carota'",

    "'Zucchina'",
    "'Semi di zucchina'",

    "'Lattuga'",
    "'Semi di lattuga'"
]
QUANTITA = [
    8.40,   # Grano duro
    0.80,   # Semi di grano duro

    18.00,  # Pomodoro
    0.10,   # Semi di pomodoro

    14.00,  # Mais
    1.00,   # Semi di mais

    17.50,  # Mais
    1.20,   # Semi di mais

    8.75,   # Soia
    0.80,   # Semi di soia

    7.00,   # Lattuga
    0.05,   # Semi di lattuga

    21.00,  # Pomodoro
    0.12,   # Semi di pomodoro

    5.00,   # Fagiolo
    0.45,   # Semi di fagiolo

    6.00,   # Patata
    0.70,   # Talee di patata

    12.00,  # Carota
    0.08,   # Semi di carota

    12.00,  # Zucchina
    0.10,   # Semi di zucchina

    10.50,  # Lattuga
    0.07    # Semi di lattuga
]
theList=list(zip(DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA))

keys = ["DATA_PRODUZIONE_AGRICOLA", "DATA_INIZIO_CICLO_COLTIVAZIONE", "CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "NOME_PRODOTTO", "QUANTITA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_PRODUZIONE_AGRICOLA, DATA_INIZIO_CICLO_COLTIVAZIONE, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, NOME_PRODOTTO, QUANTITA\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODUZIONE_AGRICOLA", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/5_produzione_agricola.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/5_produzione_agricola.sql", lines)