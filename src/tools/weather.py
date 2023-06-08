import pandas as pd
import requests

from src.tools.settings import *

cities = pd.read_csv("./src/data/cities.csv")


def get_city():
    return cities.sample(1).to_dict("records")[0]


# TODO use wind
def get_data(lat, lng):
    r = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=weathercode,temperature_2m_max,temperature_2m_min,windspeed_10m_max,winddirection_10m_dominant&forecast_days=1&timezone=Europe%2FParis"
    )
    daily = r.json()["daily"]
    return {
        "t_min": int(daily["temperature_2m_min"][0]),
        "t_max": int(daily["temperature_2m_max"][0]),
        "weathercode": f'_{daily["weathercode"][0]}',
    }


def format_population(population):
    if population > 10**6:
        return f"{int(population // 10 ** 6)}M hab."
    elif population > 10**3:
        return f"{int(population // 10 ** 3)}k hab."
    else:
        return f"{int(population)} hab."


def get_render(city, country, population, t_min, t_max, weathercode):
    gradient = WeatherGradient[weathercode].value
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            text-shadow: rgba(255, 255, 255, 1) 0 0 30px, rgba(255, 255, 255, 1) 0 0 30px, rgba(255, 255, 255, 1) 0 0 30px;
        }}

        .widget {{
            position: relative;
            display: flex;
            height: 400px;
            width: 500px;
        }}

        .image {{
            position: absolute;
            top: 0px;
            right: 0px;
        }}

        .temperature {{
            position: absolute;
            top: 20px;
            left: 26px;
            font-size: 32px;
            font-weight: bold;
        }}

        .city {{
            position: absolute;
            top: 80px;
            left: 26px;
            font-size: 24px;
        }}

        .country {{
            position: absolute;
            top: 114px;
            left: 26px;
            font-size: 18px;
        }}

        .population {{
            position: absolute;
            top: 136px;
            left: 26px;
            font-size: 18px;
        }}

        .weathercode {{
            position: absolute;
            top: 180px;
            left: 26px;
            font-size: 20px;
        }}

        .gradient {{
            position: absolute;
            height: 100%;
            width: 100%;
            background: linear-gradient(135deg, rgba({gradient["start"]},1), rgba({gradient["end"]},1) 100%);
            border-radius: 25px;
            -webkit-mask-image: -webkit-gradient(linear, right 50%, right 70%, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)))
        }}
    </style>
    <title>test</title>
</head>
<body>
    <div class="widget">
        <div class="gradient">
        </div>
        <div class="image">
            <img src="./src/data/emojis/{WeatherImage[weathercode].value}" alt="{WeatherImage[weathercode].value}">
        </div>
        <div class="temperature">
            <p>{t_min}°/{t_max}°</p>
        </div>
        <div class="city">
            <p>{city}</p>
        </div>
        <div class="country">
            <p>{country}</p>
        </div>
        <div class="population">
            <p>{format_population(population)}</p>
        </div>
        <div class="weathercode">
            <p>{WeatherType[weathercode].value}</p>
        </div>
    </div>
</body>
</html>
    """


def weather():
    city = get_city()
    data = get_data(city["lat"], city["lng"])
    return get_render(city["city"], city["country"], city["population"], data["t_min"], data["t_max"], data["weathercode"])
