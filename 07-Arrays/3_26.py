import math
import matplotlib.pyplot as plt

x = []
y = []

for degrees in range(0, 361):
    x = x + [degrees]
    y = y + [math.sin(math.radians(degrees))]   # sin() needs radians

plt.plot(x, y)
plt.title('y = sin(x)')
plt.xlabel('x [degrees]')
plt.ylabel('sin(x)')
plt.xticks(range(0, 361, 45))
plt.grid(True)
plt.show()
