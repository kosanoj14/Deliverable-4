
class Temperature:
    """Converts different temperature types"""
    def __init__(self, temp: int | float, unit: str) -> None:
        """takes in a temperature and its unit"""
        self._temp = temp
        self._unit = unit
        tolerance = 1e-9

        """A checker that sees if the unit is C, K or F"""
        if self._unit not in ("C","K","F"):
            raise ValueError("You must use either C, K or F as your unit")
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



    @property
    def temp(self) -> float:
        return self._temp

    @property
    def unit(self) -> str:
        return self._unit


temp = Temperature(100, "F")
print(temp.to_celsius())
print(temp.convert_to("F"))
print(temp.__str__())




