from  typing import TextIO
def kdocthang(readr: TextIO):
    doc=readr.readline()
    doc = readr.readline()
    while (doc.startswith("#")):
        doc=readr.readline()
    return doc

def pro(readr):
    doc=kdocthang(readr).strip()
    print(doc)
    print(readr.read())
if __name__=="__main__":
    with open("3.txt","r") as vao:
        pro(vao)
