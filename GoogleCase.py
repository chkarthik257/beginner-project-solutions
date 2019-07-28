########                          GoogleCase


x = input ('please enter ur sentence here : ')
x = x.upper()

#creating list
y = x.split(' ')

#turning first letter to lower case
z = []
for i in y:
	i = i.lower()	
	z.append(i[0])

y1 = []

#GoogleCase
for i in range(len(y)):
	a = y[i]
	b = z[i]
	c = [j for j in a]
	c[0] = b
	i = ''.join(c)
	y1.append(i)

# alternate solutions

'''
for i in range(len(y)):
	a = y[i][0]
	b = z[i]
	c = y[i].replace(a,b)
	y1.append(c)
	
or
	
z1 = z.title()
z2 = z1.swapcase()	
print (z2)	

'''
z1 = ' '.join(y1)

print ('\n' + z1)
