import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def log(x, base=math.e):
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log(x, base)

def square(x):
    return x * x

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Cannot compute percentage of zero.")
    return (part / whole) * 100
