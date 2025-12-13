import sys
from pathlib import Path
import math
import pytest

# import-time logic (needs coverage)
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, multiply, divide, log, square, sin, cos, sqrt, percentage


def test_add():
    assert add(5, 6) == 11


def test_add2():
    assert add(5, 6) != 10


def test_subtract():
    assert sub(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(8, 2) == 4


def test_divide_float():
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_square():
    assert square(5) == 25


def test_sqrt():
    assert sqrt(9) == 3


def test_sqrt_zero():
    assert sqrt(0) == 0


def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-4)


def test_log():
    assert math.isclose(log(math.e), math.log10(math.e))


def test_log_one():
    assert math.isclose(log(1), 0.0)


def test_log_zero():
    with pytest.raises(ValueError):
        log(0)


def test_log_negative():
    with pytest.raises(ValueError):
        log(-10)


def test_sin():
    assert math.isclose(sin(0), 0.0)


def test_cos():
    assert math.isclose(cos(0), 1.0)


def test_percentage():
    assert percentage(25, 100) == 0.25


def test_percentage_zero_numerator():
    with pytest.raises(ValueError):
        percentage(0, 100)


def test_percentage_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        percentage(10, 0)
