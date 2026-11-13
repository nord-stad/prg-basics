###
# A program that calculates and prints
# the average grade of a student
#

# Original code:
# math = 5
# art = 4
# music = 5
# history = '3'
# average = mat + Art - muzic + history / 4
# print("Average grade is', averege)

math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)

# Fixed errors (line numbers refer to the original code above):
# 1. history = '3' was text, it must be a number: history = 3 - line 10
# 2. mat -> math (typo) - line 11
# 3. Art -> art (Python is case-sensitive) - line 11
# 4. muzic -> music (typo) - line 11
# 5. - music -> + music (grades must be added) - line 11
# 6. added parentheses, otherwise only history was divided by 4 - line 11
# 7. "Average grade is' -> "Average grade is" (mismatched quotes) - line 12
# 8. averege -> average (typo) - line 12