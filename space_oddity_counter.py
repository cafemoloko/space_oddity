# How many times has David Bowie's 'Spece Oddity' been played since Tesla Roadset launched into space?
# Inspired by: https://www.astronomy.com/science/astronomers-just-deleted-an-asteroid-because-it-turned-out-to-be-elon-musks-tesla-roadster/

from datetime import datetime

# Tesla Roadster launch date and song duration in seconds (5 minutes 18 seconds)
launch_date = datetime(2018, 2, 6)
song_duration_seconds = 5 * 60 + 18

# Function to calculate formatted times played
def calculate_times_played(launch_date, end_date):
    return "{:,.0f}".format((end_date - launch_date).total_seconds() // song_duration_seconds).replace(",", " ")

# Calculate times played since launch until today
print(f"Times played since launch: {calculate_times_played(launch_date, datetime.today())}")

# Calculate times played until David Bowie's birthday (January 8, 2026)
bowie_birthday = datetime(2026, 1, 8)
print(f"Times played by Bowie's birthday: {calculate_times_played(launch_date, bowie_birthday)}")


