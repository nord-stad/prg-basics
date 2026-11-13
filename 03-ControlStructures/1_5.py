###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#

from validators import read_int

total_tasks = 20
tasks_ok = read_int('Enter the number of correctly completed tasks: ', 0, total_tasks)
test_passed = False

if tasks_ok >= total_tasks * 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')