import telebot
from pytube import YouTube
from pytube.cli import on_progress
import os
from keep_alive import keep_alive


keep_alive()

bot = telebot.TeleBot('6692748909:AAEbfohlABaqLjSPvbz2K4gmIMIenxasO3M')

pwd = os.getcwd()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Give url(Ex. https://youtu.be/example) of YT video I download the Video! for you...')


@bot.message_handler(commands=['video'])
def download_video(message):
    try:   
        yt = YouTube(str(message.text.split()[1]), on_progress_callback=on_progress)
        vid = yt.streams.get_highest_resolution()
        bot.send_message(message.chat.id, 'Please Wait...')
        filename = str(vid.title)
        filetype = str(vid.subtype)
        size = str(vid.filesize_mb) + ' MB'
        bitrate = str(vid.bitrate)
        audio_codec = str(vid.audio_codec)
        bot.send_message(message.chat.id, 'Filename: ' + filename + '\n'+ 'Filetype: '+ filetype + '\n' + 'Size: ' + size + '\n' + 'Bitrate: ' + bitrate + '\n' + 'Audio_Codec: ' + audio_codec)
        if vid.filesize_mb <= 50:
            out = vid.download()
            video = open(out, 'rb')
            bot.send_video(message.chat.id, video)
            bot.send_message(message.chat.id, 'Download Completed!')
        else:
            bot.send_message(message.chat.id, 'File is large to download')
    except Exception as e:
        bot.send_message(message.chat.id, e)
    finally:
        video.close()
        os.remove(out)

@bot.message_handler(commands='audio')
def download_audio(message):
    try:
        yt = YouTube(str(message.text.split()[1]), on_progress_callback=on_progress)
        audio = yt.streams.get_audio_only()
        bot.send_message(message.chat.id, 'Please Wait...')
        filename = str(audio.title)
        filetype = str(audio.subtype)
        size = str(audio.filesize_mb) + ' MB'
        bitrate = str(audio.bitrate)
        audio_codec = str(audio.audio_codec)
        bot.send_message(message.chat.id, 'Filename: ' + filename + '\n'+ 'Filetype: '+ filetype + '\n' + 'Size: ' + size + '\n' + 'Bitrate: ' + bitrate + '\n' + 'Audio_Codec: ' + audio_codec)
        if audio.filesize_mb <= 50:
                out = audio.download()
                audio = open(out, 'rb')
                bot.send_audio(message.chat.id, audio)
                bot.send_message(message.chat.id, 'Download Completed!')
        else:
            bot.send_message(message.chat.id, 'File is large to download')
    except Exception as e:
        bot.send_message(message.chat.id, e)
    finally:
        audio.close()
        os.remove(out)


bot.infinity_polling()
