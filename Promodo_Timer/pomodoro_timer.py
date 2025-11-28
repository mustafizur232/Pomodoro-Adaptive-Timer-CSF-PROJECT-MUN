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

def ask_productivity_feedback():
    """
    Ask the user how the work session went.
    Returns an integer between 1 and 5, or None if the user skips.
    """
    print("\nHow productive were you this work session?")
    print("1 = Very unproductive, 5 = Very productive")
    answer = input("Enter a number from 1 to 5 (or press Enter to skip): ").strip()

    if answer == "":
        return None

    try:
        rating = int(answer)
        if 1 <= rating <= 5:
            return rating
        else:
            print("Invalid number, skipping adaptive adjustment this time.")
            return None
    except ValueError:
        print("Invalid input, skipping adaptive adjustment this time.")
        return None
    def compute_average_rating(ratings):
        """
    Compute the average of the rating list.
    Returns None if the list is empty.
    """
    if not ratings:
        return None
    return sum(ratings) / len(ratings)
def adapt_durations(settings):
    """
    Use a simple statistical algorithm (average of past ratings) to adapt
    both work and break durations.

    - If avg >= 4.0: increase work time, slightly reduce break time.
    - If avg <= 2.5: decrease work time, slightly increase break time.
    - Otherwise: keep times the same.

    All changes are clamped within sensible limits.
    """
    ratings = settings.get("ratings", [])

    avg = compute_average_rating(ratings)
    if avg is None:
        print("Not enough data yet to adapt durations.")
        return settings

    work = settings["work_minutes"]
    brk = settings["break_minutes"]

    print(f"\nAverage productivity rating (last {len(ratings)} sessions): {avg:.2f}")

    if avg >= 4.0:
        # user is doing well: increase challenge, shorter breaks
        new_work = min(work + 5, MAX_WORK_MINUTES)
        new_break = max(brk - 1, MIN_BREAK_MINUTES)
        print(f"High productivity detected. Next work session: {new_work} min, break: {new_break} min.")
        work, brk = new_work, new_break

    elif avg <= 2.5:
        # user is struggling: shorten work, longer breaks
        new_work = max(work - 5, MIN_WORK_MINUTES)
        new_break = min(brk + 1, MAX_BREAK_MINUTES)
        print(f"Low productivity detected. Next work session: {new_work} min, break: {new_break} min.")
        work, brk = new_work, new_break

    else:
        print("Average productivity. Keeping durations unchanged.")

    settings["work_minutes"] = work
    settings["break_minutes"] = brk
    return settings
def print_menu(settings):
    """
    Show the main menu and current settings.
    """
    print("\n========== Pomodoro Timer ==========")
    print(f"Current work duration : {settings['work_minutes']} minutes")
    print(f"Current break duration: {settings['break_minutes']} minutes")
    if settings["ratings"]:
        avg = compute_average_rating(settings["ratings"])
        print(f"Past sessions recorded: {len(settings['ratings'])}, avg rating: {avg:.2f}")
    else:
        print("No productivity data recorded yet.")
    print("------------------------------------")
    print("1) Start work session")
    print("2) Start break")
    print("3) Change durations manually")
    print("4) Exit")
    choice = input("Choose an option (1-4): ").strip()
    return choice