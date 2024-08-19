from flask import Flask, jsonify, render_template
from holiday import get_today_holiday
from quote import get_inspirational_quote
from current_date import get_current_date
from weather import get_user_location, get_current_weather_by_coordinates


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/date')
def date():
    return jsonify({'date': get_current_date()})


@app.route('/api/holiday/<country_code>')
def holiday(country_code):
    return jsonify({'holiday': get_today_holiday(country_code)})


@app.route('/api/weather')
def weather():
    latitude, longitude, city = get_user_location()
    if latitude and longitude:
        weather_info = get_current_weather_by_coordinates(latitude, longitude)
        weather_info['city'] = city
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Unable to determine location"})


@app.route('/api/quote')
def quote():
    return jsonify({'quote': get_inspirational_quote()})


if __name__ == '__main__':
    app.run(debug=True)
