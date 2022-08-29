
gender = input("Sukupuolesi (nainen/mies)? ")
hg_value = int(input("Hemoglobiinisi (g/l= "))

if gender == "nainen":
    #testataan naisen ohjearvot
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on liian korkea")
elif gender == "mies":
    # testataan miehen arvot
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 195:
        print ("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on liian korkea")

