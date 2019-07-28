##                        Coin Estimator By Weight
  
 
#user's input 
a1 = input('in which mode r u submitting the weight : (grams or pounds)\n--> ' )
v = 453.592

a = float(input('\ntotal weight of \'pennies\' you have in grams \n -->' ))
b = float(input('\ntotal weight of \'nickels\' you have in grams \n -->' ))
c = float(input('\ntotal weight of \'dimes\' you have in grams \n -->'  ))
d = float(input('\ntotal weight of \'quarters\' you have in grams \n -->' ))

#converting weight from pounds to grams
aa = a*v
bb = b*v
cc = c*v
dd = d*v

if a1.lower() == 'pounds' :
  a = aa
  b = bb
  c = cc  
  d = dd
   
# weight of each coin in grams
e= 2.5
f= 5.0
g= 2.26
h= 5.67

# coins you have

p = a//e
q = b//f
r = c//g
s = d//h

print ('\n')
print ('pennies, you have  ',p)
print ('nickels, you have  ',q)
print ('dimes, you have  ',r)
print ('quarters, you have  ',s)
print ('\n')

# wrapper you would need
'''
red colour wrappers for pennies can contain 50 coins
blue colour wrappers for nickels can contain 40 coins
green colour wrappers for dimes can contain 50 coins
orange colour wrappers for quarters can contain 40 coins
'''

i = p/50
j = q/40
k = r/50
l = s/40


if i > 0 and i <= 1:
   i += 1
if j > 0 and j <= 1 :
   j += 1
if k > 0 and k <= 1 :
   k += 1
if l > 0 and l <= 1 :
   l += 1
 
print ('u will need %d red colour wrappers for pennies'%i)
print ('u will need %d blue colour wrappers for nickels'%j)
print ('u will need %d green colour wrappers for dimes'%k)
print ('u will need %d orange colour wrappers for quarters'%l)

#estimated total value of all of their money.

x = p*1 + q*5 + r*10 + s*25
y = x/100

print ('\n')
print ('estimated total value of all of their money " %f " in dollars'%y)

