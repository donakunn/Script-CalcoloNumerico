# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:46:37 2021

@author: donal
"""

from numpy import *

def proprietaAritmeticaMacchina():
        """
        Test Proprietà associativa in Aritmetica Floating Point
        
        
        Questa funzione mostra come per l'aritmetica in virgola mobile non 
        valga la proprietà associativa.
        """
        x = 1e30
        y = -1e30
        z = 1
        print("x = 1e30");
        print("y = -1e30");
        print("z = 1");
        
        S1 = x + (y + z)
        S2 = (x + y) + z
        
        print("x + (y + z) = ",S1)
        print("(x + y) + z = ",S2)
        
        