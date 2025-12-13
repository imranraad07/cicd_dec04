import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mul (a, b):
    return a*b

def div (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def log(a):
    if a <= 0:
        raise ValueError("Cannot take log of non-positive number")
    return math.log(a)

def square(a):
    return a*a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def percentage(a, b):
    return (a/b) * 100
