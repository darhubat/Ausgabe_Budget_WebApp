from flask import Flask
import pandas as pd
import plotly.express as px

app = Flask("visualisierung app")

@app.route("/viz")
def viz_country():
    country = px.data.gapminder()
    fig = px.scatter_geo(country, locations="iso_alpha", color="continent", hover_name="country", size="pop", animation_frame="year", projection="natural earth")
    fig.show()

if __name__ == "__main__":
    app.run(debug=True, port=5000)