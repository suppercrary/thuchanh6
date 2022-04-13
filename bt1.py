tentep=input("nhap ten tap tin cân sao luu: ")
tepmoi=tentep+".doc"

fo=open(tepmoi,"w")
for dong in tepmoi:
    fo.write(dong)
fo.close()