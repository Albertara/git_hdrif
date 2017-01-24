from random import *
from math import *
from time import *


loop = 1
while(loop == 1):
	val = int(input("Hvort viltu spila? 1.LaugardagsLottó eða 2.Víkingalottó?: "))

	if val == 1:
		laugarlott = sample (range(1,40), 5)
		print(laugarlott)
		rep = str(input("Viltu spila LaugardagsLottó aftur? (já/nei) Eða viltu slökkva á forritinu? (loka)"))

	elif val == 2:
		víklott = sample (range(1,48), 6)
		print(víklott)
		rep = str(input("Viltu spila Víkingalottó aftur? (já/nei) Eða viltu slökkva á forritinu? (loka)"))

	else:
		print("Þú valdir ekki töluna 1 eða 2, reyndu aftur")

	if rep == "já" or rep == "ja":
		loop == 1

	elif rep == "loka":
		break

	else:
		loop == 0

