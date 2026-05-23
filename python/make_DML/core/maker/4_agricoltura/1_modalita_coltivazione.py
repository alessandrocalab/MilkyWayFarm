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


#MODALITA_COLTIVAZIONE:NOME_MODALITA_COLTIVAZIONE NOME_PRODOTTO PH_MIN PH_MAX TEMPERATURA_MIN TEMPERATURA_MAX UMIDITA_MIN UMIDITA_MAX IMPOLLINAZIONE SISTEMA_ILLUMINAZIONE ACQUA_ML_ORA ORE_LUCE_GIORNO SOLUZIONE_NUTRITIVA QUANTITA_SOLUZIONE_ML_ORA 


NOME_MODALITA_COLTIVAZIONE = [
    "'Idro cereali base'",
    "'Idro riso sommerso'",
    "'Idro tuberi substrato'",
    "'Idro pomodoro standard'",
    "'Idro pomodoro intensivo'",
    "'Idro lattuga rapida'",
    "'Idro radici substrato'",
    "'Idro cucurbitacee'",
    "'Idro legumi base'",
    "'Idro soia nutriente'"
]

NOME_PRODOTTO = [
    "'Soluzione nutritiva idroponica base'",
    "'Soluzione nutritiva idroponica base'",
    "'Substrato in fibra di cocco'",
    "'Soluzione nutritiva idroponica base'",
    "'Soluzione nutritiva concentrata'",
    "'Soluzione nutritiva idroponica base'",
    "'Substrato in fibra di cocco'",
    "'Soluzione nutritiva concentrata'",
    "'Biofertilizzante microbico'",
    "'Soluzione nutritiva concentrata'"
]

PH_MIN = [
    6.0,
    5.5,
    5.5,
    5.8,
    5.8,
    5.8,
    6.0,
    5.8,
    6.0,
    6.0
]

PH_MAX = [
    7.0,
    6.5,
    6.5,
    6.8,
    6.8,
    6.5,
    6.8,
    6.8,
    7.0,
    7.0
]

TEMPERATURA_MIN = [
    291,
    295,
    289,
    293,
    295,
    289,
    288,
    294,
    291,
    292
]

TEMPERATURA_MAX = [
    297,
    303,
    295,
    300,
    303,
    295,
    294,
    301,
    298,
    300
]

UMIDITA_MIN = [
    55,
    70,
    60,
    60,
    65,
    65,
    60,
    60,
    55,
    55
]

UMIDITA_MAX = [
    75,
    90,
    80,
    80,
    85,
    85,
    80,
    80,
    75,
    75
]


IMPOLLINAZIONE = [
    0,  # cereali
    0,  # riso
    0,  # patata
    1,  # pomodoro
    1,  # pomodoro intensivo
    0,  # lattuga
    0,  # carota
    1,  # zucchina
    1,  # fagiolo
    1   # soia
]

SISTEMA_ILLUMINAZIONE = [
    "'LED_FULL'",
    "'LED_BIANCO'",
    "'LED_BIANCO'",
    "'LED_FULL'",
    "'LED_VIOLA'",
    "'LED_BIANCO'",
    "'LED_BIANCO'",
    "'LED_FULL'",
    "'LED_FULL'",
    "'LED_FULL'"
]

ACQUA_ML_ORA = [
    45.00,
    90.00,
    55.00,
    70.00,
    85.00,
    35.00,
    40.00,
    75.00,
    55.00,
    60.00
]

ORE_LUCE_GIORNO = [
    14,
    13,
    12,
    16,
    18,
    14,
    13,
    16,
    14,
    14
]


QUANTITA_SOLUZIONE_ML_ORA = [
    4.00,
    6.00,
    4.50,
    6.00,
    7.50,
    3.00,
    3.50,
    6.50,
    4.50,
    5.00
]
theList=list(zip(NOME_MODALITA_COLTIVAZIONE, NOME_PRODOTTO, PH_MIN, PH_MAX, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, IMPOLLINAZIONE, SISTEMA_ILLUMINAZIONE, ACQUA_ML_ORA, ORE_LUCE_GIORNO, QUANTITA_SOLUZIONE_ML_ORA))

keys = ["NOME_MODALITA_COLTIVAZIONE", "NOME_PRODOTTO", "PH_MIN", "PH_MAX", "TEMPERATURA_MIN", "TEMPERATURA_MAX", "UMIDITA_MIN", "UMIDITA_MAX", "IMPOLLINAZIONE", "SISTEMA_ILLUMINAZIONE", "ACQUA_ML_ORA", "ORE_LUCE_GIORNO", "QUANTITA_SOLUZIONE_ML_ORA"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_MODALITA_COLTIVAZIONE, NOME_PRODOTTO, PH_MIN, PH_MAX, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, IMPOLLINAZIONE, SISTEMA_ILLUMINAZIONE, ACQUA_ML_ORA, ORE_LUCE_GIORNO, QUANTITA_SOLUZIONE_ML_ORA\n"
for i in range(len(theList)):
  lines+=make_DML_line("MODALITA_COLTIVAZIONE", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/1_modalita_coltivazione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/1_modalita_coltivazione.sql", lines)