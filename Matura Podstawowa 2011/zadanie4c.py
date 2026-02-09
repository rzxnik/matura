# ord() i char()
hasla=[]
with open("hasla.txt","r") as plik:
    for linia in plik:
        linia=linia.strip()
        haslo=linia.split()
        hasla.append(str(haslo[0]))
wyniki=[]
for haslo in hasla:
    for i in range(1,len(haslo)):
        suma=ord(haslo[i-1])+ord(haslo[i])
        if suma==220:
            wyniki.append(haslo)
            print(haslo)
            break
with open("wynik4c.txt","w") as wynik:
    for haslo in wyniki:
        wynik.write(haslo+"\n")