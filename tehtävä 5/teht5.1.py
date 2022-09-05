#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.
import random
arpakuutio = int(input("Kirjoita arpakuutioiden lukumäärä"))
summa = 0

for arpakuutio in range(arpakuutio):
    numero = random.randint(1, 6)
    print(numero)
    summa += numero
print(f"Arpakuutio luku on {summa}")
