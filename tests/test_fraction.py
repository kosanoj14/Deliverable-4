import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.fraction import Fraction


def test_equal():
    """Test that equivalent fractions are equal."""
    assert Fraction(1, 2) == Fraction(2, 4)


def test_not_equal():
    """Test that different fractions are not equal."""
    assert Fraction(1, 2) != Fraction(1, 3)


def test_less_than():
    """Test less-than comparison between fractions."""
    assert Fraction(1, 3) < Fraction(1, 2)


def test_greater_than():
    """Test greater-than comparison between fractions."""
    assert Fraction(1, 1) > Fraction(1, 2)


def test_less_than_or_equal():
    """Test less-than-or-equal comparison."""
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)


def test_greater_than_or_equal():
    """Test greater-than-or-equal comparison."""
    assert Fraction(1, 1) >= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)


def test_add():
    """Test addition of two fractions."""
    assert Fraction(1, 2) + Fraction(1, 2) == Fraction(1, 1)


def test_sub():
    """Test subtraction of two fractions."""
    assert Fraction(1, 2) - Fraction(1, 4) == Fraction(1, 4)


def test_truediv():
    """Test division of two fractions."""
    assert Fraction(1, 1) / Fraction(1, 2) == Fraction(2, 1)


def test_mul():
    """Test multiplication of two fractions."""
    assert Fraction(2, 4) * Fraction(3, 2) == Fraction(3, 4)


def test_negative_denominator():
    """Test that a negative denominator raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(2, -3)


def test_float():
    """Test that float inputs raise TypeError."""
    with pytest.raises(TypeError):
        Fraction(0.2, 3)

    with pytest.raises(TypeError):
        Fraction(2, 0.3)


def test_zero_denominator():
    """Test that a zero denominator raises ValueError."""
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_zero_division():
    """Test that division by a zero fraction raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)


def test_division_by_negative_fraction():
    """Test division by a negative fraction."""
    assert Fraction(1, 2) / Fraction(-3, 4) == Fraction(-2, 3)
