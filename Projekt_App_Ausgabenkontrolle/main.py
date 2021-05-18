"""
main.py File für das Starten der Web-App Ausgabenkontrolle
"""

from flask import Flask
from flask import render_template
from flask import request
from Projekt_App_Ausgabenkontrolle.Formulare.formulardaten.datenhandling import budget_laden
from Projekt_App_Ausgabenkontrolle.Formulare.formulardaten.datenhandling import speichern_budget
from Projekt_App_Ausgabenkontrolle.Formulare.formulardaten.datenhandling import ausgaben_laden
from Projekt_App_Ausgabenkontrolle.Formulare.formulardaten.datenhandling import speichern_ausgaben
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.chartvisualisierung import viz_histogram
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.chartvisualisierung import viz_histogram_thema
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.chartvisualisierung import viz_table_ausgaben
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.chartvisualisierung import viz_table_budget


app = Flask("App Ausgabenkontrolle")


"""
Hier wird die Startseite bzw. mit Bootstrap erstellte Landing-Page aufgerufen, mit der dann auf die weiteren Seiten
navigiert werden kann.
"""
@app.route("/")
def startseite():

    return render_template('landingpage.html')


"""
Um überhaupt Ausgaben erfassen zu können, wird über diese Funktion das Ausgabeformular aufgerufen, über welches die
Ausgaben dann in eine JSON-Datei gespeichert werden mit einem eindeutigen ID-Key, damit keine Ausgabe überschrieben
werden.
"""
@app.route("/ausgaben", methods=["GET", "POST"])
def ausgaben_eingabe():
    if request.method == 'POST':
        id_key = request.form['id_key']
        datum = request.form['datum']
        ausgabe = request.form['ausgabe']
        ausgaben_thema = request.form['ausgaben_thema']
        rueckgabe_ausgaben = {'Datum': datum, 'Ausgabenbetrag': ausgabe, 'Thema': ausgaben_thema}
        daten = ausgaben_laden()
        daten.update({id_key+datum+ausgabe: rueckgabe_ausgaben})
        speichern_ausgaben(daten)
        rueckgabe = str(rueckgabe_ausgaben)
        return render_template('speicherung_ausgaben.html', div=rueckgabe)
    else:
        return render_template('formular_ausgaben.html')


"""
Um  Monatsbudgets erfassen zu können, wird über diese Funktion das Budgetformular aufgerufen, über welches die
Budgets dann in eine JSON-Datei gespeichert werden.
"""
@app.route("/budget", methods=["GET", "POST"])
def budget_eingabe():
    if request.method == 'POST':
        monat = request.form['monat']
        budget = request.form['budget']
        rueckgabe_budget = {'Budgetmonat': monat, 'Budgetbetrag': budget}
        daten = budget_laden()
        daten.update({monat: rueckgabe_budget})
        speichern_budget(daten)
        rueckgabe = str(rueckgabe_budget)
        return render_template('speicherung_budget.html', div=rueckgabe)
    else:
        return render_template('formular_budget.html')


"""
Mit den nachfolgenden Funktionen können die verschiedenen Visualisierungen aufgerufen werden, die im Directory 
'Datenvisualisierung' erstellt wurden aufgrund der erfassten Angaben aus dem Ausgaben- und Budgetformular. Es ermöglicht
den visuellen Vergleich der aktuellen Ausgaben zu den definierten Monats-Budgets, wofür Geld ausgegeben wurde und die
einzelnen Erfassungen.
"""
@app.route("/viz")
def viz_ausgaben_budget():
    div_1 = viz_histogram()
    return render_template('viz1.html', viz_div_1=div_1)


@app.route("/viz1")
def viz_ausgaben_thema():
    div_2 = viz_histogram_thema()
    return render_template('viz2.html', viz_div_2=div_2)


@app.route("/viz3")
def viz_tabelle_ausgaben():
    div_3 = viz_table_ausgaben()
    return render_template('viz3.html', viz_div_3=div_3)


@app.route("/viz4")
def viz_tabelle_budget():
    div_4 = viz_table_budget()
    return render_template('viz4.html', viz_div_4=div_4)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
