#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def kokoluku(lista):
    numero = 0
    for i in lista:
        numero = numero + i
    return numero

lukuja = [1, 2, 3, 4, 5]
print(kokoluku(lukuja))