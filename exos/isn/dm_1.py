## 1/a

def estEgyptienne(lst):
    if lst[0] < 2:
        return False
    last = lst[0]
    for a_i in (lst[1:]):
        if a_i <= last:
            return False
        last = a_i
    return True

## 1/b

from copy import deepcopy


def prod(l):
    r = 1
    for i in l:
        r*=i
    return r

def sum(l):
    r = 0
    for i in l:
        r+=i
    return r

def rationnel(lst):
    numerator = []
    for i in lst:
        numerator_part = deepcopy(lst)
        numerator_part.remove(i)
        numerator += [prod(numerator_part)]
    return sum(numerator), prod(lst)

"""
  k  |  a | b    | m | lst = L
  1  | 19 | 20   |   | []
     | 
  2  | 18 | 40   | 2 | [2]
  3  | 14 | 120  | 3 | [2, 3]
  4  |  6 | 1080 | 9 | [2, 3, 9]

lst = [2, 3, 9, 180]
"""

def fractionEgyptienne(p, q):
    a = p
    b = q
    lst = []
    print(f"""
a | b | m | lst
{p} | {q} |  | {lst}""")
    while b % a != 0:
        m = b // a + 1
        lst.append(m)
        a = a * m - b
        b = b * m
        print(f"{a} | {b} | {m} | {lst!r}")
    lst.append(b // a)
    print(f"lst = {lst!r}")
    return lst

fractionEgyptienne(19, 20)

## 1/d

"""
b = aq + r <=> b != aq si r != 0
           <=> ¬(a | b)

m_k, a_(k+1) et b_(k+1) sont définies si a_k ne divise pas b_k

m_k = ⌊ b_k/a_k ⌋ + 1
a_(k+1) = a_k * m_k - b_k
b_(k+1) = b_k * m_k
"""


## 1/e

"""
1 <= a_(k+1) < a_k

"""

## 2/a

def estPréfixe(u, v):
    for i in range(0, len(v)):
        if u[i] != v[i]:
            return False
    return True

estPréfixeOneLiner = lambda u, v: u[:len(v)] == v # drop the one-liner

"""
Le nombre maximal de comparaisons est len(v) = q
"""

## 2/b

"""
Le bord de abaababa est aba
Le bord de abababa est ababa
"""

def bord(u):
    """
    éxécution de bord("undébutuntructrucundébut")
    i  suffix                  estPrefixe
    23 ndébutuntructrucundébut False
    22 débutuntructrucundébut  False
    21 ébutuntructrucundébut   False
    20 butuntructrucundébut    False
    19 utuntructrucundébut     False
    18 tuntructrucundébut      False
    17 untructrucundébut       False
    16 ntructrucundébut        False
    15 tructrucundébut         False
    14 ructrucundébut          False
    13 uctrucundébut           False
    12 ctrucundébut            False
    11 trucundébut             False
    10 rucundébut              False
    9  ucundébut               False
    8  cundébut                False
    7  undébut                 True
    """
    for i in reversed(range(0, len(u))):
        suffix = u[len(u)-i:len(u)]
        if estPréfixe(u, suffix):
            break
    return suffix

# 2/c



# v.join([w₁, w₂]) = w