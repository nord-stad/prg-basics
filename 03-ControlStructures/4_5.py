###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char)
    char_code = char_code + 1
    new_char = chr(char_code)
    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)