######                     Change Calculator

def c():
	
	x = float(input('amount of money given to you in dollars: '))
	y = float(input('price of the item in dollars: '))
#dollars to pennies
	z = (x - y)*100
	z = int(z)                    
#different coins for different amount of change	
	d = {'quarters':0,'dimes':0,'nickels':0,'pennies':0}
	e = z - (z//25)*25
	f = e - (e//10)*10
	g = f - (f//5)*5
	
	if z>=25:
		d['quarters'] = (z//25)
	if e>=10:
		d['dimes'] = e//10
	if f>=5:
		d['nickels'] = f//5
		d['pennies'] = g
	if z<5:
		d['pennies'] = z
	print ('\nchange needed --> quarters: %d, dimes: %d, nickels: %d, pennies: %d\n'%(d['quarters'],d['dimes'],d['nickels'],d['pennies']))

while True:
	a = input('if u want to calculate change press Enter or press anything else to exit: ')
	a.lower()
	if a == '':
		c()
	else:
		break
  
