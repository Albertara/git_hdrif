from math import *
from time import *
from random import *



#Liður 1

rep1 = 1
while(rep1 == 1):
	summari = 1
	listi1=[]    
	for i in range (50):
	    listi1.append(randint(5,70))
	for u in listi1:
		summari = summari * u
	print("Listi talna prentaður út:", listi1)
	print("Allt margfaldað saman í listanum:", summari)
	print("Hæðsta talan í listanum er:", max(listi1))
	print("Lægsta talan í listanum er:", min(listi1))
	print("Óraðaður listi:", listi1)
	print("Raðaður listi:", sorted(listi1))

	voff = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if voff == "já" or voff == "ja":
		rep1 = 1
	else:
		rep1 = 0


#Liður 2

rep2 = 1
while(rep2 == 1):
	kall = 1
	listi2=[]
	for y in range(2000,3200,7):
		if y % 5 != 0:
			listi2.append(y)	
	print(listi2)
	for t in listi2:
		kall += t
	print(kall)
	

	mjá = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if mjá == "já" or mjá == "ja":
		rep2 = 1
	else:
		rep2 = 0




#Liður 3

rep3 = 1
while(rep3 == 1):
	listi3=[]




	krókódíll = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if krókódíll == "já" or krókódíll == "ja":
		rep3 = 1
	else:
		rep3 = 0