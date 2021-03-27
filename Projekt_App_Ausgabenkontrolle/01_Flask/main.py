from flask import Flask
from flask import render_template


app = Flask("App Ausgabenkontrolle")


@app.route("/")
def startseite():

    return render_template("landing_page.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
