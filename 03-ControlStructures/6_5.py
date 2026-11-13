###
# Program that simulates the operation of an electronic thermometer.
#

from validators import read_int

temperature = read_int("Enter the temperature: ", -50, 50)

if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost")