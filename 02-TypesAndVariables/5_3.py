###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#

def read_positive_int(prompt):
    while True:
        text = input(prompt)
        try:
            value = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue  # go back to the beginning of the loop
        if value <= 0:
            print("The side must be greater than 0, try again.")
            continue
        return value  # valid number, exit the function


a = read_positive_int('a=')
b = read_positive_int('b=')
c = read_positive_int('c=')

volume = a * b * c  # V = a * b * c
surface_area = 2 * (a*b + a*c + b*c)  # P = 2(ab + ac + bc), 3 pairs of equal faces
print(f'The volume of a cuboid with sides {a}, {b}, {c} is {volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c} is {surface_area}')