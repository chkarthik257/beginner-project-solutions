########                            Scarne's Dice

from time import sleep
from random import randint
import sys

print ('welcome to Scarne\'s Dice')
sleep(1)

def f():
	t1 = 0        #User1
	t2 = 0       #User2

	while t1 <= 100 and t2 <= 100:
		a = randint(1,6)
		if a == 1:
			print ('After this round User1 you now have: %d Points'%t1)
			sleep(1)
		
		else :
			t1 += a
			print ('After this round User2 you now have: %d Points'%t1)
			while t1 <= 100 :
				x = input('press Enter to reroll or press anything else to end ur chance : ')
				if x == '':
					a1 = randint(1,6)
					if a1 == 1:
						print ('After this round User1 you now have: %d Points'%t1)
						
						sleep(1)
						break
					else:
						t1 += a1
						print ('After this round User1 you now have: %d Points'%t1)
						#return t1
						sleep(1)
						continue
			
				else:
					break
			#return t1
		b = randint(1,6)
		if b == 1:
			print ('After this round User2 you now have: %d Points'%t2)
			sleep(1)
		
		else:
		
			t2 += b
			print ('After this round User2 you now have: %d Points'%t2)
			#sleep(1)
			while  t2 <= 100:
				x = input('press Enter to reroll or press anything else to end ur chance : ')
				if x == '':
					b1 = randint(1,6)
					if b1 == 1:
						print ('After this round User2 you now have: %d Points'%t2)
					
						sleep(1)
						break
					else:
						t2 += b1
						print ('After this round User2 you now have: %d Points'%t2)
						#return t2
						sleep(1)
						continue		
				
				else:
					break
			#	return t2
			
	
				
f()		
				
				
				
			
