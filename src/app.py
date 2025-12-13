import math


def add (a, b):
    return a+b


def sub (a, b):
    return a-b


def mult (a, b):
    return a*b


def div (a, b):
    if (b == 0):
        raise ValueError("Error: Division by Zero")
    return round(a/b, 3)


def log (a , base = 10):
    if (a <= 0):
        raise ValueError("Error: Logs aren't 0 or negative")
    return round(math.log(a, base), 3)


def square (a):
    return a*a


#Using degrees
def sin (a):
    return round(math.sin(math.radians(a)), 3)


def cos (a):
    return round(math.cos(math.radians(a)), 3)


def root (a):
    if (a < 0):
        raise ValueError("Error: Roots aren't negative")
    return round(math.sqrt(a), 3)


def percent(a):
    if (a < 0):
        raise ValueError("Error: Percents aren't negative")
    return a*100
