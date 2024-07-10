
from buchverwaltung import *
from mitgliedverwaltung import *
from reservierungverwaltung import *

def main():

    buch_verwaltung = BuchVerwaltung()
    mitglied_verwaltung = MitgliedVerwaltung()
    reservierung_verwaltung = ReservierungVerwaltung()

    buch_verwaltung.lese_buecher_aus_csv("Buecherei/buecher.csv")
    mitglied_verwaltung.lese_mitglieder_csv("Buecherei/mitglied.csv")
    reservierung_verwaltung.lese_reservierung_csv("Buecherei/reservierungen.csv")


if __name__ == "__main__":
    main()