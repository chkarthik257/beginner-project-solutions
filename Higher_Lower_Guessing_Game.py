#######                            Higher Lower Guessing Game


from random import randint

print '''
"This is simple game where the computer randomly selects a number between 1 and 100 
	 and u have to guess what the number is" \n'''

def x():
	#random number
	a = randint(1,100)
	# user's guess
	b = int(raw_input('\nguess the number between 1 and 100 : '))
	t = 1
	while True:
		if a == b:
			print 'u guessed correctly. "congrats"'
			print 'ur score -> no of guesses : %d'%t
			break
			
		else:
			
			if a>b :
				print 'guess is lower'	
				b = int(raw_input('\nguess again : '))
				t += 1
			elif a<b:
				print 'guess is higher'
				b = int(raw_input('\nguess again : '))
				t +=1

x()

while True:
	y = raw_input('if u wanna play again press Enter or press anthing else to exit : ')
	if y == '':
		x()
	else:
		break
	
