#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.


class Car:
    pass

    def __init__(self, license_Plate, top_speed):
        self.license_Plate = license_Plate
        self.top_speed = top_speed
        self.odometer = 0
        self.speed = 0

car1 = Car("ABC-123", 142)

print(f"Auton {car1.license_Plate} "
      f"huppunopeus on {car1.top_speed} km/h, "
      f"matkamittari: {car1.odometer} km, "
      f"tämänhetkinen nopeus: {car1.speed} km/h.")
