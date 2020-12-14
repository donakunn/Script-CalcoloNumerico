# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
def iter_OneStep():
    """
    ESEMPIO DI CONVERGENZA CON METODO ITERATIVO ONE-STEP

    Questa funzione mostra la convergenza della funzione y = x^4-2x utilizzando
    la successione generata dal metodo iterativo one-step
    """
    print('f= x**4-2*x')
    print('funzione iteratrice= x = sqrt(sqrt(2x))')
    x0 = 1.4    #valore iniziale
    print('x0 = 1.4')
    it = 0      #iterate
    tol=1e-10   #tolleranza
    print('tolleranza= ',tol)
    arresto = False
    
    while it < 50 and not(arresto):
        it = it+1
        xn = sqrt(sqrt(2*x0))
        arresto=abs(xn-x0)<tol
        x0 = xn
        print('xn= ', xn)
    print('la funzione converge a ', xn, 'dopo ', it, 'iterate')
    return xn 
    