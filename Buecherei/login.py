
from mitglieder import Mitglied
from mitgliedverwaltung import *

class Login():

    def __init__(self, mitglied_verwaltung) -> None:
        self.mitglied_verwaltung = mitglied_verwaltung

    def login(self, userName, passwort):

        for mitglied in self.mitglied_verwaltung.mitglieder:
            if mitglied.vorname == userName and mitglied.passwort == passwort:
                print(f"Gefundenes Mitglied: {mitglied.vorname} {mitglied.nachname}")

                return mitglied
        
        print("Logindaten falsch!")
        return None