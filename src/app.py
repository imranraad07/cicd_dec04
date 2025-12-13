import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul (a, b):
    return a*b

def div (a, b):
    return a/b

def log (a, base):
    return math.log(a, base)

def square (a):
    return a**2

def sin (a):
    return math.sin(a)

def cos (a):
    return math.cos(a)

def sqrt (a):
    try:
        return math.sqrt(a)
    except ValueError:
        return float("nan")

def percentage (a):
    return a/100
