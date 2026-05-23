#inserire il path DDL e creerà un file python per costruire il corrispettivo DML

import os
from python.make_DML.core.utils.get_table_data import getTableData

import sys

dir = os.getcwd()
while os.path.basename(dir) != "MilkWayFarm":
    os.chdir("..")
    dir = os.getcwd()

sys.path.append(dir)

MAKER_BASE_PATH="make_DML/core/maker/"
DATA_PATH="make_DML/data"
DML_PATH="DB/DML"


def makePyMaker(path:str):
    data=getTableData(path)
    table_name=data[0]
    attr_list=data[1]

    tmp=path.split("/")
    path_json:str=""
    path_json+="/".join(tmp[-2:])
    path_json=path_json[:-3] #rimozione sql
    path_json+="json"

    path_DML:str=DML_PATH+"/"
    path_DML+="/".join(tmp[-2:])

    maker_text = (
        "import os\n"
        "import sys\n"
        "import json\n"
        "\n"
        "dir = os.getcwd()\n"
        "while os.path.basename(dir) != \"MilkWayFarm\":\n"
        "    os.chdir(\"..\")\n"
        "    dir = os.getcwd()\n"
        "\n"
        "sys.path.append(dir)\n"
        "\n"
        "from make_DML.core.utils.make_DML_line import make_DML_line\n"
        "from make_DML.core.utils.make_DML import make_DML\n\n\n"
    )

    maker_text+=f"#{table_name}:"
    for el in attr_list:
        maker_text+=f"{el} "
    
    maker_text+="\n\n"

    for el in attr_list:
        maker_text+=f"{el} = []\n\n"
    
    maker_text+="\ntheList=list(zip("

    for el in attr_list:
        maker_text+=f"{el}, "
    
    maker_text=maker_text[:-2]#rimozione , 

    maker_text += "))\n\n"

    maker_text += "keys = ["

    for el in attr_list:
        maker_text+= f"\"{el}\", "
        
    maker_text=maker_text[:-2]

    maker_text+="]\n\n"

    maker_text+="theJsonList=[dict(zip(keys, row)) for row in theList]\n\n"

    maker_text+="lines=\"--"

    for el in attr_list:
        maker_text+=f"{el}, "

    maker_text=maker_text[:-2]

    maker_text+=(
        "\\n\"\nfor i in range(len(theList)):\n"
        f"  lines+=make_DML_line(\"{table_name}\", theList[i])+\"\\n\"\n\n"
        f"os.makedirs(\"{DATA_PATH}/{path_json.split("/")[0]}\", exist_ok=True)\n"
        f"with open(\"{DATA_PATH}/{path_json}\", \"w\", encoding=\"utf-8\") as f:\n"
        "   json.dump(theJsonList, f, indent=4, ensure_ascii=False)\n\n"
        f"make_DML(\"{path_DML}\", lines)"

    )

    #path makerPy
    path_py:str=""
    path_py+="/".join(tmp[-2:])
    path_py=path_py[:-3] #rimozione sql
    path_py+="py"
    path_py=MAKER_BASE_PATH+path_py

    with open(path_py, "w") as f:
        f.write(maker_text)


if __name__=="__main__":
   
    DDL_PATH="./DB/DDL/"

    DDL_dirs=os.listdir(DDL_PATH)
    DDL_dirs.remove('main.sql')
    DDL_dirs=sorted(DDL_dirs, key=lambda x: int(x.split("_")[0])) #ordinamento rispetto i numeri prima del primo trattino

    for dir in DDL_dirs:
        sql_files=os.listdir(DDL_PATH+dir)
        sql_files=sorted(sql_files, key=lambda x: int(x.split("_")[0]))
        os.makedirs(MAKER_BASE_PATH+dir, exist_ok=True)
        for sql in sql_files:
            makePyMaker(DDL_PATH+dir+"/"+sql)
        

