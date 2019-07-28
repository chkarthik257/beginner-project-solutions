#####              Fibonacci Sequence               


l = [1,1]
n = int(raw_input('give no'))
for i in range(0,n-1):
	x = l[i]+l[i+1]
	l.append(x)

print 'Fibonacci Sequence is : ',l
print 'nth term in sequence is :', l[n-1]

print '***********************************'

'''
# using recursion
def f(n):
	y = l[n-1]+l[n-2]
	l.append(y)
	return f(n-1)
	
f(x)
print l
'''
