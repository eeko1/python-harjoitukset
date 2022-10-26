#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km


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
        else:
            self.speed = self.top_speed

    def travelled_distance(self, hours):
        self.odometer = self.odometer + self.speed * hours


car1 = Car("ABC-123", 142)
car1.accelerate(200)
car1.travelled_distance(1.5)
car1.print_info()