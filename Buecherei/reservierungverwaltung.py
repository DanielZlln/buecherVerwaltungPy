
import csv
from reservierungen import Reservierung
from buchverwaltung import *
from datetime import datetime

class ReservierungVerwaltung():

    def __init__(self, buch_verwaltung) -> None:
        self.reservierungen = []
        self.buch_verwaltung = buch_verwaltung

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

    def zeige_alle_reservierungen(self, mitgliedsnummer):
        for res in self.reservierungen:
            if res.mitgliedsnummer == mitgliedsnummer:
                res.info()


#  Das Buch muss richtig ausgewählt werden!!!!!!!!



    def zeige_alle_reservierungen_storno(self, mitgliedsnummer, id_storno):
        for count, res in reversed(list(enumerate(self.reservierungen))):
            print(count, res)
            if res.mitgliedsnummer == mitgliedsnummer:
                for buch in self.buch_verwaltung.buecher:
                    if res.titel == buch.titel:
                        print(f"{buch.titel} mit der ID {buch.buchId} ist aktuell reserviert")
                        del self.reservierungen[count]
                        break

    def reserviere_buch(self, id, mitgliednummer):
        kein_buch = True

        for buch in self.buch_verwaltung.buecher:

            if buch.buchId == id:
                print(f"Das Buch '{buch.titel}' wurde reserviert!")

                titel = buch.titel
                reservierungsdatum = datetime.today().strftime('%d.%m.%Y')

                neue_reservierung = Reservierung(
                    mitgliednummer,
                    titel,
                    reservierungsdatum
                )

                self.reservierungen.append(neue_reservierung)

                kein_buch = False

        if kein_buch:
            print(f"Kein Buch mit der ID {id} gefunden")

    def schreibe_reservierung_csv(self, dateiname):
        with open(dateiname, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            writer.writerow(["mitgliedsnummer", "titel", "reservierungsdatum"])  # Schreibe die Überschrift

            for res in self.reservierungen:
                writer.writerow([res.mitgliedsnummer, res.titel, res.reservierungsdatum])  # Schreibe die Datenzeilen