####           Mean, Median, and Mode

y = input('Enter numbers separated by a space: ').split(' ')

#removing any extra spaces 
if '' in y:
	for i in range(y.count('')):
		y.remove('')

#converting str to int
l = []
for i in y:
	l.append(int(i))
l.sort()


def mean():
	a = len(l)
	t = 0
	for i in l:
		t += i

	x = float(t)/a
	print ('mean is : %.2f'%x)

def median():
	a = len(l)
	
	#if length has an even length
	if a%2 != 0:
		print ('median is : ',l[a//2+1])
	#if length has an odd length
	else:
		print ('median is : ',l[a//2],'and',l[a//2+1])
	
def mode():  #wrong
	c = []
	d = []
	e ={}
	# Create a list of the count for each number in the list 
	#eliminating non-repeated numbers
	for i in l:
		if l.count(i) > 1:
			c.append(i)
			d.append(l.count(i))
		
	if max(d) == 2:
		for i in c:
		#eliminating repeated numbers
			if c.count(i) == 2:
				e[i] = 2
				
	elif max(d) == 3:
		for i in c:
			if c.count(i) == 3:
				e[i] = 3
		
	elif max(d) == 4:
		for i in c:
			if c.count(i) == 4:
				e[i] = 4
		
	elif max(d) == 5:
		for i in c:
			if c.count(i) == 5:
				e[i] = 5
	else:
		for i in c:
			if c.count(i) == 6:
				e[i] = 6
	
	#obtaing mode for respective possibilities
	f = []
	for i in e.keys():
		f.append(i)
	
	print('mode is ',f)

mean()
median()
mode()
