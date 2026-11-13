from validators import read_int

human_age = read_int("Enter the dog's age in human years: ", 1, 20)

if human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 2 * 10.5 + (human_age - 2) * 4

print(f"The dog's age in dog's years is {dog_age} years.")