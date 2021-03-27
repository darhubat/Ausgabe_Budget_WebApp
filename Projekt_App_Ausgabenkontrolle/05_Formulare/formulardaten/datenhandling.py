import json


#   prüfen, ob ein JSON vorhanden ist für die Ausgaben, falls nein, neue erstellen
def ausgaben_laden():
    datei_name = "ausgaben.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


#   Speichern der erfassten Ausgaben
def speichern_ausgaben(ausgaben):
    datei = "ausgaben.json"
    with open(datei, "w") as open_file:
        json.dump(ausgaben, open_file, indent=4)


#   prüfen, ob ein JSON vorhanden ist für das Budget, falls nein, neue erstellen
def budget_laden():
    datei_name = "budget.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


#   Speichern des erfassten Budgets
def speichern_budget(budget):
    datei = "budget.json"
    with open(datei, "w") as open_file:
        json.dump(budget, open_file, indent=4)
