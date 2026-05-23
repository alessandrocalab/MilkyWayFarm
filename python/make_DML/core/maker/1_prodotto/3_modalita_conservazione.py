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


#MODALITA_CONSERVAZIONE:NOME_CONSERVAZIONE DURATA_MASSIMA_GIORNI TEMPERATURA_MAX TEMPERATURA_MIN UMIDITA_MIN UMIDITA_MAX 

NOME_CONSERVAZIONE = [
    "'Ambiente secco controllato'",
    "'Ambiente fresco controllato'",
    "'Refrigerazione standard'",
    "'Congelamento standard'",
    "'Catena del freddo sanitaria'",
    "'Conservazione semi breve termine'",
    "'Conservazione semi lungo termine'",
    "'Conservazione tuberi e radici'",
    "'Conservazione verdure fresche'",
    "'Conservazione mangimi secchi'",
    "'Conservazione biomasse organiche'",
    "'Conservazione soluzioni agricole'"
]

DURATA_MASSIMA_GIORNI = [
    365,   # cereali, legumi secchi, prodotti stabili
    180,   # prodotti freschi ma non refrigerati
    14,    # latte, uova, verdure, funghi, alghe fresche
    365,   # carne congelata, prodotti surgelati
    365,   # vaccini e farmaci refrigerati
    180,   # semi usati entro pochi cicli produttivi
    1460,  # semi da banca genetica/riserva
    120,   # patate, carote, barbabietole, radici
    10,    # lattuga, spinaci, rucola, bietola
    365,   # mangimi animali, fieno, paglia
    180,   # letame, pollina, compost sterile
    180    # soluzioni nutritive, correttori pH, concentrati
]

TEMPERATURA_MIN = [
    288.15,  # 15°C
    281.15,  # 8°C
    273.15,  # 0°C
    253.15,  # -20°C
    275.15,  # 2°C
    277.15,  # 4°C
    273.15,  # 0°C
    277.15,  # 4°C
    274.15,  # 1°C
    283.15,  # 10°C
    278.15,  # 5°C
    278.15   # 5°C
]

TEMPERATURA_MAX = [
    298.15,  # 25°C
    288.15,  # 15°C
    277.15,  # 4°C
    255.15,  # -18°C
    281.15,  # 8°C
    283.15,  # 10°C
    278.15,  # 5°C
    285.15,  # 12°C
    277.15,  # 4°C
    298.15,  # 25°C
    298.15,  # 25°C
    298.15   # 25°C
]

UMIDITA_MIN = [
    25,
    35,
    70,
    30,
    35,
    20,
    15,
    85,
    90,
    25,
    30,
    30
]


UMIDITA_MAX = [
    55,
    65,
    90,
    60,
    65,
    45,
    35,
    95,
    98,
    60,
    70,
    60
]



theList=list(zip(NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX))

keys = ["NOME_CONSERVAZIONE", "DURATA_MASSIMA_GIORNI", "TEMPERATURA_MAX", "TEMPERATURA_MIN", "UMIDITA_MIN", "UMIDITA_MAX"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_CONSERVAZIONE, DURATA_MASSIMA_GIORNI, TEMPERATURA_MAX, TEMPERATURA_MIN, UMIDITA_MIN, UMIDITA_MAX\n"
for i in range(len(theList)):
  lines+=make_DML_line("MODALITA_CONSERVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/3_modalita_conservazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/3_modalita_conservazione.sql", lines)