# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""



                TP1 pour découvrir Python

La plupart des objets seront revus au cours de l'année.
Quel est l'objectif? 
Apprivoiser la syntaxe du language python. Je vous propose d'exécuter les commandes suivantes et de faire le maximum d'expérience (en testant des variantes des codes proposés) 

"""
############################
# Utilisation dans Pyzo    #
############################

# Vous pouvez utiliser le mode interactif proposé par IEP, il suffit d'écrire le code dans le shell ouvert ci-dessus. Testez en écrivant 2+45 aprés le >>> et appuyer sur entrée. Dans le mode intéractif, les codes ne pourront pas étre conservés .... 

# vous pouvez également utiliser un fichier *.py contenant un code source. Il suffit ensuite de "compiler"/ "interpréter" votre code pour que qu'il s'exécute dans le shell.

#exemple : (surligner le code é exécuter et cliquer dans l'onglet "Exécuter la selection")

####################
# Premiére étape   #
####################


2+45

# Il ne se passe rien ...

print(2+45) 

# N'oubliez pas la commande "print" ou faite un copier-coller dans le shell.


####################
# 1-Les entiers    #
####################



print(12*45+5%3)
print(12**5)

print(7/3)
print(7//3)
print(7//3.)
print(7/3)

# Quel est le type de l'objet utilisé ?

print(type (7))
print(type (7.))

# Quelle est la différence entre 'int' et 'float'?

# Quelques mots sur la fonction id() : identificateur (unique) associé à l'objet. i.e. son adresse en mémoire.

print(id(True))
print(id(False))
print(id(2))
a=2
print(id(a))
b=a
print(id(b)==id(a))
b=3
#
a=2
b=2.0
print(id(b)==id(a))

# tester une égalité :
    
print(2==3)    
print(2==2)    
print(2==2.) # surprenant non !!  


a=2
b=2
print(a is b)
print(a==b)
print(id(a))

a=2
b=2.
print(a is b)
print(a==b)


print(21%5)  # Le reste de la division euclidienne....un peu de modulo. Trés utilie pour un imposer un critére de divisibilité. 
  
  
  
# un pgcd = plus grand divisuer commun.
  
import fractions as frc # importer le module "fractions" sous le nom "frc" qui contient 
print(dir(frc))


a=13572468
b=12345678
print(frc.gcd(a,b))

print(frc.gcd(a,b))


from fractions import * # permet d'utiliser la fonction gcd sans le suffixe "frc".
a=13572468
b=12345678
print(gcd(a,b))

# Quelle est cette fonction "gcd"? il suffit d'ouvrir le document fractions.py pour lire la définition de gcd  suivante
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# é relire aprés la petite partie sur les fonctions ...


### Attention: pour la culture:

print(5^2) # D'ou vient ce résultat ?
print(42^17)
# une explication rapide à méditer: l'écriture binaire de 42 est  42=1x32+0x16+1x8+0x4+1x2+0x1
# En binaire 42= 101010 et 17=10001 
# 42^17=111011 (le ou exclusif)= 1x32+1x16+1x8+0x4+1x2+1x1=59
# ex : 5^2= 101^10=111=7


####################
# 2-Les flottants  #
####################

print(1/3)
print(pi)

# nous aurons souvent besoin d'aide ... des bibliothéques/ des modules . Pi est défini dans la bibliothéque math. 
# on appelle une commande par "math.????"

import math 
print(dir(math)) # elle contient quoi?

print(math.pi)

# on peut changer le nom si nécessaire 

import math as m
print(m.pi)

print(type (m.pi))

# Les fonctions usuelles 

print(m.cos(2*m.pi))
print(m.sqrt(2*m.pi))

# quelques calculs avec des flottants :
    
print(2/3**6)
print((2/3)**6)
print((1/2**3)*2**3)

# Comment controler l'affichage ?

print(-3.445e02)
print(format(-3.445e-5,'.10f'))
print(format(m.pi,'.30f'))


##################################
# 3-Variables et affectations    #
##################################


# print(x)
x=5
print(x)
x=5
print(x==4)
# print(x=5)
print(x==5)
print(x) # respecter la casse
x='x'
print(x)

x=1
x=x+1
print(x)

# un test plus évolué:

x=1
y=2
x=(x+y)/2
y=(x*y)
print(x,y)

# Est-ce clair?

c=x,y,z=1,2,3
print(c)
print(x*y**z)

# De la syntaxe

s=1
s=s+1
print(s)

s=2
s+=4 # Quel est le sens de += ?  (essayer -= ou *= ou **=)
print(s)



###########################
# Complément (nombres)    # cette partie sera rarement utilisée ... elle est indicative.
###########################

# Les fractions

from fractions import *
a=Fraction(24,10)
print(a) # simplification !
print(a.numerator )
print(a.denominator)

a=Fraction.from_float(2.7)
print(a)


# Les complexes

z=complex(4,3)
print(z)

print(z.real)
print(z.imag)

i=complex(0,1)
print(i**2)


# pour le reste .... consulter dir(complex)

#  Une premiére approche de quelques types... à approfondir et explorer
# (les listes, les Tuplets, ....)

##################################
# 4-Les listes                   #
##################################

a='test'

print(a)
l=[2,5,2.2, 'test']

print(l)
print(l[1])
print(l[0])
print(l[10])
print(len(l))

print(l[-1])
print(l[-5])

print(l[0:2]) # les intervalles d'entiers sont ouverts é droite
print(l[-2:2])
print(l[0:len(l)])
print(l[-3:4])
print(l[-4:4])

l[2]=15
print(l) # les listes sont mutables...

# une liste d'entiers . (Attention les intervalles sont ouverts é droite.)

I=range(2,9)
print(type(I))
# range= gamme , plage.

I=range(2,9,2)
print(list(I))


print(list(I))
print(3 in I)

# nous complèterons l'étude des listes dans le TP2

##################################
# 5-Les Tuples                   #
##################################

t=3,4,5,6,'7'
print(t)

print(t[0])
t[0]=1 # Attention .... les Tuples ne sont pas mutables

a,b,c=1,2,3
print(a)

a=range(2,10)
print(a[2])


##################################
# 5-Les chaînes de charactères   #
##################################

a='prof de maths'
b="prof de maths"
print(a==b) # au moins c'est dit !!!
print(a is b )

print(len(a))
print(a[7:13])
print(a[-1])

a[0]='r' # Que dire des chaines?

a='il fait'
b=' chaud'
print(a+b)

c=''
c+='alpha'
print(c)


##################################
# 5-Les ensembles                #
##################################

s={'je' , 2, 'vous', 34}
print(s)

print(3 in s)
print(2 in s)

a='je' in s
b='nous' in s
print(a,b)


# les ensembles sont itérables !

s={'je' , 2, 'vous', 34}
for x in s: print(x*2)  # la syntaxe dans le prochaine TP

{s*2 for s in s}


# Les opérations ensemblistes

a={1,2,3,4,5,6}
p={2,3,4,6}
i={1,3,5}

print(p&i)# l'intersection
print(p|i)# l'union
print(a-p) # no comment


# Vérification des types et changements de type

print(type('prof de maths')) # string 
t=3,4,5,6,'7'
print(type(t)) # tuple 
l=[2,5,2.2, 'test']
print(type(l)) # list 

l=list(a)
print(l)
t=tuple(a)
print(t)
s=set(l)
print(s)

print(type(print))


##################################
# -Les dictionnaires             #
##################################


d={'a':1,'b':2,'c':3}
for i in d : print(i)

for i in d : print(i, end='')
print()

print(d['a'])
print(d)
print(d.keys())
print(d.values())
print(d.items())

l=[(1,'b'),(2,'c'),(3,'g')]
print(dict(l))

#############################################################
# 5-Tester avec if / Instruction conditionelle              #
#############################################################

if 2013%2==0:
    print('2013 est pair') 
else:
    print('Sans blague ....')  
    
if 2013%2 == 1:
        print('test 1 ok ')

if ((2013%2 == 1) and (2013 > 10**3)) or (2013 < 0):
        print('test 2 ok ')

if ((2013%2 == 1) and (2013 > 10**4)) or (2013 < 0):
    print('test 2 ok ')
else:
    print('test 2 echec ')

# Attention à la présentation indentée
    
if ((2013%2 == 1) and (2013 > 10**4)) or (2013 < 0):
    print('test 2 ok ')
else:
    print('test 2 echec ') 
        
# et le elif

n=11

if n%3==0:
    print(n,' est congru a 0 modulo 3')
elif n%3==1:
    print(n,' est congru a 1 modulo 3')
else:
    print(n,' est congru a 2 modulo 3')

  
##################################
# 6-Les fonctions                #
##################################  
# il s'agit d'une première approche... 
# la syntaxe:
# def lenomdelafonction(variable):
    #
    #corps de la fonction
    #
    #return(le résultat)

def f(x):
    return(x+1)

print(f(1))
#
def testparite(n): # le nom
    res=''
    if n%2==0:
        res+='est pair'
    else: res+='est impair'
    return(n,res) 

print(testparite(3)  )


def puiss(x,n):
    return(x**n)
    
    
puiss(11,3)  


def abs(x):
    if x>0:
        return x
    else:
        return -x

print(abs(-2))

##################################
# 8-Les polynémes                #
##################################  
# cette partie sera très utile lors de l'oral de Math/Info du concours Centrales/Supélec mais un peu moins pendant la première année
# nécessite le module "numpy"
from numpy import *
p=poly1d([2,3,4,10]) # donne le polynéme é l'aide des coefficients
print(p)	

p=poly1d([2,3,4,10], True) # donne le polynéme é l'aide des racines
print(p)

print(p.order)	# le degré 
print(p.roots)	# les racines
print(p.coeffs) # les coefficients

print(p(5.))  # évaluation en un point

##################################
# 9-Tracer des courbes           #
##################################  

# Pour retrouver les codes ... vister le site http://matplotlib.sourceforge.net/gallery.html


import matplotlib.pyplot as plt
import numpy as np

# une courbe 

x=np.linspace(-5,5,100)  # abscisse de -5 à 5 avec 100 points 
plt.plot(x,sin(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")
plt.show()
#plt.savefig(""D:/Nicolas/Informatique/Python/MPSI/fig1.pdf") # changer le chemin 


# 2 pour le prix d'une


x = np.arange(0, 10, 0.2) 
y1 = np.sin(x)
y2 = np.cos(x)
# Créer une figure
fig = plt.figure()
# Un tracé dans la figure
ax = fig.add_subplot(111)
#2 tracés avec le méme axe
l1, l2 = ax.plot(x, y1, 'd', x,y2,'+')
#Légende dans le coin en haut é gauche 
fig.legend((l1, l2),('sin','cos'),'upper left')
# L'axe des x est 't'
ax.set_xlabel('t')
# L'axe des y est 't'
ax.set_ylabel('y')
plt.show()
#plt.savefig("D:/Nicolas/Informatique/Python/MPSI/TPfig2.pdf")

##################################
# Divers                       #
##################################  

import math as m

# controler le temps:
    
import time
print(time.asctime()) # Quel est l'origine?


print(dir(time))

def d(x):
    return(format(x,'.10f'))
d(m.pi)

# Que fait la fonction d?

t=time.time()
d(time.time()-t)


t=time.time()
s=0
for i in range(10**5): s=0
print(time.time()-t)
# Tester plusieurs fois la fonction précédente (les 4 lignes )

/issues/403
# Cmment simuler le hasard?

from random import *
 
print(dir(Random))

print(randint(1,6))
print(random())
 

# un petit jeu é tester :
print('voulez-vous jouer au dés (le temps dattente dun 6)? o/n')
r=input()
if r=='n':
    print('a plus ... alors')
else:
    d=0
    i=0
    while (d<6):
        print('lance le dé')
        input()
        d=randint(1,6)
        i+=1
        if d==6:
            print('tu as obtenu un ', d, ' en ', i,' etapes')
        else:
            print('tu as obtenu un ', d)
 
 
 
# question difficile é méditer (en prévision des proba !)
from random import *
from math import *
p=len([n for n in range(1000000) if hypot(random(),random())<1]) 
print(p/1000000*4) # ça ressemble à Pi ... non? un argument pour le justifier.

help(hypot)

# installer un module avec pip (compatible pyzo).... (inutile en TP !)
#pip install "le module"



##################################
# Quelques liens                 #
##################################  

#   pour la doc de python : http://docs.python.org/2/
#   pour la doc de pyzo :  http://www.pyzo.org
#   pour la doc de numpy et scipy : http://docs.scipy.org/doc/
#   pour la doc de matplot lib : http://matplotlib.org
#   Le livre  http://inforef.be/swi/download/apprendre_python3_5.pdf




##################################
# Un peu de 3D pour le fun       #
##################################  



## Un premier jet en 3D

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')

plt.show()
plt.savefig("D:/Nicolas/Informatique/Python/MPSI/TP/fig4.pdf")
## un autre exemple

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()
plt.savefig("D:/Nicolas/Informatique/Python/MPSI/TP/fig3.pdf")

    

##

# Classe custom pour faire en sorte que ^ soit un exposant

class Number(float):
    def __init__(self, value):
        self.v = value
    
    def __xor__(self, other):
        return self.v ** other


print(Number(2)^Number(4))
