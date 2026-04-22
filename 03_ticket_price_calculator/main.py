alter = int(input("Wie alt bist du?"))
anzahl = int(input("Wie viele Tickets möchtest du haben?"))
x = 5 #preis für u18
y = 7.5 #preis für ü65
z = 10 #preis für ü18

if alter > 65:
    print("Das macht dann", y * anzahl, " Euro!")

elif alter >= 18:
    print("Das macht dann", z * anzahl, " Euro!")

else:
    print("Das macht dann", x * anzahl, " Euro!")

input("Drücke Enter zum Beenden...")