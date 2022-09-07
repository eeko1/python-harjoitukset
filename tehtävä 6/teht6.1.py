#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def heitaNoppaa():
    luku = random.randint(1, 6)
    return luku

while True:
    silmaLuku = heitaNoppaa()
    print(silmaLuku)
    if silmaLuku == 6:
        break








