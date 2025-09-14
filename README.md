<img width="300" alt="image" src="https://github.com/user-attachments/assets/d3f30ba0-6621-48ce-87c8-389d28b05bec" /><img width="300" alt="image" src="https://github.com/user-attachments/assets/f4f7005e-1576-47ce-be8e-7750411bd0d4" />


# PyPortal YouTube Counter

A sleek subscriber and view count display for your YouTube channel, powered by Adafruit PyPortal. This project fetches real-time statistics from the YouTube Data API and displays them with custom fonts, background, and even a celebratory sound when a new subscriber joins.

---

## 🚀 Features

- Displays current subscriber count and view count
- Plays a sound when a new subscriber is detected
- Custom background and fonts for a polished look
- Updates every 5 minutes (configurable)
- Modular secrets management via `secrets.py`

---

## 🧰 Hardware Requirements

- [Adafruit PyPortal](https://www.adafruit.com/product/4116)
- MicroUSB cable
- Wi-Fi connection
- Optional: Speaker or buzzer for audio feedback

---

## 📦 Setup Instructions

### 1. Clone the Repository or manually download all of the files in this repository

```bash
git clone https://github.com/pir8radio/PyPortal-YouTube-Counter.git
```

### 2. Copy the files to the root directory of your PyPortal

With the following structure:

<img width="206" height="211" alt="image" src="https://github.com/user-attachments/assets/ad3f79ff-a10c-4c92-b2a1-0490ff393e5a" />


### 3. Modify `secrets.py`

In the root directory of your PyPortal code, create or modify the file named `secrets.py` with the following structure:

```python
secrets = {
    'ssid' : 'WIFI SSID HERE',
    'password' : 'WIFI PASS HERE',
    'youtube_token' : 'YOUTUBE TOKEN HERE',
    'youtube_chID' : 'YOUTUBE CHANNEL ID HERE',
    'youtube_caption' : ' ',
    'timezone' : "America/Chicago", # http://worldtimeapi.org/timezones
}
```

---

## 🔑 How to Get Your YouTube API Key and Channel ID

### ✅ YouTube API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Navigate to **APIs & Services > Library**
4. Search for **YouTube Data API v3** and enable it
5. Go to **APIs & Services > Credentials**
6. Click **Create Credentials > API Key**
7. Copy the generated key and paste it into `secrets['youtube_token']`

### 📺 YouTube Channel ID

1. Visit your YouTube channel page
2. Click on your profile > **Your Channel**
3. Look at the URL:  
   `https://www.youtube.com/channel/UCxxxxxxxxxxxxxxxxx`  
   Copy the part after `/channel/` — that's your Channel ID  
   Paste it into `secrets['youtube_chID']`

---

## 🎨 Customization

- **Fonts**: Use `.bdf` fonts compatible with PyPortal, placed in the `/fonts/` directory
- **Sound**: Replace `coin.wav` with any short WAV file for subscriber alerts

---

## 🛠️ Troubleshooting

- If you see `Some error occurred, retrying!`, the PyPortal will auto-reload and retry the fetch
- Ensure your Wi-Fi credentials and API key are correct
- Check that your fonts and background image are properly formatted and located

---

## 📅 Update Interval

The script updates every 5 minutes by default. You can change the interval by modifying:

```python
time.sleep(300)  # Time in seconds
```

---

## 📜 License

This project is licensed under a modified MIT License.  
Commercial use of this software to manufacture or sell YouTube counter devices is prohibited without written permission.  
See the [LICENSE](./LICENSE) file for full terms.

## Tags
@adafruit - This project uses [Adafruit_CircuitPython_PortalBase](https://github.com/adafruit/Adafruit_CircuitPython_PortalBase) and is based off of this [original code](https://learn.adafruit.com/pyportal-youtube-views-and-subscribers-display/code-pyportal-with-circuitpython).
