import random
from math import *
from time import *
def lidur5():
	listi = []
	for x in range(7):
		tala1 = int(input("Sláðu inn heiltölu %d: "%(x+1)))
		listi.append(tala1)
	print("Minnsta tala listans er: ", min(listi))
	print("Hæðsta tala listans er: ", max(listi))
	summari = sum(listi)
	print("Allar tölur listans plúsaðar saman: ", summari)
	meðaljon = summari/7
	print("Meðaltal summu listans: ", meðaljon)
lidur5()