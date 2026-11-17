import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.temp_converter import Temperature


def test_abs_zero():
    temp_c = Temperature(-273.15, "C")
    temp_k = Temperature(0, "K")
    temp_f = Temperature(-459.67, "F")

    assert temp_c.to_kelvin() == pytest.approx(0, abs=1e-9, rel=0)
    assert temp_k.to_fahrenheit() == pytest.approx(-459.67, abs=1e-9, rel=0)
    assert temp_f.to_celsius() == pytest.approx(-273.15, abs=1e-9, rel=0)


def test_below_abs_zero():
    with pytest.raises(ValueError):
        Temperature(-300, "C")

    with pytest.raises(ValueError):
        Temperature(-2, "K")

    with pytest.raises(ValueError):
        Temperature(-500, "F")


def test_celsius():
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")
    temp_k = Temperature(273.15, "K")

    assert temp_c.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)
    assert temp_f.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)
    assert temp_k.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)


def test_fahrenheit():
    temp_c = Temperature(-40, "C")
    temp_f = Temperature(77, "F")
    temp_k = Temperature(233.15, "K")

    assert temp_c.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)
    assert temp_f.to_fahrenheit() == pytest.approx(77, abs=1e-9, rel=0)
    assert temp_k.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)


def test_kelvin():
    temp_c = Temperature(37, "C")
    temp_f = Temperature(98.6, "F")
    temp_k = Temperature(300, "K")

    assert temp_c.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)
    assert temp_f.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)
    assert temp_k.to_kelvin() == pytest.approx(300, abs=1e-9, rel=0)


def test_converter():
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
    temperature = Temperature(25)

    assert temperature.temp == 25
    assert temperature.unit == "C"


def test_case_insensitive_unit():
    temperature = Temperature(25, "c")

    assert temperature.unit == "C"
    assert temperature.temp == 25


def test_read_only_value():
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.temp = 30


def test_read_only_unit():
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.unit = "F"


def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "u")


def test_str():
    assert str(Temperature(25, "C")) == "25.00 °C"


def test_repr():
    assert repr(Temperature(25.0, "C")) == "Temperature(25.00, 'C')"


def test_comparisons():
    t_c = Temperature(0, "C")
    t_f = Temperature(32, "F")
    t_hot = Temperature(100, "C")

    assert t_c == t_f
    assert not (t_c != t_f)
    assert t_c < t_hot
    assert t_c <= t_f
    assert t_hot > t_c
    assert t_f >= t_c


def test_notimplemented_comparisons():
    temp = Temperature(0, "C")

    assert temp.__eq__(42) is NotImplemented
    assert temp.__ne__(42) is NotImplemented
    assert temp.__lt__(42) is NotImplemented
    assert temp.__le__(42) is NotImplemented
    assert temp.__gt__(42) is NotImplemented
    assert temp.__ge__(42) is NotImplemented


def test_convert_invalid_unit():
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to("X")