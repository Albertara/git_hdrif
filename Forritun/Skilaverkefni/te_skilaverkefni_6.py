from math import *
from time import *
from time import *


rep1 = 1
while(rep1 == 1):
	val = int(input("1. Kennitala, 2. Búa til nýtt orð, 3. Sneið af streng, 4. Hætta (type1-4): "))

	if val == 1:
		rep2 = 1
		while(rep2 == 1):
			varsumma = 0
			kt = (input("Sláðu inn kennitölu: "))
			kt = kt.replace("-","")
			vörtustrengur = [3,2,7,6,5,4,3,2]
			if(len(kt) != 10 or kt[0:2] > "31" or kt[2:4] > "12"):
				print("Kennitalan er ekki rétt")
				print("Reyndu aftur")
				rep2 = 1
			for i in range(0,len(vörtustrengur)):
				varsumma = varsumma + (int(kt[i]) * vörtustrengur[i])
			varsumma = varsumma % 11
			print(varsumma)
			x = 11 - varsumma
			

	elif val == 2:
		orð = str(input("Sláðu inn nafn: "))
		voff1 = orð[0:2] + orð[-2:]
		print(voff1)
		
