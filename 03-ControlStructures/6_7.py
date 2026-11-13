from validators import read_int

age = read_int("Enter your age: ", 1, 122)

if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")