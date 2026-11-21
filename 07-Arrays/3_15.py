numbers = (10, 20, 30, 40, 50)

reversed_numbers = numbers[::-1]

print('Tuple:', ','.join(str(n) for n in numbers))
print('Reverse order:', ','.join(str(n) for n in reversed_numbers))
