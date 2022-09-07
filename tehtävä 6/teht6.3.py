#Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän

def bensa(galloona):
    luku = galloona * 3.785
    return luku

galloona = int(input("Kirjoita gallon määrä"))
while galloona >= 0:
    litrat = bensa(galloona)
    print(f"{litrat:.2f} l")
    galloona = int(input("Kirjoita gallon määrä"))

else:
    print("Ohjelma loppuu")


