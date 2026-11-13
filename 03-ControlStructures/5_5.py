###
# Sums numbers entered by user
#

from validators import read_int

total_sum = 0
count = 0

while True:
    number = read_int("Enter a number (0 to stop): ", 0)

    if number == 0:
        break
    total_sum += number
    count += 1

print(f"The total sum of the numbers is: {total_sum}")

if count > 0:
    mean = total_sum / count
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")