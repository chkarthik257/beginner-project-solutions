####                         Factors of a Number


def f(n):
	l = []
	#for zero
	if n == 0:
		l.append(0)
	#negative numbers
	elif n<0:
		for i in range(n,-n+1):
			if i == 0:
				pass
			elif n%i == 0:
				l.append(i)
	#positive numbers
	else:
		for i in range(-n,n+1):
			if i == 0:
				pass
			elif n%i == 0:
				l.append(i)

	#sorting
	l.sort()
	a = []
	for i in l:
		a.append(str(i))
		
	print (','.join(a),'\n')
	#prime numbers
	if len(l) == 4:
		print ('given number is prime')


x = int(input('type an integer : '))
f(x)

while True:

	x = input('type an integer or press Enter to quit : ')
	if x == '':
		break
	else:
		x = int(x)
		f(x)
