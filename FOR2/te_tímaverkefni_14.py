from math import *
from time import *
from random import *



#Liður 1
"""
rep1 = 1
while(rep1 == 1):
	listi1 = []
	for i in range(5):
		listi1.append(randint(1,10))
	print("Random listi:" , listi1)
	seinast = listi1[4]
	fyrstasta = listi1[0]
	listi1[0] = seinast
	listi1[4] = fyrstasta
	print("Svissað á fyrsturstu tölunni og einustu tölunni:" , listi1)

	voff = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if voff == "já" or voff == "ja":
		rep1 = 1
	else:
		rep1 = 0


#Liður 2

rep2 = 1
while(rep2 == 1):
	listi2 = []
	for o in range(5):
		listi2.append(randint(1,10))
	print("Random listi:" , listi2)
	listi2.reverse()
	print("Listi viðsnúinn:" , listi2)

	mjá = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if mjá == "já" or mjá == "ja":
		rep2 = 1
	else:
		rep2 = 0


#Liður 3

rep3 = 1
while(rep3 == 1):
	listi3 = []
	for p in range(5):
		listi3.append(randint(1,10))
	print("Random listi:" , listi3)
	listi3.sort()
	print("Listi raðaður:" , listi3)

	blob = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if blob == "já" or blob == "ja":
		rep3 = 1
	else:
		rep3 = 0


#Liður 4

rep4 = 1
while(rep4 == 1):
	listi4 = []
	for ð in range(5):
		listi4.append(randint(1,10))
	print("Random listi:" , listi4)
	listi4.sort(reverse=True)
	print("Listi raðaður:" , listi4)

	muu = str(input("Viltu keyra forritið aftur eða halda áfram í lífinu? (já/nei): "))

	if muu == "já" or muu == "ja":
		rep4 = 1
	else:
		rep4 = 0
"""

#Liður 5

rep5 = 1
while(rep5 == 1):
	listi5 = []
	print("a. Bæta nýju innslegnu nafni við listann.")
	print("b. Eyða ákveðnu (innslegnu) nafni úr lista.")
	print("c. Athuga hvort ákveðið nafn (innslegið) sé í lista.")
	print("d. Prenta lista eins og hann kemur fyrir í forriti.")
	print("e. Prenta lista í stafrófsröð.")

	klonk = str(input("þú velja a,b,c,d,e: "))

	if klonk == "a" or klonk == "A":
		bætanafn = str(input("Láðu inn nafn sem þú vilt bæta við listann: "))
		listi5.append(bætanafn)
		print("Nafnið sem þú bættir við listann er:", bætanafn)
		print("")
		sleep(1.1)

	elif klonk == "b" or klonk == "B":
		

