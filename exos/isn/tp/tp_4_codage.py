 

def tr(texte):
    """
    >>> tr("unittestisbetter")
    [20, 13, 8, 19, 19, 4, 18, 19, 8, 18, 1, 4, 19, 19, 4, 17]
    """
    texte = "".join(t for t in texte if t != " ")
    texte = texte.lower()
    l = []
    for c in texte:
        l += [ord(c) - 97]
    return l

def rev(l):
    """
    >>> rev([20, 13, 8, 19, 19, 4, 18, 19, 8, 18, 1, 4, 19, 19, 4, 17])
    'unittestisbetter'
    """
    t = ""
    for c in l:
        t += chr(c + 97)
    return t

## 1

'hvdomzxjmwzvp'

# chars are between 97 and 122 -> 0 and 25 (so -97)

## 2

# On fait a%b

## 3
from typing import *
""" def codageCesar(t: List[int], d: int) -> List[int]:
    result = []
    for charcode in t:
        new_charcode = charcode - d
        if new_charcode < 0:
            new_charcode += 26
        result += [new_charcode]
    return result
"""

sgn = lambda x: 1 if x > 0 else (0 if x == 0 else -1)

from math import *
def codageCesar(t, d):
    n = len(t)
    res = [0 for i in range(n)]
    for i, c in enumerate(t):
        res[i] = (c-d)%26
    return res

def cesar(text: str, offset: int) -> str:
    """
    >>> cesar("avecesar", 1)
    'zudbdrzq'
    """
    return rev(codageCesar(tr(text), offset))

## 4

def decodageCesar(t: List[int], d: int) -> List[int]:
    """
    >>> decodageCesar(codageCesar([1, 2, 3], 5), 5)
    [1, 2, 3]
    """
    return codageCesar(t, -d)

## 5

def frequences(t0: List[int]) -> List[int]:
    """
    >>> frequences(tr("maitrecorbeau"))
    [2, 1, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0]
    """
    freqs = [0 for _ in range(26)]
    for v in t0:
        freqs[v] += 1
    return freqs

## 6
from matplotlib.pyplot import plot, ylabel, xlabel, show

def plot_frequencies(text: str) -> None:
    plot([rev([c]) for c in range(26)], frequences(tr(text)), 'bo')
    ylabel("fréquence")
    xlabel("lettres")
    show()

## 7

def max(l: List[Union[int, float]]) -> Union[int, float]:
    if not len(l):
        raise ValueError("l must not be empty")
    greatest = l[0]
    for v in l:
        if v > greatest:
            greatest = v
    return greatest

## 8

def decodageAuto(t0: List[int]) -> List[int]:
    # Guess the offset, assuming 'e' is the most frequent letter in t0
    e_charcode = tr('e')[0]
    frequencies = frequences(t0)
    most_frequent_charcode_count = max(frequencies)
    most_frequent_charcode = frequencies.index(most_frequent_charcode_count)
    guessed_offset = e_charcode - most_frequent_charcode
    # Decrypt
    return decodageCesar(t0, guessed_offset)

def decrypt_cesar(text: str) -> str:
    """
    >>> decrypt_cesar(cesar("I assumed e is the most frequent letter", 1))
    'iassumedeisthemostfrequentletter'
    """
    return rev(decodageAuto(tr(text)))

# plot_frequencies("I assumed e is the most frequent letter")
# print(decrypt_cesar(cesar("I assumed e is the most frequent letter", 1)))

"""
Cette méthode ne fonctionne seulement si la lettre la plus présente dans le texte original est 'e'.
"""

# --------------------------
#         Partie II
# --------------------------

## 1+2
def repeat(text: str, /, up_to: int) -> str:
    """
    >>> repeat("concours", up_to=18)
    'concoursconcoursco'
    >>> repeat("lazone", up_to=4)
    'lazo'
    """
    result = ""
    char_index = 0
    while len(result) < up_to:
        result += text[char_index]
        char_index += 1
        if char_index == len(text):
            char_index = 0
    return result

def vigenere(text: str, key: str) -> str:
    """
    >>> vigenere("becunfromage", key="jean")
    'kichwjrbvegr'
    >>> vigenere("ecolepolytechnique", key="concours")
    'gqbnsjfdahrevhziws'
    """
    key = repeat(key, up_to=len(text))
    result = ""
    for text_char, key_char in zip(text, key):
        offset = -tr(key_char)[0]
        result += cesar(text_char, offset)
    return result

# 3

def _pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, a%b
    return a

"""
Il calcule le PGCD de a et b, a ^ b
"""

## 4

def pgcd(*nums: int) -> int:
    result = 0
    nums = list(nums)
    while len(nums):
        result = _pgcd(result, nums[0])
        del nums[0]
    return result

def pgcdDesDistancesEntreRepetitions(crypted: List[int], i: int) -> int:
    """
    Returns pgcd{  }
    """
    assert 0 <= i < len(crypted) - 2, "i must be in [0, len(crypted)-2)"
    search_for = crypted[i:i+2+1]
    current_pattern: List[int] = []
    distances: List[int] = []
    for i, c in enumerate(crypted[i+3:]):
        if 0 < len(current_pattern) < 3 and c == search_for[len(current_pattern)]:
            current_pattern += [c]
        if len(current_pattern) == len(search_for):
            distances += [i]
            current_pattern = []
    return pgcd(*distances)

print(pgcdDesDistancesEntreRepetitions(vigenere("unexample", "jea"), 3))

def correction_pgcdDesDistancesEntreRepetitions(crypted: str, i):
    lprime = tr(crypted)
    pos = i
    res = 0
    for j in range(i+1, n-2):
        if lprime[j:j+3] == lprime[i:i+3]:
            res = pgcd(res, j-pos)
    return res

def longueurDeLaCle(crypted: List[int]) -> int:
    for c in crypted:
        


class correction:
    def vigenere(texte, clef):
        n = len(texte)
        t = tr(texte)
        c = tr(clef)
        k = len(c)
        res = [0 for i in range(n)]
        for i in range(n):
            res[i] = (t[i] + c[i%k])%26
        return rev(res)
