###
# A program that calculates the number of characters
# of your name, surname and full name
#

name = 'Norbert'
surname = 'Stadnik'
characters_in_name = len(name)

print(f'Your name "{name}" has {characters_in_name} characters')
print(f'Your surname "{surname} has {len(surname)} characters')
print(f'Your full name "{name+ " " +surname}" has {len(name + " " + surname)} characters') # with a space between name and surname