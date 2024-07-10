

class Buch():
    def __init__(self, buchId, isbn, titel, veroeffentlichungsdatum, autor, genre, verfuegbare_exemplare) -> None:
        self.buchId = buchId
        self.isbn = isbn
        self.titel = titel
        self.veroeffentlichungsdatum = veroeffentlichungsdatum
        self.autor = autor
        self.genre = genre
        self.verfuegbare_exemplare = verfuegbare_exemplare

    def info(self):
        print(f"Das Buch: {self.titel} ist von {self.autor} und hat noch {self.verfuegbare_exemplare} verfügbare Exemplare")
