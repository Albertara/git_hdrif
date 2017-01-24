from math import *
from time import *
from random import *

valmynd = 1
while(valmynd == 1):
	val = int(input("1. Kennitala, 2. Búa til nýtt orð, 3. Sneið af streng, 4. Hætta (type1-4): "))
	#Liður 1
	if val == 1:
		rep1 = 1
		while(rep1 == 1):
			kt = str(input("Sláðu inn kennitölu: "))
			kt = kt.replace("-","")
			kt = kt.replace(" ","")
			varstr = [3,2,7,6,5,4,3,2] 
			if len(kt) != 10 or int(kt[0:2]) > 31 or int(kt[2:4]) > 12:
				sleep(0.3)
				print("Kennitalan sem þú slóts inn virðist ekki vera kennitala")
				print("Reyndu aftur")
				print("")
				rep1 = 1
			else:
				valmynd = 0
				summa = 0
				for s in range(0,len(varstr)):
					summa += (int(kt[s]) * varstr[s])
				print(summa)
				summa %= 11
				print(summa)
				x = 11 - summa
				if int(kt[8]) != x:
					sleep(0.3)
					print("Kennitalan sem þú slóts inn virðist ekki vera kennitala")
					print("Reyndu aftur")
					print("")
					rep1 = 1		
				else:
					sleep(0.5)
					print("Þér tókst að slá inn rétta kennitölu :)")
					aftur1 = str(input("Viltu keyra liðinn aftur? (já/nei): "))
					if aftur1 == "ja" or aftur1 == "já":
						rep1 = 1
					else:
						rep1 = 0
						valmynd = 1

	#Liður 2
	elif val == 2:
		rep2 = 1
		while(rep2 == 1):
			txt = str(input("Sláðu inn orð sem inniheldur ekki minna en 5 stafi: "))
			if len(txt) < 5:
				sleep(0.3)
				print("Orðið er of stutt, reyndu aftur")
				print("")
				rep2 = 1
			else:
				ord1 = txt[0:2] + txt[-2:]
				sleep(0.3)
				print("Nýji strengurinn er:", ord1)
				print("Strengurinn í hástöfum:", ord1.upper())
				print("Strengurinn í lágstöfum:", ord1.lower())
				aftur2 = str(input("Viltu keyra liðinn aftur? (já/nei): "))
				if aftur2 == "ja" or aftur2 == "já":
					rep2 = 1
				else:
					rep2 = 0	

	#Liður 3
	elif val == 3:
		rep3 = 1
		while(rep3 == 1):
			nafn = str(input("Sláðu inn orð, því lengra því betra: "))
			for n in range(len(nafn)):
				print(nafn)
				sleep(0.2)
				nafn = nafn[1:]
			aftur3 = str(input("Viltu keyra liðinn aftur? (já/nei): "))
			if aftur3 == "ja" or aftur3 == "já":
				rep3 = 1
			else:
				rep3 = 0

	#"Liður" 4
	elif val == 4:
		print("Þú hefur valið að hætta")
		sleep(0.5)
		print("blessbless")
		sleep(1)
		exit()


	else:
		sleep(0.3)
		print("Þessi tala var ekki á milli 1-4, reyndu aftur")

	

