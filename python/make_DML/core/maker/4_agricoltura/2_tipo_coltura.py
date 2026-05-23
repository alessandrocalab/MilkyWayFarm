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


#TIPO_COLTURA:NOME_TIPO_COLTURA CATEGORIA_COLTURA DURATA_CICLO_COLTURA_GIORNI 

NOME_TIPO_COLTURA = [
    "'Grano duro'",
    "'Mais'",
    
    "'Patata'",
    "'Pomodoro'",
    "'Lattuga'",
    "'Carota'",
    "'Zucchina'",
    "'Fagiolo'",
    "'Soia'"
]

CATEGORIA_COLTURA = [
    "'CERALI'",
    "'CERALI'",
    "'CERALI'",
    "'ORTAGGI'",
    "'ORTAGGI'",
    "'ORTAGGI'",
    "'ORTAGGI'",
    "'ORTAGGI'",
    "'LEGUMI'",
    "'OLEAGINOSE'"
]

DURATA_CICLO_COLTURA_GIORNI = [
    180,  # Grano duro
    120,  # Mais
    150,  # Riso
    100,  # Patata
    90,   # Pomodoro
    45,   # Lattuga
    80,   # Carota
    55,   # Zucchina
    90,   # Fagiolo
    120   # Soia
]


theList=list(zip(NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI))

keys = ["NOME_TIPO_COLTURA", "CATEGORIA_COLTURA", "DURATA_CICLO_COLTURA_GIORNI"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_TIPO_COLTURA, CATEGORIA_COLTURA, DURATA_CICLO_COLTURA_GIORNI\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_COLTURA", theList[i])+"\n"

os.makedirs("make_DML/data/4_agricoltura", exist_ok=True)
with open("make_DML/data/4_agricoltura/2_tipo_coltura.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/4_agricoltura/2_tipo_coltura.SQL", lines)