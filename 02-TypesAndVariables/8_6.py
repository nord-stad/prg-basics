###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#

import math


def read_positive_int(prompt: str) -> int:
    value = 0
    while True:
        text = input(prompt).strip()  # remove spaces at the beginning and end
        try:
            value = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue  # go back to the beginning of the loop
        if value <= 0:
            print("The value must be greater than 0, try again.")
            continue
        break  # valid number, exit the loop
    return value


def read_positive_float(prompt: str) -> float:
    value = 0.0
    while True:
        text = input(prompt).strip().replace(',', '.')  # accept both 1,5 and 1.5
        try:
            value = float(text)  # try to convert text to float
        except ValueError:
            print("This is not a number, try again.")
            continue  # go back to the beginning of the loop
        if value <= 0:
            print("The value must be greater than 0, try again.")
            continue
        break  # valid number, exit the loop
    return value


distance = read_positive_int('Enter distance in km: ')
fuel_price = read_positive_float('Enter fuel price per liter: ')
fuel_consumption = read_positive_float('Enter fuel consumption in liters per 100 km: ')
total_fuel_consumption = distance * fuel_consumption / 100  # liters for the whole trip
total_cost = total_fuel_consumption * fuel_price  # cost of that fuel
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total cost: {total_cost:.2f}')