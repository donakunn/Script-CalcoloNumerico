# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:47:55 2021

@author: donal
"""

"""
Funzioni che utilizzano la tecnica del massimo pivot parziale con scopi diversi
"""

from fatLUMaxPivot import fattLUmaxPivot


def detUsingLU(A):
    """
    La funzione calcola il determinante di una matrice utilizzando la 
    fattorizzazione LU con tecnica del massimo Pivot parziale

    Parameters
    ----------
    A : Matrice di cui calcolare il determinante

    Returns
    -------
    det : Determinante di A

    """
    
    P,L,U = fattLUmaxPivot(A)
    det = 1
    for i in range(0,len(U)):
        det = det * U[i,i]
    return det

