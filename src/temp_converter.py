
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

        if self.to_kelvin() < 0:
            raise ValueError("Temperature can not be below absolute zero")

    def to_celsius(self) -> float:
        """Converts kelvin or farenheit to celsius"""
        if self._unit == "K":
            value = self._temp - 273.15
        elif self._unit == "F":
            value = (self._temp - 32) * (5/9)
        else:
            value = self._temp
        return value

    def to_fahrenheit(self) -> float:
        """Converts celsius or kelvin to fahrenheit"""
        if self._unit == "C":
            value = self._temp * (9/5) + 32
        elif self._unit == "K":
            value = (self._temp - 273.15) * (9/5) + 32
        else:
            value = self._temp
        return value

    def to_kelvin(self) -> float:
        """Converts celsius or fahrenheit to kelvin"""
        if self._unit == "C":
            value = self._temp + 273.15
        elif self._unit == "F":
            value = (self._temp - 32) * (5/9) + 273.15
        else:
            value = self._temp
        return value

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



    @property
    def temp(self) -> float:
        return self._temp

    @property
    def unit(self) -> str:
        return self._unit


temp = Temperature(100, "F")
print(temp.to_celsius())
print(temp.convert_to("F"))




