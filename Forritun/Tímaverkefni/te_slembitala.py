from random import *
from math import *
from time import *


#liður 1

a = 1
while(a == 1):
	for i in range(10):	
		print (randint(1,20), end=" ")
	print("\r\n")
	voff = str(input("Viltu keyra forritið aftur?(já/nei)"))
	if voff == "nei":
		a = 0


#liður 2


yo = 1
while(yo == 1):
	t1 = randint(1,6)
	t2 = randint(1,6)
	t3 = randint(1,6)

	print("Teningur 1:" , t1)
	print("Teningur 2:" , t2)
	print("Teningur 3:" , t3)


	if t1 == t2 == t3:
		print ("Allir teningar eru eins")
	elif t1 == t2:
		print ("2 teningar eru eins")
	elif t1 == t3:
		print ("2 teningar eru eins")
	elif t2 == t3:
		print ("2 teningar eru eins")
	else:
		print ("Engir teningar eru eins")
	blub = str(input("Viltu keyra forritið aftur?(já/nei)"))
	if blub == "nei":
		yo = 0

#liður 3

teljari = 0
g = 1
while(g == 1):
	teljari += 1
	print ("Reyndu að finna töfra töluna ╰( ⁰ ਊ ⁰ )━☆ﾟ.*･｡ﾟ: ")
	teningur = randint(1,10)
	swag = int(input("Sláðu inn heiltölu(1-10): "))
	if swag == teningur:
		print("Þú giskaðir á töfratöluan ╰( ⁰ ਊ ⁰ )━☆ﾟ.*･｡ﾟ, það tók þig" , teljari , "tilraunir")
		teljari = 0
		vondur = str(input("Viltu keyra þetta forrit aftur?(já/nei):"))
		if vondur == "nei":
			print ("Bless")
			exit()
