class Auto():
    """ Das ist meine Auto Klasse, sodass ich nicht jedes mal aufs Neue alles definieren muss. """
    def __init__(self, marke, modell, jahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps

    def info(self):
        print("Dein Auto hat folgende Werte:")
        print("Marke: ", self.marke)
        print("Modell: ", self.modell)
        print("Jahr: ", self.jahr)
        print("Räder: ", self.raeder)
        print("Türen: ", self.tueren)
        print("PS: ", self.ps)

    def begruessung(self):
        print("Hallo mein Lieber, ich bin " + self.marke)


    def fahren(self):
        print("Brmbrmbrm" * int(self.ps/10))


class Sportwagen(Auto):
    def __init__(self, marke, modell, jahr, tueren, ps):
        super().__init__(marke, modell, jahr, tueren, ps)
        self.auspuff = 2

    def turbo(self):
        print("Turbo activated")

    def fahren(self):
        print("RACEEEEEE")


sw1 = Sportwagen( marke= "Seat", modell= "Ibiza", jahr= 2020, tueren= 2, ps= 500)
print(sw1.modell)
a1 = Auto(marke="Seat", modell="Ibiza", jahr= 2020, tueren= 2, ps= 500)

a1.info()