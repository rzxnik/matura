hasla=[]
with open("hasla.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        haslo=linia.split()
        hasla.append(str(haslo[0]))
plik.close()
wynik=[]
for i in range(len(hasla)):
    if hasla[i]==hasla[i][::-1]:
        wynik.append(hasla[i])
        print(hasla[i])
with open("wynik4b.txt","w") as plik:
    for i in range(len(wynik)):
        plik.write(wynik[i]+"\n")