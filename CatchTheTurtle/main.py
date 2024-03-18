import turtle
import time
import random

score = -1


def move():
    tortoise.hideturtle()
    x = random.randint(-330, 330)
    y = random.randint(-330, 330)
    tortoise.setx(x)
    tortoise.sety(y)
    tortoise.showturtle()
    turtle.ontimer(move, 2000)


def updateScore(x,y):
    global score
    score += 1
    label.hideturtle()
    label.clear()
    label.penup()
    label.goto(0,330)
    label.write(f"Your Score: {score}", align="center", font=("Times New Roman", 16, "normal"))


# Screen
screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.screensize(500, 500)
screen.bgcolor("Light Blue3")
# Label
label = turtle.Turtle()
# Tortoise
tortoise = turtle.Turtle()
tortoise.penup()
tortoise.color("green")
tortoise.shape("turtle")
tortoise.shapesize(3)

updateScore(0,0)
tortoise.onclick(updateScore)
move()

turtle.mainloop()
