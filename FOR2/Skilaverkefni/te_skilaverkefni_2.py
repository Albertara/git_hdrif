from math import *

#Liður 1, MinnstaTala2
"""
tala1 = int(input("Sláðu inn tölu1: "))
tala2 = int(input("Sláðu inn tölu2: "))
tala3 = int(input("Sláðu inn tölu3: "))

if (tala1 < tala2 < tala3 or tala3 < tala2 < tala1):
	print(tala2, "er í miðjunni")
elif (tala2 < tala3 < tala1 or tala1 < tala3 < tala2):
	print(tala3, "er í miðjunni")
elif (tala3 < tala1 < tala2 or tala2 < tala1 < tala3):
	print(tala1, "er í miðjunni")






#Liður 2, Tommur_Sentimetra

print ("Sláðu inn t til að reikna tommu í sentimetra: ")
print ("Sláðu inn s til að gera það öfugt: ")
svar = input()

if(svar == "t"):
	print ("Reiknum tommur yfir í CM")
	x = float(input("Tala í tommum: "))
	print("Talan í CM er: " , x*2.54)
elif(svar == "s"):
	print("Reiknum CM yfir í tommur")
	y = float(input("Tala í CM: "))
	print("Talan í tommum er: " , y/2.54)
else:
	print("Bull og vitleysa")


"""






#Liður 3, Arstidir


x = int(input("Tala mánaðar (1-12): "))
if (x == 1 or x == 2 or x == 3):
	print ("Núna er mjög kalt")
elif (x == 4 or x == 5):
	print ("Núna er ekki jafn kalt")
elif (x == 6 or x == 7 or x == 8):
	print ("Núna er ekki kalt")
elif (x == 9 or x == 10):
	print ("Núna er vont veður. Og kalt")
elif (x == 11 or x == 12):
	print ("Nú er skítkalt")
else:
	print ("Þú kannt ekki mánaðartölur")






#Liður 4, NafnManadar









#Liður 5, Talnabil