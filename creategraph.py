#!/usr/bin/env python3

#layonthehorn
#
# this will take in numbers and colors and create a basic graph with a turtle
#
import turtle

def drawbar(alist,blist):
    wn = turtle.Screen()       
    alex = turtle.Turtle() 
    alex.hideturtle()
    alex.speed(1000)
    for i,b in zip(alist,blist):
        alex.fillcolor(b)
        alex.begin_fill()
        alex.left(90)
        alex.forward(int(i))
        alex.right(90)
        alex.forward(10)
        alex.right(90)
        alex.forward(int(i))
        alex.left(90)
        alex.backward(10) 
        alex.end_fill()
        alex.forward(10)

    wn.exitonclick()
    
    
def returnlists():
 
    mainnumber = 0
    num = "this is a placeholder!!!"
    colorlist = []
    numberlist = []
    
    while num != "":
        num = input("Enter a number leave blank to stop. ")
        
        if num != "":
            numberlist.append(num)
        
    while len(colorlist) < len(numberlist):
        colortrt = input("What color on number {0} do you want?  ".format(numberlist[mainnumber]))
        colorlist.append(colortrt)
        mainnumber += 1
    
    
   
    drawbar(numberlist,colorlist)
    
    
returnlists()
