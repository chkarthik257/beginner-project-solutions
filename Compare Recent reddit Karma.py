######                         Compare Recent reddit Karma


import requests as req
import json,sys


def f(u):
	url = 'https://www.reddit.com/user/' + u + '.json'
	
	x = req.get(url = url)
	'''
	x1 = x.status_code
	if x1 == False:
		print ('sorry try again')
		sys.exit()
	'''
	try :
		x.raise_for_status()
	except:
		print ('sorry try again')
		sys.exit()
	
	#y = json.loads(x.text)
	y = x.json()
	
	t = 0
	for i in range(5):
		a = y["data"]["children"][i]["data"]["score"]
		print ('score of %d for the most recent post %d.'%(a,i))
		t += a
	print ('Total score of %d for the 5 most recent posts.'%t)
	return t

# User 1
u1 = input("Enter the first username : ")
u1_t = f(u1)

# User 2
u2 = input("Enter the second username : ")
u2_t = f(u2)

# Final scoring
print("\n")
if u1_t > u2_t:
	print(username1 + " wins over " + username2 + " by a margin of " + str(u1_t - u2_t))
elif u1_t < u2_t:
	print(username2 + " wins over " + username1 + "by a margin of " + str(u2_t - u1_t))
else:
	print("It's a tie!")


