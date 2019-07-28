####                    Turn Based Pokemon Style Game

from random import choice,randint
from sys import exit

print ('''let's play a game...

it's simple game that allows u and the computer to take turns selecting moves to use against each other...

Both the computer and u will start out at the same amount of health (such as 100), and should be able to
choose between the three moves:

a)The first move should do moderate damage and has a small range (such as 18-25).
          ** press a to select this move **
b) The second move should have a large range of damage and can deal high or low damage (such as 10-35).
          ** press b to select this move **

c)The third move should heal whoever casts it a moderate amount, similar to the first move (such as 10-20).
          ** press c to select this move **

                          Once ur health reaches 0, u lose...
						  
''')

#health of user
hu = 100
#health of computer
hc = 100

def fc():	
	global hc
	global hu
	#computer choices
	cc = choice(['a','b','c'])
	#The first move
	r1 = randint(18,25)
	#The second move
	r2 = randint(20,35)
	#The third move
	r3 = randint(10,20)

	if cc == 'a':
		print ('computer chose first move')
		hu -= r1
		if hu <= 0:
			print ('ur health is : 0')
			print ('computer wins. u lose.. better luck next time..')
			exit()
		else:
			print ('ur health is : %d'%hu)
		return hu,hc

	elif cc == 'b':
		print ('computer chose first move')
		hu -= r2
		if hu <= 0:
			print ('ur health is : 0')
			print ('computer wins. u lose.. better luck next time..')
			exit()
		else:
			print ('ur health is : %d'%hu)
		return hu,hc

	elif cc == 'c':
		print ('computer chose first move')
		hu -= r3
		if hu <= 0:
			print ('ur health is : 0')
			print ('computer wins. u lose.. better luck next time..')
			exit()
		else:
			print ('ur health is : %d'%hu)
		return hu,hc


def f():
	global hc
	global hu
	#user choices
	cc = choice(['a','b','c'])
	#The first move
	r1 = randint(18,25)
	#The second move
	r2 = randint(20,35)
	#The third move
	r3 = randint(10,20)
	
	pc = input('please choose between a,b,c : ')

	if pc == 'a':
		print ('u chose first move')
		hc -= r1
		if hc <= 0:
			print ("computer's health is : 0")
			print ('u win.. congrats ')
			exit()
		elif hc < 35 and hc > 25:
			hc += r3
		else:
			print ("computer's health is : %d"%hc)
			fc()
		return hc,hu
		
	elif pc == 'b':
		print ('u chose second move')
		hc -= r2
		if hc <= 0:
			print ("computer's health is : 0")
			print ('u win.. congrats ')
			exit()
		elif hc < 35 and hc > 25:
			hc += r3
		else:
			print ("computer's health is : %d"%hc)
			fc()
		return hc,hu

	elif pc == 'c':
		print ('u chose third move')
		hc -= r3
		if hc <= 0:
			print ("computer's health is : 0")
			print ('u win.. congrats ')
			exit()
		elif hc < 35 and hc > 25:
			hc += r3
		else:
			print ("computer's health is : %d"%hc)
			fc()
		return hc,hu



x = input('if wanna play press Enter or press anything to exit : ')

while True:
	
	
	if x == '':
		f()
	else:
		break	
	
	
	
	
