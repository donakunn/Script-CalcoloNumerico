#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:33:50 2021

@author: kun
"""

# -*- coding: utf-8 -*-
"""

"""

import numpy as np


"""
data una matrice A, scambia la riga1 con la riga2
"""
def scambio_righe (A, riga1, riga2):
    [n_righe,n_colonne]=np.shape(A)
    B = np.copy(A)
    
    for j in range (0,n_colonne):
        B[riga1][j]=A[riga2][j]
        B[riga2][j]=A[riga1][j]
    return B

"""
codice massimo pivot - eventualmente effetto lo scambio delle righe
"""
def massimoPivot(Uk,Pk,k,h):#matrice U, matrice P, colonna, riga
            #inizializzazione
            [n_righe,n_colonne]=np.shape(Uk)
            U=np.copy(Uk)
            P=np.copy(Pk)
            spostamento_colonna =0
            #ricerca pivot con valore assoluto massimo
            s=h
            pivot = np.abs(U[h][k])
            for i in range (h+1,n_righe):
                if np.abs(U[i][k])>pivot:
                    s=i
                    pivot=np.abs(U[i][k])
            #se il pivot = 0 significa che gli elementi akk e i sottostanti sono = 0
            #pertanto bisogna spostarsi sulla colonna successiva della stessa riga 
            #ed effettuare nuovamente la ricerca
            if (pivot == 0):
                U,P,k,spostamento_colonna = massimoPivot(U,P,k+1,h)
                spostamento_colonna = spostamento_colonna +1
            else:    
            #se il pivot trovato è in un'altra riga, effettua lo scambio delle righe
                if (s!=h):
                    P = scambio_righe(P,s,h)
                    U = scambio_righe(U,s,h)
            return (U,P,k,spostamento_colonna)
    
"""
data una matrice A, fattorizza la matrice in PA=LU tramite 
eliminazione del massimo pivot parziale
"""

def riduciAscalini (A):
    [righe,colonne]=np.shape(A)
    #passo 1
    L = np.identity(righe)
    U=np.copy(A)
    P=np.identity(righe)
    c=0  #tiene il conto in caso di spostamento di colonna
    
    k=0
    #passo k
    while k<colonne-1:
        Lk= np.identity(righe)
        #massimo pivot - eventualmente effetto lo scambio delle righe
        U,P,k,c = massimoPivot(U,P,k+c,k)
        #costruzione L al passo k - calcolo i moltiplicatori di L
        for i in range (k+1,righe):
            Lk[i][k]= (-1)*(U[i][k+c]/U[k][k+c])
        #costruzione U al passo k - ogni U di k+1 = Lk * Uk
        U=np.dot(Lk,U)
        #costruisco la L finale invertendo il segno dei moltiplicatori
        for i in range (k+1,righe):
            L[i][k]= Lk[i][k]*(-1)
        #controllo per uscire dal ciclo while
        k=k+1
        if (k+c)==colonne-1:
            k=colonne-1
    return U

"""
calcolo del rango
"""
def rango(A):
    [n_righe,n_colonne]=np.shape(A)
    B = riduciAscalini(A)
    rango = 0
    
    for i in range (0,n_righe):
        j=0
        while j<n_colonne:
            if B[i][j]!=0:
                rango = rango +1
                j=n_colonne
            else:
                j=j+1
    return rango