######                         A Variation of 21

from random import choice

gs = 100

p = '_clubs'
q = '_diamonds'
r = '_hearts'
s = '_spades'

m = 'ACE_'
j = 'jack_'
k = 'king_'
n = 'queen_'

#dict containing 52 cards 
di = {m+p:1,'2'+p:2,'3'+p:3,'4'+p:4,'5'+p:5,'6'+p:6,'7'+p:7,'8'+p:8,'9'+p:9,'10'+p:10,j+p:10,k+p:10,n+p:10,
m+q:1,'2'+q:2,'3'+q:3,'4'+q:4,'5'+q:5,'6'+q:6,'7'+q:7,'8'+q:8,'9'+q:9,'10'+q:10,j+q:10,k+q:10,n+q:10,
m+r:1,'2'+r:2,'3'+r:3,'4'+r:4,'5'+r:5,'6'+r:6,'7'+r:7,'8'+r:8,'9'+r:9,'10'+r:10,j+r:10,k+r:10,n+r:10,
m+s:1,'2'+s:2,'3'+s:3,'4'+s:4,'5'+s:5,'6'+s:6,'7'+s:7,'8'+s:8,'9'+s:9,'10'+s:10,j+s:10,k+s:10,n+s:10}

x = []
y = []
y1 = di.keys()
for i in y1:
	y.append(i)

x1 = di.keys()
for i in x1:
	x.append(i)

for i in range(1,6):
	t = 0
	a = choice(x)
	print ('first card is : %s'%a)
	x.remove(a)
	b = choice(x)
	print ('second card is : %s'%b)
	x.remove(b)
	rs = di[a]+di[b]
	
	if rs <= 12:
		c = choice(x)
		print ('third card is : %s'%c)
		x.remove(c)
		d = choice(x)
		print ('fourth card is : %s'%d)
		x.remove(d)
		ss = di[c]+di[d]
		rs += ss
		
		if rs <= 21:
			print ('\n**round no : %d  , ur score : %d '%(i,rs))
			t += (21-rs)
			gs -= t
		elif rs > 21:
			print ('\n**round no : %d  , ur score : %d '%(i,rs))
			print ('**score exceeds 21. so u r busted')
			t += 21
			gs -= t
		
	elif rs > 21:
		print ('\n**round no : %d  , ur score : %d '%(i,rs) )
		print ('**score exceeds 21. so u r busted')
		t += 21
		gs -= t
	else:
		t += (21-rs)
		print ('\n**round no : %d  , ur score : %d '%(i,rs))
		gs -= t
	print ('**current game score is : %d'%t)
	print ('\n')
	x = y

print ('\nur total game score is : %d'%(gs))

#ranking
if gs >= 90 and gs <= 100:
	print ('ur rank is A')
elif gs >= 80 and gs <= 89:
	print ('ur rank is B')
elif gs >= 70 and gs <= 79:
	print ('ur rank is C')
elif gs >= 60 and gs <= 69:
	print ('ur rank is D')	
elif gs >= 50 and gs <= 59:
	print ('ur rank is E')
else:
	print ('ur rank is F')
