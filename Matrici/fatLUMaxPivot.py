#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:32:13 2021

@author: kun
"""

"""
fattorizzazione lu
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
data una matrice A, fattorizza la matrice in PA=LU tramite 
eliminazione del massimo pivot parziale
LA MATRICE DEVE ESSERE QUADRATA
"""

def fattLUmaxPivot (A):
    [m,n]=np.shape(A)
    if np.linalg.det(A)!=0:
        
        #passo 1
        L = np.identity(m)
        U=A[:][:]
        P=np.identity(m)
        #passo k
        for k in range (0,n):
            Lk= np.identity(m)
            
            #codice massimo pivot - eventualmente effetto lo scambio delle righe
            s=k
            pivot = np.abs(U[k][k])
            for i in range (k+1,m):
                if np.abs(U[i][k])>pivot:
                    s=i
                    pivot=np.abs(U[i][k])
            if (s!=k):
                P = scambio_righe(P,s,k)
                U = scambio_righe(U,s,k)
                
            #costruzione L al passo k - calcolo i moltiplicatori di L
            for i in range (k+1,m):
                Lk[i][k]= (-1)*(U[i][k]/U[k][k])
            #costruzione U al passo k - ogni U di k+1 = Lk * Uk
            U=np.dot(Lk,U)
            #costruisco la L finale invertendo il segno dei moltiplicatori
            for i in range (k+1,m):
                L[i][k]= Lk[i][k]*(-1)
    return P,L,U

