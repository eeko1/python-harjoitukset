# Jatka edellisen tehtävän ohjelmaa siten, että
# Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Elevator:

    def __init__(self, low, top, current):
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


    def fire_alarm(self):
        for x in self.elevators:
            x.elevator_movement(self.low)
            print("Fire alarm system activated!!!")


    def drive(self, number, what_floor):
        elevaattori = self.Elevators[number - 1]
        print(f"Ajetaan hissiä {number}")
        if what_floor == 3:
            self.fire_alarm()
        elevaattori.elevator_movement(what_floor)

i = Elevator(1, 5, 1)
floor = 1
Haus = House(1, 5, 3, 1)
while floor < 6:
    Elevator_number = int(input("Choose an elevator"))
    what_floor = int(input("What floor would you like to go?"))
    Haus.drive(Elevator_number, what_floor)