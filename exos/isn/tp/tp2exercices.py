from math import *
from turtle import *

## Raccourcis

fw = forward
l = left
rst = reset

## Exo 1


def sq(size):
    for _ in range(4):
        fw(size)
        l(90)

rst()

## Exo 3

def exo3():
    for i in range(10):
        sq(i+1)

rst()

## Exo 4

def exo4():
    for i in range(1, 501):
        fw(i)
        l(91)

rst()

## Exo 5

def poly(sides, size):
    angle = 360 / sides
    for i in range(sides):
        fw(size)
        left(angle)

## Exo 6

def satan():
    circle(10, steps=3)
    circle(-10, steps=6)

## Exo 7

def exo7():
    for i in range(72):
        circle(50)
        fw(10)

exo7()



input()


