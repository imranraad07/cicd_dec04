
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def square(a):
    return a * a

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def log(a):
    if a <= 0:
        raise ValueError("Log undefined for zero or negative values")
    return math.log(a)

def percentage(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero in percentage")
    return (a / b) * 100

