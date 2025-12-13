import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide,
    square, sqrt, log, sin, cos, percent
)

def test_add():
    assert add(5, 6) == 11

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_square():
    assert square(4) == 16

def test_sqrt():
    assert sqrt(9) == 3

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_log():
    assert log(1) == pytest.approx(0.0)

def test_log_invalid():
    with pytest.raises(ValueError):
        log(0)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(10, 1)

def test_sin():
    assert sin(0) == pytest.approx(0.0)

def test_cos():
    assert cos(0) == pytest.approx(1.0)

def test_percent():
    assert percent(50) == 0.5
