from typing import Optional, Any
import math

Numerical = int | float


def add(a: Numerical, b: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a, b):
        return None
    return a + b


def sub(a: Numerical, b: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a, b):
        return None
    return a - b


def multiply(a: Numerical, b: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a, b):
        return None
    return a * b


def divide(a: Numerical, b: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a, b) or b == 0:
        return None
    return a / b


def log(a: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a) or a <= 0:
        return None
    return math.log(a)


def square(a: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a):
        return None
    return a**2


def sin(a: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a):
        return None
    return math.sin(a)


def cos(a: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a):
        return None
    return math.cos(a)


def sqrt(a: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a) or a < 0:
        return None
    return math.sqrt(a)


def percentage(a: Numerical, b: Numerical) -> Optional[Numerical]:
    if not _are_numerical(a, b) or a < 0 or b <= 0:
        return None
    return 100 * a / b


def _are_numerical(*args) -> bool:
    def _is_numerical(v: Any) -> bool:
        return isinstance(v, int) or isinstance(v, float)

    for v in args:
        if not _is_numerical(v):
            return False
    return True
