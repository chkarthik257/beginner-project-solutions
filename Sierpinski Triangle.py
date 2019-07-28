#######                     Sierpinski Triangle

from turtle import Turtle,Screen
import sys


#midpoints
def m(a,b):
	return ((a[0]+b[0])/2,(a[1]+b[1])/2)

# Triangle
def q(p):
	x.up()
	x.goto(p[0][0],p[0][1])
	x.down()
	x.goto(p[1][0],p[1][1])
	x.goto(p[2][0],p[2][1])
	x.goto(p[0][0],p[0][1])
	
#depth and recursion
def d(p,depth):
	q(p)
	if depth > 0:
		d([p[0], m(p[0], p[1]),m(p[0], p[2])],depth - 1)
		d([p[1], m(p[0], p[1]),m(p[1], p[2])],depth - 1)
		d([p[2], m(p[2], p[1]),m(p[0], p[2])],depth - 1)
	
s = Screen()
s.bgcolor('light blue')
s.title('Sierpinski Triangle')

x = Turtle()
x.speed(7)
x.pencolor('red')

# points
p = [[-200,-100],[0,200],[200,-100]]

d(p,int((sys.argv)[1]))

s.exitonclick()
