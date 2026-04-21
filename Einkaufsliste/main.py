einkaufsliste = []

# Artikel hinzufügen
# Aktion -> hinzufügen, entfernen, anzeigen oder beenden

while True:
    aktion = input("Möchtest du einen Artikel hinzufügen, entfernen oder die Liste anzeigen? (hinzufügen / entfernen / anzeigen / beenden) ")

    # hinzufügen
    if aktion == "hinzufügen":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print("Artikel wurde hinzugefügt")
    # löschen
    elif aktion == "entfernen":
        artikel = input("Welchen Artikel möchtest du entfernen? ")
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            print("Artikel wurde gelöscht")
        else:
            print("Den Artikel gibt es nicht!")

    # anzeigen
    elif aktion == "anzeigen":
        print("Deine Einkaufsliste:")
        print(einkaufsliste)
    # beenden
    elif aktion == "beenden":
        print("Einkaufsliste beendet.")
        break

    else:
        print("Du musst das schon richtig eingeben.")