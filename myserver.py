from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

def server_on():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    server_on()
