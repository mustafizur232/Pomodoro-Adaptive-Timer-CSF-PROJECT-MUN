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
        
        # Basic validation
        if work <= 0:
            work = 25
        if brk <= 0:
            brk = 5
        if not isinstance(ratings, list):
            ratings = []
            # Keep only valid rating values
        cleaned_ratings = []
        for r in ratings:
            try:
                r_int = int(r)
                if 1 <= r_int <= 5:
                    cleaned_ratings.append(r_int)
            except (TypeError, ValueError):
                pass
            return {
            "work_minutes": work,
            "break_minutes": brk,
            "ratings": cleaned_ratings[-MAX_RATING_HISTORY:]
        }

    except (ValueError, json.JSONDecodeError, OSError):
        # If something goes wrong, fall back to default settings
        return default_settings
    def save_settings(settings):
        """
    Save work/break minutes and rating history into a JSON file.
    """
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f)
    except OSError:
        print("Warning: could not save settings.")
        
        def countdown(total_seconds, label):
        """
    Simple countdown that prints mm:ss each second.

    total_seconds: how many seconds to count down
    label: 'Work' or 'Break' (used for messages)
    """
    print(f"\n--- {label} session started ---")

    try:
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer_str = f"{mins:02d}:{secs:02d}"
            print(f"\rTime left: {timer_str}", end="")
            time.sleep(1)
            total_seconds -= 1
    except KeyboardInterrupt:
        # Let user interrupt the timer without crashing the program
        print("\nTimer interrupted by user.")
        return False

    print("\nSession finished!")
    return True