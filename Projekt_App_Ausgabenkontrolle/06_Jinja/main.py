from flask import Flask
from flask import render_template

app = Flask("jinja")


@app.route("/")
def jinja():
    dinger = ["Eins", "Zwei", "Drei"]
    zahl = 6

    return render_template("budget.html", dinger=dinger, zahl=zahl)