#https://github.com/carlosrabah/lab11-CR-TC.git
#Partner 1: Carlos Rabah
#Partner 2: Tyler Jin Choe

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b