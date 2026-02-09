liczby=[]
with open("cyfry.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        liczba=linia.split()
        liczby.append(int(liczba[0]))
parzyste=0
for liczba in liczby:
    if liczba%2==0:
        parzyste+=1
    else:
        continue
with open("zadanie4a.txt","w") as plik:
    plik.write(str(parzyste))