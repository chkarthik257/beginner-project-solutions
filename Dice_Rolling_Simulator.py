#######                       Dice Rolling Simulator


from random import randint

def f():
	#list containing results of dice rolls 
	c = []
	for i in range(b):
		c.append(randint(1,a))
		
	#dict of numbers and their respective occurrences	
	e = {}	
	for i in c:
		d = c.count(i)
		e[i] = d
	
	for i in e.keys():
		print ('no of times %d number came up is :%d percentage is : %.2f'%(i,e[i],(e[i]*100/b)))

while True:
	try:
		while True:
		#error handling
			try:
				a = int(input('amount of sides on a dice : '))
			except ValueError:
				print ('I need a positive integer ')
				continue
			if not a > 0:
				print("I need a positive integer(>0)")
			else:
				break
		while True:
			try:
				b = int(input('no of times dice should be rolled : '))
			except ValueError:
				print ('I need a positive integer ')
				continue
			if not b > 0:
				print("I need a positive integer(>0)")
			else:
				break
		f()
		print ('\n')
	except:
		break
