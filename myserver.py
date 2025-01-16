from flask import Flask
from threading import Thread
import os
import sys

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
    try:
        app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)  # ปิดแอปถ้ามีข้อผิดพลาด

def server_on():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    server_on()
