dane = open ("dane.txt","r")
palindromy=[]
for linia in dane:
    linia=linia.strip()
    slowo=linia.split()
    wyraz=slowo[0]
    if wyraz==wyraz[::-1]:
        print(wyraz)
        palindromy.append(wyraz)
dane.close()
wynik= open("zadanie4.txt","w")
for palindrom in palindromy:
    wynik.write(palindrom + "\n")
