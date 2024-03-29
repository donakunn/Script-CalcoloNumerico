# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:30:34 2021

@author: donal
"""

def gaussWithMaxPivot(A):
    """
    Algoritmo di eliminazione di Gauss con tecnica del massimo pivot parziale
    Parametri di input
    ------------------
    A: matrice completa di cui calcolare le soluzioni
    
    Parametri di output
    -------------------
    x: vettore delle soluzioni del sistema lineare
    """
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n-1] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n-1] -= A[k][i] * x[i]
    return x