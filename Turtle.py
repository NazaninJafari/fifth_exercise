#rasme shekle hendesi
from re import I
import turtle

t = turtle.Pen()
t.shape('turtle')
turtle.bgcolor('white') #back ground color
t.pencolor('black')

n=3
j=0
while n<=360:

    for i in range(n):
        t.left(360/n)
        t.forward(20+j)

        #if i==n-1:
        #t.backward(8)   
    j+=8     
    t.penup()
    t.goto(4,-1-j)
    t.pendown()
    n+=1
    