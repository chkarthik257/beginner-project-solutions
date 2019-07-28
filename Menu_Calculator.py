######                          Menu Calculator


print ('''
1. Chicken Strips - $3.50
2. French Fries - $2.50
3. Hamburger - $4.00
4. Hotdog - $3.50
5. Large Drink - $1.75
6. Medium Drink - $1.50
7. Milk Shake - $2.25
8. Salad - $3.75
9. Small Drink - $1.25

please take orders :

 For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered,
the u should type in 5993348 

''')
def x():
	a = input('ur order : ')
	b = [i for i in a]
	#creating menu dict
	c = {1:{'Chicken Strips':3.50},2:{'French Fries':2.50},3:{'Hamburger':4.00},
	4:{'Hotdog':3.50},5:{'Large Drink':1.75},6:{'Medium Drink':1.50},
	7:{'Milk Shake':2.25},8:{'Salad':3.75},9:{'Small Drink':1.25}}
	#creating price dict
	d = {1:3.50, 2:2.50, 3:4.00, 4:3.50, 5:1.75, 6:1.50, 7:2.25, 8:3.75, 9:1.25}
	#creating item dict
	e = {1:'Chicken Strips', 2:'French Fries', 3:'Hamburger',4:'Hotdog', 5:'Large Drink', 
	6:'Medium Drink',7:'Milk Shake',8:'Salad',9:'Small Drink'}
	
	f = {}
	
	t = 0
	for i in a:
		t += d[int(i)]

	for i in b:
		n = b.count(i)
		if n>1:
			f[i] = n
		else:
			f[i] = 1
	#printing order
	for i in f.keys():
		print ('item name: %s  count: %d'%(e[int(i)],f[i]))
	
	print ('total cost: $%.2f'%t)

x()

while True:
	y = input('if u wanna exit press x or press Enter to continue : ')
	if y == '':
		x()
	else:
		break
