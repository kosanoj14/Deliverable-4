import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.fraction import Fraction

def test_equal():
    assert Fraction(1,2) == Fraction(2, 4)

def test_not_equal():
    assert Fraction(20) != Fraction(30)

def test_less_than():
    assert Fraction(20) < Fraction(30)

def test_greater_than():
    assert Fraction(30) > Fraction(20)

def test_add():
    assert (Fraction(20) + Fraction(10)) == 30