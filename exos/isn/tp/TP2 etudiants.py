

##################################
# Premier point sur les variables#
##################################
## comment rajouter 1 à une variable?
i=10
s=0
def plus1(i):
    s=i+1
    return(s)

print(i)    
print(plus1(i))
print(s)

## la variable 's' est (dans le programme précédent) locale 

i=10
s=0
def pplus1(i):
    global s
    s=i+1
    return(s)

print(i)    
print(pplus1(i))
print(s)

## vers les effets de bords: 
#Définition : une fonction est dite à effet de bord lorsqu'elle modifie un état autre que sa valeur de retour. 

i=10
def ppplus1():
    i+=1
    return(i)
print(i)    
ppplus1()
print(i)
##
def ppplus1():
    global i
    i+=1
    return(i)
print(i)    
ppplus1()
print(i)
##

##################################
# Exercices sur les listes       #
##################################


### la concaténation de 2 listes:
l=[1,2,3]
l1=[4,5,6]

l2=l+l1
l3=l1+l

print(l2)
print(l3)   
    
    
###
# Exercice 1 : (L'aliasing) comprendre la différence entre les deux blocks suivants
##exemple 1:

a=[11,22,33] # a est affectée. Elle pointe vers une liste donnée
b=a # b point vers la même liste que a
a[0:3]=[17,42,561] # nous changeons le contenu de la liste vers qui pointe a
print(a,b) # b change également
print(id(a)==id(b))

##exemple 2:
a=[11,22,33]
b=a
a=[17,42,561]# a point vers une autre liste
print(a,b)
print(id(a)==id(b))


## un autre exemple:
    
a=[ i for i in range(10)]
b=a
print(a,b)
a[0]='a'
print(a,b)


## ou 

a=[ i for i in range(10)]
b=a
print(a,b)
b[0]='a'
print(a,b)
    
## ou 

a=[ i for i in range(10)]
b=a
print(a,b)
a=a+ [i for i in range(1,10)] # a point vers une autre liste
print(a,b)
    
    

## Exercice 2: Que valent a et b après les instructions suivantes?
# quelques exemples pour constater "la profondeur d'une liste". Une liste de listes de listes de listes....
a=[11,22,33]
b=[7,14,a]
print(b)
print(b[2][1]) # le 2eme élément du 3eme élément de b
b[2][1]=17 
print(b)
print(a)
a[0]=19
print(a,b)

    

    
## Tableau ou matrice :
    
a=[0,0]
b=[a,a]
print(b)
b[0][0]=3
print(b)
##
a=[0,0]
c=[0,0]
b=[a,c]
print(b)
b[0][0]=3
print(b)    
##
n=3
a=[0]*n
print(a)


c=[]
c=[a]*n
print(c)
# Quelle est la taille de la matrice c?
c[0][0]=1
print(c) # est-ce cohérent?

##

n=3
a=[0]
b=a*n
print(b)
a[0]=1
print(a,b)# est-ce cohérent?
# l'opérateur * a donc quelques avantages.



## une alternative:

c=[]
for i in range(n):
    c+=[[0]*n]
print(c)
c[0][0]=1
print(c) 

    
## la bonne question: comment faire une copie indépendante d'une liste (à utiliser sans hésitation !).... la copie profonde

import copy as c

a=[ i for i in range(10)]
b=c.deepcopy(a)  
print(a,b)
a[0]='test'
print(a,b)

## pourquoi une copie profonde ? tester les lignes suivantes 
import copy as c

a=[0,[1,2,3]]
b=c.copy(a)  
print(a,b)
a[0]=1
print(a,b)
a[1][0]='test'
print(a,b)
  

## Exercice 3 : Que fait la fonction suivante?

## Une fonction peut changer une liste que l'on appelle 


a=[ i for i in range(10)]
def f(l,x):
    l[0]=1
print(f(a,1)) # une action est effectuée mais laquelle?
print(a) # il y a eu une action sur a.

## comment éviter cela? Ne jamais travailler dans le corps d'une fonction sur une variable appelée.


a=[ i for i in range(10)]
def f(l,x):
    l0=c.deepcopy(l)
    l0[0]=1
    return(l0)
print(f(a,1)) # une action est effectuée mais laquelle?
print(a) # il y a eu une action sur a.

## Que font les fonctions suivantes?


