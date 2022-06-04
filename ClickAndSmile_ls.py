# ClickAndSmile.py by Louisa
import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("red")
def draw_smiley(x,y):
    print("x: ", x, " y: ", y)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Face
    t.pencolor("yellow")
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    # Left eye
    

turtle.onscreenclick(draw_smiley)