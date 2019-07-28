###            Base Jumper

def f():
	a = int(input('number to convert: '))
	b = int(input('The base the number is in: '))
	c = int(input('the base to convert the number to,(that is in the range of 2 to 16 inclusive) : '))
	if not c in range(2,17):
		print ('please enter the number that is in the range of 2 to 16 inclusive')
		c = int(input('--> '))
		
# Decimal to Other Base System
	if b == 10:
		t1 = []
		while True:
			t2 = a%c
			t3 = a//c
			t1.append(t2)
			a = t3
			if t3 == 0:
				break
		t1 = t1[::-1]
		t4 = []
		for i in t1:
			t4.append(str(i))
		t5 = ''.join(t4)
		print ('converted number is : ',t5)
		
#Other Base System to Decimal System
	elif c == 10:
		a = str(a)
		l = len(a)
		t = 0
		for i in range(l):
			s = int(a[i])*(b**((l-1)-i))
			t += s
			
		print ('converted decimal number : ',t)
		
#Other Base System to Non-Decimal System
	elif b!= 10 and c !=10:
		a = str(a)
		l = len(a)
		t = 0
		for i in range(l):
			s = int(a[i])*(b**((l-1)-i))
			t += s
		t1 = []
		while True:
			t2 = t%c
			t3 = t//c
			t1.append(t2)
			t = t3
			if t3 == 0:
				break
		t1 = t1[::-1]
		t4 = []
		for i in t1:
			t4.append(str(i))
		t5 = ''.join(t4)	
		print ('converted number is: ',t5)
		

f()

while True:
	x = input('if u want to convert another number press Enter or to exit press anything: ')
	if x =='':
		f()
	else:
		break
		
