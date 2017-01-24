import time

#liður1:

nafn = str(input("Nafn: "))
print ("Velkominn í áfangann FOR1A3U " + nafn + " Þetta verður skemmtileg önn, ég hlakka til að læra forritun")

#liður2:

x = float(input("Tala með 3 aukastöfum: "))
print ("Þú hefur valið töluna: " , round(x,1))
#liður3:

x = int(input("Heil tala: "))
y = int(input("Önnur heil tala: "))
print ("Fyrri talan magnfölduð með seinni tölu: " , x*y)
print ("Fyrri tala dregin frá seinni tölu: " , x-y)

#liður4:

x = int(input("Lengd: "))
y = int(input("Breidd: "))
z = int(input("Hæð: "))
print ("Rúmmál= " , x*y*z)

#liður5:

x = int(input("Aldur: "))
y = int(input("Aldur pabba þíns: "))
print ("Pabbi þinn var " , y-x , "ára þegar þú fæddist")

#liður6:

x = int(input("Aldur á fyrsta manni: "))
y = int(input("Aldur á öðrum manni: "))
z = int(input("Aldr á þriðja manni: "))
print ("Meðalaldur þeirra er: " , x+y+z/3)

time.sleep(1.5)

print ("Gaman að geta aðstoðað þig við þessa útreikninga" , nafn)