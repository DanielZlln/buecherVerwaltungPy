
from buch import Buch
import csv

class BuchVerwaltung:
    def __init__(self):
        self.buecher = []

    def lese_buecher_aus_csv(self, dateiname):
        with open(dateiname, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                buch = Buch(
                    buchId=int(row['BuchId']),
                    isbn=row['ISBN'],
                    titel=row['Titel'],
                    veroeffentlichungsdatum=row['Veröffentlichungsdatum'],
                    autor=row['Autor'],
                    genre=row['Genre'],
                    verfuegbare_exemplare=int(row['Verfügbare Exemplare'])
                )
                self.buecher.append(buch)

    def zeige_alle_buecher(self):
        for buch in self.buecher:
            buch.info()