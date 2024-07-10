# person.py

class Person:
    def __init__(self, name, geburtsjahr):
        self.name = name
        self.geburtsjahr = geburtsjahr

    def info(self):
        print(f"Name: {self.name}, Geburtsjahr: {self.geburtsjahr}")

    def alter(self, aktuelles_jahr):
        return aktuelles_jahr - self.geburtsjahr

    def to_dict(self):
        return {
            "name": self.name,
            "geburtsjahr": self.geburtsjahr
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["geburtsjahr"])
