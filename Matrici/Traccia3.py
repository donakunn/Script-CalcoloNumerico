# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:51:45 2021

@author: donal
"""
import numpy as np

def matriceDaConfrontare(x):
     #genera la matrice da confrontare
    mat = np.array([[x,x+2],[x-2,x**2]])
    return mat

def checksematriceContenuta(A,B):
    #controlla se B contenuto in A
    [m,n]= np.shape(A)
    [p,l] = np.shape(B)
    for i in range(0,m-p):
        for j in range(0,n-l):
            found = 0
            for k in range(0,p):
                for l in range(0,l):
                    if A[i+k][j+l] != B[k][l]:
                        found = 1
                        break
            if found == 0:
                return True
        if found == 0:
           return True
    return False
           
    
    
def estraiMatrice(A):
    [m,n] = np.shape(A)
    for i in range(0,m):
        for j in range(0,n):
            mat = matriceDaConfrontare(A[i][j])
            contenuto = checksematriceContenuta(A, mat)
            if contenuto == True:
                posizione = [i,j]
                valore = A[i][j]
                return posizione,valore
    return np.NaN
    
            