from flask import Flask
from flask import request
from flask import render_template
from funktionen.visualisierung import balkendiagramm

app = Flask("meine App")

@app.route("/", methods=["GET", "POST"])
def rechnen():
    if request.method == 'POST':
        zahl_1 = request.form['zahl_1']
        zahl_2 = request.form['zahl_2']
        zahl_3 = request.form['zahl_3']
        summe = int(zahl_1) + int(zahl_2) + int(zahl_3)
        antwort = "Die Summe deiner eingegebenen Zahl ergibt: " + str(summe)
        return antwort
    else:
        return render_template("budget.html")

@app.route("/testvis")
def testvis():
    grafik_div = balkendiagramm()  # balkendiagramm wird in grafik_div gespeichert
    return render_template('vis.html', grafik=grafik_div)  # Grafik wird auf der bestehenden URL aufgebaut


if __name__ == "__main__":
    app.run(debug=True, port=5000)