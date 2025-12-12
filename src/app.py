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
        print(f"You tried to divide by zero:")

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

if __name__ == "__main__":
    print(add("5.1", 1.9))