import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.temp_converter import Temperature

def test_explicit_magic_methods():
    """Test using explicit dunder methods like __eq__, __lt__, etc. instead of operators."""
    t_c = Temperature(0, "C")
    t_f = Temperature(32, "F")
    t_hot = Temperature(100, "C")

    # Tester __eq__ og __ne__ direkte
    assert t_c.__eq__(t_f) is True
    assert t_c.__ne__(t_f) is False

    # Tester __lt__ og __le__ direkte
    assert t_c.__lt__(t_hot) is True
    assert t_c.__le__(t_f) is True

    # Tester __gt__ og __ge__ direkte
    assert t_hot.__gt__(t_c) is True
    assert t_f.__ge__(t_c) is True

    # Eksempel på ugyldig sammenligning som skal returnere NotImplemented
    assert t_c.__eq__(5) is NotImplemented
    
def test_abs_zero():
    """Test temperature conversions at absolute zero."""
    temp_c = Temperature(-273.15, "C")
    temp_k = Temperature(0, "K")
    temp_f = Temperature(-459.67, "F")

    assert temp_c.to_kelvin() == pytest.approx(0, abs=1e-9, rel=0)
    assert temp_k.to_fahrenheit() == pytest.approx(-459.67, abs=1e-9, rel=0)
    assert temp_f.to_celsius() == pytest.approx(-273.15, abs=1e-9, rel=0)


def test_below_abs_zero():
    """Test that temperatures below absolute zero raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(-300, "C")

    with pytest.raises(ValueError):
        Temperature(-2, "K")

    with pytest.raises(ValueError):
        Temperature(-500, "F")


def test_celsius():
    """Test conversion to Celsius."""
    temp_f = Temperature(32, "F")
    temp_k = Temperature(273.15, "K")

    assert temp_f.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)
    assert temp_k.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)


def test_fahrenheit():
    """Test conversion to Fahrenheit."""
    temp_c = Temperature(-40, "C")
    temp_k = Temperature(233.15, "K")

    assert temp_c.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)
    assert temp_k.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)


def test_kelvin():
    """Test conversion to Kelvin."""
    temp_c = Temperature(37, "C")
    temp_f = Temperature(98.6, "F")

    assert temp_c.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)
    assert temp_f.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)


def test_converter():
    """Test conversion between all supported temperature units."""
    original = Temperature(100, "C")

    temp_f = original.convert_to("F")
    temp_k = temp_f.convert_to("K")
    temp_c = temp_k.convert_to("C")

    assert temp_f.unit == "F"
    assert temp_f.temp == pytest.approx(212, abs=1e-9, rel=0)

    assert temp_k.unit == "K"
    assert temp_k.temp == pytest.approx(373.15, abs=1e-9, rel=0)

    assert temp_c.unit == "C"
    assert temp_c.temp == pytest.approx(original.temp, abs=1e-9, rel=0)
    assert temp_c == original


def test_default_unit():
    """Test that Celsius is used as the default unit."""
    temperature = Temperature(25)

    assert temperature.temp == 25
    assert temperature.unit == "C"


def test_case_insensitive_unit():
    """Test that unit names are case-insensitive."""
    temperature = Temperature(25, "c")

    assert temperature.unit == "C"
    assert temperature.temp == 25


def test_read_only_value():
    """Test that the temp attribute is read-only."""
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.temp = 30


def test_read_only_unit():
    """Test that the unit attribute is read-only."""
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.unit = "F"


def test_invalid_unit():
    """Test that invalid units raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, "u")


def test_str():
    """Test the string representation of Temperature objects."""
    assert Temperature(25, "C").__str__() == "25.00 °C"


def test_repr():
    """Test the official string representation of Temperature objects."""
    temperature = Temperature(25.0, "C")

    assert temperature.__repr__() == "Temperature(25.00, 'C')"