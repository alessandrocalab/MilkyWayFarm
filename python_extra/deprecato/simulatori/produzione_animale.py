import os
import sys
import datetime
import random

def setProjectRoot():
    PROJECT_ROOT = os.getcwd()

    while os.path.basename(PROJECT_ROOT) != "MilkyWayFarm":
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
from python.DB.action.getter.get_available_agri_seed_products import get_available_agri_seed_products
from python.DB.action.getter.get_available_mission_seeds import get_available_mission_seeds
from python.DB.action.getter.get_mod_colt_by_tipo_coltura import get_mod_colt_by_tipo_coltura
from python.DB.action.getter.get_tipo_coltura_by_seed import get_tipo_coltura_by_seed

from python.DB.action.update.end_cycle import end_cycle

from python.DB.action.insert.insert_agri_production import insert_agri_production
from python.DB.action.insert.insert_cycle_use_agri_production import insert_cycle_use_agri_production
from python.DB.action.insert.insert_cycle_use_mission_seed import insert_cycle_use_mission_seed
from python.DB.action.insert.insert_coltivation_cycle import insert_coltivation_cycle


def get_table_date_key(table_name):
    date_in_key={
        ANIMALE_TABLE_NAME: ANIMALE_DATE_IN_NAME,
        CELLA_IDROPONICA_TABLE_NAME: CELLA_IDROPONICA_IN_NAME
    }

    return date_in_key[table_name]

def get_table_exit_date_key(table_name):
    date_out_key={
        ANIMALE_TABLE_NAME: ANIMALE_DATE_OUT_NAME,
        CELLA_IDROPONICA_TABLE_NAME: CELLA_IDROPONICA_OUT_NAME
    }

    return date_out_key[table_name]

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

    date_key=get_table_date_key(table_name)
    exit_date_key=get_table_exit_date_key(table_name)

    for el in table_data:
        start_date = el[date_key]
        exit_date = el[exit_date_key]

        if start_date<=date and (exit_date is None or exit_date > date):
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

    

def startCicloColtivazione(cell, current_day):
    structure=cell[CELLA_IDROPONICA_STRUTTURA_NAME]
    cell_code=cell[CELLA_IDROPONICA_CODE_NAME]

    if(random.randint(1,3)==3):
        misison_seeds=get_available_mission_seeds()
        agri_prod_seeds=get_available_agri_seed_products()

        if(len(agri_prod_seeds)>0):
            i=random.randint(0,len(agri_prod_seeds)-1)

            while(len(agri_prod_seeds)>0 and agri_prod_seeds[i][AVAIBLE_SEED_NAME]<2):
                agri_prod_seeds.pop(i)

                if(len(agri_prod_seeds)>0):
                    i=random.randint(0,len(agri_prod_seeds)-1)
        
        if len(agri_prod_seeds)==0:

            if(len(misison_seeds)>0):
                i=random.randint(0,len(misison_seeds)-1)

                while(len(misison_seeds)>0 and misison_seeds[i][AVAIBLE_SEED_NAME]<2):
                    misison_seeds.pop(i)

                    if(len(misison_seeds)>0):
                        i=random.randint(0,len(misison_seeds)-1)

            if len(misison_seeds)!=0:
                to_plant=random.randint(
                    500,
                    int(min(float(misison_seeds[i][AVAIBLE_SEED_NAME])*1000,3000))
                )
                to_plant=float(to_plant)/1000
                colt_type_data=get_tipo_coltura_by_seed(misison_seeds[i][SEMI_MISSIONE_SEED_NAME])

                if len(colt_type_data)==0:
                    return

                colt_type=colt_type_data[0][TIPO_COLTURA_NAME]
                mod_colt_types=get_mod_colt_by_tipo_coltura(colt_type)

                if len(mod_colt_types)==0:
                    return

                insert_coltivation_cycle(
                    current_day,
                    cell_code,
                    structure,
                    None,
                    mod_colt_types[random.randint(0,len(mod_colt_types)-1)][MODALITA_COLTIVAZIONE_NAME],
                    colt_type
                )
                
                insert_cycle_use_mission_seed(
                    current_day,
                    cell_code,
                    structure,
                    misison_seeds[i][SEMI_MISSIONE_SEED_NAME],
                    misison_seeds[i][SEMI_MISSIONE_ARRIVE_DATE],
                    to_plant
                )
        
        else:
            to_plant=random.randint(
                500,
                int(min(float(agri_prod_seeds[i][AVAIBLE_SEED_NAME])*1000,3000))
            )
            to_plant=float(to_plant)/1000

            colt_type_data=get_tipo_coltura_by_seed(agri_prod_seeds[i][PRODUZIONE_AGRICOLA_PROD_NAME])

            if len(colt_type_data)==0:
                return

            colt_type=colt_type_data[0][TIPO_COLTURA_NAME]
            mod_colt_types=get_mod_colt_by_tipo_coltura(colt_type)

            if len(mod_colt_types)==0:
                return

            insert_coltivation_cycle(
                current_day,
                cell_code,
                structure,
                None,
                mod_colt_types[random.randint(0,len(mod_colt_types)-1)][MODALITA_COLTIVAZIONE_NAME],
                colt_type
            )
                
            insert_cycle_use_agri_production(
                current_day,
                cell_code,
                structure,
                agri_prod_seeds[i][PRODUZIONE_AGRICOLA_PRODUCTION_DATE],
                agri_prod_seeds[i][PRODUZIONE_AGRICOLA_CYCLE_DATE],
                agri_prod_seeds[i][PRODUZIONE_AGRICOLA_CELL_CODE],
                agri_prod_seeds[i][PRODUZIONE_AGRICOLA_STRUCT_AGR],
                agri_prod_seeds[i][PRODUZIONE_AGRICOLA_PROD_NAME],
                to_plant    
            )

        if len(misison_seeds)==0 and len(agri_prod_seeds)==0:
            print("No avaible seeds")
        else:
            print(f"started a new coltivation cyle in cell: {cell_code} {structure}")
        
            



