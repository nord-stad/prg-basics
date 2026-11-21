from validators import read_int

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= n <= 7:
        return weekdays[n - 1]
    return 'unknown (enter a number from 1 to 7)'


for day in [1, 4, 7]:
    print('Day', day, 'is', weekday(day))

n = read_int('Enter day number: ')
print('Day', n, 'is', weekday(n))