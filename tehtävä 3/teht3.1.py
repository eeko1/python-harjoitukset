#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä "))
kuhan_mitta = 37.0
if kuhan_mitta >= kuhan_pituus:
    print(f"Kuhasta puuttuu {kuhan_mitta - kuhan_pituus} senttiä ")
    print("Laita kuha takaisin järveen ")