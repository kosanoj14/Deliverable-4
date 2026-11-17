import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.fraction import Fraction


def test_equal():
    assert Fraction(1,2) == Fraction(2, 4)

def test_not_equal():
    assert Fraction(1, 2) != Fraction(1, 3)

def test_less_than():
    assert Fraction(1, 3) < Fraction(1, 2)

def test_greater_than():
    assert Fraction(1, 1) > Fraction(1, 2)

def test_less_and_equal_than():
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)

def test_greater_and_equal_than():
    assert Fraction(1, 1) >= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)

def test_add():
    assert (Fraction(1, 2) + Fraction(1, 2)) == Fraction(1, 1)

def test_sub():
    assert (Fraction(1, 2) - Fraction(1, 4)) == Fraction(1, 4)

def test_truediv():
    assert (Fraction(1, 1) / Fraction(1, 2)) == Fraction(2, 1)

def test_mul():
    assert (Fraction(2, 4) * Fraction(3, 2)) == Fraction(3, 4)

def test_negativ_denominator():
    with pytest.raises(ValueError):
        (Fraction(2, -3))

def test_float():
    with pytest.raises(TypeError):
        (Fraction(0.2, 3))
    with pytest.raises(TypeError):
        Fraction(2, 0.3)

def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)


def test_division_by_negative_fraction():
    assert Fraction(1, 2) / Fraction(-3, 4) == Fraction(-2, 3)