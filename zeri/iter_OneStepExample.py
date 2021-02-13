# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
from pylab import *
from zeri import newton

def fiVsNewton():
    """
    ESEMPIO DI CONVERGENZA CON METODO ITERATIVO ONE-STEP Vs Metodo Newton

    Questa funzione mostra la convergenza della funzione y = x^4-2x utilizzando
    la successione generata dal metodo iterativo one-step e la successione 
    generata dal metodo di Newton
    """

    x = linspace(1.2,2.5,16)
    y = f(x)
    x0 = 3    #valore iniziale
    it = 0      #iterate
    tol=1e-10   #tolleranza
   
    arresto = False
    xx=[]       #vettore xn
    yy = []     #vettore ordinate calcolate in xn
    yyN=[]      #vettore ordinate calcolate in xn Newton
    while it < 50 and not(arresto):
        it = it+1
        xn = sqrt(sqrt(2*x0))
        xx.append(xn)
        arresto=abs(xn-x0)<tol
        x0 = xn
    xN,itN,xxN = newton(f,3)    #xN zero, itN numero iterate, xx array xn Newton
    print('f= x**4-2*x')
    print('funzione iteratrice= x = sqrt(sqrt(2x))')
    print('x0 = 3')
    print('tolleranza= ',tol)
    print('la funzione fi converge a ', xn, 'dopo ', it, 'iterate')
    print('il metodo di newton converge a ', xN, 'dopo ', itN, 'iterate')
    plot(x,y, label ="y = x**4-2*x")
    for x in xx:
        yy.append(f(x))
    for x in xxN:
        yyN.append(f(x))
    plot(xx,yy,'o',label="xn metodo Fi")
    plot(xxN,yyN,'o',label="xn metodo Newton")
    legend(loc='upper left')
    xlabel("asse x")
    ylabel("asse y")
    title("Grafico successioni fi e Newton") 
    return 

def f(x, ord= 0):
    if ord == 0:
        return x**4-2*x
    elif ord==1:
        return 4*x**3-2
    else:
        print('ordine di derivazione non definito')
        return    
        

