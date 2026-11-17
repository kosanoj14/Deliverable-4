import math

class Temperature:
    """Converts a temperature in one unit to one in another unit"""
    def __init__(self, temp: int | float, unit: str = "C") -> None:
        """takes in a temperature and its unit"""
        self._temp = float(temp)
        self._unit = unit.upper()
        self.tol = 1e-9

        """A checker that sees if the unit is C, K or F"""
        if self._unit not in ("C","K","F"):
            raise ValueError("You must use either C, K or F as your unit in uppercase")
        """Checks if the temperature is below absolute zero"""
        if self.to_kelvin() + self.tol < 0:
            raise ValueError("Temperature can not be below absolute zero")

    def to_celsius(self) -> float:
        """Converts kelvin or farenheit to celsius"""
        if self._unit == "K":
            self._temp = self._temp - 273.15
            self._unit = "C"
        elif self._unit == "F":
            self._temp = (self._temp - 32) * (5/9)
            self._unit = "C"
        else:
            pass
        return self._temp

    def to_fahrenheit(self) -> float:
        """Converts celsius or kelvin to fahrenheit"""
        if self._unit == "C":
            self._temp = self._temp * (9/5) + 32
            self._unit = "F"
        elif self._unit == "K":
            self._temp = (self._temp - 273.15) * (9/5) + 32
            self._unit = "F"
        else:
            pass
        return self._temp

    def to_kelvin(self) -> float:
        """Converts celsius or fahrenheit to kelvin"""
        if self._unit == "C":
            self._temp = self._temp + 273.15
            self._unit = "K"
        elif self._unit == "F":
            self._temp = (self._temp - 32) * (5/9) + 273.15
            self._unit = "K"
        else:
            pass
        return self._temp

    def convert_to(self, target_unit: str) -> float:
        """Converts the temperature to a new unit"""
        if target_unit not in ("C","K","F"):
            raise ValueError("You must use either C, K or F as your unit")
        elif target_unit == "C":
            return self.to_celsius()
        elif target_unit == "F":
            return self.to_fahrenheit()
        elif target_unit == "K":
            return self.to_kelvin()

    def __repr__(self) -> str:
        """returns an unambiguous representation of the temperature"""
        return f"Temperature({round(self._temp, 2)}, {self._unit})"

    def __str__(self) -> str:
        """returns a human readable representation of the temperature"""
        return f"{round(self._temp, 2)} °{(self._unit)}"

    """makes temp and unit a property, that is read-only"""
    @property
    def temp(self) -> float:
        return self._temp

    @property
    def unit(self) -> str:
        return self._unit

    def __eq__(self, other: object) -> bool:
        """checks if two temperatures are equal"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            math.isclose(self.to_kelvin(), other.to_kelvin(), abs_tol=self.tol)
        )

    def __ne__(self, other: object) -> bool:
        """checks if two temperatures are not equal"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        return not (
            math.isclose(self.to_kelvin(), other.to_kelvin(), abs_tol=self.tol)
        )

    def __lt__(self, other: object) -> bool:
        """checks if one temperature is less than another"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        k1 = self.to_kelvin()
        k2 = other.to_kelvin()
        return not math.isclose(k1, k2, abs_tol=self.tol) and k1 < k2

    def __le__(self, other: object) -> bool:
        """checks if one temperature is less or equal to another"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        k1 = self.to_kelvin()
        k2 = other.to_kelvin()
        return math.isclose(k1, k2, abs_tol=self.tol) or k1 < k2

    def __gt__(self, other: object) -> bool:
        """checks if one temperature is greater than another"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        k1 = self.to_kelvin()
        k2 = other.to_kelvin()
        return not math.isclose(k1, k2, abs_tol=self.tol) and k1 > k2

    def __ge__(self, other: object) -> bool:
        """checks if one temperature is greater or equal to another"""
        if not isinstance(other, Temperature):
            return NotImplemented("can not compare a non temperature object to a temperature object")
        k1 = self.to_kelvin()
        k2 = other.to_kelvin()
        return math.isclose(k1, k2, abs_tol=self.tol) or k1 > k2








