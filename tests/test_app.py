import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide,
    log, square, sin, cos,
    square_root, percentage
)

def test_add():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-3, -7) == -10

def test_add2():
    assert add(5, 6) != 10


def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2


def test_multiply():
    assert multiply(7, 6) == 42

def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(12, 4) == 3

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_log_default_base_e():
    assert math.isclose(log(math.e), 1.0)

def test_log_custom_base():
    assert math.isclose(log(100, 10), 2.0)

def test_log_negative():
    with pytest.raises(ValueError):
        log(-5)

def test_log_zero():
    with pytest.raises(ValueError):
        log(0)


def test_square():
    assert square(5) == 25

def test_square_negative():
    assert square(-4) == 16


def test_sin_zero():
    assert math.isclose(sin(0), 0.0)

def test_cos_zero():
    assert math.isclose(cos(0), 1.0)


def test_square_root():
    assert square_root(25) == 5

def test_square_root_zero():
    assert square_root(0) == 0

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-9)


def test_percentage():
    assert percentage(25, 100) == 25

def test_percentage_zero_whole():
    with pytest.raises(ValueError):
        percentage(5, 0)

def test_percentage_edge_small_numbers():
    assert percentage(1, 1000) == 0.1
