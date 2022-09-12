#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.
nimi = {"Milla"}

while True:
    userInput = input("Kirjoita nimi:")
    if userInput == "":
        break
    if userInput in nimi:
        print("Nimi on jo listassa")
    else:
        print("Nimi on lisätty listaan")
        nimi.add(userInput)

for y in nimi:
    print(y)