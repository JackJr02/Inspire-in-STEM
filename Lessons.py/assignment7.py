#Create an Analog and Digital clock
#!/usr/bin/python

######################
#   Assignment: Designing a clock
#   Name    : Wesley Jack
#   Date    : 10 /06 /2022
######################

from turtle import Turtle, Screen
import datetime

#creating window
window = Screen()
#setting window title
window.title("Jack's:Analog Clock")
#setting background color
window.bgcolor("Black")
#setting height and width of window
window.setup(width=1000, height=700)

#creating outer circle
circle = Turtle()
circle.penup()
circle.pencolor("#DDEEEE")
circle.speed(0)
circle.pensize(15)
circle.hideturtle()
circle.goto(0, -400)
circle.pendown()
circle.fillcolor("#17302A")
circle.begin_fill()
circle.circle(400)
circle.end_fill()

#creating hour hand
hHand = Turtle()
hHand.shape("arrow")
hHand.color("black")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)

#creating minute hand
mHand = Turtle()
mHand.shape("arrow")
mHand.color("Black")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

#creating second hand
sHand = Turtle()
sHand.shape("arrow")
sHand.color("powder blue")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=35)

#creating center circle
centerCircle = Turtle()
centerCircle.shape("circle")
#setting color to white
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=0.4, stretch_len=0.4)

# numbers with pen
pen = Turtle()
pen.speed(0)
pen.color("Yellow")

#number 1
pen.penup()
pen.hideturtle()
pen.goto(170, 260)
pen.write("1", align="center", font=("Kalinga", 50, "bold"))

#number 2
pen.penup()
pen.hideturtle()
pen.goto(300, 140)
pen.write("2", align="center", font=("Kalinga", 50, "bold"))

#number 3
pen.penup()
pen.hideturtle()
pen.goto(340, -30)
pen.write("3", align="center", font=("Kalinga", 50, "bold"))

#number 4
pen.penup()
pen.hideturtle()
pen.goto(300, -200)
pen.write("4", align="center", font=("Kalinga", 50, "bold"))

#number 5
pen.penup()
pen.hideturtle()
pen.goto(170, -325)
pen.write("5", align="center", font=("Kalinga", 50, "bold"))

#number 6
pen.penup()
pen.hideturtle()
pen.goto(0, -370)
pen.write("6", align="center", font=("Kalinga", 50, "bold"))

#number 7
pen.penup()
pen.hideturtle()
pen.goto(-170, -325)
pen.write("7", align="center", font=("Kalinga", 50, "bold"))

#number 8
pen.penup()
pen.hideturtle()
pen.goto(-300, -200)
pen.write("8", align="center", font=("Kalinga", 50, "bold"))

#number 9
pen.penup()
pen.hideturtle()
pen.goto(-340, -30)
pen.write("9", align="center", font=("Kalinga", 50, "bold"))

#number 10
pen.penup()
pen.hideturtle()
pen.goto(-280, 140)
pen.write("10", align="center", font=("Kalinga", 50, "bold"))

#number 11
pen.penup()
pen.hideturtle()
pen.goto(-160, 260)
pen.write("11", align="center", font=("Kalinga", 50, "bold"))

#number 12
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("12", align="center", font=("Kalinga", 50, "bold"))

#Defining function to moving hour hand
def movehHand():
   currentHourInternal = datetime.datetime.now().hour
   degree = (currentHourInternal - 15) * -30
   currentMinuteInternal = datetime.datetime.now().minute
   degree = degree + -0.5 * currentMinuteInternal
   hHand.setheading(degree)
   window.ontimer(movehHand, 60000)

#Defining function to minute hand
def movemHand():
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree = degree + (-currentSecondInternal * 0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand, 1000)

#Defining function to second hand
def movesHand():
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

window.ontimer(movehHand, 1)
window.ontimer(movemHand, 1)
window.ontimer(movesHand, 1)
window.exitonclick() 
