###
# A program that prints a university abbreviation
#
university = "Uniwersytet Ekonomiczny w Krakowie"
abbreviation = ""
for word in university:
    if word[0].isupper():  # take only words starting with a capital letter
        abbreviation += word[0]
print(abbreviation)