x = 237
a = int(x / 100)
x = x - 100 * a
b = int(x / 10)
x = x - 10 * b
c = x
Resultat = a + b * 10 + c * 100
print(Resultat)

# >>> 732

L = [12, 8, 19, 7, 3, 10]
Resultat = [20 - L[i] for i in range(len(L))]
print(Resultat)


## >>> [8, 12, 1, 13, 17, 10]


Resultat = 0
for i in range(5):
    Resultat += i + 1
print(Resultat)

## >>> 15


L = [i for i in range(10)]
for i in range(len(L)):
    if i >= 1:
        L[i] = L[i] + L[i - 1]
Resultat = L
print(Resultat)

## >>> [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]


Val, i = 0, 0
L = [7, 14, 21, 45, 52, 67, 89, 99]
while Val <= 50:
    i += 1
    Val = L[i]
Resultat = [i, Val]
print(Resultat)

## >>> [4, 52]

Somme = 0
n = 10
for i in range(n):  # il manque les deux points
    Somme += i  # indentation incorrecte
print(Somme)  # il manque la majuscule à Somme

## >>>> 45

from math import pi

Rayon = float(input("Rayon [m] ? > "))  # il manque les ""
Aire = pi * Rayon ** 2  # l' exposant se note ** et pas ^
Perimetre = 2 * pi * Rayon  # il manque la majuscule à Rayon
print(f"Aire: {Aire}, Périmètre: {Perimetre}") # f-strings!

# Rayon [m] ? > 45
# >>> Aire: 6361.725123519331, Périmètre: 282.7433388230814

import random

n = 10000
L = [random.randint(0, 1000) for i in range(n)]
a = 0
b = 0
c = 0
for i in range(len(L)):
    if L[i] < 500:
        a += 1
    elif L[i] > 500: # else if ~> elif
        b += 1
    else:
        c += 1
print(a, b, c)


##3 Code non fonctionnel


a = 25
b = 226
a = max(a, b)
b = min(a, b)
r = a
i = 0
while r >= b:
    i += 1
    r -= b
print(a, " = ", b, " * ", i, "+", r)

##1

a = 25
b = 226
a1 = max(a, b)
b = min(a, b)
r = a1
i = 0
while r >= b:
    i += 1
    r -= b
print(a1, " = ", b, " * ", i, " + ", r)

# 4 Ecriture de code

# la fonction def decompose(l) qui prend en paramètres une liste l d'entiers et retourne deux listes

def decompose(l):
    rp, ri = [], []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            rp.append(l[i])
        else:
            ri.append(l[i])
    return rp, ri


#

##une fonction def present(l,a) qui prend en paramètres une liste d'entiers l et un entier a et ##retourne le nombre de multiples de a dans la liste.


def present(l, a):
    c = 0
    for i in range(len(l)):
        if l[i] % a == 0:
            c += 1
    return c
