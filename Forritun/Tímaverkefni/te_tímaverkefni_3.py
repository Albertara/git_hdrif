from math import *

mila = float(input("Vegalengd í mílum: "))
kilo = (mila/0.6214)
print ("Vegalengd í kílómetrum: " , round(kilo,3))


gallon = float(input("Gallon: "))
l = (gallon*3.785)
print ("Lítrar: " , round(l,1))


x = int(input("Tala: "))
y = int(input("Tala 2: "))

if(x>=y):
	print ("Fjarlægð á milli talnana er: " , abs(x-y))
else:
	print ("Fjarlægð á milli talnana er: " , abs(y-x))


x = float(input("Radíus: "))
y = (4*x**2*3.1415)
print ("Yfirborð kúlu er: " , round(y,3))


x = float(input("Radíus Sívalings: "))
y = float(input("Hæð Sívalings: "))
x2 = (x**2)
z = (2*x2*pi+2*x*pi*y)
print ("Yfirboð: " , round(z,2))