#Tulostaa valikon ja palauttaa käyttäjän valinnan.

def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("0 - lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("Valitse:"))
        return valinta

# Lisää uuden lentoaseman annettuun sanakirjaan
def lisääUusi(asemat):
    icao = input("Aseman ICAO-koodi :")
    nimi = input("Aseman nimi: ")
    asemat[icao] = nimi


#Tulostaa halutun aseman annetusta sanakirjasta.
def hae(asemat):
    icao = input("Aseman ICAO koodi:")
    if icao in asemat:
        print(asemat[icao])

#    Pääohjelma
lentoasemat = {}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisääUusi(lentoasemat)
    elif valinta == 2:
        hae(lentoasemat)
    valinta = valitse()