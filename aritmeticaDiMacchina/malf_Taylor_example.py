# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:39:02 2020

@author: donal
"""

from taylor_exp import taylor_exp

def MalFunz_Taylor_example():
    """
    La funzione mostra come l'errore relativo diventa molto piccolo per cifre
    positive, mentre si ferma ad un ordine di grandezza considerevole per le 
    cifre negative, risolto considerando in questi casi e**x = 1/e**-x

    Returns
    -------
    None.

    """
    print('i valori considerati sono: 5 (in rosso), -20 (arancio e blu)')
    print('dopo 75 iterate')
    taylor_exp(-20,75)
    taylor_exp(5,75)
    
MalFunz_Taylor_example()