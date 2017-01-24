#Kt: 081200-3270 (Helgi Steinarr Júlíusson) - 18.01.2017
import re
from random import *
print("  _______________________")
print(" |                       | ")
print(" | ><[Skilaverkefni 1]>< | ")  #Segir hvaða verkefni þetta er
print(" |_______________________| ")

#Hér undir eru listar sem ég nota til að greyna hvort notandinn játaði eða neitaði.
ja_listi = ["j","já","ja","jamm","j","y","jam","jas","yes","yas","mhm","mhmm","aha"]
nei_listi = ["n","ne","nei","na","nah","ne","neh","no","huh"]
def keyra_aftur(d_nr): #Function sem ég get notað til að spurja notandann hvort hann vilji keyra liðinn aftur
    while(True):
        aft = str(input(" \nViltu keyra liðinn aftur?[J/N]: "))
        if aft.lower() in ja_listi:  #Þessi athugar hvort inputið hjá notandanum er í já listanum og ef svo er þá veit forritið að hann svaraði já
            print("Þú hefur valið að keyra liðinn aftur.")
            if d_nr == 1:      #Ef breytan sem stjórnar loopunni er 1 gerist ekkert
                d_nr += 0
            else:              #Annars bætir forritið við 1 svo það eina sem breytan getur verið er 1 ef notandinn vil keyra það aftur.
                d_nr += 1
            return(d_nr)
        if aft.lower() in nei_listi:    #Sama og ef sagt er já nema öfugt.
            print("Þú hefur valið að keyra liðinn [EKKI] aftur.")
            if d_nr == 0:
                d_nr -= 0
            else:
                d_nr -= 1
            return d_nr
        else:
            print("Skil ekki..")

valmynd = 1
while valmynd == 1:
    print("  ______________")
    print(" |              | ")
    print(" |  [1] Dæmi 1  | ")
    print(" |  [2] Dæmi 2  | ")
    print(" |  [3] Dæmi 3  | ") #Valmynd sem sýnir dæmin í verkefninu á léttilegan máta
    print(" |  [4] Dæmi 4  | ")
    print(" |  [5] Dæmi 5  | ")
    print(" |  [6] Loka    | ")
    print(" |______________|\n ")
    while True:
        try:
            val = int(input("Hvaða dæmi viltu keyra?[1-6]: "))
            break
        except ValueError:
            print("Ekki tala..")
    print("Þú hefur valið að keyra dæmi [" + str(val) + "]")
    if val == 1:
        d1 = 1    #'d' hef ég fyrir 'Dæmi'
        while(d1 == 1):
            teljari = 0
            talnalisti = []
            for i in range(7):
                teljari += 1
                while(True):
                    try:
                        tala = int(input("Sláðu inn tölu [" + str(teljari) + "]: "))
                        break
                    except ValueError:
                        print("Ekki tala")
                talnalisti.append(tala)
            minnsta = min(talnalisti)
            staersta = max(talnalisti)
            radad = sorted(talnalisti)
            print("Minnsta talan:", minnsta)
            print("Stærsta talan:", staersta)
            print("Listinn raðaður:", radad)
            print("Talnalistinn prentaður með for loopu: ", end="")
            a = 0
            for p in range(len(talnalisti)):
                print(sorted(talnalisti)[a], end=";")
                a += 1
            tal = 0
            und_505 = []
            for f3 in range(len(talnalisti)):
                tal += 1
                if f3 <= 50.5:
                    und_505.append(f3)
            print("\nTölur undir eða jafnt og 50,5:", und_505, "Þær eru", tal, "talsins")
            d1 = keyra_aftur(d1)
    elif val == 2:
        d2 = 1    #'d' hef ég fyrir 'Dæmi'
        while(d2 == 1):
            randtal = []
            for f4 in range(70):
                randtal.append(randint(1,500))
            d2 = keyra_aftur(d2)










