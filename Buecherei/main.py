
from buchverwaltung import *
from mitgliedverwaltung import *
from reservierungverwaltung import *
from login import *

def main():

    buch_verwaltung = BuchVerwaltung()
    mitglied_verwaltung = MitgliedVerwaltung()
    reservierung_verwaltung = ReservierungVerwaltung(buch_verwaltung)


    buch_verwaltung.lese_buecher_aus_csv("buecher.csv")
    mitglied_verwaltung.lese_mitglieder_csv("mitglied.csv")
    reservierung_verwaltung.lese_reservierung_csv("reservierungen.csv")

    login_verwaltung = Login(mitglied_verwaltung)

    userName = input("Bitte Namen eingeben: ")
    passwort = input("Bitte Passwort eingeben: ")

    mitglied = login_verwaltung.login(userName, passwort)
    mit_nummer = mitglied.mitgliedsnummer

    if mitglied:
        while True:
            print("------------------------------------------")
            print("Wähle eines der Folgenden Menüs aus: \n" + 
                "a) Buch reservieren \n" +
                "b) Meine Reservierungen anzeigen \n" +
                "c) Reservierung stornieren \n" +
                "d) Speichern \n" +
                "e) Beenden")

            var = input("Welches Menü möchtest du aufrufen: ").lower()

            if var == "a":
                print("Buch reservieren")
                buch_verwaltung.zeige_alle_buecher()

                print("Welches Buch soll reserviert werden?")

                try:
                    id_res = int(input("Gib die ID des Buches ein: "))
                    reservierung_verwaltung.reserviere_buch(id_res, mit_nummer)
                except ValueError:
                    print("Ungültige Eingabe. Bitte gib eine numerische ID ein.")

            elif var == "b":
                print("Meine Reservierungen anzeigen")
                reservierung_verwaltung.zeige_alle_reservierungen(mit_nummer)

            elif var == "c":
                try:
                    print("Welches Buch soll storniert werden?")
                    id_res = int(input("Gib die ID des Buches ein: "))
                    reservierung_verwaltung.zeige_alle_reservierungen_storno(mit_nummer, id_res)
  
                except ValueError:
                    print("Ungültige Eingabe. Bitte gib eine numerische ID ein.")

            elif var == "d":
                print("Speichern")

                reservierung_verwaltung.schreibe_reservierung_csv("reservierungen.csv")

            elif var == "e":
                print("Beenden")
                break


if __name__ == "__main__":
    main()