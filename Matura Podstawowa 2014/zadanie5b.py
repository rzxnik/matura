def nwd(a,b):
    tmp=0
    while b!=0:
        tmp=b
        b=a%b
        a=tmp
    return a
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
    if nwd(a,b)==1:
        print(a,b)
        ile+=1
with open("zadanie5b.txt","w") as plik:
    plik.write(str(ile))