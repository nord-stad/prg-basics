import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]


colors = ['red', 'green', 'blue', 'yellow', 'black', 'white']

print('Array:', colors)
for i in range(5):
    print('Random element:', rand_elem(colors))
