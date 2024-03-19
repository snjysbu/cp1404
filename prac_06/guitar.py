class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage (50 or more years old)."""
        return self.get_age(current_year) >= 50


# Sample usage
if __name__ == "__main__":
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar1)

    current_year = 2024
    print(f"The guitar is {guitar1.get_age(current_year)} years old.")
    if guitar1.is_vintage(current_year):
        print("This guitar is vintage.")
    else:
        print("This guitar is not vintage.")
