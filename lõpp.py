# Tegemata:
# vastuste ajalugu
# kasutajaliidesele kujundus (?)

from tkinter import *
from winsound import Beep 
from time import sleep

sonastik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}

def eesti_morse():
    kasutaja_sisend = eesti.get()
    vastus = ""
    blank.delete(0, END) # puhastab vastust sisaldava kasti eelmisest vastusest
    for i in kasutaja_sisend:
            if i == " ": #sõnadevaheline tühik on võrdne kolme tühikuga morse koodis
                vastus += "   "
            else: #võtame sõnastikust väärtusi iga tähe kohta, tähtede vahel on tühik
                taht = sonastik[i.upper()]
                vastus += taht + " "
    blank.insert(0, vastus) # väljastame vastuse
    return vastus
    
def morse_eesti():
    kasutaja_sisend = morse.get()
    vastus = ""
    blank2.delete(0, END) # puhastab vastust sisaldava kasti eelmisest vastusest
    a = kasutaja_sisend.replace("   ", " t ").split(" ") #lihtsustamise mõttes asendan sõnadevahelise tühiku esialgu t-tähega
    for i in a:
        if i == "t":
            vastus += " "
        else: #võtame sõnastikust väärtusi (seekord tuleb võtmeid väärtuste abil leida)
            for j in sonastik:
                if sonastik[j] == i:
                    vastus += j.lower()
    blank2.insert(0, vastus) # väljastame vastuse
    
def kuula():
    vastus = eesti_morse()
    for märk in vastus:
        if märk==".": #punkt on kolm korda lühem kui kriips/tühik
            Beep(1000, 300)
        elif märk=="-":
            Beep(1000, 900)
        elif märk==" ":
            sleep(0.9)

main = Tk()
main.title("Morsekoodi translaator")
Label(main, text = "Sisesta eestikeelne sõna:").grid(row=0)
Label(main, text = "Sisesta morsekood: ").grid(row=2)
Label(main, text = "Tõlge: ").grid(row=1)
Label(main, text = "Tõlge: ").grid(row=3)

eesti = Entry(main)
morse = Entry(main)
blank = Entry(main)
blank2 = Entry(main)

eesti.grid(row=0, column=1)
morse.grid(row=2, column=1)
blank.grid(row=1, column=1)
blank2.grid(row=3, column=1)


Button(main, text='Välju', command=main.destroy).grid(row=4, column=1, sticky=W, pady=4)
Button(main, text='Tõlgi', command=eesti_morse).grid(row=0, column=3, sticky=W, pady=4, padx=10)
Button(main, text="Tõlgi", command=morse_eesti).grid(row=2, column=3, sticky=W, pady=4, padx=10)
Button(main, text="Kuula", command=kuula).grid(row=1, column=3, sticky=W, pady=4, padx=10)

mainloop()