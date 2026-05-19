X = 'X'
O = 'O'
Nista = " "
# prvi = input("Unesite X ili O : ")
valX = int(input("Unesite broj kolona: ")) 
valY = int(input("Unesite broj vrsta: "))
PvP = input("Unesite P za PlayerVsPlayer ili C za PlayerVsComputer: ")
if(PvP == 'C'):
    kompjuter = input("Unesite sta igra kompjuter: ")
else:
    kompjuter = X
tabla =[[Nista for i in range(valX)] for j in range(valY)]

# def print_repr(symbol):
#     return (f'{symbol}'
#     if symbol in [X, O]
#     else ' ')

def odigrajPotez(igr, stanje):
    potez = input("Unesite potez igraca "+igr+": ") 
    xKoordinata = potez[0]
    yKoordinata = potez[1]
    xKoordinata2 = abs(ord(xKoordinata)-48-valY)
    yKoordinata2 = ord(yKoordinata)-65
    return proveriPotez(xKoordinata2,yKoordinata2, igr, stanje)

def igraj(igr, odigraj, stanje):
    xKoordinata = odigraj[0]
    yKoordinata = odigraj[1]
    # xKoordinata2 = abs(ord(xKoordinata)-48-valY)
    # yKoordinata2 = ord(yKoordinata)-65
    return proveriPotez(xKoordinata,yKoordinata, igr, stanje)

def proveriPotez(x:int, y:int, igr, stanje)->bool:
    prom = False
    pomocnaLista = []
    pomocnaTabla =stanje.copy()
    if(igr==X):
        if(x>0 and x<valY and y>=0 and y<valX and stanje[int(x-1)][int(y)]==Nista and stanje[int(x)][int(y)]==Nista and stanje[int(x-1)][int(y)]!='O' and stanje[int(x)][int(y)]!='O'):
            prom = True
            pomocnaTabla[int(x)][int(y)] ='X'
            pomocnaTabla[int(x-1)][int(y)] ='X'
            pomocnaLista = ([[pomocnaTabla[m][n] for n in range(0, valX)] for m in range(0, valY)])
            #print_table(pomocnaTabla, localX, localY)
            pomocnaTabla[int(x)][int(y)] =Nista
            pomocnaTabla[int(x-1)][int(y)] =Nista
            return pomocnaLista
            #igrac = 'O'
    else:
        if(x>=0 and x<valY and y>=0 and y<valX-1 and stanje[int(x)][int(y)]==Nista and stanje[int(x)][int(y+1)]==Nista and stanje[int(x)][int(y)]!='X' and stanje[int(x)][int(y+1)]!='X'):
            prom = True
            pomocnaTabla[int(x)][int(y)] ='O'
            pomocnaTabla[int(x)][int(y+1)] ='O'
            pomocnaLista = ([[pomocnaTabla[m][n] for n in range(0, valX)] for m in range(0, valY)])
            #print_table(pomocnaTabla, localX, localY)
            pomocnaTabla[int(x)][int(y)] =Nista
            pomocnaTabla[int(x)][int(y+1)] =Nista
            return pomocnaLista
            #igrac = X

def proveriNesto(x:int, y:int, igr, stanje)->bool:
    prom = False
    if(igr==X):
        if(x>0 and x<valY and y>=0 and y<valX and stanje[int(x-1)][int(y)]==Nista and stanje[int(x)][int(y)]==Nista and stanje[int(x-1)][int(y)]!='O' and stanje[int(x)][int(y)]!='O'):
            prom = True
            #igrac = 'O'
    else:
        if(x>=0 and x<valY and y>=0 and y<valX-1 and stanje[int(x)][int(y)]==Nista and stanje[int(x)][int(y+1)]==Nista and stanje[int(x)][int(y)]!='X' and stanje[int(x)][int(y+1)]!='X'):
            prom = True
            #igrac = X
    # if prom==False:
    #     print("Nevalidan potez!") 
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

def nova_stanja(igrac,tabla: list[list], x:int, y:int, crtajPoteze:bool):
    imaPotez = 0
    localX = x
    localY = y
    if igrac == O:
        for i in range(localY):
            for j in range(localX):
                    if(not crtajPoteze):
                        if(proveriNesto(i,j,igrac, tabla)):
                            yield(i,j)
    else:
        for i in range(localY):
            for j in range(localX):
                    if(not crtajPoteze):
                        if(proveriNesto(i,j,igrac, tabla)):
                            yield(i,j)
    # [print_table(pomocnaLista[z] , valX, valY) for z in range(0, len(pomocnaLista))]
    # if imaPotez == 0:
    #     print("Kraj igre za "+igrac+"!")
    #     return None
    # else:
    #     print(imaPotez)
    #     return pomocnaLista
    
