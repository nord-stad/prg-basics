###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)  # Pythagorean theorem: d = sqrt(a^2 + b^2)
diagonal_rounded = round(diagonal, 4)
print(f"Diagonal of a rectangle with sides a = {a} and b = {b} is {diagonal}, rounded: {diagonal_rounded}")