def simulateCell(cell, current_day):
    structure=cell[CELLA_IDROPONICA_STRUTTURA_NAME]
    cell_code=cell[CELLA_IDROPONICA_CODE_NAME]

    is_working=is_cella_working(cell_code, structure)

    if not is_working:
        return startCicloColtivazione(cell,current_day)

    LCC_data=get_last_cycle(cell_code, structure)[0]
    LCC_start=LCC_data[CICLO_COLTIVAZIONE_START_DATE_NAME]
    LCC_span=get_colt_cycle_dur(LCC_start, cell_code, structure)[0][TIPO_COLTURA_CYCLE_SPAN]
    print(f"cell: {structure} {cell_code}: is now working from {(current_day-LCC_start).days}/{LCC_span}")

    days_from_start=(current_day-LCC_start).days
    if(endCycleProb(days_from_start, LCC_span)):

        is_fail=is_cycle_failed((current_day-LCC_start).days, LCC_span)
        planted_quantity=get_planted_seed_quantity(LCC_start, cell_code, structure)[0]["QUANTITA"]
        if(not is_fail):
            possible_products=get_possible_agri_products(LCC_data[CICLO_COLTIVAZIONE_COLT_TYPE_NAME])

            for prod in possible_products:
                producted=planted_quantity*prod[TIPO_COLTURA_TIPO_PRODOTTO_STIMA_NAME]*random.triangular(0.5,1.5,1.0) #minimo, massimo, valore più probabile

                insert_agri_production(current_day, LCC_start, cell_code, structure, prod[TIPO_COLTURA_TIPO_PRODOTTO_PROD_NAME], producted)

    
        end_cycle(LCC_start, cell_code, structure, current_day)

        print(f"cell: {structure} {cell_code}: has now ended the cycle")
    
    

    

TODAY=datetime.datetime.now()

animale_data=get_table_data(ANIMALE_TABLE_NAME)
cella_idroponica_data=get_table_data(CELLA_IDROPONICA_TABLE_NAME)
    
SIM_START_DAY=getSimStartDay(animale_data, cella_idroponica_data) #troviamo il minimo tra il giorno di arrivo del primo animale o la prima cella idroponica

current_day=SIM_START_DAY




while current_day<TODAY:
    avaible_cell=getAvaibleInDate(current_day, cella_idroponica_data, CELLA_IDROPONICA_TABLE_NAME)
    avaible_animals=getAvaibleInDate(current_day, animale_data, ANIMALE_TABLE_NAME)

    for cell in avaible_cell:
        simulateCell(cell, current_day)

    current_day=current_day+datetime.timedelta(days=1)