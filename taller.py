import numpy as np
from Libreria1 import *

def proba(a,b):
    aux = ProductIntVec(b,a)
    res = (modulo(aux))**2
    return res
#4.3.1
def posibles(a, indice):
    s = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]
    result = []
    for i in range((indice*2)-2,indice*2):
        if proba(a,s[i])!= 0.0:
            result = result + s[i]
    return result
#4.3.2
def calculo(a, indice):
    matrices = [[[(1,0),(0,0)],[(0,0),(-1,0)]],[[(0,0),(0,-1)],[(0,1),(0,0)]],[[(0,0),(1,0)],[(1,0),(0,0)]]]
    vp = []
    aux = posibles(a, indice)
    probas = []
    res = 0
    for i in range(3):
        valores,no = np.linalg.eig(matrices[i])
        vp = vp + valores
    for i in range(len(aux)):
        probas = probas + proba(a, aux[i])
    for i in range(2):
        res = res + (proba[i]*vp[indice][i])
    return res
#4.4.1
def comprueba():
    s = (2**(1/2))/2
    U1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    U2 = [[(s,0),(s,0)],[(s,0),(-s,0)]]
    if Uni(U1) and Uni(U2):
        aux = multiMatrix(U1,U2)
        return Uni(aux)

#4.4.2
def billar():
    s = 1/ (2**(1/2))
    matriz =[[(0,0),(s,0),(s,0),(0,0)],
             [(0,s),(0,0),(0,0),(s,0)],
             [(s,0),(0,0),(0,0),(0,s)],
             [(0,0),(s,0),(-s,0),(0,0)]]
    vector = [(1,0),(0,0),(0,0),(0,0)]
    for i in range(3):
        vector = Accion(matriz,vector)
    proba = (modulo(vector[3]))**2
    return proba
