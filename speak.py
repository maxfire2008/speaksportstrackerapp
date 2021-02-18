import pyttsx3
import feedparser
import requests

ttsengine = pyttsx3.init()
readevents = []

while True:
    rssrawdata = requests.get("https://sportstrackerapp.com/feed/ST-BIIJKDCEE-121/rss").content.decode()
    d = feedparser.parse(rssrawdata)
    print(repr(readevents))
    for entry in d.entries:
        if entry not in readevents:
            readevents.append(entry)
            ttsengine.say(entry["summary"])
            ttsengine.runAndWait()
            print(entry["summary"])