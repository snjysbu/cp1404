from guitar import Guitar


def test_guitar_methods():
    """Test the Guitar class methods."""
    # Create a Guitar instance for testing
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test get_age()
    expected_age_gibson = 100
    actual_age_gibson = gibson.get_age(2022)
    print(f"{gibson.name} get_age() - Expected {expected_age_gibson}. Got {actual_age_gibson}")

    # Test is_vintage()
    expected_vintage_gibson = True
    actual_vintage_gibson = gibson.is_vintage(2022)
    print(f"{gibson.name} is_vintage() - Expected {expected_vintage_gibson}. Got {actual_vintage_gibson}")

    # Create another Guitar instance for testing
    another_guitar = Guitar("Another Guitar", 2013, 500)

    # Test get_age() for another guitar
    expected_age_another_guitar = 9
    actual_age_another_guitar = another_guitar.get_age(2022)
    print(f"{another_guitar.name} get_age() - Expected {expected_age_another_guitar}. Got {actual_age_another_guitar}")

    # Test is_vintage() for another guitar
    expected_vintage_another_guitar = False
    actual_vintage_another_guitar = another_guitar.is_vintage(2022)
    print(
        f"{another_guitar.name} is_vintage() - Expected {expected_vintage_another_guitar}. Got {actual_vintage_another_guitar}")


if __name__ == "__main__":
    test_guitar_methods()
