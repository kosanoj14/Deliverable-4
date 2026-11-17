
class Temperature:
    """Converts different temperature types"""
    def __init__(self, temp: int | float, unit: str) -> None:
        """takes in a temperature and its unit"""
        self._temp = temp
        self._unit = unit
        tolerance = 1e-9

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