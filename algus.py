kasutaja_keel = input("Mis keelest soovid tõlkida (morse, eesti)? ")
kasutaja_sisend = input("Sisesta sõna, mida soovid tõlkida: ")

sonastik = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-"}
vastus = ""

if kasutaja_keel=="eesti":
    for i in kasutaja_sisend:
        taht = sonastik[i.upper()]
        vastus+=taht + " "

if kasutaja_keel=="morse":
    for el in sonastik:
        a = kasutaja_sisend.split(" ")
        for j in a:
            if sonastik[el]==j:
                vastus+=el.lower()

print(vastus)