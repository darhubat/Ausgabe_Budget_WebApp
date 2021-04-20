"""
Funktionen, die für das Laden und speichern der Formulareingaben (Budget/Ausgaben) in zwei
JSON-Dateien verantwortlich sind
"""

import json


#   Prüft, ob ein JSON-Datei im Ordner Formulare vorhanden ist für die Ausgaben, falls nein, wird eine Neue erstellt
def ausgaben_laden():
    datei_name = 'Formulare/ausgaben.json'

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


#   Speichert die erfassten Ausgaben in der JSON-Datei
def speichern_ausgaben(ausgaben):
    datei = 'Formulare/ausgaben.json'
    with open(datei, "w") as open_file:
        json.dump(ausgaben, open_file, indent=4)


#   Prüft, ob ein JSON-Datei vorhanden ist für das Budget, falls nein, wird eine Neue erstellt
def budget_laden():
    datei_name = 'Formulare/budget.json'

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


#   Speichert die erfassten Budgets in der JSON-Datei
def speichern_budget(budget):
    datei = 'Formulare/budget.json'
    with open(datei, "w") as open_file:
        json.dump(budget, open_file, indent=4)
