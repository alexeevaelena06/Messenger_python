import time
from pprint import pprint
import requests

response = requests.get("http://127.0.0.1:5000/status")
pprint(response.json())


response = requests.post("http://127.0.0.1:5000/send",
                         json={"username": "nick", "text": "Hello",
                               "time": time.time()})
pprint(response.json())
