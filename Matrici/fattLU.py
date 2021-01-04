# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:36:00 2021

@author: donal
"""
from numpy import *

def fattlu(A):
    """
    Fattorizzazione LU
    ---------------------------------------------
    INPUT
    A: matrice da fattorizzare
    ---------------------------------------------
    OUTPUT
    L: matrice triangolare inferiore speciale
    U: matrice triangolare superiore    
    """
    [m,n]=shape(A)
    if m!=n:
        print("matrice non quadrata")
    A=copy(A)# altrimenti sovrascriviamo la A nella shell
    tol=1e-15
    L=identity(n)
    for k in range(0,n-1):
        if abs(A[k,k])<tol:
            print("minore principale nullo")
            return
        for i in range(k+1,n):
            mik=-A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j]=A[i,j]+mik*A[k,j]
            L[i,k]=-mik
    U=triu(A) # estrae la parte triang. sup. di A
    return L,U 