from flask import Flask
import daten  # daten.py vorhanden, das wird aufgerufen


app = Flask("Daten")


@app.route("/liste")
def auflisten():
    aktivitaeten = daten.aktivitaeten_laden()

    aktivitaeten_liste = ""
    for key, value in aktivitaeten.items():
        zeile = str(key) + ": " + value + "<br>"  # br break für genutzt für eine neue Zeile
        aktivitaeten_liste += zeile  # alles in einer Text-Datei zusammengefügt, Zeile für Zeile

    return aktivitaeten_liste  # mit render_template könnte hier auch noch formatiert werden


if __name__ == '__main__':
    app.run(debug=True, port=5000)
