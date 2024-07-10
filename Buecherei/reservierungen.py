

class Reservierung():
    def __init__(self, mitgliedsnummer, titel, reservierungsdatum) -> None:
        self.mitgliedsnummer = mitgliedsnummer
        self.titel = titel
        self.reservierungsdatum = reservierungsdatum

    def info(self):
        print(f"Mitglied mit der Nummer {self.mitgliedsnummer} hat das Buch {self.titel} am {self.reservierungsdatum} reserviert")
