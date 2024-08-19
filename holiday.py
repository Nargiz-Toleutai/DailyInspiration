import datetime
import requests


def get_today_holiday(country_code):
    year = datetime.datetime.now().year
    api_url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        holidays = response.json()

        today = datetime.datetime.now().date()
        for holiday in holidays:
            holiday_date = datetime.datetime.strptime(holiday['date'], "%Y-%m-%d").date()
            if holiday_date == today:
                return holiday['localName']
        return "There is no holiday"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"
    except ValueError:
        return "Error processing data from API"
