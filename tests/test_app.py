import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, multiply, divide, square, square_root, log, sin, cos, percentage

# ===== BASIC OPERATIONS TESTS =====

# Addition Tests
def test_add():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -6) == -11

# Subtraction Tests
def test_sub():
    assert sub(10, 5) == 5

def test_sub_negative():
    assert sub(5, 10) == -5

# Multiplication Tests
def test_multiply():
    assert multiply(5, 6) == 30

def test_multiply_zero():
    assert multiply(5, 0) == 0

# Division Tests
def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) is None

# ===== ADVANCED OPERATIONS TESTS =====

# Square Tests
def test_square():
    assert square(5) == 25

def test_square_negative():
    assert square(-5) == 25

# Square Root Tests
def test_square_root():
    assert square_root(25) == 5

def test_square_root_negative():
    assert square_root(-5) is None

# Logarithm Tests
def test_log():
    assert abs(log(math.e) - 1.0) < 0.0001

def test_log_zero():
    assert log(0) is None

def test_log_negative():
    assert log(-5) is None

# Sin Tests
def test_sin():
    assert abs(sin(0) - 0) < 0.0001

def test_sin_pi():
    assert abs(sin(math.pi / 2) - 1.0) < 0.0001

# Cos Tests
def test_cos():
    assert abs(cos(0) - 1.0) < 0.0001

def test_cos_pi():
    assert abs(cos(math.pi) - (-1.0)) < 0.0001

# Percentage Tests
def test_percentage():
    assert percentage(50, 100) == 50.0

def test_percentage_zero_denominator():
    assert percentage(50, 0) is None