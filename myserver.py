from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

# ฟังก์ชันที่ใช้สำหรับรัน Flask app
def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

# ฟังก์ชันเพื่อเริ่มต้น Thread ที่รัน Flask app
def server_on():
    t = Thread(target=run)
    t.start()

# เรียกใช้ฟังก์ชัน server_on() เมื่อบอททำงาน
if __name__ == "__main__":
    server_on()
