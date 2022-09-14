#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


vuodenAjat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Kirjoita kuukausi numeroina 0-11: (0 = tammikuu 11 = joulukuu)"))

if kuukausi < 12 and kuukausi > 0:
    print(f"{kuukausi} on {vuodenAjat[kuukausi]} kuukausi")

else:
    print("Virheellinen numero")




