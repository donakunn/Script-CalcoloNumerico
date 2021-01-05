# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:48:25 2020

@author: donal
"""

from numpy import *
def dir_cost(f,m,x0,tol,itmax):
    """
    METODO DELLA DIREZIONE COSTANTE

    Parametri di input
    ------------------
    f: funzione di cui ricercare uno zero    
    m: parametro del metodo della dir cost.
    x0: stima iniziale dello zero
    tol: accuratezza richiesta
    itmax: numero massimo di iterate consentite

    Parametri di output
    -------------------
    x1: approssimazione dello zero
    it: numero di iterazioni effettuate
   """

    it=0
    arresto=False
    while not(arresto) and it<=itmax:
        it=it+1
        x1=x0-m*f(x0)
        arresto=abs(x1-x0)<tol 
        x0=x1
    if not(arresto):
        print("precisione non raggiunta")
    return x1,it