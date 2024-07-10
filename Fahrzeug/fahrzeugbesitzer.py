# fahrzeugbesitzer.py

from fahrzeugeUnterklasse import Auto, Motorrad
from personUnterklasse import Fahrer, Passagier

class FahrzeugBesitzer:
    def __init__(self, person, fahrzeug):
        self.person = person
        self.fahrzeug = fahrzeug

    def info(self):
        print("Besitzerinformation:")
        self.person.info()
        print("Fahrzeuginformation:")
        self.fahrzeug.info()

class FahrzeugMechaniker:
    def __init__(self, person, fahrzeug):
        self.person = person
        self.fahrzeug = fahrzeug

    def info(self):
        print("Fahrzeuginformation:")
        self.fahrzeug.info()
        print("Besitzerinformation:")
        self.person.info()