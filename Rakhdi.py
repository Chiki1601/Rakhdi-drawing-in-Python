#Rakhdi Drawing in Python


import turtle
from turtle import *

t = turtle.Turtle()

def setPosition(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

setPosition(-200, 200)
t.color("orange")
t.write("Happy RakshaBandhan lovely sis! ", 
font=("Calibri", 25, "bold")
)

setPosition(-160, 170)
t.color("black")
t.write("best wishes from Pooja Patel :)", 
font=("Calibri", 20, "bold")
)

t.speed("fastest")
t.pensize(5)
t.pencolor("red")
setPosition(0, 0)
for i in range(130):
    if i > 80:
        t.pencolor("orange")
    elif i > 50:
        t.pencolor("yellow")
        
    t.circle(10 + i, 45)

begin_fill()
t.speed("fastest")
for i in range(15):
    setPosition(-150 - (i*10), 0)
    t.dot(20, "red" if i % 2 == 0 else "orange")

for i in range(20):
    setPosition(-300, -0 - (i*10))
    t.dot(20, "red" if i % 2 == 0 else "orange")

for i in range(15):
    setPosition(150 + (i*10), 0)
    t.dot(20, "red" if i % 2 == 0 else "orange")

for i in range(20):
    setPosition(300, 0 + (i*10))
    t.dot(20, "red" if i % 2 == 0 else "orange")
    
    
t.done()
