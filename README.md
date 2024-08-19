# Daily Inspiration Calendar

Daily Inspiration Calendar is a Flask-based web application that provides daily inspirational quotes, public holidays for various countries, and weather updates. This project integrates several external APIs to deliver real-time data.

## Features

- **Daily Inspirational Quotes**: Displays a random inspirational quote each day.
- **Holiday Information**: Shows public holidays for a specified country.
- **Current Weather**: Provides current weather data for a selected city.

## Project Structure


## Getting Started

### Prerequisites

- **Python 3.8+**
- **pip** (Python package installer)
- **API Keys** for the following services:
  - [OpenWeatherMap API](https://openweathermap.org/api)
  - [Quotable API](https://quotable.io)
  - [Nager.Date API](https://date.nager.at)

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Nargiz-Toleutai/DailyInspiration-Calendar.git
   cd DailyInspiration-Calendar

2. **Set up virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Set up environment variables:**
Create a .env file in the project root and add your API keys and other environment-specific settings.
    ```bash
   OPENWEATHER_API_KEY=your_openweathermap_api_key
    ```
4. **Run the application**
    ```bash
   python app.py
    ```
### Usage
- **The homepage (/)** 
  - displays the daily quote, holiday information, and weather for a specified city.
- **Use /api/date**
  - to get the current date in JSON format.
- **Use /api/holiday/<country_code>**
  - to get the holiday information for a specified country (e.g., /api/holiday/US).
- **Use /api/weather/<city>**
  - to get weather information for a specified city (e.g., /api/weather/New York).
