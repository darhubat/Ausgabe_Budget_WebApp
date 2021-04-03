import pandas as pd
import datetime as dt


def daten_budgeteingabe():
    df = pd.read_json(r'Projekt_App_Ausgabenkontrolle/04_Formulare/budget.json')
    df = df.T  # transponiert die Tabelle in gewünschte Form
    df['Budgetbetrag'] = df['Budgetbetrag'].apply(pd.to_numeric)  # Ausgaben als Zahl definieren, war ein Objekt
    df['Budgetmonat'] = pd.to_datetime(df['Budgetmonat'])  # Datum als datetime definieren für spätere Gruppierung
    df['Thema'] = 'Kein Thema'
    budget_daten = df.groupby([df['Budgetmonat'].dt.year.rename('Jahr'), df['Budgetmonat'].dt.month.rename('Monat'), df['Thema'], df['Budgetmonat'].rename('date')])['Budgetbetrag'].sum().reset_index()
    budget_daten = budget_daten.sort_values(by=['Jahr', 'Monat'])
    budget_daten['typ'] = 'Budget'
    budget_daten.rename(columns={'Budgetbetrag': 'Betrag'}, inplace=True)
    return budget_daten


def daten_ausgabeneingabe():
    df = pd.read_json(r'Projekt_App_Ausgabenkontrolle/04_Formulare/ausgaben.json')
    df = df.T
    df['Datum'] = pd.to_datetime(df['Datum'])  # Datum als datetime definieren für spätere Gruppierung
    df['Ausgabenbetrag'] = df['Ausgabenbetrag'].apply(pd.to_numeric)  # Ausgaben als Zahl definieren, war ein Objekt
    # Die Tagesausgaben werden mit groupby auf Monatsbasis und Jahr summiert, um den Vergleich mit dem Budget machen zu können
    ausgaben_daten = df.groupby([df['Datum'].dt.year.rename('Jahr'), df['Datum'].dt.month.rename('Monat'), df['Thema'], df['Datum'].rename('date')])['Ausgabenbetrag'].sum().reset_index()
    ausgaben_daten = ausgaben_daten.sort_values(by=['Jahr', 'Monat'])
    ausgaben_daten['typ'] = 'Ausgaben'
    ausgaben_daten.rename(columns={'Ausgabenbetrag': 'Betrag'}, inplace=True)
    return ausgaben_daten


def daten_mergen():
    budget = daten_budgeteingabe()
    ausgaben = daten_ausgabeneingabe()
    df_final = ausgaben.merge(budget, how='outer')
    return df_final
