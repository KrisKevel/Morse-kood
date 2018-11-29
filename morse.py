# Tegemata:
# kasutajaliidesele kujundus (?)

from tkinter import *
from winsound import Beep 
from time import sleep

sonastik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}
ajalugu_sonastik = {}

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

    ajalugu_sonastik[kasutaja_sisend]=vastus
    ajalugu.insert(END, kasutaja_sisend)

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

    ajalugu.insert(END, kasutaja_sisend)

    ajalugu_sonastik[kasutaja_sisend] = vastus
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


#kui keegi vajutab ajaloo rea peale, siis programm jälle näitab vastuse
def ajaloo_kasutamine():
    valik = ""
    if ajalugu.curselection() != (): #kui midagi on valitud, siis saame selle sõne kätte
        valik = ajalugu.get(ajalugu.curselection()[0])

    if "." in valik or "-" in valik: #kui tegu on morsega, siis kuvame vastuse sonastikust morse väljale
        blank2.delete(0, END)
        morse.delete(0, END)
        blank2.insert(0, ajalugu_sonastik[valik])
        morse.insert(0, valik)

    else: #kui tegu on eesti keelega, siis kuvame vastuse sonastikust eesti keele väljale
        blank.delete(0, END)
        eesti.delete(0, END)
        blank.insert(0, ajalugu_sonastik[valik])
        eesti.insert(0, valik)

def tuhjaks(): #et oleks võimalus kõike tühistada, loome sellise käsu
    blank2.delete(0, END)
    morse.delete(0, END)
    blank.delete(0, END)
    eesti.delete(0, END)



main = Tk()
main.title("Morsekoodi translaator")

#kõik kirjed
Label(main, text = "Sisesta eestikeelne sõna:").grid(row=0)
Label(main, text = "Sisesta morsekood: ").grid(row=3)
Label(main, text = "Tõlge: ").grid(row=1)
Label(main, text = "Tõlge: ").grid(row=4)
Label(main, text = "").grid(row=2)
Label(main, text="Ajalugu").grid(row=0,column=4)

#kõik väljad
eesti = Entry(main)
morse = Entry(main)
blank = Entry(main)
blank2 = Entry(main)



#ajaloo kuvamine ja nn scrollimine
frame = Frame(main)
frame.grid(row=1, rowspan=4, column=4)

vertikaalne = Scrollbar(frame, orient=VERTICAL)
horisontaalne = Scrollbar(frame, orient=HORIZONTAL)
ajalugu = Listbox(frame, yscrollcommand=vertikaalne.set, xscrollcommand=horisontaalne.set)

vertikaalne.config(command=ajalugu.yview)
vertikaalne.grid(row=0, rowspan=4, column=1, sticky=N+S)
horisontaalne.config(command=ajalugu.xview)
horisontaalne.grid(row=4, columnspan=4, column=0, sticky=W+E)


#paigutame välju
eesti.grid(row=0, column=1)
morse.grid(row=3, column=1)
blank.grid(row=1, column=1)
blank2.grid(row=4, column=1)
ajalugu.grid(row=0, rowspan=4, column=0, sticky=N+S+E+W)


#kõik vajalikud nupud
Button(main, text='Välju', width=10, command=main.destroy).grid(row=5, column=1, pady=4)
Button(main, text='Tõlgi', width=10, command=eesti_morse).grid(row=0, column=3, sticky=W, pady=4, padx=10)
Button(main, text="Tõlgi", width=10, command=morse_eesti).grid(row=3, column=3, sticky=W, pady=4, padx=10)
Button(main, text="Kuula", width=10, command=kuula).grid(row=1, column=3, sticky=W, pady=4, padx=10)
Button(main, text="Tühista", width=10, command=tuhjaks).grid(row=2, column=1)
Button(main, text='Tuleta meelde', width=15, command=ajaloo_kasutamine).grid(row=5, column=4)


mainloop()