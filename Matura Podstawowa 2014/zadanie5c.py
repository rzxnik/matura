def sumacyfr(a,b):
    suma_a=0
    suma_b=0
    while a!=0:
        suma_a+=a%10
        a=a//10
    while b!=0:
        suma_b+=b%10
        b=b//10
    if suma_a==suma_b:
        return True
    return False
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
    if sumacyfr(a,b)==True:
        ile+=1
        print(a,b)
with open("zadanie5c.txt","w") as plik:
    plik.write(str(ile))