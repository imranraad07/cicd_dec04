import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def square(a):
    return a ** 2

def sqrt(a):
    if a < 0:
        raise ValueError("Square root of negative number")
    return math.sqrt(a)

def log(a):
    if a <= 0:
        raise ValueError("Logarithm of non-positive number")
    return math.log(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def percentage(value, percent):
    return (value * percent) / 100
