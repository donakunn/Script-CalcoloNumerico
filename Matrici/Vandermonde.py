#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:12:32 2021

@author: kun
"""
import numpy as np

def vandermonde(x):
    """
    La funzione genera la matrice di Vandermonde a partire dal vettore delle 
    incognite passato come argomento

    Parameters
    ----------
    x : vettore delle incognite

    Returns
    -------
    van : Matrice di Vandermonde

    """
    dim = len(x)
    van = np.zeros((dim,dim))
    
    for i in range (0,dim):
        for j in range(0,dim):
            van[i][j] = x[i]**j
    return van
    

def detDiVandermonde(x):
    """
    La funzione calcola il determinante di una matrice di Vandermonde, il 
    quale equivale al prodotto delle differenze di elementi della matrice
    
    Parameters
    ----------
    x: array incognite

    Returns
    -------
    det = determinante della matrice di Vandermonde
    
    """
    dim = len(x)
    j = dim-1
    det = 1
    
    while j > 0:
        for i in range(0,j-1):
            det = det * (x[j]-x[i])
        j= j-1
        print (det)
    return det

    detDiVandermonde(np.array([2,3,4,5]))