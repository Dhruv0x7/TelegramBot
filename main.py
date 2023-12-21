import telebot
from pytube import YouTube
from pytube.cli import on_progress
import os
from keep_alive import keep_alive


keep_alive()

bot = telebot.TeleBot('6800114319:AAFN1thIzE0wydvadH47xO-PZZx9huk19CE')

pwd = os.getcwd()
print(pwd)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Give url(Ex. https://youtu.be/example) of YT video I download the Video! for you...')

@bot.message_handler(func=lambda message: True)
def download(message):
    try:
        yt = YouTube(message.text, on_progress_callback=on_progress)
        vid = yt.streams.get_highest_resolution()
        bot.send_message(message.chat.id, 'Please Wait...')
        out = vid.download()
        filename = str(out.split('/')[-1:])
        size = str(vid.filesize_mb) + ' MB'
        bitrate = str(vid.bitrate)
        audio_codec = str(vid.audio_codec)
        bot.send_message(message.chat.id, 'Filename: ' + filename + '\n' + 'Size: ' + size + '\n' + 'Bitrate: ' + bitrate + '\n' + 'Audio_Codec: ' + audio_codec)
        video = open(out, 'rb')
        bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, 'Download Completed!')
        video.close()
        os.remove(out)
    except Exception as e:
        bot.send_message(message.chat.id, e)


bot.infinity_polling()
