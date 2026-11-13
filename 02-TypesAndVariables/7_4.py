import math

def read_positive_int(prompt: str) -> int:
    value = 0
    while True:
        text = input(prompt).strip()  # remove spaces at the beginning and end
        try:
            value = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue
        if value <= 0:
            print("The value must be greater than 0, try again.")
            continue
        break
    return value


circumference = read_positive_int('Enter tree circumference in cm: ')
diameter = circumference / math.pi  # circumference = pi * diameter
can_cut = diameter >= 50  # "at least 50 cm" means 50 is still OK
print(f'Tree can be cut down: {can_cut}')