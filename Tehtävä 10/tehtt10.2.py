#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
#Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
#Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
#Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


class Elevator:

    def __init__(self, low, top, current):
        self.low = low
        self.top = top
        self.current = current

    def elevator_movement(self, floor):
        if self.current < floor:
            Elevator.move_up(e)
        elif self.current > floor:
            Elevator.move_down(e)
        elif self.current == floor:
            print("You are already at that floor")

    def move_up(self): #kerros_ylös
        while self.current != floor:
            Elevator.printing(self)
            self.current += 1
            if self.current == floor:
                print(f"Currently at: Floor{self.current}")

    def move_down(self): #kerros_alas
        while self.current != floor:
            Elevator.printing(self)
            self.current -= 1
            if self.current == floor:
                print(f"Currently at: Floor{self.current}")

    def printing(self):
        print(self.current)


class House:

    def __init__(self, low, top, number, current):
        self.low = low
        self.top = top
        self.number = number
        self.current = current
        self.elevators = []
        for i in range(number):
            self.elevators.append(Elevator(1, 4, 1))

    def drive(self, number, what_floor):
        ele = self.elevators[number - 1]
        print(f"Elevator {number} moving")
        ele.elevator_movement(what_floor)

floor = 1
e = Elevator(1, 4, 1)
h = House(1, 5, 3, 1)
while floor < 6:
    Elevator_number = int(input("Choose an elevator:"))
    what_floor = int(input("What floor would you like to go?"))
    if what_floor > 6:
        break
