import os

def checkDir():
    dir=os.getcwd()
    while(os.path.basename(dir)!="MilkWayFarm"):
        os.chdir("..")
        dir=os.getcwd()