import time
from validators import read_int

countdown = read_int("Enter the number of seconds to count down: ")

words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

while countdown > 0:
    if countdown <= 5:
        print(words[countdown])
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)

print("Time's up!")