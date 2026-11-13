def read_int(prompt: str) -> int:
    value = 0
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("This is not an integer, try again.")
            continue
        break
    return value


speed = read_int('Enter vehicle speed: ')
speed_ok = 40 <= speed <= 140
print(f'Speed is valid: {speed_ok}')