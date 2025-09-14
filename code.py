# Made by Pir8Radio
# https://github.com/pir8radio/PyPortal-YouTube-Counter

import time
import board
import supervisor
from adafruit_pyportal import PyPortal

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("All Settings are kept in secrets.py, please add them there!")
    raise

# pylint: disable=line-too-long
DATA_SOURCE = "https://www.googleapis.com/youtube/v3/channels/?part=statistics&id="+secrets['youtube_chID']+"&key="+secrets['youtube_token']
DATA_LOCATION1 = ["items", 0, "statistics", "viewCount"]
DATA_LOCATION2 = ["items", 0, "statistics", "subscriberCount"]
# pylint: enable=line-too-long

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(DATA_LOCATION1, DATA_LOCATION2),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/youtube_background.bmp",
                    text_font=cwd+"/fonts/Collegiate-50.bdf",
                    text_position=((120, 125), (108, 176)),
                    text_color=(0xFFFFFF, 0xFFFFFF),
                    caption_text=secrets['youtube_caption'],
                    caption_font=cwd+"/fonts/Collegiate-24.bdf",
                    caption_position=(40, 220),
                    caption_color=0xFFFFFF)

# track the last value so we can play a sound when it updates
last_subs = 0
last_views = 0

while True:
    try:
        views, subs = pyportal.fetch()
        subs = int(subs)
        views = int(views)
        print("Subscribers:", subs)
        print("Views:", views)
        if last_subs < subs:  # Count went up!
            print("New subscriber!")
            pyportal.play_file(cwd+"/coin.wav")
        last_subs = subs
    except (RuntimeError, OSError, ConnectionError) as e:
        print("Some error occured, retrying! -", e)
        supervisor.reload()

    time.sleep(300) # 5 min update time, can be as low as 1 min if you like
