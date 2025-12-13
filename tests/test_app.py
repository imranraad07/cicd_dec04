import sys
import pytest
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mul, div, square, sqrt, log, sin, cos, percentage

def test_add():
    assert add(5, 6) == 11
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(10, 5) == 5
    assert sub(5, 10) == -5
    assert sub(0, 0) == 0

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6
    assert mul(0, 5) == 0

def test_div():
    assert div(10, 2) == 5
    assert div(5, 2) == 2.5
    assert div(-10, 2) == -5

def test_div_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        div(10, 0)

def test_square():
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0

def test_sqrt():
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(4) == 2

def test_sqrt_negative():
    with pytest.raises(ValueError, match="Square root of negative number"):
        sqrt(-1)

def test_log():
    assert log(1) == 0
    assert log(math.e) == 1

def test_log_non_positive():
    with pytest.raises(ValueError, match="Logarithm of non-positive number"):
        log(0)
    with pytest.raises(ValueError, match="Logarithm of non-positive number"):
        log(-1)

def test_sin():
    assert sin(0) == 0
    assert sin(math.pi / 2) == 1

def test_cos():
    assert cos(0) == 1
    assert cos(math.pi) == -1

def test_percentage():
    assert percentage(100, 10) == 10
    assert percentage(200, 50) == 100
    assert percentage(0, 100) == 0