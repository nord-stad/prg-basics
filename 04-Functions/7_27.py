def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False                       # wrong length or not only digits
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    return digits_sum % 7 == control_digit

product_code = input('Enter product code: ')
print('f("' + product_code + '") returns', f(product_code))