import math
import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add, sub, mult, div,
    log, square, sin, cos,
    sqrt, percent
)

def test_add1():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10


def test_sub1():
    assert sub(10, 4) == 6

def test_sub2():
    assert sub(-5, 3) == -8


def test_mult1():
    assert mult(3, 4) == 12

def test_mult2():
    assert mult(0, 99) == 0


def test_div1():
    assert div(10, 2) == 5

def test_div2():
    assert div(7, 2) == 3.5

def test_div3():
    with pytest.raises(ValueError):
        div(5, 0)


# -------------------
# ADVANCED OPERATIONS
# -------------------

def test_log1():
    assert log(10, 100) == 2

def test_log2():
    assert log(math.e, math.e**3) == 3

def test_log3():
    with pytest.raises(ValueError):
        log(10, 0)

def test_log4():
    with pytest.raises(ValueError):
        log(-2, 10)

def test_log5():
    with pytest.raises(ValueError):
        log(1, 10)


def test_square1():
    assert square(5) == 25

def test_square2():
    assert square(-4) == 16


def test_sin1():
    assert sin(0) == 0


def test_cos1():
    assert cos(0) == 1


def test_sqrt1():
    assert sqrt(9) == 3

def test_sqrt2():
    assert sqrt(0) == 0

def test_sqrt3():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_percent1():
    assert percent(0.25) == 25

def test_percent2():
    assert percent(-0.5) == -50