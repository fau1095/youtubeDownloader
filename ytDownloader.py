# Coded by Fau
#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

from pytube import YouTube
from pydub import AudioSegment
from sys import argv
from pathlib import Path
import os
import shutil

link = input((argv[0])+"\n Enter the URL: ")
yt = YouTube(link)
myDesiredFolder = '/Users/fabriziomendez/Documents/Studio One/Multitracks/audiodownloader'

print ("Title: ", yt.title)
print ("Views: ", yt.views)

# yd = yt.streams.get_highest_resolution()
ya = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# yd.download("/Users/fabriziomendez/Downloads")

#ya = yt.streams.filter(only_audio=True)
ya.download()

def downloadedFile():
# used to rename file extension
# Convert mp4 to mp3
    file_name = yt.title + '.mp4'
    sound = AudioSegment.from_file(file_name, format="mp4")

# Set the mp3 file name
    mp3_file = yt.title + '.mp3'

# Export the mp3 file
    sound.export(mp3_file, format="mp3")

# Delete the mp4 file
    os.remove(file_name)

    folder_location = myDesiredFolder
    if not os.path.exists(folder_location):
        os.makedirs(folder_location)
    shutil.move(mp3_file, folder_location)

downloadedFile()
