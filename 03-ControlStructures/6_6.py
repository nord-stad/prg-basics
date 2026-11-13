from validators import read_int

hours = read_int("Enter the number of parking hours: ")

if hours >= 1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0

print(f"Parking fee: {fee} PLN")