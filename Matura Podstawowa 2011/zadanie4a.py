hasla=[]
with open("hasla.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        haslo=linia.split()
        hasla.append(str(haslo[0]))
plik.close()
nieparzyste=0
parzyste=0
for i in range(len(hasla)):
    if len(hasla[i])%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
with open("wynik4a.txt","w") as wynik:
    txt="Parzyste: " + str(parzyste) + " Nieparzyste: " + str(nieparzyste)
    wynik.write(txt)