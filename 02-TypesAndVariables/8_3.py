###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

import math

ABSOLUTE_ZERO = -273.15  # the lowest possible temperature in Celsius

def read_celsius(prompt: str) -> float:
    value = 0.0
    while True:
        text = input(prompt).strip().replace(',', '.')  # accept both 1,5 and 1.5
        try:
            value = float(text)  # try to convert text to float
        except ValueError:
            print("This is not a number, try again.")
            continue  # go back to the beginning of the loop
        if not math.isfinite(value):
            print("The value must be a regular number (not nan or inf), try again.")
            continue
        if value < ABSOLUTE_ZERO:
            print(f"Temperature cannot be lower than {ABSOLUTE_ZERO} C, try again.")
            continue
        break  # valid temperature, exit the loop
    return value


# read temperature in Celsius from the keyboard
celsius = read_celsius('Enter temperature in Celsius: ')

# convert to Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# convert to Fahrenheit: F = C * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32

# print results
print(f'{celsius:.2f} C = {kelvin:.2f} K')
print(f'{celsius:.2f} C = {fahrenheit:.2f} F')