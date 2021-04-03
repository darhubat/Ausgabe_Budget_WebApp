import plotly.express as px
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_budgeteingabe
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_ausgabeneingabe
from Projekt_App_Ausgabenkontrolle.Datenvisualisierung.datenvorbereitung.datengrundlage import daten_mergen




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
    return div
