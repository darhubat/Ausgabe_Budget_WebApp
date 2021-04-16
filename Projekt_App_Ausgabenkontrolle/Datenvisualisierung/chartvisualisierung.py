"""
Funktionen, die den Ausgaben-/Budget-Vergleich mit Plotly Epress visualisieren und zusätzlich die Ausgaben
nach Ausgaben-Thema zusammenfasst und ebenfalls visuell darstellt
"""

import plotly.express as px
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_budgeteingabe
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_ausgabeneingabe
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_mergen
from plotly.offline import plot
import plotly.graph_objects as go


def data_viz():
    data = daten_mergen()
    return data

def viz_histogram():
    data = daten_mergen()
    fig = px.histogram(data, x='date', y='Betrag', hover_name='typ', hover_data=['Thema'], color='typ',
                         barmode='group')
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
                         barmode='group')
    fig.update_layout(xaxis_title='Jahre', yaxis_title='Betrag in CHF', bargap=0.2, hovermode='x')
    fig.update_traces(xbins_size="M1")
    fig.update_xaxes(ticklabelmode='period', showspikes=True)
    fig.update_yaxes(showspikes=True)
    div_2 = plot(fig, output_type='div')
    return div_2


def viz_table_ausgaben():
    data = daten_ausgabeneingabe()
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[data.Jahr, data.Monat, data.Thema, data.date, data.Betrag, data.typ],
                   fill_color='lavender',
                   align='left'))
    ])
    div_3 = plot(fig, output_type='div')
    return div_3


def viz_table_budget():
    data_1 = daten_budgeteingabe()
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data_1.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[data_1.Jahr, data_1.Monat, data_1.Thema, data_1.date, data_1.Betrag, data_1.typ],
                   fill_color='lavender',
                   align='left'))
    ])
    div_4 = plot(fig, output_type='div')
    return div_4
