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


#SOSTANZA:NOME_SOSTANZA IS_POTENZIALE_ALLERGENE IS_POTENZIALE_INTOLLERANTE 

NOME_SOSTANZA = [
    "'Lattosio'",
    "'Caseina'",
    "'Proteine del siero del latte'",
    "'Albumina sierica bovina'",

    "'Proteine dell uovo'",
    "'Ovoalbumina'",
    "'Ovomucoide'",

    "'Glutine'",
    "'Gliadina'",
    "'Glutenina'",
    "'Fruttani'",

    "'Proteine del mais'",

    "'Proteine della soia'",
    "'Lecitina di soia'",
    "'Proteine dei legumi'",
    "'Vicilina'",
    "'Convicilina'",
    "'Lectine vegetali'",
    "'Galatto oligosaccaridi'",
    "'Raffinosio'",
    "'Stachiosio'",

    "'Fruttosio'",
    "'Salicilati naturali'",
    "'Ossalati'",
    "'Solanina'",
    "'Capsaicina'",
    "'Istamina'",
    "'Nichel alimentare'",
    "'Glucosinolati'",
    "'Inulina'",
    "'Purine'",

    "'Proteine fungine'",
    "'Chitina fungina'",

    "'Ficocianina algale'",
    "'Iodio algale'",

    "'Alfa gal'",
    "'Proteine della carne bovina'",
    "'Proteine della carne suina'",
    "'Proteine della carne ovina'",
    "'Proteine della carne caprina'",
    "'Proteine della carne avicola'",
    "'Proteine della carne di coniglio'"
]

IS_POTENZIALE_ALLERGENE = [
    0, 1, 1, 1,

    1, 1, 1,

    1, 1, 1, 0,

    1,

    1, 1, 1, 1, 1, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

    1, 1,

    1, 0,

    1, 1, 1, 1, 1, 1, 1
]

IS_POTENZIALE_INTOLLERANTE = [
    1, 0, 0, 0,

    0, 0, 0,

    1, 1, 1, 1,

    0,

    0, 0, 0, 0, 0, 1, 1, 1, 1,

    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

    0, 1,

    0, 1,

    0, 0, 0, 0, 0, 0, 0
]

if len(NOME_SOSTANZA) == len(IS_POTENZIALE_ALLERGENE) ==  len(IS_POTENZIALE_INTOLLERANTE):


  theList=list(zip(NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE))

  keys = ["NOME_SOSTANZA", "IS_POTENZIALE_ALLERGENE", "IS_POTENZIALE_INTOLLERANTE"]

  theJsonList=[dict(zip(keys, row)) for row in theList]

  lines="--NOME_SOSTANZA, IS_POTENZIALE_ALLERGENE, IS_POTENZIALE_INTOLLERANTE\n"
  for i in range(len(theList)):
    lines+=make_DML_line("SOSTANZA", theList[i])+"\n"

  os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
  with open("make_DML/data/1_prodotto/2_sostanza.json", "w", encoding="utf-8") as f:
    json.dump(theJsonList, f, indent=4, ensure_ascii=False)

  make_DML("DB/DML/1_prodotto/2_sostanza.sql", lines)