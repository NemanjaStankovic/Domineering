X = 'X'
O = 'O'
Nista = " "
prvi = input("Unesite X ili O : ")
valX = int(input("Unesite broj kolona: ")) 
valY = int(input("Unesite broj vrsta: "))
tabla =[[Nista for i in range(valX)] for j in range(valY)]

# def print_repr(symbol):
#     return (f'{symbol}'
#     if symbol in [X, O]
#     else ' ')

def odigrajPotez(igr):
    potez = input("Unesite potez igraca "+igr+": ") 
    xKoordinata = potez[0]
    yKoordinata = potez[1]
    xKoordinata2 = abs(ord(xKoordinata)-48-valY)
    yKoordinata2 = ord(yKoordinata)-65
    return proveriPotez(xKoordinata2,yKoordinata2, igr)

def proveriPotez(x:int, y:int, igr)->bool:
    prom = False
    if(igr==X):
        if(x>0 and x<valY and y>=0 and y<valX and tabla[int(x-1)][int(y)]==Nista and tabla[int(x)][int(y)]==Nista):
            tabla[int(x)][int(y)]=igr
            tabla[int(x-1)][int(y)]=igr
            prom = True
            #igrac = 'O'
    else:
        if(x>=0 and x<valY and y>=0 and y<valX-1 and tabla[int(x)][int(y)]==Nista and tabla[int(x)][int(y+1)]==Nista):
            tabla[int(x)][int(y)]=igr
            tabla[int(x)][int(y+1)]=igr
            prom = True
            #igrac = X
    if prom==False:
        print("Nevalidan potez!") 
    print_table(tabla, int(valX), int(valY))
    return prom

def zapocniIgru():
    print_table(tabla, valX, valY)

def print_table(stanje: list[list], x: int, y: int):
    pom="  "
    pom2="  "
    for i in range(x):
        pom+=chr(65+i)+" "
        pom2+="= "

    print(pom)
    print(pom2)
    pom3=str(y)+"ǁ"
    z = y
    for w in stanje:
        for i in range(0,len(w)):
            if(i!=len(w)-1):
                pom3+=w[i]+"|"
            else:
                pom3+=w[i]+"ǁ"+str(z)
        print(pom3)
        z-=1
        pom3=str(z)+"ǁ"
    print(pom2)
    print(pom)

def proveriKraj(igrac,tabla: list[list], x:int, y:int):
    imaPotez = 0
    localX = x
    localY = y
    if igrac == O:
        for i in range(localY):
            for j in range(localX-1):
                if(tabla[i][j] == Nista and tabla[i][j+1] == Nista):
                    imaPotez+=1
    else:
        for i in range(localY-1):
            for j in range(localX):
                if(tabla[i][j] == Nista and tabla[i+1][j] == Nista):
                    imaPotez+=1
    if imaPotez == 0:
        print("Kraj igre za "+igrac+"!")
        return imaPotez
    else:
        print(imaPotez)
        return imaPotez

def igra():
    zapocniIgru()
    if(prvi=='X'):
        igr = X
    else:
        igr = O
    while(proveriKraj(igr, tabla, valX, valY)>0):
        if(odigrajPotez(igr)==True):
            if(igr == X):
                igr = O
            else:
                igr = X

igra()