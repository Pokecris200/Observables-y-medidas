import numpy as np
import Libreria1 as lib

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
