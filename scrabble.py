punkty = 0
znaki = {"a":1, "ą":5, "b":3,
         "c":2, "ć":6, "d":2,
         "e":1, "ę":5, "f":5,
         "g":3, "h":3, "i":1,
         "j":3, "k":2, "l":2,
         "ł":3, "m":2, "n":1,
         "ń":7, "o":1, "ó":5,
         "p":2, "r":1, "s":1,
         "ś":5, "t":2, "u":3,
         "w":1, "y":2, "z":1,
         "ź":9, "ż":5}

slowo = input("podaj słowo do policzenia punktów: ")
print(slowo)
slowo = slowo.lower()
print(slowo)

for literka in slowo:
    if literka in znaki:
        punkty = punkty + znaki[literka]
        print(literka, "- punktów: ", znaki[literka])

print("Twoje punkty: ", punkty)
