from flask import Flask

app = Flask("Hello World")

@app.route("/")
def start():
    return "Start ist hier"

@app.route("/hello/")
@app.route("/hello/<name>")
def hallo(name=False):
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again..."


    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
