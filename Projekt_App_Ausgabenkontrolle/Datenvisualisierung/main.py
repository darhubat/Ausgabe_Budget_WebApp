from flask import Flask
from flask import render_template
import plotly.express as px
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_mergen
from plotly.offline import plot


app = Flask("Datenvisualisierung")

def data_viz():
    data = daten_mergen()
    return data

def viz_barchart():
    data = data_viz()
    fig = px.bar(data, x='Monat', y='Betrag', hover_data=['typ', 'Jahr', 'Monat', 'Betrag', 'Thema'], color='typ',
                 title='Ausgaben-/Budgetvergleich', animation_frame='Jahr', barmode='group')
    fig.update_xaxes(dtick=1, range=[1, 12])
    fig.update_layout(xaxis_title='Monate', yaxis_title='Betrag in CHF')
    div = fig.show()
    #  div = plot(fig, output_type='div')
    return div


@app.route("/viz")
def index():
    div = viz_barchart()
    return render_template('index.html', viz_div=div)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
