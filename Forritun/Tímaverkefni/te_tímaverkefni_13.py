from random import *

#Liður 1
listi1 = [1,2,3,4,5]
print(listi1)


#Liður 2
summari = 0
listi2 = [1,2,3,4,5]
for i in listi2:
	summari += i
print(summari)


#Liður 3
listi3 = [1,2,3,4,5]
listi3.pop()
del listi3[0]
print(listi3)


#Liður 4
listi4 = [1,2,3,4,5]
listi4.append(8)
print(listi4)


#Liður 5
summa = 0
listi5 = []
for u in range(5):
	listi5.append(randint(1,10))
for y in listi5:
	summa = summa + y
meðaltal = summa/5
print("Listi með 5 slembitölum frá 1-10:" , listi5 , "Meðaltal tölum listans:" , meðaltal)


#Liður 6
listi6 = []
for u in range(5):
	listi6.append(randint(1,10))
print(listi6) 
x = max(listi6)
y = min(listi6)
print("Hæsta talan er:", x, "Lægsta talan er:", y)


#Liður 7
listi7 = [1,2,3,4,5]
print(*listi7, sep=' ')


#Liður 8
listi8 = [1,2,3,4,5]
listi8.append("}")
listi8.insert(0,"{")
print(*listi8, sep=' ')


#Liður 9
listi9 = [1,2,3,4,5]
for r in listi9:
	print(r)


