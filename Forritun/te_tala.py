from math import *
import time


#notum max til að finna hæstu töluna
x = int(input("Tala1: "))
y = int(input("Tala2: "))
print ("Hærri talan er: " , max(x , y))
print ("Lægri talan er: " , min(x , y))
time.sleep(1.5)
print ("")

print ("Rúmmál sívalings")
x = int(input("Radíus: "))
y = int(input("Hæð: "))
print ("Rúmmál Sívalingsins" , x*x*(pi)*y)
time.sleep(1.5)
print ("")

print ("Rúmmál kúlu")
x = int(input("Radíus: "))
r = 4 * x**3 * (pi)/3
print ("Rummál kúlu: " , round(r,2))
time.sleep(1.5)
print("")

x = int(input("Lengd Skammhliðar 1: "))
y = int(input("Lengd skammhliðar 2: "))
z = sqrt(x**2+y**2)
print ("Lengd langhliðar: " , round(z,2))
time.sleep(5)
print ("Bæ")