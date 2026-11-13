###
# A program that calculates the distance to the horizon (in km)
# Formula: d = 3.57 * sqrt(h)
#
import math

h = 0
while True:
    text = input("Enter the height of the observer in meters: ")
    text = text.replace(",", ".")  # replace comma with dot
    try:
        h = float(text)  # try to convert text to a number
    except ValueError:
        print("This is not a number, try again.")
        continue  # go back to the beginning of the loop
    if h < 0:
        print("Height cannot be negative, try again.")
        continue
    break  # valid number, exit the loop

d = 3.57 * math.sqrt(h)  # distance to the horizon in km
print(f"From a height of {h} m the horizon is {d:.2f} km away")