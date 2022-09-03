#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

userInput = input("Sano luku:")
maxValue = minValue = int(userInput)

while True:
    userInput = input("Sano luku:")
    if userInput == "":
        break
    userInputInt = int(userInput)
    if userInputInt < minValue:
        minValue = userInputInt
    if userInputInt > maxValue:
        maxValue = userInputInt
print(f"Pienin arvo: {minValue}, suurin arvo: {maxValue}")