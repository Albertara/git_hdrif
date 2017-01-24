from math import *
from time import *
import random




valmynd = 1
while(valmynd == 1):
	print("")
	print("Til að velja lið, skráðu inn töluna sem passar við hann")
	print("1. Skrifa tölur 255-4000 VARÚÐ: ÞAÐ TEKUR MJÖG LANGANN TÍMA AÐ PRENTA ALLT ÞETTA ÚT")
	print("2. Slembitölur")
	print("3. Strengir")
	print("4. Hætta og loka forriti")
	val = int(input("Veldu þér lið (type 1-4): "))


	if val == 1:
		#Liður 1
		listi1 = []
		#Mæli með að breyta 4001 í eitthvað minna þar sem það tekur óhemju langann tíma að prenta allt þetta út, veit ekki af hverju. Kannski bara talvan.
		for listi1 in range(255,4001):
			print(listi1, end=" ")


	elif val == 2:
		#Liður 2, ekki kláraður

		listi2 = []
		for i in range(200):
			listi2.append(random.randint(190,1000))
		print(listi2)
		sleep(2)

	elif val == 3:
		#Liður 3

		print("Sláðu inn settningu: ")
		string_input = input()
		input_list = string_input.split()
		input_list = [str(a) for a in input_list]
		x = len(input_list)
		print("Fjöldi orða er: ", x)
		print("Settningin með lágstöfum: ", string_input.lower())
		txt = string_input
		#Fann ekki út á tíma hvernig á að replacea öllu nema e með ?. Svo hérna er allur strengurinn skiptur út með einu ?
		print(txt.replace(txt, "?"))
		sleep(3)



	elif val == 4:
		print("Þú hefur valið að hætta")
		sleep(1)
		exit()

#Eins og þú sérð kannski þá vil ég helst taka minn tíma í að gera verkefnin svo ég geti pælt vel út í öllu. Er heldur ekki nógu klár á að vinna með tölur í listum.