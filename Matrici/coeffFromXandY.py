#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:06:09 2021

@author: kun
"""
from Vandermonde import vandermonde
from Gauss import gaussWithMaxPivot 
import numpy as np

def coeffFromXandY(x,y):
    """
    La funzione calcola i coefficienti del polinomio interpolante, dati i 
    vettori x delle incognite e y delle soluzioni dati.
    Trasforma il vettore delle incognite in una matrice di Vandermonde,
    la rende completa aggiungendo il vettore delle soluzioni, e calcola i 
    coefficienti utilizzando l'algoritmo di eliminazione di Gauss con tecnica
    del massimo Pivot parziale

    Parameters
    ----------
    x : vettore delle incognite
    y : vettore delle soluzioni

    Returns
    -------
    a : vettore dei coefficienti

    """
    if len(x) != len(y):
        print('Errore: vettore delle incognite  e vettore delle soluzioni hanno'
              ' dimensioni diverse')
        return
    
    A = vandermonde(x)
    A = np.c_[A,y]
    print (A)
    a = gaussWithMaxPivot(A)
    
    return a
    