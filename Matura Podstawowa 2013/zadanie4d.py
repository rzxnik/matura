napisy=[]
wyniki=16*[0]
with open("napisy.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        napisy.append(linia[0])
for napis in napisy:
    dl=len(napis)-1
    wyniki[dl]+=1
print(wyniki)
with open("zadanie4d.txt","w") as plik:
    for i in range(1,len(wyniki)):
        plik.write(f"k={(i+1)} - {wyniki[i]} \n")