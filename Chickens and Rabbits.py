####                           Chickens and Rabbits


def f(x,y):	
	for a in range(x):
		b = x-a
		if 2*a+4*(b) == y:
			return a,b

#heads
x = 35
#legs     
y = 94
print (f(x,y))
