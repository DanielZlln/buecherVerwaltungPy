# personUnterklasse.py

from person import Person

class Fahrer(Person):
    def __init__(self, name, geburtsjahr, fuehrerschein):
        super().__init__(name, geburtsjahr)
        self.fuehrerschein = fuehrerschein

    def info(self):
        super().info()
        print(f"Führerschein: {self.fuehrerschein}")

    def to_dict(self):
        data = super().to_dict()
        data["fuehrerschein"] = self.fuehrerschein
        data["type"] = "Fahrer"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["geburtsjahr"], data["fuehrerschein"])

class Passagier(Person):
    def __init__(self, name, geburtsjahr):
        super().__init__(name, geburtsjahr)

    def info(self):
        super().info()

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Passagier"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["geburtsjahr"])

class Mechaniker(Person):
    def __init__(self, name, geburtsjahr, gebiet):
        super().__init__(name, geburtsjahr)
        self.gebiet = gebiet

    def info(self):
        super().info()
        print(f"Aufgabengebiet: {self.gebiet}")

    def to_dict(self):
        data = super().to_dict()
        data["gebiet"] = self.gebiet
        data["type"] = "Mechaniker"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["geburtsjahr"], data["gebiet"])
