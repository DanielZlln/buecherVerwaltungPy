

class Mitglied():
    def __init__(self, mitgliedsnummer, vorname, nachname, email, geburtsdatum, passwort) -> None:
        self.mitgliedsnummer = mitgliedsnummer
        self.vorname = vorname
        self.nachname = nachname
        self.email = email
        self.geburtsdatum = geburtsdatum
        self.passwort = passwort

    def info(self):
        print(f"{self.vorname} {self.nachname} hat die Mitgliedsnummer: {self.mitgliedsnummer}")
    