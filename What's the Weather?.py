#####                        What's the Weather?

import requests as req

import json,sys

u = 'https://fcc-weather-api.glitch.me/api/current?lat=77.22&lon=28.67'

r1 = req.get(url = u)
r = r1.json()

'''
try:
	r.raise_for_status()
except:
	print ('try again')
	sys.exit()
'''	
a1 = r['weather'][0]['description']
a2 = r['main']['temp']
a3 = r['main']['pressure']
a4 = r['main']['humidity']
a5 = r['main']['temp_min']
a6 = r['main']['temp_max']
a7 = r['sys']['country']
a8 = r['name']
a = 'today\'s weather at %s in %s is \n ...%s... \n temp:%f degrees Celsius \n pressure:%f hpa\n humidity:%f\n temp_min:%f degrees Celsius\n temp_max:%f degrees Celsius'%(a8,a7,a1,a2,a3,a4,a5,a6)
print(a)

with open('p34.txt','r+') as b:
	b.write(a)
