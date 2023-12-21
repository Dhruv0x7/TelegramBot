from pytube import YouTube
from pytube.cli import on_progress



link = input("Enter link: ")
print('Connecting, Please wait...')

yt = YouTube(link, on_progress_callback=on_progress)
vid = yt.streams.get_highest_resolution()

vid.download()
print("Done!")


