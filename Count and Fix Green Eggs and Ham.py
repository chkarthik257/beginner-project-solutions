#####                          Count and Fix Green Eggs and Ham

a = open('p25.txt','r+')
c = a.readlines()
d = len(c)
a.close()

#reopen file
a = open('p25.txt','r+')
e = 'Sam-i-am!'
f = 'Sam-i-am'
g = 'Sam-i-am.'
#changing I in Sam-i-am
e1 = e.split('-')
e1[1] = 'I' 
e2 = '-'.join(e1)

f1 = e.split('-')
f1[1] = 'I' 
f2 = '-'.join(f1)

g1 = g.split('-')
g1[1] = 'I' 
g2 = '-'.join(g1)


z = []
t = 0
for i in range(d):
	b = (a.readline()).split()
	if len(b)>=1:
		
		if b[0] == 'i':
			b[0] = 'I'
			t += 1
		#changing I in Sam-i-am
		if e in b :
			b[-1] = e2
			t += 1
		if f in b :
			b[-1] = f2
			t += 1
		if b[0] == 'i' and e in b : 
			b[0] = 'I'
			b[-1] = e2
			t += 1
		if f in b and b[0] == 'i':
			b[0] = 'I'
			b[-1] = f2
			t += 1
		if g in b:
			b[-1] = g2
			t += 1
		if b[0] == 'i' and g in b : 
			b[0] = 'I'
			b[-1] = g2
			t += 1
			
	h = ' '.join(b)
	z.append(h)
	
print (t)
s = '\n'.join(z)	

a.close()

x = open('p25_1.txt','w')
x.write(s)	
			
x.close()			
	
