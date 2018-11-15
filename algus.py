#from winsound import Beep https://docs.python.org/3.7/library/winsound.html

#iga morse tähemärgi vahel 1 tühik, iga morse sõna vahel 3 tühikut

sonastik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}
vastuste_ajalugu = ""

while True:
    tegevus = input("Mida soovid teha? (tõlge, ajalugu, lõpp)")

    if tegevus=="tõlge":
        kasutaja_keel = input("Sisesta, mis keelest soovid tõlkida (eesti, morse): ")
        kasutaja_sisend = input("Sisesta sõna, mida soovid tõlkida: ")

        vastus = ""
        
        if kasutaja_keel == "eesti":
            for i in kasutaja_sisend:
                if i == " ":
                    vastus += "   "
                else:
                    taht = sonastik[i.upper()]
                    vastus += taht + " "

        if kasutaja_keel == "morse":
            a = kasutaja_sisend.replace("   ", " t ").split(" ") #lihtsustamise mõttes asendan sõnadevahelise tühiku esialgu t-tähega
            for i in a:
                if i == "t":
                    vastus += " "
                else:
                    for j in sonastik:
                        if sonastik[j] == i:
                            vastus += j.lower()

        vastuste_ajalugu += "Sisend: " + kasutaja_sisend + "; Tõlge: " + vastus + "\n"
        print(vastus)

    elif tegevus == "ajalugu":
        print(vastuste_ajalugu)

    elif tegevus == "lõpp":
        break
