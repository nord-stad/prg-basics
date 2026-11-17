import math


def read_int(prompt, min_value = 0, max_value = 9999):
    value = 0
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("This is not an integer, try again.")
            continue
        if min_value is not None and value < min_value:
            print(f"The value must be at least {min_value}, try again.")
            continue
        if max_value is not None and value > max_value:
            print(f"The value must be at most {max_value}, try again.")
            continue
        break
    return value


def read_float(prompt):
    value = 0.0
    while True:
        text = input(prompt).strip().replace(',', '.')
        try:
            value = float(text)
        except ValueError:
            print("This is not a number, try again.")
            continue
        if not math.isfinite(value):
            print("The value must be a regular number (not nan or inf), try again.")
            continue
        break
    return value


def read_positive_float(prompt: str) -> float:
    while True:
        value = read_float(prompt)
        if value > 0:
            return value
        print("The value must be greater than 0, try again.")