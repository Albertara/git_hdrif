from math import *
from time import *
from random import *


#Liður 1


loop = 1
while(loop == 1):

	amount = int(input("Sláðu inn lengd í sentimetrum: "))


	metri = amount // 100
	amount = amount % 100

	desimetri = amount // 10
	amount = amount % 10

	sentimetri = amount

	print ("Þetta gera: ")

	if metri > 0:
		print(metri , "metrar")
	if desimetri > 0:
		print(desimetri , "desimetrar")
	if sentimetri > 0:
		print(sentimetri , "sentimetrar")
	print("")


	voff = str(input("viltu keyra forritið aftur? (já/nei): "))

	if voff == "já" or voff == "ja" or voff == "j":
		loop = 1
	else:
		loop = 0




#Liður 2

laap = 1
while(laap == 1):

	x = int(input("Sláðu inn heiltölu: "))
	n = int(input("Sláðu inn veldisvísi: "))

	svar = x**n

	for veldi in range(1):
		print(x , "í" , n , "veldi er" , svar)

	mjá = str(input("viltu keyra forritið aftur? (já/nei): "))

	if mjá == "já" or mjá == "ja" or mjá == "j":
		laap = 1
	else:
		laap = 0




#Liður 3

luup = 1
while(luup == 1):

	n = 0
	v = int(input("sláðu inn tölu á bilinu 1-9: "))

	if v > 9:
		print("Þetta var ekki tala á bilinu 1-9, reyndu aftur")
	else:

		for u in range (0,v):
		    n = n + 1
		    for a in range (0, n-1):
		        print ('*', end = '')
		    print()

		for b in range (0,v):
		    n = n - 1
		    for d in range (0, n+1):
		        print ('*', end = '')
		    print()

		baa = str(input("viltu keyra forritið aftur? (já/nei): "))

		if baa == "já" or baa == "ja" or baa == "j":
			luup = 1
		else:
			luup = 0


