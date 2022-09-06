#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
#Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

kokonaisluku = int(input("Syötä kokonaisluku"))
jako = 2

if kokonaisluku >= 1:
        for n in range(2,kokonaisluku):
            if kokonaisluku % n == 0:
                print(kokonaisluku, "ei ole alkuluku")
                break
            jako += 1
        else:
            print(kokonaisluku," on alkuluku")
