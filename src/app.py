import math

def is_number(x) -> bool:
    numbers = set([int, float])
    return type(x) in numbers

def add (a, b):
    if not (is_number(a) and is_number(b)):
        raise Exception("Not a number")
    return a+b

def sub (a, b):
    if not (is_number(a) and is_number(b)):
        raise Exception("Not a number")
    return a-b

def multiplication(a, b):
    if not (is_number(a) and is_number(b)):
        raise Exception("Not a number")
    return a * b

def division(a, b):
    if not (is_number(a) and is_number(b)):
        raise Exception("Not a number")
    try:
        return a / b
    except ZeroDivisionError as e:
        return 0

def square(a):
    if not is_number(a):
        raise Exception("Not a number")
    return a * a

def square_root(a):
    if not is_number(a):
        raise Exception("Not a number")
    if a < 0:
        raise Exception("No real answer")
    return math.sqrt(a)

def sine(a):
    if not is_number(a):
        raise Exception("Not a number")
    return math.sin(a)

def cosine(a):
    if not is_number(a):
        raise Exception("Not a number")
    return math.cos(a)

def percentage(a, b):
    """
    Return a% of b
    """
    if not (is_number(a) and is_number(b)):
        raise Exception("Not a number")
    if a < 0:
        raise Exception("No negative percentages")
    return (a / 100) * b

def log(base, x):
    if not (is_number(base) and is_number(x)):
        raise Exception("Not a number")    
    if x < 0 or base <= 0:
        raise Exception("Base and x cannot be negative")
    return math.log(x, base)
