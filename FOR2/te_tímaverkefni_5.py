from math import *
import time


p1 = str(input("Sláðu inn nafn á persónu 1: "))
a1 = int(input("Sláðu inn aldur á persónu 1: "))
p2 = str(input("Sláðu inn nafn á persónu 2: "))
a2 = int(input("Sláðu inn aldur á persónu 2: "))

if (a1 > a2):
	print (p1 , "er eldri, sú persóna er" , a1 , "ára")
elif (a1 < a2):
	print(p2 , "er eldri, sú persóna er" , a2 , "ára")
if (a1 == a2):
	print ("Þessar persónur eru jafn gamlar")



x = int(input("Sláðu inn einkunn (1-10): "))

if (x == 9) or (x == 10):
	print ("Þú fékkst A í einkunn")
elif (x == 7) or (x == 8):
	print ("Þú fékkst B í einkunn")
elif (x == 5) or (x == 6):
	print ("Þú fékkst C í einkunn")
elif (x == 4) or (x == 3) or (x == 2) or (x == 1) or (x == 0):
	print ("Þú fékkst F í einkunn :(")
else:
	print ("Þetta er ekki gild einkunn frá 1-10")


x = float(input("Sláðu inn þyngd: "))
y = float(input("Sláðu inn hæð: "))

formula = (x/y**2)
bmi = (round (formula,2))

if (10 <= bmi <= 18):
	print ("Þitt BMI er" , bmi , "þú ert of létt/ur")
elif (19 <= bmi <= 25):
	print ("Þitt BMI er" , bmi , "þú ert í eðlilegri þyngd")
elif (26 <= bmi <= 29):
	print ("Þitt BMI er" , bmi , "þú ert og þung/ur")
elif (bmi > 30):
	print ("Þitt BMI er" , bmi , "þú ert skilgreind/ur með offitu")
else:
	print("Þitt BMI er" , bmi , "þú ert of létt/ur til að vera líffræðilega lifandi")