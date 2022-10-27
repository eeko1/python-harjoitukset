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
        self.travel_hours = 0
        self.travel_distance = 0

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


def car_create():
    cars = []
    for i in range (10):
        cars.append(Car("a-"+ str(i), 50))
    return cars


cars = car_create()
race_length = 10000

for car in cars:
    while car.travel_distance < race_length:
        random_speed = random.randint(-15, 15)
        Car.accelerate(car, random_speed)
        Car.travelled_distance(car, 1)
        if car.travel_distance >= race_length:
            Car.print_info(car)