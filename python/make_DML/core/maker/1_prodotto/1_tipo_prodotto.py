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


#TIPO_PRODOTTO:NOME_PRODOTTO ALCOL FIBRE PROTEINE GRASSI CARBOIDRATI UNITA_MISURA IS_EDIBILE 


NOME_PRODOTTO = [
    "'Latte bovino'", "'Latte caprino'", "'Latte ovino'", "'Uova di gallina'", "'Uova di quaglia'",
    "'Carne bovina'", "'Carne suina'", "'Carne ovina'", "'Carne caprina'", "'Carne di pollo'",
    "'Carne di tacchino'", "'Carne di coniglio'", "'Miele'", "'Formaggio fresco'", "'Yogurt naturale'",
    "'Burro'", "'Panna'",

    "'Grano duro'", "'Farina di grano'", "'Mais'", "'Riso'", "'Patata'", "'Pomodoro'", "'Lattuga'",
    "'Spinacio'", "'Carota'", "'Zucchina'", "'Cetriolo'", "'Melanzana'", "'Peperone'",
    "'Fagiolo'", "'Ceci'", "'Lenticchie'", "'Piselli'", "'Soia'", "'Fragola'", "'Mela'", "'Pera'",
    "'Uva'", "'Erbe aromatiche miste'", "'Funghi coltivati'", "'Alghe alimentari'",

    "'Semi di grano duro'", "'Semi di mais'", "'Semi di riso'", "'Semi di pomodoro'", "'Semi di lattuga'",
    "'Semi di spinacio'", "'Semi di carota'", "'Semi di zucchina'", "'Semi di cetriolo'", "'Semi di peperone'",
    "'Semi di fagiolo'", "'Semi di ceci'", "'Semi di lenticchie'", "'Semi di soia'",
    "'Spore di funghi coltivati'", "'Talee di patata'",

    "'Soluzione nutritiva idroponica base'", "'Soluzione nutritiva concentrata'",
    "'Correttore pH acido'", "'Correttore pH basico'",
    "'Substrato in fibra di cocco'", "'Lana di roccia agricola'", "'Compost sterile'",
    "'Biofertilizzante microbico'",

    "'Fieno essiccato'", "'Paglia'", "'Mangime bovini crescita'", "'Mangime bovini lattazione'",
    "'Mangime ovicaprini'", "'Mangime suini'", "'Mangime pollame ovaiole'",
    "'Mangime pollame ingrasso'", "'Mangime conigli'", "'Sale minerale zootecnico'",

    "'Antibiotico veterinario bovini'", "'Antibiotico veterinario ovicaprini'",
    "'Antibiotico veterinario suini'", "'Antibiotico veterinario pollame'",
    "'Antiparassitario bovini'", "'Antiparassitario ovicaprini'",
    "'Antiparassitario suini'", "'Antiparassitario pollame'",
    "'Antinfiammatorio veterinario'", "'Disinfettante ferite animali'",
    "'Integratore vitaminico veterinario'", "'Reidratante orale veterinario'",
    "'Probiotico veterinario'", "'Pomata cicatrizzante veterinaria'",

    "'Vaccino bovini respiratorio'", "'Vaccino bovini clostridiosi'", "'Vaccino bovini mastite'",
    "'Vaccino ovicaprini clostridiosi'", "'Vaccino ovicaprini enterotossiemia'",
    "'Vaccino suini parvovirosi'", "'Vaccino suini mal rosso'",
    "'Vaccino pollame Newcastle'", "'Vaccino pollame bronchite infettiva'",
    "'Vaccino pollame coccidiosi'", "'Vaccino conigli mixomatosi'",
    "'Vaccino conigli malattia emorragica'",

    "'Lana ovina'", "'Pelle bovina'", "'Letame bovino'", "'Letame ovino'",
    "'Letame suino'", "'Pollina'", "'Piume di pollame'", "'Cera d api'"
]

FIBRE = [
    0,0,0,0,0,0,0,0,0,0,
    0,0,0.2,0,0,0,0,

    10.0,2.7,7.3,1.3,2.2,1.2,1.3,2.2,2.8,1.1,
    0.5,3.0,2.1,6.4,7.6,7.9,5.1,6.0,2.0,2.4,
    3.1,0.9,4.0,2.5,3.5,

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"
]

PROTEINE = [
    3.2,3.6,5.4,12.6,13.1,26.0,25.0,25.0,27.0,27.0,
    29.0,21.0,0.3,11.0,3.8,0.8,2.1,

    13.0,10.0,9.4,7.1,2.0,0.9,1.4,2.9,0.9,1.2,
    0.7,1.0,1.0,21.0,19.0,25.0,5.4,36.0,0.7,0.3,
    0.4,0.7,3.0,3.1,8.0,

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"
]

GRASSI = [
    3.6,4.1,6.0,10.6,11.1,15.0,20.0,17.0,10.0,14.0,
    7.0,8.0,0,20.0,3.3,81.0,35.0,

    2.5,1.0,4.7,0.7,0.1,0.2,0.2,0.4,0.2,0.3,
    0.1,0.2,0.3,1.2,6.0,1.1,0.4,20.0,0.3,0.2,
    0.1,0.2,1.0,0.3,1.5,

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"
]

CARBOIDRATI = [
    4.8,4.5,5.1,1.1,0.4,0,0,0,0,0,
    0,0,82.0,2.0,4.7,0.1,3.0,

    71.0,76.0,74.0,80.0,17.0,3.9,2.9,3.6,9.6,3.1,
    3.6,5.9,6.0,47.0,61.0,60.0,14.0,30.0,7.7,14.0,
    15.0,18.0,8.0,3.3,10.0,

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL","NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL",
    "NULL","NULL",

    "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"
]

UNITA_MISURA = [
    "'L'", "'L'", "'L'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",
    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",

    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",
    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",
    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",

    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",
    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",

    "'L'", "'L'", "'L'", "'L'", "'kg'", "'kg'", "'kg'", "'L'",

    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'",

    "'mL'", "'mL'", "'mL'", "'mg'", "'mL'", "'mL'", "'mL'", "'mg'",
    "'mL'", "'mL'", "'mg'", "'g'", "'g'", "'g'",

    "'mL'", "'mL'", "'mL'", "'mL'", "'mL'", "'mL'", "'mL'", "'mL'", "'mL'", "'mL'",
    "'mL'", "'mL'",

    "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'", "'kg'"
]

IS_EDIBILE = [
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,

    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,

    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,

    0,0,0,0,0,0,0,0,

    0,0,0,0,0,0,0,0,0,0,

    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,

    0,0,0,0,0,0,0,0,0,0,
    0,0,

    0,0,0,0,0,0,0,0
]

theList=list(zip(NOME_PRODOTTO, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE))

keys = ["NOME_PRODOTTO", "FIBRE", "PROTEINE", "GRASSI", "CARBOIDRATI", "UNITA_MISURA", "IS_EDIBILE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, FIBRE, PROTEINE, GRASSI, CARBOIDRATI, UNITA_MISURA, IS_EDIBILE\n"
for i in range(len(theList)):
  lines+=make_DML_line("TIPO_PRODOTTO", theList[i])+"\n"

os.makedirs("make_DML/data/1_prodotto", exist_ok=True)
with open("make_DML/data/1_prodotto/1_tipo_prodotto.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/1_prodotto/1_tipo_prodotto.sql", lines)