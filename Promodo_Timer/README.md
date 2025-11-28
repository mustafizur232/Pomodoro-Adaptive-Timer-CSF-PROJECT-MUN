
### 1. What is this project?
- “My project is a **command-line Pomodoro timer with adaptive scheduling**.”
- The unique part of my project is that it adapts the work and break durations automatically based on the user’s productivity. After each work session, the user rates how productive they felt, and the program uses a simple statistical algorithm to adjust the timing for future sessions.
- “The standard Pomodoro technique uses fixed 25/5 intervals.”
- “In reality, people are different: some work better with longer sessions, some with shorter ones.”
- “So I wanted a simple program that **learns from the user’s feedback** and adjusts the timing automatically.”


### 2. Why this idea?

- “The standard Pomodoro technique uses fixed 25/5 intervals.”
- “In reality, people are different: some work better with longer sessions, some with shorter ones.”
- “So I wanted a simple program that **learns from the user’s feedback** and adjusts the timing automatically.”



### 3. List of all Features

## Pomodoro Timer:
- Standard 25-minute work session followed by a 5-minute break.
## Adaptive Scheduling:
- Adjusts the work and break durations based on productivity ratings.
## User Feedback:
- After each work session, the user is asked to rate their productivity on a scale of 1 to 5.
## Data Persistence:
- Saves work/break durations and productivity ratings to a JSON file.
## Manual Adjustment:
- Allows users to manually change the work and break durations.
## Simple CLI Interface:
- Easy-to-use command-line interface for interaction.



### Known Bugs or Limitations

- Limited Adaptive Logic: The adaptive logic currently only adjusts the work and break durations based on the average rating of the last few sessions. More complex algorithms (e.g., machine learning) could be implemented for better adaptability.

- Limited Customization: The user can only manually adjust the work and break times within a predefined range (10-60 minutes for work, 3-20 minutes for breaks).

- No Advanced Error Handling: There is basic error handling, but the program might not handle edge cases (e.g., invalid input types or extremely large inputs) as gracefully as desired.

- No Visual Feedback: The program is entirely text-based and doesn't provide any graphical user interface (GUI). Future enhancements could include a visual timer or notifications.


