import math

#Comment to trigger changes

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a * b

def div (a, b):
    if b == 0:
        return "undef"
    return a / b

def log (base, a):
    if a < 0:
        return "undef"
    if a == 0:
        return "undef"
    if base < 0:
        return "undef"
    if base == 0:
        return "undef"
    if base == 1:
        return "undef"
    
    return math.log(a) / math.log(base)

def square(a):
    return mult(a, a)

def sin(a):
    return math.sin(a)

def sqrt(a):
    if(a < 0):
        return "undef"
    return math.sqrt(a)

def percentage(a):
    return mult(a, 100)