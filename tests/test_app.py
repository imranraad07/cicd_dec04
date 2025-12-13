import sys
import pytest
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import *

def test_is_number():
    assert is_number(1)
    assert not is_number("1")

    assert is_number(1.5)
    assert not is_number("1.5")

def test_add():
    # A few basic examples
    assert add(5, 6) == 11
    assert add(6, 5) == 11

    # test non-numeric
    with pytest.raises(Exception) as e:
        add("a", "b")
    assert "Not a number" in str(e.value)

def test_sub():
    # A few basic examples
    assert sub(5, 6) == -1
    assert sub(6, 5) == 1

    # test non-numeric
    with pytest.raises(Exception) as e:
        sub("a", "b")
    assert "Not a number" in str(e.value)

def test_multiplication():
    # A few basic examples
    assert multiplication(5, 6) == 30
    assert multiplication(6, 5) == 30

    # test non-numeric
    with pytest.raises(Exception) as e:
        multiplication(3.1, "b")
    assert "Not a number" in str(e.value)

def test_division():
    # A few basic examples
    assert division(10, 2) == 5.0
    assert division(2, 10) == 0.2

    # divide by zero
    assert division(3.1, 0) == 0
    
    # test non-numeric
    with pytest.raises(Exception) as e:
        division(3.1, "b")
    assert "Not a number" in str(e.value)

def test_square():
    # A few basic examples
    assert square(2) == 4
    assert square(-2) == 4

    # test non-numeric
    with pytest.raises(Exception) as e:
        square("b")
    assert "Not a number" in str(e.value)

def test_square_root():
    # A few basic examples
    assert square_root(4) == 2

    # test non-numeric
    with pytest.raises(Exception) as e:
        square_root("b")
    assert "Not a number" in str(e.value)

    # test negative
    with pytest.raises(Exception) as e:
        square_root(-4)
    assert "No real answer" in str(e.value)

def test_sine():
    # A few basic examples
    assert sine(math.pi / 2) == pytest.approx(1)
    assert sine(math.pi) == pytest.approx(0)

    # test non-numeric
    with pytest.raises(Exception) as e:
        sine("b")
    assert "Not a number" in str(e.value)

def test_cosine():
    # A few basic examples
    assert cosine(math.pi / 2) == pytest.approx(0)
    assert cosine(math.pi) == pytest.approx(-1)

    # test non-numeric
    with pytest.raises(Exception) as e:
        cosine("b")
    assert "Not a number" in str(e.value)

def test_cosine():
    # A few basic examples
    assert cosine(math.pi / 2) == pytest.approx(0)
    assert cosine(math.pi) == pytest.approx(-1)

    # test non-numeric
    with pytest.raises(Exception) as e:
        cosine("b")
    assert "Not a number" in str(e.value)

def test_percentage():
    # A few basic examples
    assert percentage(10, 50) == pytest.approx(5)
    assert percentage(50, 50) == pytest.approx(25)

    # test non-numeric
    with pytest.raises(Exception) as e:
        percentage("b", 10)
    assert "Not a number" in str(e.value)

    with pytest.raises(Exception) as e:
        percentage(-1, 10)
    assert "No negative percentages" in str(e.value)

def test_log():
    # A few basic examples
    assert log(2, 4) == pytest.approx(2)

    # test non-numeric
    with pytest.raises(Exception) as e:
        log("b", 10)
    assert "Not a number" in str(e.value)

    with pytest.raises(Exception) as e:
        log(-1, 10)
    assert "Base and x cannot be negative" in str(e.value)

