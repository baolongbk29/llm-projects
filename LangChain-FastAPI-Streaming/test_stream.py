import json

import requests

url = "http://localhost:9000/stream_chat"
message = "Write poem for my wife"
data = {"content": message}

headers = {"Content-type": "application/json"}

with requests.post(url, data=json.dumps(data), headers=headers, stream=True) as r:
    for chunk in r.iter_content(1024):
        print(chunk)