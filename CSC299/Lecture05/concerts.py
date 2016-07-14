import json
import urllib


artist = raw_input('artist: ')
f = urllib.urlopen('http://api.seatgeek.com/2/events?performers.slug='+artist)
data = json.load(f)

for event in data['events']:
    print event['title'], event['datetime_local']
