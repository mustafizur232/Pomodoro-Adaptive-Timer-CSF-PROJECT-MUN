import time
import json
import os

SETTINGS_FILE = "pomodoro_settings.json"

# Some simple limits so things don't get crazy
MIN_WORK_MINUTES = 10
MAX_WORK_MINUTES = 60
MIN_BREAK_MINUTES = 3
MAX_BREAK_MINUTES = 20
MAX_RATING_HISTORY = 10  # how many past ratings we consider


def load_settings():
    """
    Load work/break minutes and rating history from a JSON file.
    If the file doesn't exist or is invalid, use default values.
    """
    default_settings = {
        "work_minutes": 25,
        "break_minutes": 5,
        "ratings": []  # list of past productivity ratings (1–5)
    }

    if not os.path.exists(SETTINGS_FILE):
        return default_settings

    try:
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)

        work = int(data.get("work_minutes", 25))
        brk = int(data.get("break_minutes", 5))
        ratings = data.get("ratings", [])