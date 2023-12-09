import requests


def get_weather_data(city_name):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=89c240d0282909824611a7dffedf1266&units=metric&lang=ua").json()
    return weather_data


def get_weather_style_data(weather_data):
    temp = weather_data['main']['temp']
    if temp < 0:
        return {"image":"winter.jpg",
                "bg":"bg-dark-subtle",
                "text":"text-light"}
    if temp > 0 and temp < 15:
        return {"image":"winter.jpg",
                "bg":"bg-success",
                "text":"text-primary"}
    else:
        return {"image":"summer.jpg",
                "bg":"bg-warning",
                "text":"text-info"}
