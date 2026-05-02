import telebot
import yt_dlp
import os

API_TOKEN = '8793504257:AAGZ4rBZzvomOKD9uR09VawooozsuSjm3q4'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ارسل رابط تيك توك")

@bot.message_handler(func=lambda m: "tiktok.com" in m.text)
def download(message):
    file_id = f"{message.chat.id}.mp4"
    opts = {'format': 'best', 'outtmpl': file_id}
    
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([message.text])
        
        with open(file_id, 'rb') as v:
            bot.send_video(message.chat.id, v)
        os.remove(file_id)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()
