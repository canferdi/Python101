import turtle

screen = turtle.Screen()
screen.bgcolor("aquamarine1")
screen.title("Draw Star")

turtleInstance = turtle.Turtle()

turtleInstance.left(36)
turtleInstance.forward(100)
for i in range(4):
    turtleInstance.left(144)
    turtleInstance.forward(100)
    turtleInstance.right(72)
    turtleInstance.forward(100)
turtleInstance.left(144)
turtleInstance.forward(100)

turtle.done()