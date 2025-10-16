from main import fetch_weather, save_to_db, get_latest_weather
from datetime import datetime
import sqlite3

def test_fetch_weather_types():
    temp, wind, code = fetch_weather()
    assert isinstance(temp, (int, float))
    assert isinstance(wind, (int, float))
    assert isinstance(code, int)

def test_fetch_weather_ranges():
    temp, wind, code = fetch_weather()
    assert -50 <= temp <= 50
    assert 0 <= wind <= 100
    assert 0 <= code <= 100

def test_save_to_db_and_retrieve():
    temp, wind, code = 12.5, 3.2, 1
    save_to_db(temp, wind, code)

    latest = get_latest_weather()
    assert latest is not None
    assert abs(float(latest[2]) - temp) < 0.01
    assert abs(float(latest[3]) - wind) < 0.01
    assert int(latest[4]) == code
    assert isinstance(latest[1], str)  # timestamp
    assert datetime.fromisoformat(latest[1])  # valid ISO format
