from flask import Flask
from flask import render_template


app = Flask("App Ausgabenkontrolle")


@app.route("/start")
def startseite():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
