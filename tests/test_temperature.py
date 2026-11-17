import pytest
from src.temp_converter import Temperature


def test_abs_zero():
    tempC = Temperature(-273.15, "C")
    tempK = Temperature(0, "K")
    tempF = Temperature(-459.67, "F")

    assert tempC.to_kelvin() == pytest.approx(0, abs=1e-9, rel=0)
    assert tempK.to_fahrenheit() == pytest.approx(-459.67, abs=1e-9, rel=0)
    assert tempF.to_celsius() == pytest.approx(-273.15, abs=1e-9, rel=0)
    

def test_below_abs_zero():
    with pytest.raises(ValueError):
        Temperature(-300, "C")

    with pytest.raises(ValueError):
        Temperature(-2, "K")

    with pytest.raises(ValueError):
        Temperature(-500, "F")



def test_celsius():
    tempF = Temperature(32, "F")
    tempK = Temperature(273.15, "K")

    assert tempF.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)
    assert tempK.to_celsius() == pytest.approx(0, abs=1e-9, rel=0)


def test_fahrenheit():
    tempC = Temperature(-40, "C")
    tempK = Temperature(233.15, "K")

    assert tempC.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)
    assert tempK.to_fahrenheit() == pytest.approx(-40, abs=1e-9, rel=0)


def test_kelvin():
    tempC = Temperature(37, "C")
    tempF = Temperature(98.6, "F")

    assert tempC.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)
    assert tempF.to_kelvin() == pytest.approx(310.15, abs=1e-9, rel=0)


def test_converter():
    original = Temperature(100, "C")

    tempF = original.convert_to("F")
    tempK = tempF.convert_to("K")
    tempC = tempK.convert_to("C")

    assert tempF.unit == "F"
    assert tempF.value == pytest.approx(212, abs=1e-9, rel=0)

    assert tempK.unit == "K"
    assert tempK.value == pytest.approx(373.15, abs=1e-9, rel=0)

    assert tempC.unit == "C"
    assert tempC.value == pytest.approx(original.value, abs=1e-9, rel=0)
    assert tempC == original


def test_default_unit():
    temperature = Temperature(25)

    assert temperature.value == 25
    assert temperature.unit == "C"


def test_case_insensitive_unit():
    temperature = Temperature(25, "c")

    assert temperature.unit == "C"
    assert temperature.value == 25


def test_read_only_value():
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.value = 30


def test_read_only_unit():
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.unit = "F"


def test_invalid_unit(unit):
    with pytest.raises(ValueError):
        Temperature(25, unit)


def test_str(value, unit, expected):
    assert str(Temperature(value, unit)) == expected


def test_repr():
    temperature = Temperature(25.0, "C")

    assert repr(temperature) == "Temperature(25.0, 'C')"