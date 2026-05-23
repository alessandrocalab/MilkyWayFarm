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


#ANIMALE_ALLOCATO_BLOCCO:NUMERO_BLOCCO NOME_STRUTTURA CODICE_AREA ETICHETTA_ANIMALE DATA_ALLOCAZIONE DATA_DEALLOCAIONE 

NUMERO_BLOCCO = [
    # A00B - BOVINI
    "'0001'",
    "'0001'",
    "'0001'",
    "'0001'",

    # A00B - CAPRE E PECORE
    "'0002'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0002'",
    "'0002'",

    # A00B - MAIALI
    "'0003'",
    "'0003'",
    "'0003'",
    "'0003'",
    "'0003'",

    # A00B - GALLINE
    "'0004'",
    "'0004'",
    "'0004'",
    "'0004'",
    "'0004'",
    "'0004'",
    "'0004'",
    "'0004'",

    # A00B - TACCHINI
    "'0005'",
    "'0005'",
    "'0005'",
    "'0005'",

    # A00B - CONIGLI
    "'0006'",
    "'0006'",
    "'0006'",
    "'0006'",
    "'0006'",
    "'0006'",

    # A00A - PICCOLA QUARANTENA / ISOLAMENTO
    "'001'",
    "'002'",

    # A00C - BLOCCO DISMESSO
    "'0001'",
    "'0002'",
    "'0003'",
    "'0002'",

    # A00D - NUOVA AREA
    "'0001'",
    "'0001'",
    "'0002'",
    "'0002'"
]

NOME_STRUTTURA = [
    # A00B - BOVINI
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00B - CAPRE E PECORE
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00B - MAIALI
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00B - GALLINE
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00B - TACCHINI
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00B - CONIGLI
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00A
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00C
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",

    # A00D
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'",
    "'Struttura Zootecnica'"
]

CODICE_AREA = [
    # A00B - BOVINI
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00B - CAPRE E PECORE
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00B - MAIALI
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00B - GALLINE
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00B - TACCHINI
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00B - CONIGLI
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",
    "'A00B'",

    # A00A
    "'A00A'",
    "'A00A'",

    # A00C
    "'A00C'",
    "'A00C'",
    "'A00C'",
    "'A00C'",

    # A00D
    "'A00D'",
    "'A00D'",
    "'A00D'",
    "'A00D'"
]

ETICHETTA_ANIMALE = [
    # A00B - BOVINI
    "'0000000001'",
    "'0000000002'",
    "'0000000003'",
    "'0000000004'",

    # A00B - CAPRE E PECORE
    "'0000000005'",
    "'0000000006'",
    "'0000000007'",
    "'0000000008'",
    "'0000000009'",
    "'0000000010'",

    # A00B - MAIALI
    "'0000000011'",
    "'0000000012'",
    "'0000000013'",
    "'0000000014'",
    "'0000000015'",

    # A00B - GALLINE
    "'0000000016'",
    "'0000000017'",
    "'0000000018'",
    "'0000000019'",
    "'0000000020'",
    "'0000000021'",
    "'0000000022'",
    "'0000000023'",

    # A00B - TACCHINI
    "'0000000024'",
    "'0000000025'",
    "'0000000026'",
    "'0000000027'",

    # A00B - CONIGLI
    "'0000000028'",
    "'0000000029'",
    "'0000000030'",
    "'0000000031'",
    "'0000000032'",
    "'0000000033'",

    # A00A
    "'0000000034'",
    "'0000000035'",

    # A00C
    "'0000000036'",
    "'0000000037'",
    "'0000000038'",
    "'0000000039'",

    # A00D
    "'0000000040'",
    "'0000000041'",
    "'0000000042'",
    "'0000000043'"
]

DATA_ALLOCAZIONE = [
    # A00B - BOVINI
    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",

    # A00B - CAPRE E PECORE
    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",
    "DATE '2025-02-26'",
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",

    # A00B - MAIALI
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    # A00B - GALLINE
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",
    "DATE '2025-02-27'",

    # A00B - TACCHINI
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    # A00B - CONIGLI
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    # A00A
    "DATE '2025-02-24'",
    "DATE '2025-02-24'",

    # A00C
    "DATE '2025-02-26'",
    "DATE '2025-02-27'",
    "DATE '2025-02-28'",
    "DATE '2025-02-28'",

    # A00D
    "DATE '2025-05-04'",
    "DATE '2025-05-04'",
    "DATE '2025-05-05'",
    "DATE '2025-05-05'"
]

DATA_DEALLOCAIONE = [
    # A00B - BOVINI
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00B - CAPRE E PECORE
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00B - MAIALI
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00B - GALLINE
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00B - TACCHINI
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00B - CONIGLI
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",

    # A00A
    "NULL",
    "NULL",

    # A00C
    "DATE '2025-03-18'",
    "DATE '2025-03-18'",
    "DATE '2025-03-19'",
    "DATE '2025-03-19'",

    # A00D
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]


theList=list(zip(NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE))

keys = ["NUMERO_BLOCCO", "NOME_STRUTTURA", "CODICE_AREA", "ETICHETTA_ANIMALE", "DATA_ALLOCAZIONE", "DATA_DEALLOCAIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, ETICHETTA_ANIMALE, DATA_ALLOCAZIONE, DATA_DEALLOCAIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("ANIMALE_ALLOCATO_BLOCCO", theList[i])+"\n"

os.makedirs("make_DML/data/6_associazioni", exist_ok=True)
with open("make_DML/data/6_associazioni/9_animale_allocato_blocco.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/6_associazioni/9_animale_allocato_blocco.sql", lines)