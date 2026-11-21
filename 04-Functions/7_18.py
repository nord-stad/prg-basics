def f(sentence):
    return sentence.replace(' ', '')

sentence = input('Enter sentence: ')
print('f("' + sentence + '") returns "' + f(sentence) + '"')