import numpy as np
from rich import traceback, pretty, print
for f in traceback, pretty: f.install()

def recherche_pichou(A, b, j):
    pivot_loc = j
    for i in range(j+1, A.shape[0]):
        if abs(A[i, j]) > abs(A[pivot_loc, j]):
            pivot_loc = i
    if pivot_loc != j:
        A[[pivot_loc, j]] = A[[j, pivot_loc]]
        b[[pivot_loc, j]] = b[[j, pivot_loc]]

def élimination_bas(A, b, j):
    for i in range(j+1, A.shape[0]):
        b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]
        A[i] = A[i] - (A[i, j] / A[j, j]) * A[j]

def descente(A, b):
    for j in range(A.shape[1]-1):
        recherche_pichou(A, b, j)
        élimination_bas(A, b, j)

def élimination_haut(A, b, j):
    for i in range(j):
        b[i] = b[i] - (A[i, j] / A[j, j]) * b[j]
        A[i] = A[i] - (A[i, j] / A[j, j]) * A[j]

def remontée(A, b):
    for j in range(A.shape[1]-1, 0, -1):
        élimination_haut(A, b, j)

def solve_diagonal(A, b):
    for k in range(b.shape[0]):
        b[k] = b[k] / A[k, k]
    return b

def gauss(A, b):
    U, v = A.copy(), b.copy()
    descente(U, v)
    remontée(U, v)
    return solve_diagonal(U, v)

def inverse(A):
    return gauss(A, np.identity(A.shape[0]))

print(inverse(np.identity(12)))
