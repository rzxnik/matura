slowa_stare=[]
slowa_nowe=[]
ilosci=[]
with open("slowa.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        linia=linia[0]
        slowa_stare.append(linia)
with open("nowe.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        linia=linia[0]
        slowa_nowe.append(linia)
#print(slowa_nowe)
for slowo in slowa_nowe:
    ile=0
    ile_odbite=0
    for slowo2 in slowa_stare:
        if slowo==slowo2:
            ile+=1
        if slowo[::-1]==slowo2:
            ile_odbite+=1
    ilosci.append([ile,ile_odbite])
with open("zadanie5c.txt","w") as plik:
     i=0
     for slowo in slowa_nowe:
         print(ilosci[i][0],ilosci[i][1])
         plik.write(f"{slowo}  {ilosci[i][0]}  {ilosci[i][1]}  \n")
         i+=1
