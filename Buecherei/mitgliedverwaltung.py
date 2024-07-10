
from mitglieder import Mitglied
import csv

class MitgliedVerwaltung():

    def __init__(self) -> None:
        self.mitglieder = []

    def lese_mitglieder_csv(self, dateiname):

        with open(dateiname, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                mitglied = Mitglied(
                    mitgliedsnummer=int(row['mitgliedsnummer']),
                    vorname=row['vorname'],
                    nachname=row['nachname'],
                    email=row['email'],
                    geburtsdatum=row['geburtsdatum'],
                    passwort=row['passwort'],

                )
                self.mitglieder.append(mitglied)

    def zeige_alle_mitglieder(self):
        for mitglied in self.mitglieder:
            mitglied.info()