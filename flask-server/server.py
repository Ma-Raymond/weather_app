from flask import Flask
import datetime as dt
import requests

app = Flask(__name__)

# Route for the API

@app.route('/items/<name>')
def members(name):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "286ab1a2e60badb11ca2831fad6bd006"
    CITY = name

    url = BASE_URL + "appid=" + API_KEY + "&q="+CITY + "&units=metric"

    response = requests.get(url).json()

    feelslike = round(response['main']['feels_like'])
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    name = response['name']
    wind = response['wind']['speed']

    sunrise = sunrise_time.strftime('%I') +":"+ sunrise_time.strftime('%M') + sunrise_time.strftime('%p')
    sunset = sunset_time.strftime('%I') +":"+ sunset_time.strftime('%M') + sunset_time.strftime('%p')
    return {
        "feelslike":feelslike,
        "humidity":humidity,
        'description':description,
        "sunset":sunset,
        "sunrise":sunrise,
        "name":name,
        "wind":wind
    }
if __name__ == "__main__":
    app.run(debug=True)