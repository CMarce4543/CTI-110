#Christian Marcellino
#4/7/2024
#P4LAB1
#Using 'Import Turtle' for drawing capabilities.

import turtle
win = turtle.Screen()         
win.bgcolor('pink')
win.title('Drawing Shapes with Turles')

#Changes the triangle pen shape to a Turtle
turtle.shape('turtle')

#Turtles names are Ben and Lisa
Ben = turtle.Turtle()
Lisa = turtle.Turtle()

#Move Ben forward by 100 units
for _ in range(4):
    Ben.forward(100)
#Turn right by 90 degrees 4 times making a square
    Ben.right(90)

#Moves Lisa to a new position so shapes do not overlap
Lisa.pensize()
Lisa.goto(100, -50)  
Lisa.pendown()

#Move forward by 100 units
for _ in range(3):
    Lisa.forward(100)
    
#Turn right by 120 degrees 3 times making a square 
    Lisa.left(120)

