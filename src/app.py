import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def log(value, base=math.e):
    if value <= 0:
        raise ValueError("Logarithm is undefined for non-positive values.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(value, base)


def square(value):
    return value * value


def sqrt(value):
    if value < 0:
        raise ValueError("Square root is undefined for negative values.")
    return math.sqrt(value)


def sin(radians):
    return math.sin(radians)


def cos(radians):
    return math.cos(radians)


def percentage(part, whole):
    if whole == 0:
        raise ValueError("Cannot compute percentage with a zero denominator.")
    return (part / whole) * 100
