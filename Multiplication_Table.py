######                      Multiplication Table


r=9
#creating row
for i in range(1,r+1):
	j = 1
	#creating column
	while j in range(1,r+1):		
		y = '%2d * %2d = %3d || '%(j,i,j*i)
		j += 1
		print (y, end=' ') 
		
			
	print ('\n')


def x():
	for i in range(1,r+1):
		j = 1
		while j in range(1,r+1):		
			y = '%2d * %2d = %3d || '%(j,i,j*i)
			j += 1
			print (y, end=' ') 
		
		print ('\n')
while True:
	r = input('choose a number to change the size of the table or press Enter to exit: ')
	print ('\n')
	if r == '':
		break
	else:
		r = int(r)
		x()
		
