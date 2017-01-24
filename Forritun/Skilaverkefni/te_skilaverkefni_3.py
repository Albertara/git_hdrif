from math import *
import time


#Liður 1

"""
aftur = 1
while(aftur == 1):
	x = int(input("Sláðu inn heiltölu: "))
	print ("Þú hefur valið töluna: " , x)
	aftur = str(input("Viltu slá inn aðra heiltölu? (já/nei)"))
	if (aftur == "já"):
		aftur = 1
	else:
		aftur = 0
print ("")


#liður 2


svar = "já"
while(svar == "já"):
	l = float(input("Sláðu inn lengd ferhyrnings: "))
	b = float(input("Sláðu inn breidd ferhyrnings: "))
	flatarmál = l*b 
	print ("Flatarmálið er:" , flatarmál)
	print("")
	svar = input("Viltu reikna aftur? (já/nei)")
print ("")


#Liður 3


leyni = "leyniorð"

while True:

	x = str(input("Hvað er leyniorðið? "))

	if (x == leyni):
		print ("Þú giskaðir rétt!")
		break
	else:
		print ("Þú giskaðir Vitlaust :(")
print ("")


"""
#Liður 4


amount = int(input("Sláðu inn upphæð í krónum: "))

fiveK = amount // 5000
amount = amount % 5000

oneK = amount // 1000
amount = amount % 1000

halfK = amount // 500
amount = amount % 500

hundrad = amount // 100
amount = amount % 100

fimmtiu = amount // 50
amount = amount % 50

tiu = amount // 10
amount = amount % 10

fimm = amount // 5
amount = amount % 5

einn = amount


print ("þetta gera: ")

if fiveK > 0:
	print (fiveK , "stk 5000kr")
if oneK > 0:
	print (oneK , "stk 1000kr")
if halfK > 0:
	print (halfK , "stk 500kr")
if hundrad > 0:
	print (hundrad , "stk 100kr")
if fimmtiu > 0:
	print (fimmtiu , "stk 50kr")
if tiu > 0:
	print (tiu , "stk 10kr")
if fimm > 0:
	print (fimm , "stk 5kr")
if einn > 0:
	print (einn , "krónur")
print ("")


#Liður 5
"""
count = 0

while True:
	count = count + 1
	print ("1.Þú skrifar inn 10 tölur og ég reikna út summu og meðaltal þeirra")
	print ("2.Þú slærð inn tölu og ég læt þig vita hvort talan sé slétt tala eða oddatala")
	print ("3.Ég slekk á mér og hrósa þeim sem bjó mig til")

	val = int(input("1-3: "))

	if val == 1:
		t1 = int(input("tala 1:"))
		t2 = int(input("tala 2:"))
		t3 = int(input("tala 3:"))
		t4 = int(input("tala 4:"))
		t5 = int(input("tala 5:"))
		t6 = int(input("tala 6:"))
		t7 = int(input("tala 7:"))
		t8 = int(input("tala 8:"))
		t9 = int(input("tala 9:"))
		t10 = int(input("tala 10:"))

		summa = t1+t2+t3+t4+t5+t6+t7+t8+t9+t10
		meðaltal = summa / 10

		print ("Summa talnana er:" , summa)
		print ("Meðtal talnana er:" , meðaltal)
		print ("")

	elif val == 2:

		tala = int(input("Sláðu inn tölu: "))

		if tala % 2 == 1:
			print("Talan sem þú skrifaðir er oddatala")
			print("")
		else:
			print("Talan sem þú skrifaðir er slétt tala")
			print("")

	elif val == 3:
		for tala in range(10):
			print ("Albert er frábær forritari")
		print("Þú keyrðir forritið", count, "sinnum")
		break

	else:
		print("Þú valdir ekki 1, 2 eða 3. Vinsamlegast veldur aftur")

	time.sleep(0.7)
	"""