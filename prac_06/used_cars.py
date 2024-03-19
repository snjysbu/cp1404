from cars import Car  # Importing Car class from cars.py

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")  # Creating a named car
    my_car.drive(30)
    print(my_car)

    limo = Car(100, "Limo")  # Creating a named car "Limo" with 100 units of fuel
    limo.add_fuel(20)  # Adding 20 more units of fuel
    print(f"Amount of fuel in {limo.name}: {limo.fuel}")

    limo.drive(115)  # Attempting to drive 115 km
    print(limo)  # Printing the limo object to check the __str__ method

main()
