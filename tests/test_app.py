import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add,
    sub,
    multiply,
    divide,
    square,
    sqrt,
    log,
    sin,
    cos,
    percentage,
)

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

#advanced

def test_square():
    assert square(5) == 25


def test_sqrt():
    assert sqrt(9) == 3


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-4)


def test_log():
    assert log(math.e) == pytest.approx(1.0)


def test_log_zero():
    with pytest.raises(ValueError):
        log(0)


def test_log_negative():
    with pytest.raises(ValueError):
        log(-1)


def test_sin():
    assert sin(0) == 0


def test_cos():
    assert cos(0) == 1


def test_percentage():
    assert percentage(50) == 0.5