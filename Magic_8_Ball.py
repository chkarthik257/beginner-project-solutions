###            Magic 8 Ball

import random

l = ['It is certain.','It is decidedly so.',' Without a doubt.','Yes - definitely.',' You may rely on it.',
 'As I see it, yes.',' Most likely.',' Outlook good.',' Yes.',' Signs point to yes.',' Reply hazy, try again.',
 'Ask again later.',' Better not tell you now.','Cannot predict now.',' Concentrate and ask again.',
 ' Don\'t count on it.',' My reply is no.',' My sources say no.','Outlook not so good.','Very doubtful.'] 
 
for x in range (20):
   r = random.choice(l)    
   x2 = input('Ask the magic 8 ball a question or (press enter to quit)\n-->  ')
   if x2 =='':                                                                          
       break
   print ('wait a moment .....\nanswer is : '+ r)
   