def procenaStanja(igrac,tabla: list[list], x:int, y:int, comp):
    imaPotez = 0
    maxPoteza = x*(x-1)+1
    localX = x
    localY = y
    if igrac == O:
        provera = -199
        for i in range(localY):
            for j in range(localX-1):
                if(tabla[i][j] == Nista and tabla[i][j+1] == Nista):
                    imaPotez+=1
                    if(provera < imaPotez):
                        provera = imaPotez
    else:
        provera = 199
        for i in range(localX-1):
            for j in range(localY):
                if(tabla[i][j] == Nista and tabla[i+1][j] == Nista):
                    imaPotez-=1
                    if(provera > imaPotez):
                        provera = imaPotez

    if imaPotez == 0:
        print("Kraj igre za "+igrac+"!")
        return provera
    else:
        #print(imaPotez)
        return maxPoteza-imaPotez

def minimax(stanje, dubina, moj_potez, potez=None):
    lista_poteza = list(nova_stanja(moj_potez, stanje, valX, valY, False))
    min_max_stanje = min_stanje if moj_potez=='X' else max_stanje
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        return(potez, procenaStanja(moj_potez, stanje, valX, valY, kompjuter))
    return min_max_stanje([minimax(igraj(moj_potez, x, stanje), dubina - 1, 'X' if moj_potez=='O' else 'O', x if potez is None else potez) for x in lista_poteza])

def max_stanje(lsv):
    return max(lsv, key=lambda x: x[1])

def min_stanje(lsv):
    return min(lsv, key=lambda x: x[1])

def max_value(stanje, dubina, moj_potez, alpha, beta, potez=None):
    lista_poteza = list(nova_stanja(moj_potez, stanje, valX, valY, False))
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        #print(potez, procenaStanja(moj_potez, stanje, valX, valY, kompjuter))
        return(potez, procenaStanja(moj_potez, stanje, valX, valY, kompjuter))
    else:
        for s in lista_poteza:
            alpha = max(alpha, min_value(igraj(moj_potez, s, stanje), dubina - 1, 'X' if moj_potez=='O' else 'O',
            alpha, beta, s if potez is None else potez), key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha

def min_value(stanje, dubina, moj_potez, alpha, beta, potez=None):
    lista_poteza = list(nova_stanja(moj_potez, stanje, valX, valY, False))
    if dubina == 0 or lista_poteza is None or len(lista_poteza) == 0:
        potez, procenaStanja(moj_potez, stanje, valX, valY, kompjuter)
        return(potez, procenaStanja(moj_potez, stanje, valX, valY, kompjuter))
    else:
        for s in lista_poteza:
            beta = min(beta, max_value(igraj(moj_potez, s, stanje), dubina - 1, 'X' if moj_potez=='O' else 'O',
            alpha, beta, s if potez is None else potez), key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta

def minimax_alpha_beta(stanje, dubina, moj_potez, alpha=(None, -999), beta=(None, +999)):
    if moj_potez == X:
        return max_value(stanje, dubina, moj_potez, alpha, beta)
    else:
        return min_value(stanje, dubina, moj_potez,  alpha, beta)


def igraPvC():
    zapocniIgru()
    igr = X

    tabla = [[Nista for i in range(valX)] for j in range(valY)]
    while(procenaStanja(igr, tabla, valX, valY, kompjuter)!=199 and procenaStanja(igr, tabla, valX, valY, kompjuter)!=-199):
        if(igr == kompjuter):
            min_max_result = minimax_alpha_beta(tabla, 3, igr)
            naj = min_max_result[0] if type(min_max_result[0]) is tuple else (0, 0) 
            print(naj)
            tabla = proveriPotez(naj[0], naj[1], igr, tabla)
            print_table(tabla, valX, valY)
            if(igr == X):
                igr= O
            else:
                igr = X
        else:
            promenljiva = odigrajPotez(igr, tabla)
            if(promenljiva == None):
                while(promenljiva == None):
                    promenljiva = odigrajPotez(igr, tabla)
            tabla = promenljiva
            print_table(tabla, valX, valY)
            if(igr == X):
                igr= O
            else:
                igr = X


def igraPvP():
    zapocniIgru()
    igr = X

    tabla = [[Nista for i in range(valX)] for j in range(valY)]
    while(procenaStanja(igr, tabla, valX, valY, kompjuter)!=199 and procenaStanja(igr, tabla, valX, valY, kompjuter)!=-199):
        if(igr == kompjuter):
            promenljiva = odigrajPotez(igr, tabla)
            if(promenljiva == None):
                while(promenljiva == None):
                    promenljiva = odigrajPotez(igr, tabla)
            tabla = promenljiva
            print_table(tabla, valX, valY)
            if(igr == X):
                igr= O
            else:
                igr = X
        else:
            promenljiva = odigrajPotez(igr, tabla)
            if(promenljiva == None):
                while(promenljiva == None):
                    promenljiva = odigrajPotez(igr, tabla)
            tabla = promenljiva
            print_table(tabla, valX, valY)
            if(igr == X):
                igr= O
            else:
                igr = X

if(PvP == 'C'):
    igraPvC()
else:
    igraPvP()
