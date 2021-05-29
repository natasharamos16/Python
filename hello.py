#Natasha Ramos-Gomez
#hello.py
#Jan 18, 2020

#importing a function
import turtle

print ("Hello, world!")

wn = turtle.Screen()
wn.bgcolor("gray")#creates a graphics window
donatello = turtle.Turtle()#naming my turtle
donatello.shape('turtle')#turning my pen into a turtle shape

donatello.begin_fill()#begins the process to use fill in color
donatello.color("pink")#setting the color for the turtle
for i in range(10):#used to count how many times it goes over the shape
    donatello.forward(50)
    donatello.right(144)
donatello.pensize(12)#size of the pen
donatello.end_fill()#fills in the shape with color choice

wn.exitonclick()#closes the window when user clicks



#Python is Fun!

