from math import *
from time import *
from random import *
import re


valmynd = 1
while (valmynd == 1):
    val = int(input("Veldu lið: Liður 1-5 (type 1-5): "))
    # Verkefni1

    if val == 1:
        listi = []
        for i in range(7):
            innslattur = int(input("Sláðu inn tölu: "))
            listi.append(innslattur)
        for tala in listi:
            print(tala, end=";")
        print("\n")
        minnsta = min(listi)
        staersta = max(listi)
        radad = sorted(listi)
        print(minnsta)
        print(staersta)
        print(radad)
