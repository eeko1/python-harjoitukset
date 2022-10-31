#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
#Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
#Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
#Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


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

    def move_up(self): #kerros_ylös
        while self.current != floor:
            self.current += 1
            if self.current == floor:
                Elevator.printing(i)
                print(f"Currently at: Floor{self.current}")

    def move_down(self): #kerros_alas
        while self.current != floor:
            Elevator.printing(i)
            self.current -= 1
            if self.current == floor:
                Elevator.printing(i)
                print(f"Currently at: Floor{self.current}")

    def printing(self):
        print(self.current)


class House:

    def __init__(self, low, top, number, current):
        self.low = low
        self.top = top
        self.number = number
        self.current = current
        self.Elevators = []
        for i in range(1, 4):
           self.Elevators.append(Elevator(1, 50, 1))

    def aja(self, number, kohde):
        elevator = self.Elevators[number - 1]
        print(f"Ajetaan hissiä {number}")


i = Elevator(1, 50, 1)    # i = h
floor = 1
Haus = House(1, 50, 3, 1)
while floor < 51:
    Elevator_number = int(input("Valitse hissi"))
    what_floor = int(input("Mihin kerrokseen haluat?"))
    Haus.aja(Elevator_number, what_floor)