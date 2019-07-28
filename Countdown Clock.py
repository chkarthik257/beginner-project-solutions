
#####                            Countdown Clock



from time import *

def f():

	t = input('please enter "future" time in (hours min sec) format with space between them: ')
	d = input('please enter "future" date in (dd mm yy) format with space between them: ')

	z = d + ' ' + t
	#converting string representing time to struct_time
	try :
		x = strptime(z,"%d %m %Y %H %M %S")
	except ValueError:
		x = strptime(z,"%d %B %Y %H %M %S")
	finally:                   
		
		#seconds passed since epoch to struct_time in local time
		c = mktime(x)
		#the number of seconds passed since epoch
		a = time()
		
		d = c - a
		for i in range (0,int(d),3):
			print ('ramaining time in seconds : ', d-i)
			print ('\n')
			sleep(3)
	
f()
	
while True:
	x = input('press Enter to quit or press anything to start over : ')
	if x == '':
		break
	else:
		sleep(1)
		f()
