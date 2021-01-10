# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:56:54 2020

@author: felix
"""

from numpy import *
from pylab import *
def cond_log():
    """
    Mostra il mal condizionamento della funzione logaritmo
    in un intorno di 1
    Lavoreremo in singola precisione, prendendo come valori di riferimento
    quelli ottenuti in doppia precisione
    """
    # 100 punti che si addensano a 1 con distribuzione logaritmica
    distanza=logspace(-8,0,100)
    x=1+distanza
    # valori di riferimento mediante cui calcolare l'errore relativo
    y_ref=log(x)
    # trasformiamo x in singola precisione
    xs=float32(x)
    ys=log(xs)
    # Errore relativo
    Er=abs(ys-y_ref)/abs(y_ref)
    # parte grafica
    loglog(distanza,Er)
    title('Condizionamento di log(x)')
    xlabel('distanza da 1')
    ylabel('errore relativo')
    grid(axis='both')
    
    
    
    
