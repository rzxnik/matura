def sumacyfr(liczba):
    liczba=str(liczba)
    suma=0
    for cyfra in liczba:
        suma+=int(cyfra)
    return suma

liczby=[]
with open("cyfry.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        liczba=linia.split()
        liczby.append(int(liczba[0]))
min=liczby[0]
max=liczby[0]
for liczba in liczby:
    if sumacyfr(liczba)>sumacyfr(max):
        max=liczba
    elif sumacyfr(liczba)<sumacyfr(min):
        min=liczba
    else:
        continue
with open("zadanie4b.txt","w") as plik:
    plik.write(str((f"Najwieksza liczba jest {max} a Najmniejsza jest {min}")))
