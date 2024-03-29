"""
Funktionen, welche die gespeicherten Daten aus der JSON-Dateien (Budget/Ausgaben) mithilfe von Pandas in die
richtige Form bringen und mergt, um die Datenvisualisierung mit Plotly Express zu erstellen
"""

import pandas as pd

"""
Damit die Viusalisierung der Budget-Eingaben aus der JSON-Datei visualisiert werden können, werden die Daten mit Pandas
in eine Tabellenform gebracht, die Spaltennamen vereinheitlicht und für den späteren Merge mit den Ausgaben-Eingaben vorbereitet
"""
def daten_budgeteingabe():
    df = pd.read_json(r'Formulare\budget.json')
    df = df.T  # transponiert die Tabelle in gewünschte Form
    df['Budgetbetrag'] = df['Budgetbetrag'].apply(pd.to_numeric)  # Ausgaben als Zahl definieren, war ein Objekt
    df['Budgetmonat'] = pd.to_datetime(df['Budgetmonat'])  # Datum als datetime definieren für spätere Gruppierung
    df['Thema'] = 'Kein Thema'
    budget_daten = df.groupby([df['Budgetmonat'].dt.year.rename('Jahr'), df['Budgetmonat'].dt.month.rename('Monat'), df['Thema'], df['Budgetmonat'].rename('Date')])['Budgetbetrag'].sum().reset_index()
    budget_daten = budget_daten.sort_values(by=['Jahr', 'Monat'])
    budget_daten['Typ'] = 'Budget'
    budget_daten.rename(columns={'Budgetbetrag': 'Betrag'}, inplace=True)
    return budget_daten


"""
Damit die Viusalisierung der Ausgaben-Eingaben aus der JSON-Datei visualisiert werden können, werden die Daten mit Pandas
in eine Tabellenform gebracht, die Tages-Erfassungen auf Monatsbasis summiert und die Spaltennamen vereinheitlicht und
für den späteren Merge mit den Budget-Eingaben vorbereitet
"""
def daten_ausgabeneingabe():
    df = pd.read_json(r'Formulare\ausgaben.json')
    df = df.T
    df['Datum'] = pd.to_datetime(df['Datum'])  # Datum als datetime definieren für spätere Gruppierung
    df['Ausgabenbetrag'] = df['Ausgabenbetrag'].apply(pd.to_numeric)  # Ausgaben als Zahl definieren, war ein Objekt
    # Die Tagesausgaben werden mit groupby auf Monatsbasis und Jahr summiert, um den Vergleich mit dem Budget machen zu können
    ausgaben_daten = df.groupby([df['Datum'].dt.year.rename('Jahr'), df['Datum'].dt.month.rename('Monat'), df['Thema'], df['Datum'].rename('Date')])['Ausgabenbetrag'].sum().reset_index()
    ausgaben_daten = ausgaben_daten.sort_values(by=['Jahr', 'Monat'])
    ausgaben_daten['Typ'] = 'Ausgaben'
    ausgaben_daten.rename(columns={'Ausgabenbetrag': 'Betrag'}, inplace=True)
    return ausgaben_daten


"""
Die beiden vorbereiteten Pandas-Tabellen der Budgets und Ausgaben werden hier gemergt in einer gemeinsamen Tabelle, was
die Visualisierungen vereinfacht
"""
def daten_mergen():
    budget = daten_budgeteingabe()
    ausgaben = daten_ausgabeneingabe()
    df_final = ausgaben.merge(budget, how='outer')
    return df_final
