import os

def make_DML(path:str, lines:str,mode="w"):
    dir=path.split("/")[:-1]
    dir="/".join(dir)
    os.makedirs(dir, exist_ok=True)
    with open(path, mode) as f:
        f.write(lines)