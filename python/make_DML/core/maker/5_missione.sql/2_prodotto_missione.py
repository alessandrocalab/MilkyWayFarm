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


#PRODOTTO_MISSIONE:NOME_PRODOTTO NOME_MISSIONE QUANTITA DATA_PRODUZIONE 

NOME_PRODOTTO = [
    # Ares Supply 01
    "'Acqua potabile'",
    "'Soluzione nutritiva idroponica base'",
    "'Semi di grano duro'",
    "'Semi di mais'",

    # Ares Supply 02
    "'Acqua potabile'",
    "'Mangime bovini crescita'",
    "'Mangime pollame ovaiole'",
    "'Antiparassitario bovini'",

    # Demetra Cargo 01
    "'Substrato in fibra di cocco'",
    "'Lana di roccia agricola'",
    "'Biofertilizzante microbico'",

    # Demetra Cargo 02
    "'Acqua potabile'",
    "'Semi di pomodoro'",
    "'Semi di lattuga'",
    "'Soluzione nutritiva concentrata'",

    # Hermes BioLab 01
    "'Vaccino bovini respiratorio'",
    "'Vaccino pollame Newcastle'",
    "'Antibiotico veterinario pollame'",

    # Hermes BioLab 02
    "'Mangime ovicaprini'",
    "'Mangime suini'",
    "'Reidratante orale veterinario'",

    # Atlas Storage 01
    "'Acqua potabile'",
    "'Compost sterile'",
    "'Fieno essiccato'",
    "'Paglia'",

    # Atlas Storage 02
    "'Acqua potabile'",
    "'Semi di carota'",
    "'Semi di zucchina'",
    "'Correttore pH acido'",
    "'Correttore pH basico'"
]
NOME_MISSIONE = [
    # Ares Supply 01
    "'Ares Supply 01'",
    "'Ares Supply 01'",
    "'Ares Supply 01'",
    "'Ares Supply 01'",

    # Ares Supply 02
    "'Ares Supply 02'",
    "'Ares Supply 02'",
    "'Ares Supply 02'",
    "'Ares Supply 02'",

    # Demetra Cargo 01
    "'Demetra Cargo 01'",
    "'Demetra Cargo 01'",
    "'Demetra Cargo 01'",

    # Demetra Cargo 02
    "'Demetra Cargo 02'",
    "'Demetra Cargo 02'",
    "'Demetra Cargo 02'",
    "'Demetra Cargo 02'",

    # Hermes BioLab 01
    "'Hermes BioLab 01'",
    "'Hermes BioLab 01'",
    "'Hermes BioLab 01'",

    # Hermes BioLab 02
    "'Hermes BioLab 02'",
    "'Hermes BioLab 02'",
    "'Hermes BioLab 02'",

    # Atlas Storage 01
    "'Atlas Storage 01'",
    "'Atlas Storage 01'",
    "'Atlas Storage 01'",
    "'Atlas Storage 01'",

    # Atlas Storage 02
    "'Atlas Storage 02'",
    "'Atlas Storage 02'",
    "'Atlas Storage 02'",
    "'Atlas Storage 02'",
    "'Atlas Storage 02'"
]
QUANTITA = [
    # Ares Supply 01
    1200.00,  # L acqua
    500.00,   # L soluzione nutritiva base
    40.00,    # kg semi grano duro
    35.00,    # kg semi mais

    # Ares Supply 02
    1500.00,  # L acqua
    750.00,   # kg mangime bovini crescita
    300.00,   # kg mangime pollame ovaiole
    65.00,    # mL antiparassitario bovini

    # Demetra Cargo 01
    350.00,   # kg substrato fibra cocco
    250.00,   # kg lana di roccia
    180.00,   # L biofertilizzante

    # Demetra Cargo 02
    1000.00,  # L acqua
    8.00,     # kg semi pomodoro
    5.00,     # kg semi lattuga
    350.00,   # L soluzione concentrata

    # Hermes BioLab 01
    180.00,   # mL vaccino bovini respiratorio
    90.00,    # mL vaccino pollame Newcastle
    250.00,   # mg antibiotico pollame

    # Hermes BioLab 02
    500.00,   # kg mangime ovicaprini
    600.00,   # kg mangime suini
    80.00,    # g reidratante orale

    # Atlas Storage 01
    1800.00,  # L acqua
    600.00,   # kg compost sterile
    900.00,   # kg fieno essiccato
    700.00,   # kg paglia

    # Atlas Storage 02
    1500.00,  # L acqua
    6.00,     # kg semi carota
    5.00,     # kg semi zucchina
    120.00,   # L correttore pH acido
    100.00    # L correttore pH basico
]
DATA_PRODUZIONE = [
    # Ares Supply 01
    "DATE '2023-05-25'",
    "DATE '2023-05-20'",
    "DATE '2023-05-10'",
    "DATE '2023-05-12'",

    # Ares Supply 02
    "DATE '2023-08-12'",
    "DATE '2023-08-05'",
    "DATE '2023-08-07'",
    "DATE '2023-08-10'",

    # Demetra Cargo 01
    "DATE '2023-12-20'",
    "DATE '2023-12-18'",
    "DATE '2024-01-02'",

    # Demetra Cargo 02
    "DATE '2024-06-28'",
    "DATE '2024-06-15'",
    "DATE '2024-06-17'",
    "DATE '2024-06-25'",

    # Hermes BioLab 01
    "DATE '2025-01-28'",
    "DATE '2025-01-30'",
    "DATE '2025-02-01'",

    # Hermes BioLab 02
    "DATE '2025-09-01'",
    "DATE '2025-09-02'",
    "DATE '2025-09-05'",

    # Atlas Storage 01
    "DATE '2025-12-27'",
    "DATE '2025-12-20'",
    "DATE '2025-12-22'",
    "DATE '2025-12-23'",

    # Atlas Storage 02
    "DATE '2026-03-08'",
    "DATE '2026-03-01'",
    "DATE '2026-03-03'",
    "DATE '2026-03-05'",
    "DATE '2026-03-05'"
]
theList=list(zip(NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE))

keys = ["NOME_PRODOTTO", "NOME_MISSIONE", "QUANTITA", "DATA_PRODUZIONE"]

theJsonList=[dict(zip(keys, row)) for row in theList]

lines="--NOME_PRODOTTO, NOME_MISSIONE, QUANTITA, DATA_PRODUZIONE\n"
for i in range(len(theList)):
  lines+=make_DML_line("PRODOTTO_MISSIONE", theList[i])+"\n"

os.makedirs("make_DML/data/5_missione.sql", exist_ok=True)
with open("make_DML/data/5_missione.sql/2_prodotto_missione.json", "w", encoding="utf-8") as f:
   json.dump(theJsonList, f, indent=4, ensure_ascii=False)

make_DML("DB/DML/5_missione.sql/2_prodotto_missione.sql", lines)