def input_string(message):
    text = input(message)
    return text

def input_integer(message):
    text = input(message)
    return int(text)

def input_real(message):
    text = input(message)
    return float(text)

def input_boolean(message):
    text = input(message)
    return text.strip().lower() == 'y'