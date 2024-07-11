
from buchverwaltung import *
from mitgliedverwaltung import *
from reservierungverwaltung import *
from login import *

def main():

    buch_verwaltung = BuchVerwaltung()
    mitglied_verwaltung = MitgliedVerwaltung()
    reservierung_verwaltung = ReservierungVerwaltung()


    buch_verwaltung.lese_buecher_aus_csv("buecher.csv")
    mitglied_verwaltung.lese_mitglieder_csv("mitglied.csv")
    reservierung_verwaltung.lese_reservierung_csv("reservierungen.csv")

    login_verwaltung = Login(mitglied_verwaltung)

    userName = input("Bitte Namen eingeben: ")
    passwort = input("Bitte Passwort eingeben: ")

    login = login_verwaltung.login(userName, passwort)

    while(login):

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

        elif var == "b":
            print("Meine Reservierungen anzeigen")
            reservierung_verwaltung.zeige_alle_reservierungen()

        elif var == "c":
            print("Reservierung stornieren")

        elif var == "d":
            print("Speichern")

        elif var == "e":
            print("Beenden")
            break


if __name__ == "__main__":
    main()