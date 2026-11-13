###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#

import random

def read_dice_number(prompt: str) -> int:
    value = 0
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue
        if not (1 <= value <= 6):
            print("The number must be between 1 and 6, try again.")
            continue
        break  # valid number, exit the loop
    return value


# COMPUTER TURN
computer = random.randint(1, 6)  # a die has sides 1-6
# YOUR TURN
you = read_dice_number('Guess the number (1-6): ')
won = you == computer
print(f'Computer rolled: {computer}')
print(f'You won: {won}')