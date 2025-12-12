import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def log(base, x):
    if x <= 0:
        raise ValueError("Logarithm undefined for x <= 0.")
    if base <= 0:
        raise ValueError("Logarithm base must be positive.")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1.")
    return math.log(x, base)

def square(x):
    return x * x

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def sqrt(x):
    if x < 0:
        raise ValueError("Square root undefined for negative numbers.")
    return math.sqrt(x)

def percent(x):
    return x * 100