def f(l,i,j):
    l[i]=l[i]+l[j]
    l[j]=l[i]-l[j]
    l[i]=l[i]-l[j]
 
a=[ i for i in range(10)]   
f(a,0,1)
print(a)
##
def g(i,j):
    l[i]=l[i]+l[j]
    l[j]=l[i]-l[j]
    l[i]=l[i]-l[j]
    
l=[0,1,2,3]
print(l)
g(0,1)  
print(l)
# Attention aux effets de bords ! 
# Définition : une fonction est dite à effet de bord lorsqu'elle modifie un état autre que sa valeur de retour.  


## Exercice 4: Concaténation
# y-a-t-il une différence ?

a=[2,3,4,6]
print(id(a))
a=a+[2]
print(id(a)) # en rajoutant 2 ... ce n'est plus la même liste.

# comment conserver la même liste ?
a=[2,3,4,6]
print(id(a))
a.append(2)
print(id(a))

# nous l'utiliserons dans le TP sur les piles.


## Exercice 5: Insertion /Suppression
# Que font les fonctions suivantes?
help(range)
help(list)
# toujours penser à utiliser l'aide !

a=list(range(20))
print(a)
a.insert(2, 18)
print(a)

a=list(range(20))
print(a)

del a[3]
print(a)

del a[2:4]
print(a)

a=[1,1,2,2,3,3,4,4,5,5,6,6]
print(a)

## Attention aux effets de bords ! (vers les piles )

a=[1,1,2,2,3,3,4,4,5,5,6,6]
print(a)

print(a.pop())
print(a)
for i in range(3):
    a.pop()
print(a)


print(a.pop(3))
print(a)

a.remove(4)
print(a)


## tester sur les listes les fonctions: sorted, min, max , sum 
a=[]
n=10
a=[n-i**2 for i in range(n)]
print(a)
print(sorted(a), min(a), max(a), sum(a))



##################################
# 2 - Itérations                 #
##################################

#En Python, un objet est dit itérable lorsqu'il est possible de renvoyer un par un tous ses éléments. la syntaxe: "for x in l", la variable x prend successivement toutes les valeurs des éléments de l.
# Les objets itérables: les listes, les chaînes de caractères, les tuples, les "range", les ensembles, les dictionnaires.

l=['a','b', 'c']
s=range(len(l))
print(s)

## on peut écrire
for i in s: 
    print(l[i])

##On prefère
for lettre in l: 
    print(lettre)
   
   
##     

texte="vous avez de la chance!"
for lettre in texte:
    print(lettre)   
   
    
##un autre exemple: calcul de la norme de vecteurs de R2
from math import sqrt # la racine carrée 

vecteurs= [(0,1),(2,2),(2,3)]
for vect in vecteurs:
    norme=sqrt(vect[0]^2+vect[1]^2)
    print('norme=',norme)
   
# Ou sinon
vecteurs= [(0,1),(2,2),(2,3)]
for (x,y) in vecteurs:
    norme=sqrt(x^2+y^2)
    print('norme=',norme)
    
    
    
# LES EXERCICES A TRAITER. 
    
####################################################################
# Exercice 1: Ecrire un fonction "mini" qui renvoie le plus petit élément d'un liste.
#La tester sur une liste de couples, une chaîne de caractères.
####################################################################

####################################################################
# Exercice 2: Ecrire une fonction "bis" qui prend une chaîne de caractères et renvoie une chaîne avec chaque caractère 2 fois de suite
####################################################################


# Itérations avancées: Tester les blocks suivants (reverse , enumerate, zip,...)

l=[1,2,'a','b',4,'test']
l1=reversed(l)   
print(l,l1)
l1=list(l1)
print(l,l1)



####################################################################
# Exercice 3: Ecrire une fonction qui à une liste renvoie la liste renversée (sans utiliser "reversed")
####################################################################

# Enumerate : enumerate(l) est un itérateur paresseux qui renvoie les couples i, l[i](pour i variant de 0 à len(l)-1)

s='un test facile'
for c in enumerate(s):
    print(c)

for (i,x) in enumerate(s):
    print(x)

for (i,x) in enumerate(s):
    print(x,end='')
print()

####################################################################
# Exercice 4: Ecrire une fonction minind(l) qui renvoie le couple contenant le minimum de l et la liste des indices associées.
####################################################################


