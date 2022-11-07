#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan
# rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden
# ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
#jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton
# (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan
# kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random


class Car:

    car_amount = 0

    def __init__(self, license_number, top_speed):
        self.car_amount = Car.car_amount
        Car.car_amount = Car.car_amount + 1
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = 0
        self.travel_distance = 0
        self.travel_hours = 0

    def print_info(self):
        print(f"Car {self.car_amount}: {self.license_number}, Topspeed: {self.top_speed} km/h, travelled distance:{self.travel_distance} km.")


class ElectricCar(Car):
    def __init__(self, licence_number, top_speed, battery):
        self.battery = battery
        super().__init__(licence_number, top_speed)

    def print_info(self):
        super().print_info()
        print(f"Battery: {self.battery}")


class GasCar(Car):

    def __init__(self, licence_number, top_speed, gas):
        self.gas = gas
        super().__init__(licence_number, top_speed)

    def print_info(self):
        super().print_info()
        print(f"Gas: {self.gas}")


class Race:

    def __init__(self, lenght, cars):
        self.race_lenght = lenght
        self.cars = cars

    def car_speed_calculator(self):

        for car in self.cars:
            car_accelerate = random.randint(10, 70)
            if 0 < car.speed + car_accelerate < car.top_speed:
                car.speed = car.speed + car_accelerate
            elif car.speed + car.accelerate <= 0:
                car.speed = 0
            else:
                car.speed = car.top_speed

    def racing(self):
        for car in self.cars:
            car.travel_distance = car.travel_distance + (car.speed * self.race_lenght)

cars = []
cars.append(ElectricCar("ABC-15", 180, 52.5))
cars.append(GasCar("ACD-123", 165, 32.3))
for t in cars:
    t.print_info()

race = Race(3, cars)
race.car_speed_calculator()
race.racing()
for t in cars:
    t.print_info()