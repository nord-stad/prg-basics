###
# Calculation of circle area and circumference
#

r = float(input('Enter radius: '))
PI = 3.14

area = PI * r ** 2  # A = pi * r^2
circumference = 2 * PI * r  # C = 2 * pi * r

print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')