# l'itérateur zip

lettre=['a','b','c']
nbr=[1,2,3,4,5]

for x in zip(lettre, nbr):
    print(x)

####################################################################
# Exercice 5: 
#Ecrire une fonction moycoef(notes, coefs) qui prend une liste de notes et une liste de coefficients et renvoie la moyenne pondérée.
####################################################################

def moycoef(notes, coefs):
    total = 0
    for n, c in zip(notes, coefs):
        total += n*c
    return total/sum(coefs)

##################################
# Boucle While                   #
##################################

## premiers pas ....

i=0
while (i<10):
    i+=1
    print(i)
##    
i=1
u=1
while (u>10**(-5)):
    i+=1
    u/=10
print(i,u)
## le compteur i 
i=0
u=1.
while (u>10**(-5)):
    i+=1
    u/=2.
    
print(u,i)
print(i)
from math import *
print(floor((5*log(10)/log(2)))+1)

##Pourquoi la valeur finale de i est-elle égale à la partie entière +1 de 5*log_2(10) ?

"""

 - floor parce que i est un entier
 - +1 parce que c'est le nombre d'itérations
 - 

"""

## un jeu de dé: 

from random import *

print(dir(Random))

print(randint(1,6))
print(random())
 

## un petit jeu
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
            print('tu as obtenu un ', d, ' en ', i,' étapes')
        else:
            print('tu as obtenu un ', d)
 


##################################
# 3 - Compréhension              #
##################################
## Python permet de définir facilement des listes par «compréhension»

l=[3*i**2 + 1 for i in range(1,10)]
print(l)

l=[(i,j) for i in range(4) for j in range(i)]
print(l)

l=[[(i,j) for i in range(2)] for j in range(i)]
print(l)

l=[[(i,j) for j in range(i)] for i in range(2)]
print(l)


## On peut également filtrer 

l=[i for i in range(10) if i%2]
print(l)

l=[i if i%3 else 0 for i in range(10)]
print(l)

# Comment comprendre %2 ?
#il faut comprendre "if i%3" comme "if i%3 == 0". 
#En Python, toutes les valeurs sont comprises comme vrai sauf
#• la constante False
#• la constante None 
#•0
#• la liste vide []
#• le tuple vide ()
#• l’ensemble vide set() 
#• le dictionnaire vide {}

####################################################################
# Exercice 6:
    # -Ecrire une fonction imp(n) qui renvoie la liste des nombres impairs inférieur à n
    # -Calculer la somme des i**2 pour i inférieur à 100
    # -Déterminer la somme des i**j pour i, j vérifiant 0<i<=j<101
####################################################################    

def imp(n):
    return [ n for n in range(n) if n % 2 != 0 ]
    
print(sum([ i**2 for i in range(100) ]))


_ = []
for j in range(0, 101):
    for i in range(0, j+1):
        _.append(i**j)

print(sum(_))
     

##################################
# 4 - Exercices                  #
##################################

####################################################################
# Exercice 7: Ecrire une fonction qui à x et n renvoie x**n sans utiliser "**"
# Exercice 8: Ecrire des fonctions renvoyant la somme des éléments d'une liste et son maximum.
# Exercice 9: Ecrire une fonction calculant le n ième terme d'une suite arithmético-géométrique vérifiant u[n+1]=au[n]+b
# Exercice 10: Ecrire une fonction qui permet de savoir si un mot est dans une phrase.
####################################################################

def pow(x, n):
    for _ in range(n):
        x *= x
    return x

def sum(L):
    sum = 0
    for item in L:
        sum += item
    return sum
    
def max(L):
    if not len(L):
        raise ValueError("L must not be empty")
    
    max = 0
    for item in L:
        if item > max:
            max = item
        

def u(n, u_0, a, b):
    u = u_0
    for _ in range(n+1):
        u = a*u+b
        
    return u


def suite_arithmético_géométrique(u_0, a, b):
    def u(n):
        u = u_0
        for _ in range(n+1):
            u = a*u+b
        return u
    return u

u1 = suite_arithmético_géométrique(u_0=2, a=4, b=5)

print(u1(4))


def word_in_sentence(sentence, word):
    searched_word = word
    for word in sentence.split(" "):
        if word == searched_word:
            return True
            
    return False
