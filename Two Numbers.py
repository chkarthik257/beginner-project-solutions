#####                      Two Numbers

from random import choice

z = input('Give an array of integers separated by commas : ')
x = [int(i) for i in z.split(',')]
y = int(input('target value : '))

#list containing required numbers
l = []
for i in x:
	if (y-i) in x:
		a = x.index(i)
		b = x.index(y-i)
		if a != b:
			l.append(a)
			l.append(b)

#removing repetitons
for i in l:
	if l.count(i) > 1:
		l.remove(i)


if l == []:
	print ("None of these numbers add up to " + str(y))

else:
	print ('two numbers : ' + str(sorted(l)))
