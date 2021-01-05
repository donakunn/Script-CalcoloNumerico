#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:30:03 2021

@author: kun
"""

import numpy as np

def algoritmoSostituzione (A,b):
    
    """
    Algoritmo di sostituzione all'indietro, nel caso in cui la matrice sia 
    triangolare superiore, o in avanti nel caso in cui sia triangolare inferiore
    
    Parametri di input
    ------------------
    A: matrice triangolare sup o inferiore di cui calcolare le soluzioni
    b: vettore dei termini noti
    
    Parametri di output
    -------------------
    x: vettore delle soluzioni del sistema lineare
    """
    [n_righe,n_colonne]= np.shape(A)
    [dim] = np.shape(b)
    #A deve essere quadrata e il vettore b deve avere la stessa 
    #lunghezza di righe/colonne di A
    if n_righe==n_colonne and dim==n_righe:
        n =0
        #verifica se A è una matrice triangolare superiore
        for i in range (1,n_righe):
            j=0
            while j < i:
                if A[i][j]!=0:
                    j=i
                else:
                    n=1
                    j= j+1
        #verifica se A è una matrice triangolare inferiore 
        #dopo aver controllato che non è triangolare superiore
        if n==0:
            for i in range (1,n_righe):
                j=i+1
                while j<n_colonne:
                    if A[i][j]!=0:
                        j=n_colonne
                    else:
                        n=2
                        j=j+1
        #caso in cui la matrice è tringolare superiore
        if n==1:
            #controllo che gli elementi della diagonale siano tutti diversi 
            #da 0
            d = np.diag(A)
            min = np.min(d)
            if np.abs(min) > 1e-15:
                #calcolo del vettore delle incognite con il metodo di 
                #sostituzione all'indietro
                x = [0]*n_colonne #crea una lista di dimensione n_colonne 
                                  #contenente degli 0
                x[n_colonne-1] = b[n_righe-1]/A[n_righe-1][n_righe-1]
                for i in range (n_righe-2,-1,-1):
                    sommatoria = 0
                    for j in range (i,n_colonne):
                        sommatoria = sommatoria + A[i][j]*x[j]
                    x[i]=(b[i] - sommatoria)/A[i][i]
                return x
            else:
                print('Errore: elemento della diagonale nullo')
                return -1
        #caso in cui la matrice è triangolare inferiore
        elif n==2:
            #controllo che gli elementi della diagonale siano tutti diversi da 0
            d = np.diag(A)
            min = np.min(d)
            if np.abs(min) > 1e-15:
                #calcolo del vettore delle incognite con il metodo di 
                #sostituzione in avanti
                x = [0]*n_colonne #crea una lista di dimensione n_colonne 
                                  #contenente degli 0
                x[0] = b[0]/A[0][0]
                for i in range (1,n_righe):
                    sommatoria = 0
                    for j in range (n_colonne-1,i,-1):
                        sommatoria = sommatoria + A[i][j]*x[j]
                    x[i]=(b[i] - sommatoria)/A[i][i]
                return x
            else:
                print('Errore: elemento della diagonale nullo')
                return -1
        else:
            print('Errore: la matrice non è triangolare inf o sup');
            return -1
    else:
        print('Errore: La matrice non è quadrata.')
        return -1
    
            
            
            