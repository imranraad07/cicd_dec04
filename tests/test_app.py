import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add

def test_add_pos_pos():
    assert add(5, 6) == 11

def test_add_neg_pos():
    assert add(-8, 3) == -5

def test_add_neg_neg():
    assert add(-4, -5) == -9

def test_add_double_nan():
    assert math.isnan(add(float("nan"), float("nan")))

def test_add_nan():
    for i in range(-100, 100):
        assert math.isnan(add(i, float("nan")))
        assert math.isnan(add(float("nan"), i))

def test_add_inverse():
    for i in range(-100, 100):
        assert add(i, -i) == 0

def test_add_commutative():
    for i in range(-100, 100):
        for j in range(-100, 100):
            assert add(i, j) == add(j, i)

def test_add_identity():
    for i in range(-100, 100):
        assert add(i, 0) == add(0, i)
        assert add(i, 0) == i


