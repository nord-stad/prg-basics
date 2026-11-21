MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def month(n):
    if 1 <= n <= 12:
        return MONTHS[n - 1]
    return 'unknown (enter a number from 1 to 12)'