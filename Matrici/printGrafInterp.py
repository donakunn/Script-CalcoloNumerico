#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:04:09 2021

@author: kun
"""
import numpy as np
from pylab import *
from polLagrange import valInterpolazione

def printGraficoInterp(f,a,b,n):
    """
    La funzione genera un grafico che rappresenta nell'intervallo [a,b] il
    grafico della funzione f, i punti (xi,yi) ed il grafico del polinomio 
    interpolante

    Parameters
    ----------
    f : funzione 
    a,b : estremi dell'intervallo
    n : numero di nodi equidistanti dell'intervallo [a,b]
    """
    xFunz = np.linspace(a,b,100)
    x = np.linspace(a,b,n)
    y = f(x)
    xx = np.linspace(a,b,100)
    yFunz = f(xFunz)
    yy = valInterpolazione(x,y, xx)
    
    plot(xFunz,yFunz,label="grafico funzione")
    plot(x,y,'o',label="nodi")
    plot(xx,yy,label= "grafico polinomio interpolante")
    legend(loc='upper right')
    
    