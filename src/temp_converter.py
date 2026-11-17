
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

    def to_celsius(self) -> float:
        """Converts kelvin or farenheit to celsius"""

    def to_fahrenheit(self) -> float:
        """Converts celsius or kelvin to fahrenheit"""

    def to_kelvin(self) -> float:
        """Converts celsius or fahrenheit to kelvin"""

    @property
    def temp(self) -> float:
        return self._temp

    @property
    def unit(self) -> str:
        return self._unit


temp = Temperature(100, "K")

