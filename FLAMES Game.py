####                         FLAMES Game

import sys


x1 = input ('give ur name : ')
y1 = input ('give ur partners\'s name : ')
f1 = 'FLAMES'
f = [i for i in f1]

d = {'F':'Friends','L':'Lovers','A':'Affection','M':'Marriage','E':'Enemies','S':'Siblings'}

x =[i for i in x1]
y =[i for i in y1]

z1 = x + y
p1 = len(z1)
#print (f[2:])

#remove_match_chars if common character is found
for i in x:
	if i in y:
		j = z1.count(i)
		if j > 1 :
			for k in range(j):
				z1.remove(i)

# if no common characters is found
p = len(z1)
if p == p1:
	print ('no common characters')
	sys.exit()


while len(f) > 1:                #imp
	
	a = p % len(f) - 1
	
	# anticlock-wise circular fashion counting
	if a >= 0:      #ramaining characters more than 6
		
		b = f[a+1 :]
		c = f[: a]
		
		f = b + c
	else:           #ramaining characters less than 6
		f = f[:len(f)-1]
		
		
print("Relationship status is :", d[f[0]])

