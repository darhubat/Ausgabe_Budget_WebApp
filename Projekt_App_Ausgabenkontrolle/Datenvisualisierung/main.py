from flask import Flask
from flask import render_template
import plotly.express as px
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_mergen
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_ausgabeneingabe
from plotly.offline import plot


app = Flask("Datenvisualisierung")


def data_viz():
    data = daten_mergen()
    return data


""""
def viz_barchart():
    data = data_viz()
    fig = px.bar(data, x='Monat', y='Betrag', hover_data=['typ', 'Jahr', 'Monat', 'Betrag', 'Thema'], color='typ',
                 title='Ausgaben-/Budgetvergleich', animation_frame='Jahr', barmode='group')
    fig.update_xaxes(dtick=1, range=[1, 12])
    fig.update_layout(xaxis_title='Monate', yaxis_title='Betrag in CHF')
    div = fig.show()
    #  div = plot(fig, output_type='div')
    return div
"""


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
    div_1 = fig.show()
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


@app.route("/viz")
def index():
    div = viz_histogram()
    return render_template('index.html', viz_div=div)


@app.route("/viz2")
def index_2():
    div_1 = viz_histogram_thema()
    return render_template('index.html', viz_div=div_1)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
