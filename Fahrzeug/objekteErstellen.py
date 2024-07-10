from fahrzeugeUnterklasse import Auto, Motorrad, LKW
from personUnterklasse import Fahrer, Passagier, Mechaniker
from fahrzeugbesitzer import FahrzeugBesitzer, FahrzeugMechaniker

def erstelle_auto(fahrzeuge):
    marke = input("Geben Sie die Marke des Autos ein: ")
    modell = input("Geben Sie das Modell des Autos ein: ")
    baujahr = int(input("Geben Sie das Baujahr des Autos ein: "))
    sitze = int(input("Geben Sie die Anzahl der Sitze des Autos ein: "))
    auto = Auto(marke, modell, baujahr, sitze)
    fahrzeuge.append(auto)
    print("Auto erfolgreich erstellt!")


def erstelle_motorrad(fahrzeuge):
    marke = input("Geben Sie die Marke des Motorrads ein: ")
    modell = input("Geben Sie das Modell des Motorrads ein: ")
    baujahr = int(input("Geben Sie das Baujahr des Motorrads ein: "))
    hubraum = int(input("Geben Sie den Hubraum des Motorrads in ccm ein: "))
    motorrad = Motorrad(marke, modell, baujahr, hubraum)
    fahrzeuge.append(motorrad)
    print("Motorrad erfolgreich erstellt!")
    return motorrad

def erstelle_lkw(fahrzeuge):
    marke = input("Geben Sie die Marke des LKWs ein: ")
    modell = input("Geben Sie das Modell des LKWs ein: ")
    baujahr = int(input("Geben Sie das Baujahr des LKWs ein: "))
    traglast = int(input("Geben Sie die Traglast des LKWs in Tonnen ein: "))
    lkw = LKW(marke, modell, baujahr, traglast)
    fahrzeuge.append(lkw)
    print("LKW erfolgreich erstellt!")
    return lkw

def erstelle_fahrer(personen):
    name = input("Geben Sie den Namen des Fahrers ein: ")
    geburtsjahr = int(input("Geben Sie das Geburtsjahr des Fahrers ein: "))
    fuehrerschein = input("Geben Sie die Führerscheinklasse des Fahrers ein: ")
    fahrer = Fahrer(name, geburtsjahr, fuehrerschein)
    personen.append(fahrer)
    print("Fahrer erfolgreich erstellt!")
    return fahrer

def erstelle_passagier(personen):
    name = input("Geben Sie den Namen des Passagiers ein: ")
    geburtsjahr = int(input("Geben Sie das Geburtsjahr des Passagiers ein: "))
    passagier = Passagier(name, geburtsjahr)
    personen.append(passagier)
    print("Passagier erfolgreich erstellt!")
    return passagier

def erstelle_mechaniker(personen):
    name = input("Geben Sie den Namen des Mechanikers ein: ")
    geburtsjahr = int(input("Geben Sie das Geburtsjahr des Mechanikers ein: "))
    gebiet = input("Geben Sie das Spezialgebiet des Mechanikers ein: ")
    mechaniker = Mechaniker(name, geburtsjahr, gebiet)
    personen.append(mechaniker)
    print("Mechaniker erfolgreich erstellt!")
    return mechaniker

def erstelle_fahrzeugbesitzer(personen, fahrzeuge, besitzer):
    print("Wählen Sie eine Person aus der Liste aus:")
    for i, person in enumerate(personen):
        print(f"{i + 1}. {person.name}")

    person_index = int(input("Person Nummer: ")) - 1
    person = personen[person_index]

    print("Wählen Sie ein Fahrzeug aus der Liste aus:")
    for i, fahrzeug in enumerate(fahrzeuge):
        print(f"{i + 1}. {fahrzeug.marke} {fahrzeug.modell}")

    fahrzeug_index = int(input("Fahrzeug Nummer: ")) - 1
    fahrzeug = fahrzeuge[fahrzeug_index]

    besitzer_obj = FahrzeugBesitzer(person, fahrzeug)
    besitzer.append(besitzer_obj)
    print("FahrzeugBesitzer erfolgreich erstellt!")

def erstelle_fahrzeugmechaniker(personen, fahrzeuge, besitzer):
    print("Wählen Sie einen Mechaniker aus der Liste aus:")
    for i, person in enumerate(personen):
        if isinstance(person, Mechaniker):
            print(f"{i + 1}. {person.name}")

    person_index = int(input("Mechaniker Nummer: ")) - 1
    person = personen[person_index]

    print("Wählen Sie ein Fahrzeug aus der Liste aus:")
    for i, fahrzeug in enumerate(fahrzeuge):
        print(f"{i + 1}. {fahrzeug.marke} {fahrzeug.modell}")

    fahrzeug_index = int(input("Fahrzeug Nummer: ")) - 1
    fahrzeug = fahrzeuge[fahrzeug_index]

    mechaniker_obj = FahrzeugMechaniker(person, fahrzeug)
    besitzer.append(mechaniker_obj)
    print("FahrzeugMechaniker erfolgreich erstellt!")

def zeige_alle_besitzer(besitzer):
    for besitzer_obj in besitzer:
        besitzer_obj.info()
        print()
