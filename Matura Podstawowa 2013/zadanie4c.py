def same(napis):
    zera=0
    jedynki=0
    for znak in napis:
        if znak=="0":
            zera+=1
        else:
            jedynki+=1
    if len(napis)==zera:
        return "0"
    elif len(napis)==jedynki:
        return "1"
    else: 
        return -1
napisy=[]
with open("napisy.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        napisy.append(linia[0])
zera=0
jedynki=0
for napis in napisy:
    if same(napis)=="0":
        zera+=1
    elif same(napis)=="1":
        jedynki+=1
    else:
        continue
with open("zadanie4c.txt","w") as plik:
    plik.write(str(f"same zera: {zera}, same jedynki: {jedynki}"))