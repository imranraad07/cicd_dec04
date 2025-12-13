import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (add, sub, mul, div,
    square, sqrt, sin, cos,
    log, percentage
)

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(3, 7) == 21

def test_div():
    assert div(12, 3) == 4

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)




# ----------------MORE ADVANCED FUNCTIONS ----------------


def test_square():
    assert square(5) == 25

def test_sqrt():
    assert sqrt(16) == 4

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-4)

def test_sin_90():
    # Should be 1 (within numerical tolerance)
    assert abs(sin(90) - 1) < 1e-6

def test_cos_0():
    assert abs(cos(0) - 1) < 1e-6

def test_log():
    assert log(1) == 0

def test_log_invalid():
    with pytest.raises(ValueError):
        log(0)

def test_percentage():
    assert percentage(50, 100) == 50

def test_percentage_zero():
    with pytest.raises(ZeroDivisionError):
        percentage(5, 0)
