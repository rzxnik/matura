slowa=[]
ilosci=12*[0]
with open("slowa.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        linia=linia[0]
        slowa.append(linia)
for slowo in slowa:
    dl=len(slowo)
    ilosci[dl-1]+=1
print(ilosci)
with open("zadanie5a.txt","w") as plik:
    for i in range(12):
        plik.write(f"{(i+1)} - {ilosci[i]} \n")
     