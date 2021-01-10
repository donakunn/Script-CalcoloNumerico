#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:28:42 2021

@author: kun
"""

def baseDiLagrange(X,k,x):
    """
    La funzione genera la k-esima base di lagrange per il vettore delle x 
    passato come input.
    Parameters
    ----------
    X : vettore delle ascisse dei nodi di cui calcolare la k-esima base
    k : k valore di cui calcolare la base
    x : incognita della base
 
    Returns
    -------
    Lk : base di Lagrange
    """
    Lk = 1;
    for i in range(0,len(X)):
        if i != k:
            Lk= Lk* ((x-X[i])/(X[k]-X[i]))
    return Lk
        

def polinomioDiLagrange(Lkx,y):
    """
    La funzione genera il polinomio interpolante utilizzando i vettori delle
    basi di lagrange e il vettore delle y

    Parameters
    ----------
    LkX : vettore delle basi di Lagrange
    y : vettore delle ordinate dei nodi

    Returns
    -------
    Pnx : valutazione del polinomio di lagrange
    """ 
    if len(Lkx) != len(y):
        print('Errore, numero basi diverso da numero ordinate')
        return
    
    Pn = 0
    for i in range(0,len(Lkx)):
        Pn = Pn + Lkx[i]*y[i]
    return Pn
    
def valInterpolazione(x,y,xx):
    """
    La funzione genera il polinomio interpolante per i vettori di nodi x e y
    dati in input, e li valuta nei nodi xx

    Parameters
    ----------
    x : vettore delle ascisse dei nodi
    y : vettore delle ordinate dei nodi
    xx : vettore dei punti in cui valutare il polinomio

    Returns
    -------
    yy : valutazioni del polinomio che interpola i dati x,y, nei punti dell'
            array xx
    """
    yy = []
    Lkx = []
    if len(x) != len(y):
        print('Errore, numero ascisse e ordinate nodi diverso')
        return
    
    for i in range(0,len(xx)):
        #genero basi per xx[i]
        for j in range(0,len(x)):
            Lkx.append(baseDiLagrange(x,j,xx[i]))
        #valuto il polinomio e lo aggiungo all array delle valutazioni
        yy.append(polinomioDiLagrange(Lkx,y))
        #pulisco array basi
        Lkx.clear()
    return yy

    
    