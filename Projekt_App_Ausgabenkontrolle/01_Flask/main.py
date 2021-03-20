from flask import request

from flask import Flask
from flask import render_template


app = Flask("Ausgaben/Budget App")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html", name="Dario")


@app.route("/test")
def test_seite():
    return "funktioniert"

@app.route("/liste")
def liste():
    seiten_titel = "Partygäste"
    gaeste_liste = ["Fabian", "Azra", "Wolfgang"]
    return render_template("auflistung.html", titel=seiten_titel, partygaeste=gaeste_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5000)