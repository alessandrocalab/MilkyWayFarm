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


#REGISTRAZIONE_SENSORE:SERIALE DATA_SECONDI NOME_PRODUTTORE MISURAZIONE 

import random

random.seed(42)

AREE = [
    # codice_area, nome_struttura, temp_min, temp_max, um_min, um_max, pressione_pa, volume_m3
    ("A00A", "Primo Modulo", 288.15, 298.15, 25, 55, 98000, 75),
    ("A00B", "Primo Modulo", 288.15, 298.15, 25, 55, 98000, 30),

    ("A00A", "Struttura Agricola", 288.15, 298.15, 25, 55, 98000, 100),
    ("A00B", "Struttura Agricola", 288.15, 298.15, 25, 55, 98000, 40),
    ("A00C", "Struttura Agricola", 288.15, 298.15, 25, 55, 98000, 60),

    ("A00A", "Struttura Stoccaggio", 288.15, 298.15, 25, 55, 98000, 75),
    ("A00B", "Struttura Stoccaggio", 281.15, 288.15, 35, 65, 98000, 45),
    ("A00C", "Struttura Stoccaggio", 273.15, 277.15, 70, 90, 98500, 55),
    ("A00D", "Struttura Stoccaggio", 253.15, 255.15, 30, 60, 99000, 40),
    ("A00E", "Struttura Stoccaggio", 275.15, 281.15, 35, 65, 99500, 25),
    ("A00F", "Struttura Stoccaggio", 277.15, 283.15, 20, 45, 98000, 35),
    ("A00G", "Struttura Stoccaggio", 273.15, 278.15, 15, 35, 98500, 30),
    ("A00H", "Struttura Stoccaggio", 277.15, 285.15, 85, 95, 98000, 55),
    ("A00I", "Struttura Stoccaggio", 274.15, 277.15, 90, 98, 98500, 35),
    ("A00J", "Struttura Stoccaggio", 283.15, 298.15, 25, 60, 98000, 70),
    ("A00K", "Struttura Stoccaggio", 278.15, 298.15, 30, 70, 99000, 60),
    ("A00L", "Struttura Stoccaggio", 278.15, 298.15, 30, 60, 98500, 45),

    ("A00A", "Struttura Zootecnica", 288, 298, 25, 55, 103000, 60),
    ("A00B", "Struttura Zootecnica", 278, 308, 0, 100, 98000, 1120),
    ("A00C", "Struttura Zootecnica", 298, 308, 80, 100, 99000, 240),
    ("A00D", "Struttura Zootecnica", 278, 308, 0, 100, 101000, 210),

    ("A00A", "Struttura Agricola II", 281.15, 298.15, 55, 75, 101000, 200),
    ("A00B", "Struttura Agricola II", 283.15, 300.15, 60, 80, 101000, 350),
]


SERIALE = []
DATA_SECONDI = []
NOME_PRODUTTORE = []
MISURAZIONE = []


def valore_normale(min_val, max_val, rumore):
    medio = (min_val + max_val) / 2
    valore = medio + random.uniform(-rumore, rumore)

    # tengo il valore dentro i limiti, tranne nei casi di anomalia
    if valore < min_val:
        valore = min_val + random.uniform(0, rumore)
    if valore > max_val:
        valore = max_val - random.uniform(0, rumore)

    return round(valore, 2)


def potenza_area(volume_m3, nome_struttura, codice_area):
    base = 200 + volume_m3 * 6

    if nome_struttura == "Struttura Stoccaggio":
        if codice_area in ["A00C", "A00D", "A00E", "A00I"]:
            base += 900  # refrigerazione, congelamento, sanitario
        else:
            base += 250

    elif nome_struttura == "Struttura Agricola":
        base += 1200  # luci, pompe, controllo coltivazione

    elif nome_struttura == "Struttura Agricola II":
        base += 1500

    elif nome_struttura == "Struttura Zootecnica":
        base += 900

    else:
        base += 300

    return round(base + random.uniform(-120, 120), 2)


# 3 registrazioni per ogni sensore
# 0 secondi, 3600 secondi, 7200 secondi
TEMPI = [0, 3600, 7200]


for indice_area, area in enumerate(AREE, start=1):
    codice_area, nome_struttura, t_min, t_max, u_min, u_max, pressione, volume = area

    seriale_temp = f"'T{indice_area:03d}'"
    seriale_umid = f"'H{indice_area:03d}'"
    seriale_pot = f"'P{indice_area:03d}'"

    for t in TEMPI:

        # -------------------------
        # TEMPERATURA
        # -------------------------
        SERIALE.append(seriale_temp)
        DATA_SECONDI.append(t)
        NOME_PRODUTTORE.append("'EnviroSense'")

        if nome_struttura == "Struttura Agricola" and codice_area == "A00B" and t == 3600:
            # anomalia rara: surriscaldamento coltivazione
            MISURAZIONE.append(round(t_max + 4.80, 2))
        else:
            MISURAZIONE.append(valore_normale(t_min, t_max, 1.20))

        # -------------------------
        # UMIDITA
        # -------------------------
        SERIALE.append(seriale_umid)
        DATA_SECONDI.append(t)
        NOME_PRODUTTORE.append("'EnviroSense'")

        if nome_struttura == "Struttura Agricola" and codice_area == "A00B" and t == 3600:
            # anomalia rara: calo umidità
            MISURAZIONE.append(round(u_min - 9.00, 2))
        else:
            MISURAZIONE.append(valore_normale(u_min, u_max, 4.00))

        # -------------------------
        # POTENZA ELETTRICA
        # -------------------------
        SERIALE.append(seriale_pot)
        DATA_SECONDI.append(t)
        NOME_PRODUTTORE.append("'PowerGrid Systems'")

        if nome_struttura == "Struttura Agricola" and codice_area == "A00B" and t == 3600:
            # anomalia rara: picco elettrico pompe/luci
            MISURAZIONE.append(4870.00)
        else:
            MISURAZIONE.append(potenza_area(volume, nome_struttura, codice_area))

theList=list(zip(SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE))

keys = ["SERIALE", "DATA_SECONDI", "NOME_PRODUTTORE", "MISURAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--SERIALE, DATA_SECONDI, NOME_PRODUTTORE, MISURAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("REGISTRAZIONE_SENSORE", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/8_registrazione_sensore.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/8_registrazione_sensore.sql", lines)