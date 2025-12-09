import math
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import (
    add,
    cos,
    divide,
    log,
    multiply,
    percentage,  # type: ignore
    sin,
    sqrt,
    square,
    sub,
)


def test_add():
    assert add(5, 6) == 11
    assert add("5", "6") is None


def test_sub():
    assert sub(5, 6) == -1
    assert sub("5", "6") is None


def test_multiply():
    assert multiply(5, 6) == 30
    assert multiply("5", "6") is None


def test_divide():
    assert divide(5, 6) == 5 / 6
    assert divide("5", "6") is None
    assert divide(5, 0) is None


def test_log():
    assert log(5) == math.log(5)
    assert log("5") is None
    assert log(0) is None


def test_square():
    assert square(5) == 25
    assert square("5") is None


def test_sin():
    assert sin(5) == math.sin(5)
    assert sin("5") is None


def test_cos():
    assert cos(5) == math.cos(5)
    assert cos("5") is None


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt("4") is None
    assert sqrt(0) == 0
    assert sqrt(-1) is None


def test_percentage():
    assert percentage(5, 8) == 62.5
    assert percentage("5", "8") is None
    assert percentage(5, 0) is None
