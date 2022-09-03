import random

pelaajanluku = int(input("Anna luku 1-10 väliltä:"))
luku = random.randint(1, 10)

while pelaajanluku < luku:
    print("Liian pieni arvaus")
    pelaajanluku = int(input("Anna luku 1-10 väliltä:"))

    if pelaajanluku > luku:
        print("Liian suuri arvaus")
        pelaajanluku = int(input("Anna luku 1-10 väliltä:"))

    if pelaajanluku == luku:
        print("Oikein.")