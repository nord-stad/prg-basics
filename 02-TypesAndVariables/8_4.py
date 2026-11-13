###
# A program that prints your height both in cm and in feet and inches.
#

cm_per_foot = 30.48
cm_per_inch = 2.55

cm = 182
feet = int(cm // cm_per_foot)
remaining_cm = cm % cm_per_foot
inches = remaining_cm / cm_per_inch

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.2f} inches')