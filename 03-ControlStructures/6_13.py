from validators import read_int

speed_limit_min = 40
speed_limit_max = 140
car_speed = read_int("Enter car speed: ")

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is valid.")