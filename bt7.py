from typing import  TextIO
from  io import StringIO
def read( reader: TextIO)->list:
    line = reader.readline()
    if not line:
        return None

    if not (line.startswith("cmnt") or line.isspace()):
        key,name=line.split()
        mole=[name]
    else:
        mole=None

    reading=True
    while reading:
        line=reader.readline()
        if line.startswith("End"):
            reading= False
        elif not(line.startswith("cmnt") or line.isspace()):
            key, num, atm ,x,y,z= line.split()
            if mole== None:
                mole=[]
            mole.append([atm,x,y,z])
    return mole
def readall(reader: TextIO)->list:
    result=[]
    reading=True
    while reading:
        mole= read(reader)
        if mole:
            result.append(mole)
        else:
            reading=False
    return result

if __name__=="__main__":
    file= open("5.txt","r")
    moles=readall(file)
    file.close()
    print(moles)

