from random import randint
zahl = randint(a=1, b=100)

print("Hey, ich habe mir eine Zahl zwischen 1 und 100 ausgedacht! ")

while True:
    versuch = int(input("Rate meine Zahl: "))

    if versuch == zahl:
        print("Super, du hast die Zahl erraten!")
        break

    elif versuch < zahl:
        print("Die Zahl ist zu klein!")

    else:
        print("Die Zahl ist zu groß!")