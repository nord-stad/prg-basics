def read_int(prompt: str) -> int:
    value = 0
    while True:
        text = input(prompt).strip()  # remove spaces at the beginning and end
        try:
            value = int(text)  # try to convert text to an integer
        except ValueError:
            print("This is not an integer, try again.")
            continue  # go back to the beginning of the loop
        break  # valid integer, exit the loop
    return value


number = read_int('Enter number: ')
even = number % 2 == 0  # % gives the remainder of division
print(f'Number is even: {even}')