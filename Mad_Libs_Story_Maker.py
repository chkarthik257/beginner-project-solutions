##             Mad Libs Story Maker

import time,re

print ('hi , now we are going to play "Mad Libs style" game')

time.sleep(2)

a = input('\nplease input an "exclamation" type word\n--> ' )
b = input('\nplease input an "adverb" type word\n--> ' )
c = input('\nplease input an "noun" type word\n--> ' )
d = input('\nplease input an "adjective" type word\n--> ' )

#changing the first letter to a capital letter
c1 = c.capitalize()
 
x= " %s! he said %s as he jumped into his convertible %s and drove off with his %s wife.\n" %(a,b,c1,d)

y = [i for i in x.split(' ')]

#Change the word "a" to "an" when the next word in the sentence begins with a vowel
if 'a' in y:
	i = y.index('a')
	z = ['a','e','i','o','u']
	if y[i+1][0] in z:
		y[i] = 'an'

x = ' '.join(y)


print ('\nwait for it....')
time.sleep(2)
print ('\nFinally, the completed story is \n')
print (x)

