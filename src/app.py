# src/app.py
import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def square(x): return x * x

def sqrt(x):
    if x < 0:
        raise ValueError("Square root undefined for negative numbers")
    return math.sqrt(x)

def log(x, base=math.e):
    if x <= 0:
        raise ValueError("Log undefined for x <= 0")
    if base <= 0 or base == 1:
        raise ValueError("Log base must be > 0 and != 1")
    return math.log(x, base)

def sin(x): return math.sin(x)
def cos(x): return math.cos(x)
def percent(x): return x / 100.0
