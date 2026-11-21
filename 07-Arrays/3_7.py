names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name

print('Names:', ' '.join(names))
print('Longest name:', longest)
