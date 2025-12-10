import math

# Basic Operations
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

# Advanced Operations
def square(a):
    return a ** 2

def square_root(a):
    if a < 0:
        return None
    return math.sqrt(a)

def log(a):
    if a <= 0:
        return None
    return math.log(a)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def percentage(a, b):
    if b == 0:
        return None
    return (a / b) * 100