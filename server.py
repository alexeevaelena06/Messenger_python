from datetime import datetime
import time

from flask import Flask, request

app = Flask(__name__)

messages = [
    {"username": "jack",
     "text": "Hello",
     "time": time.time()},
    {"username": "mary",
     "text": "Hello",
     "time": time.time()}
]
users = {
    # username: password
    "jack": "black",
    "mary": "12345"
}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime("%Y/%m/%d")
    }


@app.route("/send", methods=["POST"])
def send():
    """
    request: {"username": "str", "password": "str", "text": "str"}
    response: {"ok": true}

    """
    data = request.json  # JSON -> dict
    username = data["username"]
    password = data["password"]
    text = data["text"]

    # if user doesn't exist --> register
    # else validate password

    if username in users:
        rel_password = users[username]
        if rel_password != password:
            return {"ok": False}
    else:
        users[username] = password

    messages.append({"username": username,
                     "text": text,
                     "time": time.time()})
    return {"ok": True}


@app.route("/history")
def history():
    """
    request: ?after=1234567890.4567
    response: {"messages": [
    {"username": "str",
    "text": "str",
    "time": "float"}}
    Returns:

    """
    after = float(request.args["after"])

    # filtered_messages = []
    # for message in messages:
    #     if after < message["time"]:
    #         filtered_messages.append(message)
    filtered_messages = [message for message in messages if after < message["time"]]
    return {
        'messages': filtered_messages
    }

app.run()
