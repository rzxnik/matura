napisy=[]
ile=0
with open("napisy.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        napisy.append(linia[0])
for napis in napisy:
    zera=0
    jedynki=0
    for cyfra in napis:
        if cyfra=="0":
            zera+=1
        else:
            jedynki+=1
    if zera==jedynki:
        ile+=1
with open("zadanie4b.txt","w") as plik:
    plik.write(str(ile))