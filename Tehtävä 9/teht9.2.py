#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    pass

    def __init__(self, license_Plate, top_speed):
        self.license_Plate = license_Plate
        self.top_speed = top_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.license_Plate} "
              f"huppunopeus on {self.top_speed} km/h, "
              f"matkamittari: {self.odometer} km, "
              f"tämänhetkinen nopeus: {self.speed} km/h.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        else:
            self.speed = self.top_speed

car1 = Car("ABC-123", 142)

accelerateAmount = 3

while accelerateAmount >= 0:
    if accelerateAmount == 3:
        amount = 30
        car1.accelerate(amount)
        accelerateAmount -= 1
    elif accelerateAmount == 2:
        amount = 70
        car1.accelerate(amount)
        accelerateAmount -= 1
    elif accelerateAmount == 1:
        amount = 50
        car1.accelerate(amount)
        amount = 0
        break


car1.print_info()
amount = -200
car1.accelerate(amount)
car1.print_info()