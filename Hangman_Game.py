	
			######                         Hangman Game

from random import choice
from sys import exit

print ('''........let's play Hangman game.......
u have upto 9 chances for correct guess\n''')

#random word
x ='awake bad bent bitter blue certain cold complete cruel dark dead dear delicate different dirty dry false feeble female foolish future green ill last late left loose loud low male mixed narrow old opposite public rough sad safe secret short shut simple slow small soft solid special strange thin white wrong'
y = x.split()
z1 = choice(y)
z1 = z1.lower()

z = [i for i in z1]

#blank spots for each letter in the word
l =len(z)
r = []
for i in range(l):
	r.append('-')
s = ' '.join(r)
print (s)	
a = input('guesse a letter : ')

#user guesses
def f():
	if a in z:
		for i in range(l):
			if z[i] == a:
				r[i] = a
		s1 = ''.join(r)
		print (s1)
		if s1 == z1:
			print ('congrats!! . u guessed correctly  ',z1)
			exit()
	
	else:
		print ('wrong letter\n')
	
f()

# loop
t = 0
while t<9:
	
	a = input('guesse again or if u wanna give up press Enter : ')
	if a == '':
		break
	else:
		t += 1
		f()
else:
	print ('ur 9 chances r over... u lose\ncorrect word is :',z1)
	
