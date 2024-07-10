import json
from fahrzeugeUnterklasse import Auto, Motorrad, LKW
from personUnterklasse import Fahrer, Passagier, Mechaniker
from fahrzeugbesitzer import FahrzeugBesitzer, FahrzeugMechaniker
from objekteErstellen import *

# Listen zum Speichern von Objekten
fahrzeuge = []
personen = []
besitzer = []

def save_data(filename, fahrzeuge, personen):
    data = {
        "fahrzeuge": [fahrzeug.to_dict() for fahrzeug in fahrzeuge],
        "personen": [person.to_dict() for person in personen]
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Daten erfolgreich gespeichert!")

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        fahrzeuge = []
        for item in data["fahrzeuge"]:
            if item["type"] == "Auto":
                fahrzeuge.append(Auto.from_dict(item))
            elif item["type"] == "Motorrad":
                fahrzeuge.append(Motorrad.from_dict(item))
            elif item["type"] == "LKW":
                fahrzeuge.append(LKW.from_dict(item))
        personen = []
        for item in data["personen"]:
            if item["type"] == "Fahrer":
                personen.append(Fahrer.from_dict(item))
            elif item["type"] == "Passagier":
                personen.append(Passagier.from_dict(item))
            elif item["type"] == "Mechaniker":
                personen.append(Mechaniker.from_dict(item))
        print("Daten erfolgreich geladen!")
        return fahrzeuge, personen
    except FileNotFoundError:
        print("Keine gespeicherten Daten gefunden.")
        return [], []

def main():
    global fahrzeuge, personen
    fahrzeuge, personen = load_data("data.txt")

    while True:
        print("\n--- Menü ---")
        print("1. Auto erstellen")
        print("2. Motorrad erstellen")
        print("3. LKW erstellen")
        print("4. Fahrer erstellen")
        print("5. Passagier erstellen")
        print("6. Mechaniker erstellen")
        print("7. FahrzeugBesitzer erstellen")
        print("8. FahrzeugMechaniker erstellen")
        print("9. Alle Besitzer anzeigen")
        print("10. Speichern und Beenden")
        
        wahl = input("Wählen Sie eine Option: ")
        
        if wahl == "1":
            erstelle_auto(fahrzeuge)
        elif wahl == "2":
            erstelle_motorrad(fahrzeuge)
        elif wahl == "3":
            erstelle_lkw(fahrzeuge)
        elif wahl == "4":
            erstelle_fahrer(personen)
        elif wahl == "5":
            erstelle_passagier(personen)
        elif wahl == "6":
            erstelle_mechaniker(personen)
        elif wahl == "7":
            erstelle_fahrzeugbesitzer(personen, fahrzeuge, besitzer)
        elif wahl == "8":
            erstelle_fahrzeugmechaniker(personen, fahrzeuge, besitzer)
        elif wahl == "9":
            zeige_alle_besitzer(besitzer)
        elif wahl == "10":
            save_data("data.txt", fahrzeuge, personen)
            break
        else:
            print("Ungültige Option, bitte wählen Sie erneut.")
        
        # Hier füge ich die Zeile hinzu, um das erste Fahrzeug in der Liste zu drucken
        if fahrzeuge:
            print("Details der Fahrzeuge in der Liste:")
            for fahrzeug in fahrzeuge:
                fahrzeug.info()

if __name__ == "__main__":
    main()
