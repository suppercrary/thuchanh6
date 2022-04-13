from typing import TextIO
def kdoc(reader: TextIO):
    doc=reader.readline()
    doc=reader.readline()
    while(doc.startswith("#")):
        doc=reader.readline()
    return doc
def xuly(reade):
    hoc= kdoc(reade).strip()
    if (hoc !=" "):
        nho=int(hoc)
        for hoc in reade:
            hoc=hoc.strip()
            if (hoc=="-"):
                continue
            value=int(hoc)
            nho=max(value,nho)
        return nho
if __name__=="__main__":
    with open("4.txt","r") as vao:
        print(xuly(vao))