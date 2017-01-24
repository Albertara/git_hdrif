#Skilgreinum lista með 3 tölum

listi = [5,4,9]
#Prentum  í allann listann
print(listi)
#Prentum út eitt stak númer 0, 1 eða 2 (Byrjar að telja frá 0)
print(listi[0])
print(listi[1])
print(listi[2])


#bætum við "aftast" í lista
listi.append(2)
print(listi)


#tek tölu og skipti henni út með annari tölu
listi[0] = 10
print(listi)


#Bæti við tölu í miðjan listann, tek enga tölu út í staðinn
listi.insert(2,7)
print(listi)


#Lúppum í gegnum listann...
for i in listi:
	print(i)


#Að eyða öftustu tölunni úr listanum
listi.pop()
print(listi)
#pop eyðir alltaf aftast


#tala aftur úr eitthverju hólfi að vild
del listi[1]
print(listi)


#eyðum ákveðnu gildi úr lista
listi.remove(7)
print(listi)