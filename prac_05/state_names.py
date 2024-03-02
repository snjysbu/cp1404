"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# Print all the code and its name:
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")


while True:
    # Convert the given short code into uppercase:
    state_code = input("Enter short state: ").upper()

    if state_code == "":
        break

    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
