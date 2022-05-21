# SquareSpiral1.py
import turtle
t=turtle.Pen()
turtle.bgcolor("black")
sides = 5
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    print(f"x = {x}")
    t.pencolor(colors[x%sides])
    print(f"x * 3/sides + x = {x * 5/sides + x}")
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

