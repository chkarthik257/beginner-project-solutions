###                                 Rock Paper Scissors Game


import random

def r():
#computer's choice
 z = ['rock', 'paper', 'scissors']
 x = random.choice(z)

#Compare the choices and decide who wins
 if b == x:
    print ('pick again')
      
 elif b == 'rock' and x == 'paper' :
    print ('paper covers rock ',  'computer wins')
    
 elif b == 'rock' and x == 'scissors':
    print ('rock crushes scissors',  'you win')
    
 elif b == 'paper' and x == 'rock' :
    print ('paper covers rock ',  'you win')
    
 elif b == 'paper' and x == 'scissors' :
    print ('scissors cuts paper ',  'computer wins')
    
 elif b == 'scissors' and x == 'rock' :
    print ('rock crushes scissors ', 'computer wins')
    
 elif b == 'scissors' and x == 'paper' :
    print ('scissors cuts paper ',  'you win')
    
    
while True:
  a = input('\npick rock, paper or scissors  or  (press enter to quit)\n-->'   )
  b = a.lower()
  if b == '':
      break  
#error handling
  elif b != 'rock' and b != 'paper' and b != 'scissors' :
     raise ValueError('please pick between rock, paper or scissors  only') 
     
  else :
       r()

