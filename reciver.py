import datetime
import time

import requests

last_msg_time = 0
while True:
    response = requests.get("http://127.0.0.1:5000/history",
                            params={"after": last_msg_time})
    data = response.json()
    for message in data["messages"]:
        # float --> datetime
        bt = datetime.datetime.fromtimestamp(message["time"])
        bt = bt.strftime("%Y/%m/%d")
        print(bt, message["username"])
        print(message["text"])
        print()
        last_msg_time = message["time"]

    time.sleep(1)
