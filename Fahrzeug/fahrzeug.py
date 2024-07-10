# fahrzeug.py

class Fahrzeug:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def info(self):
        print(f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}")

    def alter(self, aktuelles_jahr):
        return aktuelles_jahr - self.baujahr

    def to_dict(self):
        return {
            "marke": self.marke,
            "modell": self.modell,
            "baujahr": self.baujahr
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["marke"], data["modell"], data["baujahr"])
