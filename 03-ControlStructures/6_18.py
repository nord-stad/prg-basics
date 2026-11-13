from validators import read_int

x = read_int("Enter x coordinate: ")
y = read_int("Enter y coordinate: ")

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin of the coordinate system.")
elif x == 0:
    print(f"Point P({x},{y}) is on the Y axis.")
elif y == 0:
    print(f"Point P({x},{y}) is on the X axis.")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")