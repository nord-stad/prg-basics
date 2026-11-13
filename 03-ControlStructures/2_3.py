###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#

from validators import read_int

while True:
    driving_mode = input('Enter driving mode (A/M/E): ').strip().upper()
    if driving_mode in ('A', 'M', 'E'):
        break
    print('Incorrect driving mode, try again.')

distance = read_int('Enter distance in km: ', min_value=1)

if driving_mode == 'A':
    fuel_consumption = 7
elif driving_mode == 'M':
    fuel_consumption = 9
else:
    fuel_consumption = 6

total_consumption = distance * fuel_consumption / 100
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')