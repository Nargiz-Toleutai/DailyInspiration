import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
GEO_API_KEY = os.getenv('IPINFO_API_KEY')


def get_user_location():
    try:
        response = requests.get(f"https://ipinfo.io/json?token={GEO_API_KEY}")
        response.raise_for_status()
        location_data = response.json()
        loc = location_data['loc'].split(',')
        latitude, longitude = loc[0], loc[1]
        city = location_data.get('city', 'Unknown location')
        return latitude, longitude, city
    except requests.exceptions.RequestException as err:
        return None, None, None


def get_weather_emoji(description):
    description = description.lower()
    if 'clear' in description:
        return '☀️'
    elif 'cloud' in description:
        return '☁️'
    elif 'rain' in description or 'drizzle' in description:
        return '🌧️'
    elif 'thunderstorm' in description:
        return '⛈️'
    elif 'snow' in description:
        return '❄️'
    elif 'mist' in description or 'fog' in description:
        return '🌫️'
    elif 'smoke' in description:
        return '💨'
    elif 'haze' in description:
        return '🌁'
    else:
        return '🌡️'


def get_current_weather_by_coordinates(latitude, longitude):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        emoji = get_weather_emoji(description)
        return {
            'description': f"{description.capitalize()} {emoji}",
            'temperature': temperature
        }
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"
    except ValueError:
        return "Error processing data from API"
