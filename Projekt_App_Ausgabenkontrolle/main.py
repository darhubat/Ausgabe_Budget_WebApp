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
import plotly.express as px
from plotly.offline import plot
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_mergen
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_ausgabeneingabe


app = Flask("App Ausgabenkontrolle")


@app.route("/")
def startseite():

    return render_template("landing_page.html")


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
        return "Die folgende Ausgaben-Erfassung wurde erfolgreich gespeichert: " + '<br>' + str(rueckgabe_ausgaben)
    else:
        return render_template("ausgaben.html")


@app.route("/budget", methods=["GET", "POST"])
def budget_eingabe():
    if request.method == 'POST':
        monat = request.form['monat']
        budget = request.form['budget']
        rueckgabe_budget = {'Budgetmonat': monat, 'Budgetbetrag': budget}
        daten = budget_laden()
        daten.update({monat: rueckgabe_budget})
        speichern_budget(daten)
        return "Die folgende Budget-Erfassung wurde erfolgreich gespeichert: " + '<br>' + str(rueckgabe_budget)
    else:
        return render_template("budget.html")


def data_viz():
    data = daten_mergen()
    return data


def viz_histogram():
    data = data_viz()
    fig = px.histogram(data, x='date', y='Betrag', hover_name='typ', hover_data=['Thema'], color='typ',
                        title='Ausgaben-/Budgetvergleich', barmode='group')
    fig.update_layout(xaxis_title='Monat/Jahr', yaxis_title='Betrag in CHF', bargap=0.2, hovermode='x')
    fig.update_traces(xbins_size="M1")
    fig.update_xaxes(ticklabelmode='period', dtick='M1', tickformat='%b\n%Y', showspikes=True)
    fig.update_yaxes(showspikes=True)
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    div_1 = plot(fig, output_type='div')
    return div_1


def viz_histogram_thema():
    data = daten_ausgabeneingabe()
    fig = px.histogram(data, x='Jahr', y='Betrag', hover_name='typ', hover_data=['Thema'], color='Thema',
                        title='Ausgaben nach Thema', barmode='group')
    fig.update_layout(xaxis_title='Jahre', yaxis_title='Betrag in CHF', bargap=0.2, hovermode='x')
    fig.update_traces(xbins_size="M1")
    fig.update_xaxes(ticklabelmode='period', showspikes=True)
    fig.update_yaxes(showspikes=True)
    div_2 = fig.show()
    return div_2


@app.route("/viz1")
def index():
    div_1 = viz_histogram()
    div_1 = div_1.show()
    return render_template('viz1.html', viz_div=div_1)


@app.route("/viz2")
def index_2():
    div_2 = viz_histogram_thema()
    return render_template('viz2.html', viz_div=div_2)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
