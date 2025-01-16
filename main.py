import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from database import create_table, add_key, get_available_key

# ตั้งค่าบอท
TOKEN = os.getenv('TOKEN')  # ดึง Token จาก Environment Variables
if TOKEN is None:
    raise ValueError("Token not found in environment variables")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# คำสั่ง /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("ยินดีต้อนรับสู่บอทขาย Key!\n\nกรุณาพิมพ์ /buy เพื่อซื้อ Key")

# คำสั่ง /buy เพื่อซื้อ Key
def buy_key(update: Update, context: CallbackContext) -> None:
    key = get_available_key()  # รับ Key ที่ยังไม่ได้ถูกขายจากฐานข้อมูล
    if key:
        update.message.reply_text(f"คุณได้รับคีย์: {key[1]}\nกรุณาชำระเงินเพื่อรับคีย์นี้.")
        # เปลี่ยนสถานะ Key เป็น "sold" หลังจากที่ขาย
        conn = sqlite3.connect('keys.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE keys SET status = 'sold' WHERE id = ?", (key[0],))
        conn.commit()
        conn.close()
    else:
        update.message.reply_text("ขออภัย ไม่มี Key สำหรับขายในขณะนี้.")

# ฟังก์ชันหลัก
def main():
    # สร้างฐานข้อมูลหากยังไม่มี
    create_table()

    # สร้าง Updater และบอท
    updater = Updater(TOKEN)

    # เพิ่ม Handler สำหรับคำสั่งต่างๆ
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("buy", buy_key))

    # เริ่มบอท
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
