import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data = json.load(response)
spotlist = data["result"]["results"]
for spot in spotlist:
    splitpic = spot["file"].split("http")
    firstpic = "http"+splitpic[1]
    print(spot["stitle"]+","+spot["longitude"] +
          ","+spot["latitude"]+","+firstpic)
