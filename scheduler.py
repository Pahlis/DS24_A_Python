"""
Scheduler for weather data retrieval.
Drives main.py at scheduled intervals.
"""

import schedule
import time
import logging
from main import main as run_weather_job

# Set up logging
logger = logging.getLogger("scheduler")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler("scheduler.log")
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


def job() -> None:
    """
    Wrapper job to run the scheduled weather retrieval and storage process.
    """
    try:
        logger.info("Scheduled run starting...")
        run_weather_job()
        logger.info("Scheduled run completed.")
    except Exception:
        logger.error(f"Error during scheduled run:", exc_info=True)



def main() -> None:
    """
    Starts the scheduler and keeps it running.
    """
    # Schedule job – choose one option:

    # Option 1: Every 30 minutes (good for testing)
    # schedule.every(30).minutes.do(job)

    # Option 2: Every day at 08:00
    # schedule.every().day.at("08:00").do(job)

    # Option 3: Every 5 minutes (good for demo)
    schedule.every(5).minutes.do(job)

    logger.info("Scheduler started")
    print("Scheduler running! Press Ctrl+C to stop.")
    print("Logging to scheduler.log and weather.log")

    # Run the first job immediately
    job()

    # Keep the scheduler alive
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user")
        print("\nScheduler terminated.")

if __name__ == "__main__":
    logger.info("Scheduler script started")  # Flytta hit
    main()