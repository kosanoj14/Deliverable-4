
class Temperature:
    """Converts a temperature in one unit to one in another unit"""
    def __init__(self, temp: int | float, unit: str) -> None:
        """takes in a temperature and its unit"""
        self._temp = temp
        self._unit = unit
        tol = 1e-9

        """A checker that sees if the unit is C, K or F"""
        if self._unit not in ("C","K","F"):
            raise ValueError("You must use either C, K or F as your unit in uppercase")
        """Checks if the temperature is below absolute zero"""
        if self.to_kelvin() < 0:
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
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() == other.to_kelvin()
        )


    def __ne__(self, other: object) -> bool:
        """checks if two temperatures are not equal"""
        if not isinstance(other, Temperature):
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() != other.to_kelvin()
        )

    def __lt__(self, other: object) -> bool:
        """checks if one temperature is less than another"""
        if not isinstance(other, Temperature):
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() < other.to_kelvin()
        )

    def __le__(self, other: object) -> bool:
        """checks if one temperature is less or equal to another"""
        if not isinstance(other, Temperature):
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() <= other.to_kelvin()
        )

    def __gt__(self, other: object) -> bool:
        """checks if one temperature is greater than another"""
        if not isinstance(other, Temperature):
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() > other.to_kelvin()
        )

    def __ge__(self, other: object) -> bool:
        """checks if one temperature is greater or equal to another"""
        if not isinstance(other, Temperature):
            raise NotImplemented("can not compare a non temperature object to a temperature object")
        return (
            self.to_kelvin() >= other.to_kelvin()
        )



t1 = Temperature(0, "C")
t2 = Temperature(32, "F")

print(t1.__eq__(t2))
print(t1.__ne__(t2))
print(t1.__lt__(t2))
print(t1.__le__(t2))
print(t1.__gt__(t2))
print(t1.__ge__(t2))







