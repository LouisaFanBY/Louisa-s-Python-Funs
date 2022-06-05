# ClickAndSmile.py by Louisa
import random
import turtle
pen = turtle.Pen()
pen.speed(0)
pen.hideturtle()
turtle.bgcolor("red")
def draw_smiley(x,y):
    print("x: ", x, " y: ", y)
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    # Face
    pen.pencolor("yellow")
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    # Left eye
    pen.penup()
    pen.setpos(x-15, y+60)
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    # Right eye
    pen.penup()
    pen.setpos(x+15, y+60)
    pen.pendown()
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    # Mouth
    pen.setpos(x-25, y+40)
    pen.pencolor("white")
    pen.width(10)
    pen.goto(x-10, y+20)
    pen.goto(x+10, y+20)
    pen.goto(x+25, y+40)
    pen.width(1)
turtle.onscreenclick(draw_smiley)