#turtle setup
import turtle
greg = turtle.Turtle()
wn = turtle.Screen()

#user input(num of lines, length of line, turn degree)
line_count = input("How many lines would you like Greg to draw?")
line_length = input("What length would you like the lines to be?")
degree = input("How many degrees would you like Greg to turn?")

#movement
for j in range(int(line_count)):
    greg._rotate(int(degree))
    greg.forward(int(line_length))

wn.exitonclick()#close window
