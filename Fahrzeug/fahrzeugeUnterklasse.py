# fahrzeugUnterklasse.py

from fahrzeug import Fahrzeug

class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, sitze):
        super().__init__(marke, modell, baujahr)
        self.sitze = sitze

    def info(self):
        super().info()
        print(f"Anzahl der Sitze: {self.sitze}")

    def to_dict(self):
        data = super().to_dict()
        data["sitze"] = self.sitze
        data["type"] = "Auto"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["marke"], data["modell"], data["baujahr"], data["sitze"])

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, hubraum):
        super().__init__(marke, modell, baujahr)
        self.hubraum = hubraum

    def info(self):
        super().info()
        print(f"Hubraum: {self.hubraum} ccm")

    def to_dict(self):
        data = super().to_dict()
        data["hubraum"] = self.hubraum
        data["type"] = "Motorrad"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["marke"], data["modell"], data["baujahr"], data["hubraum"])

class LKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, traglast):
        super().__init__(marke, modell, baujahr)
        self.traglast = traglast

    def info(self):
        super().info()
        print(f"Traglast: {self.traglast}t")

    def to_dict(self):
        data = super().to_dict()
        data["traglast"] = self.traglast
        data["type"] = "LKW"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["marke"], data["modell"], data["baujahr"], data["traglast"])
