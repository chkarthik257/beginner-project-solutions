###                     Pythagorean Triples Checker



def x():
#Allows the user to input the sides of any triangle in any order
	try:
		a = float(input('input the length of side of the triangle  -->  '))
		
	except ValueError:
		a = float(input('please enter valid number  -->  '))
		
	try:
		b = float(input('input the length of side of the triangle -->  '))
				
	except ValueError:
		b = float(input('please enter valid number -->  '))
		
	try:
		c = float(input('input the length of side of the triangle -->  '))
	
	except ValueError:	
		c = float(input('please enter valid number -->  '))

#checking whether the triangle is a Pythagorean Triple or not
	x = (a)**2 + (b)**2
	y = (c)**2
  
	if x == y:
		print ('the triangle is a Pythagorean Triple')
	else :
		print ('the triangle is "not" a Pythagorean Triple')
		
#Loop the program so the user can use it more than once without having to restart the program.

while True:
	x()
	
