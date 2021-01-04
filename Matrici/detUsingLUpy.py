# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:47:55 2021

@author: donal
"""

from fattLU import fattlu


def detUsingLU(A):
    """
    La funzione calcola il determinante di una matrice utilizzando la 
    fattorizzazione LU

    Parameters
    ----------
    A : Matrice di cui calcolare il determinante

    Returns
    -------
    det : Determinante di A

    """
    
    L,U = fattlu(A)
    det = 1
    for i in range(0,len(U)):
        det = det * U[i,i]
    return det
