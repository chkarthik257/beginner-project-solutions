#####                          99 Bottles

def b1():
 
    for x in range(1,100):
     y = 100-x
     if y > 2:
       print ('''%d bottles of beer on the wall, %d bottles of beer.
Take one down, pass it around, %d bottles of beer on the wall...\n''' %(y,y,(y-1)))
     elif y == 2 :
       print ('''2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall...\n''')
     elif y == 1:
       print ('''1 bottle of beer on the wall, 1 bottle of beer.
Take one down, pass it around, No more bottles of beer on the wall...\n
No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the wall...''')
	 
b1()

