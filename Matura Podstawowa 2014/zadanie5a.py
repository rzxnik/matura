liczby=[]
ile=0
with open("PARY_LICZB.TXT","r") as plik:
    for linia in plik:
        linia=linia.strip()
        linia=linia.split()
        linia[0],linia[1]=int(linia[0]),int(linia[1])
        liczby.append(linia)
for para in liczby:
    a=para[0]
    b=para[1]
    if b%a==0 or a%b==0:
        ile+=1
with open("zadanie5a.txt","w") as plik:
    plik.write(str(ile))