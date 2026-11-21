###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

window = turtle.Screen()
window.setup(width=500, height=400)
window.bgcolor("lightgreen")

pen = figures.pen
pen.speed(5)

## Draw figures
# Squares
pen.penup()
pen.goto(-170, 120)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(-170, -20)
pen.pendown()
figures.draw_square(50)

# Triangles
pen.penup()
pen.goto(-50, 40)
pen.pendown()
figures.draw_triangle(80)

pen.penup()
pen.goto(-50, -110)
pen.pendown()
figures.draw_triangle(50)

# Rectangles
pen.penup()
pen.goto(70, 120)
pen.pendown()
figures.draw_rectangle(100, 50)

pen.penup()
pen.goto(70, -20)
pen.pendown()
figures.draw_rectangle(70, 35)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()