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


#TIPO_SENSORE:NOME_PRODUTTORE NOME_MODELLO VALORE_MIN VALORE_MAX PRECISIONE GRANDEZZA_MISURATA UNITA_MISURA FREQUENZA_RILEVAMENTO_HZ 

NOME_PRODUTTORE = [
    "'EnviroSense'",
    "'EnviroSense'",
    "'PowerGrid Systems'"
]

NOME_MODELLO = [
    "'TEMP-K100'",
    "'HUM-RH100'",
    "'PWR-A5000'"
]

VALORE_MIN = [
    193.15,   # temperatura minima misurabile, -80°C
    0,        # umidità relativa minima
    0         # potenza minima
]

VALORE_MAX = [
    333.15,   # temperatura massima misurabile, 60°C
    100,      # umidità relativa massima
    5000      # potenza massima area, 5000 W
]

PRECISIONE = [
    0.10,     # ±0.10 K
    1.00,     # ±1%
    10.00     # ±10 W
]

GRANDEZZA_MISURATA = [
    "'Temperatura'",
    "'Umidita relativa'",
    "'Potenza elettrica'"
]

UNITA_MISURA = [
    "'K'",
    "'%'",
    "'W'"
]

FREQUENZA_RILEVAMENTO_HZ = [
    1.0,     # una misura ogni 1 secondi
    1.0,     # una misura ogni 1 secondi
    1.00      # una misura ogni secondo
]


theList=list(zip(NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ))

keys = ["NOME_PRODUTTORE", "NOME_MODELLO", "VALORE_MIN", "VALORE_MAX", "PRECISIONE", "GRANDEZZA_MISURATA", "UNITA_MISURA", "FREQUENZA_RILEVAMENTO_HZ"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODUTTORE, NOME_MODELLO, VALORE_MIN, VALORE_MAX, PRECISIONE, GRANDEZZA_MISURATA, UNITA_MISURA, FREQUENZA_RILEVAMENTO_HZ\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/6_tipo_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/6_tipo_sensore.sql", lines)