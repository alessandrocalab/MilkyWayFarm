import os
import sys
import datetime
import random

def setProjectRoot():
    PROJECT_ROOT = os.getcwd()

    while os.path.basename(PROJECT_ROOT) != "MilkWayFarm":
        parent = os.path.dirname(PROJECT_ROOT)

        if parent == PROJECT_ROOT:
            raise RuntimeError("Cartella MilkWayFarm non trovata risalendo dal path corrente")

        os.chdir("..")
        PROJECT_ROOT = os.getcwd()

    sys.path.append(PROJECT_ROOT)

setProjectRoot() #verifichiamo che il programma sia nella directory principale del progetto

from python.simulatori.config import *
from python.DB.action.getter.get_table_tuples import get_table_data
from python.DB.action.getter.is_cella_working import is_cella_working
from python.DB.action.getter.get_last_cycle import get_last_cycle
from python.DB.action.getter.get_colt_cycle_dur import get_colt_cycle_dur
from python.DB.action.getter.get_planted_seed_quantity import get_planted_seed_quantity
from python.DB.action.getter.get_possible_agri_products import get_possible_agri_products

from python.DB.action.update.end_cycle import end_cycle

def get_table_date_key(table_name):
    date_in_key={
        ANIMALE_TABLE_NAME: ANIMALE_DATE_IN_NAME,
        CELLA_IDROPONICA_TABLE_NAME: CELLA_IDROPONICA_IN_NAME
    }

    return date_in_key[table_name]

def getFirstTableIn(table_data, table_name):
    date_min=None

    for el in table_data:
        if date_min is None or el[get_table_date_key(table_name)]<date_min:
            date_min=el[get_table_date_key(table_name)]
    return date_min

def getSimStartDay(animale_data, cella_idroponica_data):
    return min(getFirstTableIn(animale_data, ANIMALE_TABLE_NAME), getFirstTableIn(cella_idroponica_data, CELLA_IDROPONICA_TABLE_NAME))


def getAvaibleInDate(date, table_data, table_name):
    avaible=[]
    for el in table_data:
        if el[get_table_date_key(table_name)] <= date:
            avaible.append(el)
    return avaible

def endCycleProb(start, end):
    maxD = max(start, end)
    n=random.randint(min(start, end), maxD)

    if(n==maxD):
        return True
    
    if(maxD!=end):
        n=random.randint(1, 10)
        if (n==10):
            return True
    
    return False

def is_cycle_failed(time, prev): #se il ciclo termina prima del 80% del tempo previsto viene interpretato come fallito (piante appassite)
    limit=prev*0.8
    return bool(time<limit)

    

def startCicloColtivazione(cell):
    return



def simulateCell(cell, current_day):
    structure=cell[CELLA_IDROPONICA_STRUTTURA_NAME]
    cell_code=cell[CELLA_IDROPONICA_CODE_NAME]

    is_working=is_cella_working(structure, cell_code)

    if not is_working:
        return startCicloColtivazione(cell)

    LCC_data=get_last_cycle(structure, cell_code)[0]
    LCC_start=LCC_data[CICLO_COLTIVAZIONE_START_DATE_NAME]
    LCC_span=get_colt_cycle_dur(LCC_start, cell_code, structure)
    print(f"cell: {structure} {cell_code}: is now working from {LCC_start}/{LCC_span}")

    if(endCycleProb(LCC_start, LCC_span)):
        producted=[]

        is_fail=is_cycle_failed((current_day-LCC_start).days, LCC_span)
        if(not is_fail):
            possible_products=get_possible_agri_products(LCC_data[CICLO_COLTIVAZIONE_COLT_TYPE_NAME])
    
        end_cycle(LCC_start, cell_code, structure, current_day)


    
    

    

TODAY=datetime.datetime.now()

animale_data=get_table_data(ANIMALE_TABLE_NAME)
cella_idroponica_data=get_table_data(CELLA_IDROPONICA_TABLE_NAME)
    
SIM_START_DAY=getSimStartDay(animale_data, cella_idroponica_data) #troviamo il minimo tra il giorno di arrivo del primo animale o la prima cella idroponica

current_day=SIM_START_DAY





avaible_cell=getAvaibleInDate(current_day, cella_idroponica_data, CELLA_IDROPONICA_TABLE_NAME)
avaible_animals=getAvaibleInDate(current_day, animale_data, ANIMALE_TABLE_NAME)

for cell in avaible_cell:
    simulateCell(cell, current_day)