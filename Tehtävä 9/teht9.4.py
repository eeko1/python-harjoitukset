#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

class Car:
    pass

    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.license_plate} "
              f"huppunopeus on {self.top_speed} km/h, "
              f"matkamittari: {self.odometer} km, "
              f"tämänhetkinen nopeus: {self.speed} km/h.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0

    def travelled_distance(self, hours):
        self.odometer += self.speed * hours

cars = []
for i in range(10):
    bil = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(bil)

has_won = False
while not has_won:
    for i in cars:
        i.accelerate(random.randint(-10, 15))
        i.travelled_distance(1)
        if i.speed >= 10000:
            has_won = True
            print(f"Voittaja on: {i.license_plate}")
            break

cars.sort()
print("---------------")
for i in cars:
    print(f"Rekisterinumero: {i.license_plate}")
    print(f"Huippunopeus: {i.top_speed}")
    print(f"Nykyinen nopeus: {i.speed}")
    print(f"Kuljettu matka: {i.odometer}")
    print("---------------")