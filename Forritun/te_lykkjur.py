from math import *
import time


#Tímaverkefni 6.1

teljari=1

while(teljari <= 10):
	time.sleep(0.04)
	print(teljari)
	teljari = teljari + 1

time.sleep(1)

#Tímaverkefni 6.2

talaya=20

while(talaya >= 1):
	time.sleep(0.04)
	print(talaya)
	talaya = talaya - 1

time.sleep(1)

#Tímaverkefni 6.3

tula = 0

while(tula <= 60):
	time.sleep(0.04)
	print(tula)
	tula = tula + 6

time.sleep(1)

#Tímaverkefni 6.4

x = int(input("Margföldunnartafla (0-∞): "))
y = (x * 10)
tala = 0 

while(tala <= y):
	print(tala)
	tala = tala + x

#Tímaverkefni 6.5

time.sleep(1)

a = int(input("Heiltala: "))

if a <= 20:
	voff = a
	while(voff <= 20):
		time.sleep(0.03)
		print(voff)
		voff = voff + 1

elif a >= 20:
	voff = a
	while(voff >= 20):
		time.sleep(0.03)
		print(voff)
		voff = voff - 1