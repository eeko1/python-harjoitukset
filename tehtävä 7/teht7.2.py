#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimi = {"Milla"}

userInput = input("Kirjoita nimi:")
while userInput != "":
    if userInput in nimi:
        print("Nimi on jo annettu:")
        userInput = input("Kirjoita nimi:")
        if userInput == "":
            break
    else:
        nimi.add(userInput)
        print("Nimi lisätty listaan")
        if userInput == "":
            break
    userInput = input("Kirjoita nimi")

for x in nimi:
    print(x)

