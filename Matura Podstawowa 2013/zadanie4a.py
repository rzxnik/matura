napisy=[]
parzyste=0
with open("napisy.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        napisy.append(linia[0])
for napis in napisy:
    if len(napis)%2==0:
        parzyste+=1
with open("zadanie4a.txt","w") as plik:
    plik.write(str(parzyste))