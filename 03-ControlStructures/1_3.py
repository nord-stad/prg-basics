###
# Checking whether a car exceeded the speed limit
#

from validators import read_int

speed_limit = 140
car_speed = read_int('Enter car speed (km/h): ')

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')