import requests


def get_inspirational_quote():
    api_url = "https://api.quotable.io/random"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        quote_data = response.json()
        return f"{quote_data['content']} - {quote_data['author']}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"
    except ValueError:
        return "Error processing data from API"
