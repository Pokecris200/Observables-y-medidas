import math

def Suma (a, b):
    return (a[0]+b[0], a[1]+ b[1])

def prettyPrinting(a):
    if a[1]>=0 :
        print(a[0],"+",a[1],"i")
    else :
        print(a[0],a[1],"i")
        
def resta(a, b):
    return (a[0]-b[0], a[1]-b[1])

def multiplicacion (a, b):
    First = (a[0]*b[0])-(a[1]*b[1])
    Second = (a[0]*b[1])+(a[1]*b[0])
    return(First, Second)

def div (a,b):
    num1 = (a[0]*b[0])+(a[1]*b[1])
    den = (b[0]**2)+(b[1]**2)
    num2 =(b[0]*a[1])-(a[0]*b[1]) 
    return ((num1/den), (num2/den))

def conj (a):
    Conjugado = (a[1] * (-1))
    return (a[0], Conjugado)

def modulo (a):
    rad = (a[0]**2) + (a[1]**2)
    mod = math.sqrt (rad)
    mod = round (mod, 2)
    return mod

def Polar (a):
    f = (a[0]**2) + (a[1]**2)
    rho = math.sqrt (f)
    d = a[1] / a[0]
    Theta = math.atan (d)
    Theta = round (Theta,2)
    rho = round (rho ,2)
    return (rho, Theta)

def Fase (a):
    c = Polar (a)
    return c[1]

def sumaVect(a,b):
    matriz = []
    i = 0
    for i in range(len(a)):
        matriz = matriz + [Suma (a[i],b[i])]
    return matriz

def inversaVect(a):
    matriz = []
    i = 0
    s = (-1,0)
    for i in range(len(a)):
        matriz = matriz + [multiplicacion (a[i], s)]
    return matriz

def productoEscalarV(a, b):
    matriz = []
    i = 0
    for i in range(len(a)):
        matriz = matriz + [multiplicacion (a[i], b)]
    return matriz

def sumaMatrix (a, b):
    i = 0
    j = 0
    n,m = len(a),len(a[0])
    N,M = len(b),len(b[0])
    
    if n == N and m == M:
        c = [[0 for j in range (m) ]for i in range (n)]
        for i in range (n):
            for j in range (m):
                c[i][j] = Suma (a[i][j], b[i][j])
    return c

def inversaMatrix(a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = multiplicacion (a[i][j], (-1,0))
    return c

def multiEscalarMatrix (a, b):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = multiplicacion (a[i][j], b)
    return c

def matrixTrans (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = a [j][i]
    return c

def matrixConj (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = conj (a[i][j])
    return c

def matrixAdj (a):
    c = matrixTrans (matrixConj (a))
    return c

def multiMatrix (a, b):
    n,m = len(a),len(a[0])
    N,M = len(b), len(b[0])
    c = [[(0,0) for j in range (m) ]for i in range (n)]
    if m == N :
        for i in range (n):
            for j in range (M):
                for k in range (N):
                    p = multiplicacion (a[i][k], b[k][j])
                    q = c [i][j]
                    c[i][j] = Suma (p, q)

    return c

def Accion (a, b):
    n,m = len(a),len(a[0])
    B = len (b)
    c = []
    if B == m:
        S = (0,0)
        for i in range (n):
            for j in range (m):
                p = multiplicacion (a[i][j], b[j])
                S = Suma (S, p)
            c = c + [S]
            S = (0,0) 
    return c

def ProductIntVec (a, b):
    c = (0,0)
    for i in range (len(a)):
        n = multiplicacion(conj(a[i]), b[i])
        c = Suma (c, n)     
    return c

def norma (a):
    e = ProductIntVec(a, a)
    c = (e[0])**(1/2)
    c = round(c, 2)
    return c

def distancia (a, b):
    f = inversaVect (b)
    d = sumaVect(a,f)
    c = ProductIntVec(d,d)
    Res = (c[0]) ** (1/2)
    Res = round (Res, 2)
    return Res
def ID (m, n):
    c = [[(0,0) for j in range (m) ]for i in range (n)]
    for i in range (n):
        for j in range (m):
            if i == j:
                c[i][j]= ((2/2),0)
    return c
    
def Uni (a):
    p = multiMatrix(matrixAdj(a), a)
    i = ID(len(a),len(a[0]))
    if p == i :
        return True
    else:
        return False

def Herm (a):
    c = matrixAdj (a)
    if a == c:
        return True
    else:
        return False

def Tensor (a, b):
    r = []
    m = 0
    n = 0
    while (m < ((len(a)-1)*2)):
        f1 = a[m]
        f2 = b[n]
        aux = []
        for i in f1:
            for j in f2:
                aux = aux + [multiplicacion (i, j)]
        m = m + 1
        f2 = b[n]
        r = r + [aux]
        aux = []
        for i in f1:
            for j in f2:
                aux = aux + [multiplicacion (i, j)]
        m = m + 1
        n = n - 1
        r = r + [aux]
    return r

