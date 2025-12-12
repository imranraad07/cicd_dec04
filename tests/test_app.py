import math
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src import app


def test_addition():
    assert app.add(2, 3) == 5
    assert app.add(-1, -4) == -5


def test_subtraction():
    assert app.sub(10, 4) == 6
    assert app.sub(-3, -2) == -1


def test_multiplication():
    assert app.mul(3, 5) == 15
    assert app.mul(-2, 4) == -8


def test_division():
    assert app.div(10, 2) == 5
    with pytest.raises(ValueError):
        app.div(1, 0)


def test_logarithm():
    assert app.log(math.e) == pytest.approx(1)
    assert app.log(100, 10) == pytest.approx(2)
    with pytest.raises(ValueError):
        app.log(0)
    with pytest.raises(ValueError):
        app.log(10, 1)
    with pytest.raises(ValueError):
        app.log(10, -2)


def test_square_and_square_root():
    assert app.square(4) == 16
    assert app.square(-3) == 9
    assert app.sqrt(9) == 3
    assert app.sqrt(0) == 0
    with pytest.raises(ValueError):
        app.sqrt(-1)


def test_trigonometry():
    assert app.sin(math.pi / 2) == pytest.approx(1)
    assert app.cos(math.pi) == pytest.approx(-1)


def test_percentage():
    assert app.percentage(50, 200) == 25
    assert app.percentage(-5, 10) == -50
    with pytest.raises(ValueError):
        app.percentage(1, 0)
