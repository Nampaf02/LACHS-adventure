# Hier werden Waffen generiert
from Items import item


class waffen(item):
    def __init__(self, name, beschreibung, wert, schaden):
        self.schaden = schaden
        super().__init__(name, beschreibung, wert)

    def __str__(self):
        return "{}\n=====\n{}\nWert: {}\nSchaden: {}".format(self.name, self.beschreibung, self.wert, self.schaden)

class kurzschwert(waffen):
    def __init__(self):
        super().__init__(name = "Kurzschwert",
                         beschreibung = "Ein Schwert mit einer kurzen beidseitig geschliffenen Klinge",
                         wert = 15,
                         schaden = 7)

t = kurzschwert()
print(t)
