#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
numero = []
numeroLukija = True
while numeroLukija:
    strInput = input("Anna numero")
    if strInput == "":
        numeroLukija = False
    else:
        numero.append(int(strInput))
print(numero)
numero.sort(reverse=True)
print(numero)
print(numero[0:5])
for numerot in numero[:5]:
    print(numerot)