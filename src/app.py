import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def multiply (a, b):
    return a*b

def divide (a, b):
    if b == 0:
        raise ValueError("can't divide by 0")
    return a / b

#advanced

def square (x):
    return x*x

def sqrt (x):
    if x < 0:
        raise ValueError("can't sqrt negative number")
    return math.sqrt(x)

def log (x):
    if x <= 0:
        raise ValueError("log is undefined for 0 or neg numbers")
    return math.log(x)

def sin (x):
    return math.sin(x)

def cos (x):
    return math.cos(x)

def percentage (x):
    return x / 100