import pandas as pd
import datetime as dt


def daten_budgeteingabe():
    df = pd.read_json(r'Projekt_App_Ausgabenkontrolle/05_Formulare/budget.json')
    budget_daten = df.T  # transponiert die Tabelle in gewünschte Form
    budget_daten['Jahr'] = pd.DatetimeIndex(budget_daten['Budgetmonat']).year
    budget_daten['Monat'] = pd.DatetimeIndex(budget_daten['Budgetmonat']).month
    return budget_daten


def daten_ausgabeneingabe():
    df = pd.read_json(r'Projekt_App_Ausgabenkontrolle/05_Formulare/ausgaben.json')
    df = df.T
    df['Datum'] = pd.to_datetime(df['Datum'])  # Datum als datetime definieren für spätere Gruppierung
    df['Ausgabenbetrag'] = df['Ausgabenbetrag'].apply(pd.to_numeric)  # Ausgaben als Zahl definieren, war ein Objekt
    # Die Tagesausgaben werden mit groupby auf Monatsbasis und Jahr summiert, um den Vergleich mit dem Budget machen zu können
    ausgaben_daten = df.groupby([df['Datum'].dt.year.rename('Jahr'), df['Datum'].dt.month_name().rename('Monat')])['Ausgabenbetrag'].sum().reset_index()
    return ausgaben_daten
