import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3),
    (-1, 5, 4),
    (100, 200, 300)
])
def test_add(a, b, result):
    assert calc.add(a, b) == result


@pytest.mark.parametrize("a, b, result", [
    (5, 3, 2),
    (3, 5, -2),
    (10, 10, 0)
])
def test_subtract(a, b, result):
    assert calc.subtract(a, b) == result


@pytest.mark.parametrize("a, b, result", [
    (2, 3, 6),
    (-1, 5, -5),
    (10, 0, 0)
])
def test_multiply(a, b, result):
    assert calc.multiply(a, b) == result


def test_divide_valid():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (0, False),
])
def test_is_prime(n, expected):
    assert calc.is_prime(n) == expected
