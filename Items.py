# Items 

class item():
    def __init__(self, name, beschreibung, wert):
        self.name = name
        self.beschreibung = beschreibung
        self.wert = wert
    def __str__(self):
        return "{}\n=====\n{}\nWert: {}\n".format(self.name, self.beschreibung, self.wert)
    
class gold(item):
    def __init__(self, menge):
        self.menge = menge
        super().__init__(name="Gold",
                         beschreibung="Ein rundes Stueck Gold mit einer {} auf der Vorderseite.".format(str(self.menge)),
                         wert=self.menge)



g = gold('345')
print(g)
