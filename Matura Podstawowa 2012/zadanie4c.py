def ciagrosnacy(liczba):
    liczba=str(liczba)
    for i in range(0,len(liczba)-1):
        cyfra1=int(liczba[i])
        cyfra2=int(liczba[i+1])
        if cyfra2>cyfra1:
            continue
        else:
            return False
    return True
liczby=[]
wynik=[]
with open("cyfry.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        liczba=linia.split()
        liczby.append(int(liczba[0]))
for liczba in liczby:
    if ciagrosnacy(liczba)==True:
        wynik.append(liczba)
with open("zadanie4c.txt","w") as plik:
    plik.write(str(wynik))