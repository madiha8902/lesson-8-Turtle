import turtle
turtle.Screen().bgcolor("green")

s=turtle.Screen()
s.setup(500,500)

turtle.title("welcome to turtle")

board=turtle.Turtle()
board.fillcolor("blue")
board.begin_fill()
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.end_fill()
turtle.done()