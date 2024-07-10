
import csv
from reservierungen import Reservierung

class ReservierungVerwaltung():

    def __init__(self) -> None:
        self.reservierungen = []

    def lese_reservierung_csv(self, dateiname):
        with open(dateiname, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                reservierung = Reservierung(
                    mitgliedsnummer=int(row['mitgliedsnummer']),
                    titel=row['titel'],
                    reservierungsdatum=row['reservierungsdatum'],
                )
                self.reservierungen.append(reservierung)

    def zeige_alle_reservierungen(self):
        for res in self.reservierungen:
            res.info()