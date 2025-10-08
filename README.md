# DS24_A_Python
Course: Advanced Programming in Python

# 🌦️ Weather Data Collector

Automated script to fetch weather data for Malmö using the [Open-Meteo API](https://open-meteo.com/), store it in an SQLite database, and log activity. Includes a scheduler and test suite.

## Project Structure

weather_project/
├── main.py              # Fetches and saves weather data
├── scheduler.py         # Runs main.py at scheduled intervals
├── test_weather.py      # Pytest-based tests for core functions
├── weather.db           # SQLite database (auto-created)
├── weather.log          # Log file for weather retrieval
├── scheduler.log        # Log file for scheduler activity
└── requirements.txt     # Project dependencies


## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
