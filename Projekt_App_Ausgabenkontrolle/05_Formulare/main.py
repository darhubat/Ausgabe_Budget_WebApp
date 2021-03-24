from flask import Flask
from flask import request
from flask import render_template


app = Flask("App Ausgabenkontrolle")


@app.route("/budget", methods=["GET", "POST"])
def budget_eingabe():
    if request.method == 'POST':
        monat = request.form['monat']
        budget = request.form['budget']
        return monat, budget
    else:
        return render_template("index.html")


@app.route("/ausgaben", methods=["GET", "POST"])
def ausgaben_eingabe():
    if request.method == 'POST':
        datum = request.form['datum']
        ausgabe = request.form['ausgabe']
        ausgaben_thema = request.form['ausgaben_thema']
        return datum, ausgabe, ausgaben_thema
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
