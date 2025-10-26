"""
Automated script to fetch weather data from the Open-Meteo API
and save it to an SQLite database.
"""

import requests
import sqlite3
import logging
from datetime import datetime
from typing import Tuple

# Configuration API and database
API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = 55.60  # Malmö
LONGITUDE = 13.00
DB_PATH = "weather.db"
LOG_PATH = "weather.log"


# Logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(LOG_PATH)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

# Fetch weather data
def fetch_weather() -> Tuple[float, float, int]:
    """
    Fetches current weather in Malmo from the Open-Meteo API.
    
    Returns:
        Tuple with (temperature, windspeed, weathercode)
        
    Raises:
        requests.RequestException: If the API call fails.
    """
    try:
        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "current_weather": "true"
        }
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        weather = data["current_weather"]
        
        temp = weather["temperature"]
        wind = weather["windspeed"]
        code = weather["weathercode"]
        
        logger.info(f"Fetched weather data: {temp}°C, {wind} m/s, code {code}")
        return temp, wind, code
        
    except requests.RequestException as e:
        logger.error(f"Error during API call {e}")
        raise


def save_to_db(temp: float, wind: float, code: int) -> None:
    """
    Saves weather data to the SQLite database.
    
    Args:
        temp: Temperature in Celsius
        wind: Wind speed in m/s
        code: Weather code from Open-Meteo
        
    Raises:
        sqlite3.Error: If the database operation fails
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            
            # Create table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    temperature REAL NOT NULL,
                    windspeed REAL NOT NULL,
                    weathercode INTEGER NOT NULL
                )
            """)
            
            # Insert new weather data
            timestamp = datetime.now().isoformat()
            cursor.execute(
                "INSERT INTO weather (timestamp, temperature, windspeed, weathercode) VALUES (?, ?, ?, ?)",
                (timestamp, temp, wind, code)
            )
            conn.commit()
            
        logger.info(f"Data saved to database: {timestamp}")
        
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise

def get_latest_weather() -> Tuple[str, float, float, int]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 1")
        return cursor.fetchone()

def main() -> None:
    """
    Main function to run the weather data fetching and saving process.
    Logs start and end of execution.
    """
    try:
        logger.info("=" * 50)
        logger.info("Starting weather retrieval...")
        
        # Fetch weather data
        temp, wind, code = fetch_weather()
        
        # Save to database
        save_to_db(temp, wind, code)
        
        logger.info("Execution completed successfully")
        
    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")
        raise


if __name__ == "__main__":
    main()