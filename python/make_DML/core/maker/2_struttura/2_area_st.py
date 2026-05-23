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


#AREA_ST:CODICE_AREA NOME_STRUTTURA DATA_TERMINAZIONE TEMPERATURA_MIN TEMPERATURA_MAX UMIDITA_MIN UMIDITA_MAX LIVELLO_SICUREZZA PRESSIONE_PA VOLUME_M3 SUPERFICIE_MQ DATA_ATTIVAZIONE 

CODICE_AREA = [
    "'A00A'",  # Ambiente secco controllato
    "'A00B'",  # Ambiente fresco controllato
    "'A00C'",  # Refrigerazione standard
    "'A00D'",  # Congelamento standard
    "'A00E'",  # Catena del freddo sanitaria
    "'A00F'",  # Conservazione semi breve termine
    "'A00G'",  # Conservazione semi lungo termine
    "'A00H'",  # Conservazione tuberi e radici
    "'A00I'",  # Conservazione verdure fresche
    "'A00J'",  # Conservazione mangimi secchi
    "'A00K'",  # Conservazione biomasse organiche
    "'A00L'"   # Conservazione soluzioni agricole
]

NOME_STRUTTURA = [
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'",
    "'Struttura Stoccaggio'"
]

DATA_TERMINAZIONE = [
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
    "NULL"
]
TEMPERATURA_MIN = [
    288.15,  # Ambiente secco controllato
    281.15,  # Ambiente fresco controllato
    273.15,  # Refrigerazione standard
    253.15,  # Congelamento standard
    275.15,  # Catena del freddo sanitaria
    277.15,  # Semi breve termine
    273.15,  # Semi lungo termine
    277.15,  # Tuberi e radici
    274.15,  # Verdure fresche
    283.15,  # Mangimi secchi
    278.15,  # Biomasse organiche
    278.15   # Soluzioni agricole
]

TEMPERATURA_MAX = [
    298.15,
    288.15,
    277.15,
    255.15,
    281.15,
    283.15,
    278.15,
    285.15,
    277.15,
    298.15,
    298.15,
    298.15
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
LIVELLO_SICUREZZA = [
    "'L2'",  # secco
    "'L2'",  # fresco
    "'L3'",  # refrigerato
    "'L4'",  # congelato
    "'L5'",  # vaccini/farmaci sensibili
    "'L3'",  # semi breve
    "'L4'",  # semi lungo termine
    "'L2'",  # tuberi/radici
    "'L3'",  # verdure fresche
    "'L2'",  # mangimi
    "'L4'",  # biomasse organiche
    "'L3'"   # soluzioni agricole
]

PRESSIONE_PA = [
    98000,
    98000,
    98500,
    99000,
    99500,
    98000,
    98500,
    98000,
    98500,
    98000,
    99000,
    98500
]

VOLUME_M3 = [
    75,
    45,
    55,
    40,
    25,
    35,
    30,
    55,
    35,
    70,
    60,
    45
]
SUPERFICIE_MQ = [
    22,
    15,
    18,
    12,
    8,
    12,
    10,
    16,
    12,
    20,
    18,
    14
]

DATA_ATTIVAZIONE = [
    "DATE '2023-08-05'",
    "DATE '2023-08-05'",
    "DATE '2023-08-06'",
    "DATE '2023-08-07'",
    "DATE '2023-08-07'",
    "DATE '2023-08-08'",
    "DATE '2023-08-08'",
    "DATE '2023-08-09'",
    "DATE '2023-08-09'",
    "DATE '2023-08-10'",
    "DATE '2023-08-10'",
    "DATE '2023-08-11'"
]

theList=list(zip(CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE))

keys = ["CODICE_AREA", "NOME_STRUTTURA", "DATA_TERMINAZIONE", "TEMPERATURA_MIN", "TEMPERATURA_MAX", "UMIDITA_MIN", "UMIDITA_MAX", "LIVELLO_SICUREZZA", "PRESSIONE_PA", "VOLUME_M3", "SUPERFICIE_MQ", "DATA_ATTIVAZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--CODICE_AREA, NOME_STRUTTURA, DATA_TERMINAZIONE, TEMPERATURA_MIN, TEMPERATURA_MAX, UMIDITA_MIN, UMIDITA_MAX, LIVELLO_SICUREZZA, PRESSIONE_PA, VOLUME_M3, SUPERFICIE_MQ, DATA_ATTIVAZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("AREA_ST", theList[i])+"\n"

os.makedirs("make_DML/data/2_struttura", exist_ok=True)
with open("make_DML/data/2_struttura/2_area_st.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/2_struttura/2_area_st.sql", lines,"a")