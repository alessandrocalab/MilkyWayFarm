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


#CICLO_COLTIVAZIONE:DATA_INIZIO CODICE_CELLA_IDR CODICE_AREA NOME_STRUTTURA DATA_FINE_EFFETTIVA QUANTITA_SEMI NOME_MOD_COLTIVAZIONE NOME_TIPO_COLTURA 

DATA_INIZIO = [
    "DATE '2023-07-01'",
    "DATE '2024-03-01'",
    "DATE '2025-06-01'",

    "DATE '2023-07-05'",
    "DATE '2024-01-15'",
    "DATE '2025-01-10'",

    "DATE '2023-08-01'",
    "DATE '2024-04-01'",

    "DATE '2023-07-10'",
    "DATE '2024-02-01'",
    "DATE '2025-05-10'",

    "DATE '2026-04-05'",
    "DATE '2026-05-21'",
    "DATE '2026-04-05'",
    "DATE '2026-04-04'"
]

CODICE_CELLA_IDR = [
    "'000A'",
    "'000A'",
    "'000A'",

    "'000B'",
    "'000B'",
    "'000B'",

    "'000C'",
    "'000C'",

    "'000D'",
    "'000D'",
    "'000D'",

    "'001A'",
    "'001A'",
    "'001B'",
    "'001C'"
]

CODICE_AREA = [
    "'A00A'",
    "'A00A'",
    "'A00A'",

    "'A00A'",
    "'A00A'",
    "'A00A'",

    "'A00B'",
    "'A00B'",

    "'A00C'",
    "'A00C'",
    "'A00C'",

    "'A00A'",
    "'A00A'",
    "'A00A'",
    "'A00A'"
]

NOME_STRUTTURA = [
    "'Struttura Agricola'",
    "'Struttura Agricola'",
    "'Struttura Agricola'",

    "'Struttura Agricola'",
    "'Struttura Agricola'",
    "'Struttura Agricola'",

    "'Struttura Agricola'",
    "'Struttura Agricola'",

    "'Struttura Agricola'",
    "'Struttura Agricola'",
    "'Struttura Agricola'",

    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'",
    "'Struttura Agricola II'"
]




DATA_FINE_EFFETTIVA = [
    "DATE '2023-12-28'",  # Grano duro, 180 giorni
    "DATE '2024-05-30'",  # Pomodoro, 90 giorni
    "DATE '2025-09-29'",  # Mais, 120 giorni

    "DATE '2023-11-02'",  # Mais, 120 giorni
    "DATE '2024-05-14'",  # Soia, 120 giorni
    "DATE '2025-02-24'",  # Lattuga, 45 giorni

    "DATE '2023-10-27'",  # Pomodoro, 90 giorni
    "DATE '2024-06-28'",  # Fagiolo, 90 giorni

    "DATE '2023-10-18'",  # Patata, 100 giorni
    "DATE '2024-04-21'",  # Carota, 80 giorni
    "DATE '2025-07-04'",  # Zucchina, 55 giorni

    "DATE '2026-05-20'",  # Lattuga, 45 giorni
    "NULL",               # Fagiolo ancora aperto
    "NULL",               # Mais ancora aperto
    "NULL"                # Patata ancora aperta
]
QUANTITA_SEMI = [
    0.6,  # kg Grano duro
    0.3,   # kg Pomodoro
    0.4,  # kg Mais

    0.5,  # kg Mais
    0.35,  # kg Soia
    0.2,   # kg Lattuga

    0.3,   # kg Pomodoro
    0.2,  # kg Fagiolo

    0.2,  # kg Patata/talee
    0.8,   # kg Carota
    0.4,   # kg Zucchina

    0.3,   # kg Lattuga
    0.3,  # kg Fagiolo
    0.5,  # kg Mais
    0.2   # kg Patata/talee
]
NOME_MOD_COLTIVAZIONE = [
    "'Idro cereali base'",
    "'Idro pomodoro standard'",
    "'Idro cereali base'",

    "'Idro cereali base'",
    "'Idro soia nutriente'",
    "'Idro lattuga rapida'",

    "'Idro pomodoro intensivo'",
    "'Idro legumi base'",

    "'Idro tuberi substrato'",
    "'Idro radici substrato'",
    "'Idro cucurbitacee'",

    "'Idro lattuga rapida'",
    "'Idro legumi base'",
    "'Idro cereali base'",
    "'Idro tuberi substrato'"
]

NOME_TIPO_COLTURA = [
    "'Grano duro'",
    "'Pomodoro'",
    "'Mais'",

    "'Mais'",
    "'Soia'",
    "'Lattuga'",

    "'Pomodoro'",
    "'Fagiolo'",

    "'Patata'",
    "'Carota'",
    "'Zucchina'",

    "'Lattuga'",
    "'Fagiolo'",
    "'Mais'",
    "'Patata'"
]


theList=list(zip(DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, QUANTITA_SEMI, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA))

keys = ["DATA_INIZIO", "CODICE_CELLA_IDR", "CODICE_AREA", "NOME_STRUTTURA", "DATA_FINE_EFFETTIVA", "QUANTITA_SEMI", "NOME_MOD_COLTIVAZIONE", "NOME_TIPO_COLTURA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--DATA_INIZIO, CODICE_CELLA_IDR, CODICE_AREA, NOME_STRUTTURA, DATA_FINE_EFFETTIVA, QUANTITA_SEMI, NOME_MOD_COLTIVAZIONE, NOME_TIPO_COLTURA\n"
for i in range(len(theList)):
  lines+=make_DML_line("CICLO_COLTIVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/3_ciclo_coltivazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/3_ciclo_coltivazione.sql", lines)