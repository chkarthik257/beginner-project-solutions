####                      Watch for new TIL facts


import requests,json,sys,time,re

def f():
	
	x = requests.get('https://www.reddit.com/r/todayilearned/new.json')
	
	try:
		x.raise_for_status()
	except:
		print ('try again')
		sys.exit()
		
	y = json.loads(x.text)
	
	for i in range(3):
		a = y["data"]["children"][i]["data"]["title"]
		#removing phraseslike "TIL ", "TIL that", etc
		if 'TIL' in a:
			b = re.sub('TIL','',a,1)
			print (b)
		elif 'TIL that' in a:
			b = re.sub('TIL that','',a,1)
			print (b)
		else:
			print (a)
		time.sleep(30)
		
	
f()
