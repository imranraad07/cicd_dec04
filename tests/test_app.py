import sys
from pathlib import Path


rt = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(rt / "src"))




from app import add, sub, mult, div, log, square, sin, cos, root, percent


def test_add():
    assert add(5, 6) == 11


def test_add2():
    assert add(5, 6) != 10


def test_sub():
    assert sub(5,6) == -1


def test_sub2():
    assert sub(5,6) != -2


def test_mult():
    assert mult(5,6) == 30


def test_mult2():
    assert mult(5,6) != 29


def test_div():
    assert div(5,6) == 0.833


def test_div2():
    assert div(5,6) != 1


def test_log():
    assert log(0) == "error"


def test_log2():
    assert log(1) == 0


def test_log3():
    assert log(1) != -1


def test_square():
    assert square(2) == 4


def test_square2():
    assert square(-2) == 4


def test_square3():
    assert square(-2) != -4


def test_sin():
    assert sin(0) == 0


def test_sin2():
    assert sin(30) == 0.5


def test_sin3():
    assert sin(-30) == -0.5


def test_sin4():
    assert sin(0) != 1


def test_cos():
    assert cos(0) == 1


def test_cos2():
    assert cos(60) == 0.5


def test_cos3():
    assert cos(-60) == 0.5


def test_cos4():
    assert cos(-60) != -0.5


def test_root():
    assert root(-1) == "error"


def test_root2():
    assert root(0) == 0


def test_root3():
    assert root(1) == 1


def test_root4():
    assert root(-1) != 0


def test_percent():
    assert percent(-1) == "error"


def test_percent2():
    assert percent(.1) == 10


def test_percent3():
    assert percent(1) == 100


def test_percent4():
    assert percent(2) == 200


def test_percent5():
    assert percent(2) != 100