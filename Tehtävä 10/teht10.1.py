#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
#Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
# esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia
#niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:

    def __init__(self,low, top, current):
        self.low = low
        self.top = top
        self.current = current

    def elevator_movement(self, floor):
        if self.current < floor:
            Elevator.move_up(i)
        elif self.current > floor:
            Elevator.move_down(i)
        elif self.current == floor:
            print("You are already there")

    def move_up(self):
        while self.current != floor:
            self.current += 1
            if self.current == floor:
                Elevator.printing(i)
                print(f"Currently at: Floor{self.current}")

    def move_down(self):
        while self.current != floor:
            Elevator.printing(i)
            self.current -= 1
            if self.current == floor:
                Elevator.printing(i)
                print(f"Currently at: Floor{self.current}")

    def printing(self):
        print(self.current)


i = Elevator(1,4,1)
floor = 1

while floor <= 5:
    floor = int(input("What floor you want to go?"))
    Elevator.elevator_movement(i,floor)