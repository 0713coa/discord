from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

# ลบการใช้ app.run() เพราะ gunicorn จะจัดการให้เอง
def run():
    pass

def server_on():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    server_on()
