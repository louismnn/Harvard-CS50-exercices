import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

# JSON = javascript object notation (it's agnostic)
# curly braces = accolades

import json
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json()) to print the json API
print(json.dumps(response.json(), indent = 2)) #Will pretty printing the API
# indent = mettre en retrait

o = response.json()
for result in o["result"]:
    print(result["Trackname"])
# To know all the track name of the songs


