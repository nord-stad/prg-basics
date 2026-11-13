###
# Two variables x and y have values of 7 and 34.
# A program that swaps variable values (x should be 34 and y should be 7)
# using an additional, auxiliary variable.
#
x = 7
y = 34
z = 0  # additional, auxiliary variable
print(f"Before swapping: x = {x}, y = {y}")

# swap the values
z = x  # save x in the auxiliary variable
x = y  # copy y into x
y = z  # copy the saved value of x into y

print(f"After swapping: x = {x}, y = {y}")