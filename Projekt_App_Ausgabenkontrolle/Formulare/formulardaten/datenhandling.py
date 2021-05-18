"""
Funktionen, die für das Laden und speichern der Formulareingaben (Budget/Ausgaben) in zwei
JSON-Dateien verantwortlich sind
"""

import json


"""
Diese Funktion ist da, um zu prüfen, ob bei einer Erfassung im Ausgabenformular bereits eine JSON-Datei mit den Ausgaben
besteht und falls nicht, soll im Ordner Formulare eine neue Datei erstellt werden und sonst die bestehende Datei geladen werden.
"""
def ausgaben_laden():
    datei_name = 'Formulare/ausgaben.json'

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


"""
Diese Funktion ist da, um die erfassten Ausgaben aus dem Ausgabenformular in die geladen JSON-Datei zu speichern
"""
def speichern_ausgaben(ausgaben):
    datei = 'Formulare/ausgaben.json'
    with open(datei, "w") as open_file:
        json.dump(ausgaben, open_file, indent=4)


"""
Diese Funktion ist da, um zu prüfen, ob bei einer Erfassung im Budgetformular bereits eine JSON-Datei mit den Budgets
besteht und falls nicht, soll im Ordner Formulare eine neue Datei erstellt werden und sonst die bestehende Datei geladen werden.
"""
def budget_laden():
    datei_name = 'Formulare/budget.json'

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


"""
Diese Funktion ist da, um die erfassten Budgets aus dem Budgetformular in die geladen JSON-Datei zu speichern.
"""
def speichern_budget(budget):
    datei = 'Formulare/budget.json'
    with open(datei, "w") as open_file:
        json.dump(budget, open_file, indent=4)
