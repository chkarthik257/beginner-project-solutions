#####              Fibonacci Sequence               


l = [1,1]
n = int(input('please type any integer : '))
for i in range(0,n-1):
	x = l[i]+l[i+1]
	l.append(x)

print ('Fibonacci Sequence is : ',l)
print ('%dth term in sequence is :'%n, l[n-1])



'''
# using recursion
def f(n):
	y = l[n-1]+l[n-2]
	l.append(y)
	return f(n-1)
	
f(x)
print (l)
'''
