# How many times has David Bowie's 'Spece Oddity' been played since Tesla Roadset launched into space?
# Inspired by: https://www.astronomy.com/science/astronomers-just-deleted-an-asteroid-because-it-turned-out-to-be-elon-musks-tesla-roadster/

from datetime import datetime

# Tesla Roadster launch date: February 6, 2018
launch_date = datetime(2018, 2, 6)
current_date = datetime.today()

time_elapsed = current_date - launch_date
total_seconds_elapsed = time_elapsed.total_seconds()

# Song duration in seconds (5 minutes 18 seconds)
song_duration_seconds = 5 * 60 + 18

times_played = total_seconds_elapsed // song_duration_seconds

formatted_times_played = "{:,.0f}".format(times_played).replace(",", " ")
print(formatted_times_played)

