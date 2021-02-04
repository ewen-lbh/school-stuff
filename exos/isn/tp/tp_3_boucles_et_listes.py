## 2/3
n = 0
while abs(u(n)**2 - 2) >= 2e-5:
    n += 1
print(n)

# n == 4
# √2 ≈ 1.4142156862745097

## 2/4
n = 0
q = 4 # choose this
def u_q(n):
    if n <= 0:
        return 1
    return (1/q)*(u(n-1)+q/u(n))
while abs(u_q(n)**q - q) >= q*1e-5:
    n += 1
print(n)

## 3/1/a

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

## 3/1/b

def binom(n, p):
    return fact(n)//(fact(p)*fact(n-p))

## 3/2 sans la formule de Pion

def coefs_binomiaux(n):
    coefs = []
    for p in range(0, n+1):
        coefs.append(binom(n, p))
    return coefs

def coefs_binomiaux_fast(n):
    u=1
    coefs = [u]
    for p in range(n):
        u *= (n-p)//(p+1)
        coefs.append(u)
    return coefs

## bonus mdr

def triangle_pascal_upto(n, align_char="<"):
    triangle = [coefs_binomiaux(ligne) for ligne in range(n)]
    max_int_length = max(max(len(str(i)) for i in ligne) for ligne in triangle)
    for ligne in triangle:
        print(" ".join([f"{i:{align_char}{max_int_length}}" for i in ligne]))

## 1/7

from math import sqrt, log as ln

def isprime(n):
    i = 2
    while i <= int(sqrt(n)):
        if n%i==0:
            return False
        i+=1
    return True

def π(n):
    return len([p for p in range(2, n+1) if isprime(p)])

for n in range(10**6):
    print(f"""
            ln {n}
    π({n}) --------------------- = {π(n)*(ln(n)/n)}
            {n}
    """)
