# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:52:59 2019

@author: felix
"""

from numpy import *
from pylab import *
def taylor_exp(x,n):
    """
    approssimazione di exp(x) mediante polinomio di Taylor
    x: valore in cui valutare exp(x)
    n: grado del polinomio di Taylor
    """
    expx=exp(x)
    fatt=1
    S=zeros(n+1)
    S[0]=1
    z=1
    for k in range(1,n+1):
        fatt=fatt*k
        z=z*x
        S[k]=S[k-1]+z/fatt
    Er=abs(S-expx)/expx
    
    fatt=1
    S1=zeros(n+1)
    S1[0]=1
    z=1
    s=sign(x)
    x=abs(x)
    for k in range(1,n+1):
        fatt=fatt*k
        z=z*x
        S1[k]=S1[k-1]+z/fatt
    if s==-1:
        S1=1/S1
    Er1=abs(S1-expx)/expx

    #parte grafica
    semilogy(arange(0,n+1),Er,'.-',arange(0,n+1),Er1,'.-')
    grid(axis='both')
    xlabel('grado del polinomio di Taylor')
    ylabel('errore relativo')



