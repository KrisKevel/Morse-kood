from winsound import Beep 
from time import sleep
from tkinter import *
from tkinter import ttk

#iga morse tähemärgi vahel 1 tühik, iga morse sõna vahel 3 tühikut

sonastik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}
vastuste_ajalugu = "" #siia hakkame vastusi salvestama

while True: #kogu programm jookseb tsüklis
    tegevus = input("Mida soovid teha? (tõlge, ajalugu, lõpp) ") #soovitud tegevus

    if tegevus=="tõlge": #tõlkimise plokk
        kasutaja_keel = input("Sisesta, mis keelest soovid tõlkida (eesti, morse): ")
        kasutaja_sisend = input("Sisesta sõna, mida soovid tõlkida: ")

        vastus = ""

        if kasutaja_keel == "eesti": #lähtekeel on eesti keel
            for i in kasutaja_sisend:
                if i == " ": #sõnadevaheline tühik on võrdne kolme tühikuga morse koodis
                    vastus += "   "
                else: #võtame sõnastikust väärtusi iga tähe kohta, tähtede vahel on tühik
                    taht = sonastik[i.upper()]
                    vastus += taht + " "
            print(vastus)

            kas_soovib_kuulata = input("Kas soovid vastust kuulda? (jah/ei) ")

            if kas_soovib_kuulata == "jah": #vastust saab soovi korral ka kuulata! yay
                for märk in vastus:
                    if märk==".": #punkt on kolm korda lühem kui kriips/tühik
                        Beep(1000, 300)
                    elif märk=="-":
                        Beep(1000, 900)
                    elif märk==" ":
                        sleep(0.9)


        if kasutaja_keel == "morse": #kui lähtekeel on morse
            a = kasutaja_sisend.replace("   ", " t ").split(" ") #lihtsustamise mõttes asendan sõnadevahelise tühiku esialgu t-tähega
            for i in a:
                if i == "t":
                    vastus += " "
                else: #võtame sõnastikust väärtusi (seekord tuleb võtmeid väärtuste abil leida)
                    for j in sonastik:
                        if sonastik[j] == i:
                            vastus += j.lower()
            print(vastus)


        vastuste_ajalugu += "Sisend: " + kasutaja_sisend + "; Tõlge: " + vastus + "\n" #ajaloo täiendamine

    elif tegevus == "ajalugu": #ajaloo väljastamine
        print(vastuste_ajalugu)

    elif tegevus == "lõpp": #programmi lõpetamine
        break

    print() #tühik lugemuse jaoks