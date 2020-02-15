import datetime
import time

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


def status():
    return {
        'status': True,
        # 'time': time.ctime()
        'time': datetime.datetime.now().strftime()
    }


app.run()