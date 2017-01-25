from time import *  #Hér eru importin sem við þurfum í verkefnið
import random




def verkefni1():    #Við notum def til að einfalda while lykkjur og köllum á defið þegar við þurfum það, sjá neðst á skjali
    while True:
        listi = []
        for i in range(7):
            innslattur = int(input("Sláðu inn tölu: ")) #Beðið um tölu
            listi.append(innslattur)
        for tala in listi:
            print(tala, end=";")    #Prentað út tölu með ";" á milli
        print("\n")
        minnsta = min(listi)    #Læsta talan sett í breytu
        staersta = max(listi)   #Stærsta talan sett í breytu
        radad = sorted(listi)   #Sorteraður listi settur í breytu
        print(minnsta)
        print(staersta)
        print(radad)
        sleep(0.7)

        aftur1 = input(str("Viltu keyra liðinn aftur? (já/nei): "))  #Spurt hvort notandinn vill keyra liðinn aftur
        if aftur1 == "nei":
            break


def verkefni2():
    while True:
        random_tala = [random.randint(1, 500) for x in range(70)]   #Hér er random listi settur í breytu
        print("stærsta talan í listanum er: ", max(random_tala))    #Hér er stærsta talan í random listanum prentuð út
        print("minnsta talan í listanum er: ", min(random_tala))    #Hér er minnsta talan í random listanum prentuð út
        random_listi = reversed(random_tala)    #Hérna er listanum snúið við
        listi = []
        for each in random_listi:
            listi.append(each)
        print("listi öfugur: ", listi)

        print()
        print("Listinn með 4 tölum í hverri línu: ")
        teljari = 0
        for i in (random_tala):     #Þesso for lykkja gerir listann þannig að það prentast út fjórar tölur í línu
            teljari = teljari+1
            if(teljari%4 == 0):
                print(i)
            else:
                print(i, end=" ")

        print()
        teljari = 0
        for i in (random_tala):        #Þessar for lykkjur greinir hversu margar tölur eru yfir og undir 250
            if(i >= 1 and i <= 250):
                teljari = teljari+1
        teljari_2 = 0
        for x in (random_tala):
            if(x >= 251 and x <= 500):
                teljari_2 = teljari_2+1

        print()
        print("Listinn með 6 tölum í línu og raðaður í öfuga röð: ")
        rod = sorted(random_tala)
        teljari_3 = 0
        for i in reversed(rod):     #Hér er listanum snúið við og prentaðar út sex tölur í hverri línu
            teljari_3 += 1
            if teljari_3 == 6:
                print(i)
                teljari_3 = 0
            else:
                print(i, end=" ")

        print("hve oft tölurnar 1-250 komu upp: ",teljari)
        print("hve oft tölurnar 251-500 komu upp: ",teljari_2)
        

        aftur2 = input(str("Viltu keyra liðinn aftur? (já/nei): "))  
        if aftur2 == "nei":
            break


def verkefni3():
    while True:
        nafnalisti = []
        for i in range(5):
            nafn = str(input("Sláðu inn nafn: "))   #Beðið notanda um að slá inn 5 nöfn
            nafnalisti.append(nafn)
        while True:
            print("1. Birta nöfnin óröðuð")
            print("2. Raðað nöfnum í stafrófsröð og skrifa á skjáinn")
            print("3. Raðað nöfnum í öfuga stafrófsröð og skrifa á skjáinn")
            print("4. Birta eitt ákveðið nafn eftir númeravali")
            print("5. Hætta í verkefni 3")
            nafnaval = int(input("Sláðu inn tölu frá 1-5: "))   #Hérna er önnur valmynd

            if nafnaval == 1:
                print(nafnalisti)
                print()
            if nafnaval == 2:
                nafnalisti.sort()
                print(nafnalisti)
                print()
            if nafnaval == 3:
                nafnalisti.sort()
                print(nafnalisti[::-1])
            if nafnaval == 4:
                nafnaval_1 = int(input("Veldu tölu til að birta eitt nafn (type 1-5): ")) #Hér er valið hvaða nafn á að birtast við viðeigandi númer
                if nafnaval_1 == 1:
                    print()
                    print(nafnalisti[0])
                    print()
                if nafnaval_1 == 2:
                    print()
                    print(nafnalisti[1])
                    print()
                if nafnaval_1 == 3:
                    print()
                    print(nafnalisti[2])
                    print()
                if nafnaval_1 == 4:
                    print()
                    print(nafnalisti[3])
                    print()
                if nafnaval_1 == 5:
                    print()
                    print(nafnalisti[4])
                    print()
            if nafnaval == 5:
                return      #return er notað til að hoppa beint út def yfir í valmyndina aftur


def verkefni4():
    while True:
        oll_kost = []
        fjoldi_kasta = int(input("Hversu mörgum sexhliða teningum viltu kasta? "))
        for i in range(fjoldi_kasta):   #Hér er fengið út hvað kemur á teninginn
            oll_kost.append(random.randint(1,6))
        print(oll_kost)
        mesti_fjoldi = -1
        oftast_upp = 0
        minnsti_fjoldi = None      #Nota None sem gildi því vantaði gildi sem höfðu ekkert í sér
        for x in range(1, 7):
            hversu_oft = oll_kost.count(x)  #count telur hveru mörg köst eru af hverju númeri á teningnum
            if hversu_oft > mesti_fjoldi:
                mesti_fjoldi = hversu_oft
                oftast_upp = x      #x gefur okkur hversu oft ákveðin tala kom upp
            if minnsti_fjoldi is None or hversu_oft < minnsti_fjoldi:
                minnsti_fjoldi = hversu_oft
                sjaldnast_upp = x
            print(x, "kom", hversu_oft)
        print(oftast_upp, "kom oftast upp")
        print(sjaldnast_upp, "kom sjaldnast upp")



def verkefni5():
    nöfn_nemenda = []
    fjoldi_nemenda = int(input("Hversu margir eru í FOR1TÖ05BU?: "))
    for nemandi in range(fjoldi_nemenda):   #Hér er beðið um tölu og gefið upp jafn mörg input eftir hvaða tala var skrifuð inn
        nafn = str(input("Nafn nemanda: "))
        nöfn_nemenda.append(nafn)
    nöfn_nemenda.sort()     #Sorterar nöfnin eftir stafrófsröð
    for nemandi in (nöfn_nemenda):      #Þessi lykkja raðar nemendum þannig að það er eitt nafn í hverri línu
        print(nemandi)






valmynd = 1
while (valmynd == 1):                               #Hérna er aðal-valmyndin
    print("Verkefni 1: Listi yfir tölur")
    print("Verkefni 2: Random tölur")
    print("Verkefni 3: Strengjalisti")
    print("Verkefni 4: Fjöldi teningakasta ákveðinn af notanda")
    print("Verkefni 5: Skráning í áfanga")
    val = int(input("Veldu verkefni (1-5), veldu 6 til að hætta: "))

    if val == 1:        
        verkefni1()     #Hérna t.d notum við "verkefni1()" til þess að kalla á þann kóða sem stendur undir #def verkefni1() ef valið var 1 í valmyndinni
    elif val == 2:
        verkefni2()
    elif val == 3:
        verkefni3()
    elif val == 4:
        verkefni4()
    elif val == 5:
        verkefni5()
    elif val == 6:
        valmynd = 0
        print("Þú hefur valið að hætta.")
        print()
        sleep(1)
        print("Hætti í forriti eftir 3 sekúndur...")
        sleep(3)
    else:
        print("Þetta var ekki tala frá 1-6. Reyndu aftur")
