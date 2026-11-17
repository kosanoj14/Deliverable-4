class Fraction:
    """Represent a mathematical fraction"""

    def __init__(self, numerator, denominator):
        """Initialize a fraction with an integer numerator and denominator."""
        if type(numerator) is not int:
            raise TypeError("Numerator must be an integer")

        if type(denominator) is not int:
            raise TypeError("Denominator must be an integer")

        if denominator <= 0:
            raise ValueError("Denominator must be greater than zero")

        self.numerator = numerator
        self.denominator = denominator

    def __truediv__(self, other):
        """Divide this fraction by another fraction and check if we not have a zero devision."""
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction")
        
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator 

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        return Fraction(numerator, denominator)

    def __add__(self, other):
        """Add to fractions."""
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Subtract one fraction from another."""
        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Mulitiply two fractions."""
        numerator = self.numerator * other.numerator 
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)


    def __eq__(self, other):
        """Return True if two fractions are equal."""
        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )


    def __ne__(self, other):
        """Return True if two fractions are not equal."""
        return (
            self.numerator * other.denominator
            != other.numerator * self.denominator
        )

    def __lt__(self, other):
        """Return True if this fraction is less than another."""
        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    def __le__(self, other):
        """Return True if this fraction is less than or equal to another."""
        return (
            self.numerator * other.denominator
            <= other.numerator * self.denominator
        )

    def __gt__(self, other):
        """Return True if this fraction is greater than another."""
        return (
            self.numerator * other.denominator
            > other.numerator * self.denominator
        )

    def __ge__(self, other):
        """Return True if this fraction is greater than og equal to another."""
        return (
            self.numerator * other.denominator
            >= other.numerator * self.denominator
        )

