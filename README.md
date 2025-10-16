
---

## 🌦️ Weather Data Collector

Automated Python script that fetches current weather data for Malmö using the [Open-Meteo API](https://open-meteo.com/), stores it in a local SQLite database, and logs all activity. Includes a scheduler and test suite.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [Fetching Weather Data](#fetching-weather-data)
  - [Storing Weather Data](#storing-weather-data)
  - [Scheduler](#scheduler)
- [Testing](#testing)
- [Logging](#logging)

---

## Features

- Fetches current temperature, windspeed, and weather code for Malmö.
- Stores data in a local SQLite database (`weather.db`).
- Logs all operations and errors to `weather.log` and `scheduler.log`.
- Includes a scheduler that runs the script every 30 minutes.
- Contains tests to verify API response and database integrity.

---

## Project Structure

```
weather_project/
├── main.py              # Fetches and stores weather data
├── scheduler.py         # Runs main.py at intervals
├── test_weather.py      # Pytest-based tests
├── requirements.txt     # Dependencies
├── weather.db           # SQLite database (auto-created)
├── weather.log          # Weather log file
├── scheduler.log        # Scheduler log file
```

---

## Setup and Installation

Clone the repository:
```bash
git clone https://github.com/Pahlis/DS24_A_Python.git
cd DS24_A_Python
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Configuration

Edit `main.py` to change:
- `LATITUDE`, `LONGITUDE`: coordinates for your location
- `DB_PATH`: database file name
- `LOG_PATH`: log file name

---

## Usage

Run manually:
```bash
python main.py
```

Run with scheduler:
```bash
python scheduler.py
```

The scheduler runs the weather job every 30 minutes by default. You can change the interval in `scheduler.py`.

---

## How It Works

### Fetching Weather Data
The `fetch_weather()` function calls the Open-Meteo API and returns:
- Temperature (°C)
- Windspeed (m/s)
- Weather code (int)

### Storing Weather Data
The `save_to_db()` function creates the table (if needed) and inserts the latest weather data with a timestamp.

### Scheduler
`scheduler.py` uses the `schedule` library to run `main.py` at regular intervals. It logs each run and handles errors gracefully.

---

## Testing

Run all tests using `pytest`:
```bash
pytest test_weather.py
```

Tests include:
- Type and range checks for API data
- Database save and retrieval
- Timestamp format validation

---

## Logging

- `weather.log`: logs weather retrieval and database operations
- `scheduler.log`: logs scheduled runs and errors

<img width="719" height="194" alt="image" src="https://github.com/user-attachments/assets/dd1abc7e-e306-46f5-8ac0-00e0ace5ea77" />



---
