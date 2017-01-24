#Liður 1

x = int(input("Sláðu inn tölu: "))
y = int(input("Sláðu inn aðra tölu:"))

print("Tölur lagðar saman", x+y)
print("Tölur margfaldaðan saman", x*y)


#Liður 2

fn = str(input("Fornafn: "))
en = str(input("Eftirnafn: "))

print("Halló", fn, en)


#Liður 3

lengd = float(input("Sláðu inn lengd kílómetrum: "))
metri = lengd*1000

print(metri, "Metrar")


#Liður 4

laun = float(input("Laun á klukkustund: "))
klukk = float(input("Fjöldi klukkustunda: "))

print('Heildarlaun:', laun*klukk)


#Liður 5

laun = float(input("Laun á klukkustund: "))
klukk = float(input("Fjöldi klukkustunda: "))
heild = laun*klukk

if heild > 30000:
    skattur = heild * 0.20

elif heild < 30000:
    skattur = 0

print("Heildarlaunin þín eru: ", heild)
print("Skattur er: ", skattur, "krónur")


#Liður 6


gradur = int(input("Sláðu inn gráður: "))
hringir = gradur//360
gradur = gradur % 360

print("Það gerir", hringir, "marga hringi og", gradur, "gráður")