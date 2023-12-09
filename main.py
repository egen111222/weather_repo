from flask import Flask,render_template,request,redirect
import requests
from lib import get_weather_data,get_weather_style_data

app = Flask(__name__,
            static_url_path="")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather",methods=["GET","POST"])
def weather_page():
    if request.method == "POST":
        form_data = request.form
        city_name = form_data.get("city_name")
        weather_data = get_weather_data(city_name)
        style_data = get_weather_style_data(weather_data)
        return render_template("weather.html",
                               weather_data=weather_data,
                               bg_class=style_data['bg'],
                               text_color_class=style_data['text'],
                               img=style_data['image'])
    return redirect("/")


if __name__ == "__main__":
    app.run()
