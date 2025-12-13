import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mul, div, log, square, sin, cos, sqrt, percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(6, 5) == 1

def test_mul():
    assert mul(5, 6) == 30

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)

def test_log():
    assert log(1) == 0

def test_log_error():
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-1)

def test_square():
    assert square(5) == 25

def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(0) == 1

def test_sqrt():
    assert sqrt(4) == 2

def test_sqrt_error():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_percentage():
    assert percentage(10, 100) == 10