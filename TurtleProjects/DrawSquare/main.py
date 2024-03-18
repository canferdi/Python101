import turtle

screen = turtle.Screen()
screen.bgcolor("aquamarine1")
screen.title("Draw Square")

turtleInstance = turtle.Turtle()

for i in range(4):
    turtleInstance.forward(200)
    turtleInstance.left(90)
turtle.done()

