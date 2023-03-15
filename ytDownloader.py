from pytube import YouTube
from pydub import AudioSegment
import os
import shutil

link = input("Enter the URL: ")
try:
    yt = YouTube(link)
except:
    print("Error: Invalid YouTube link.")
    exit()

myDesiredFolder = '/Users/fabriziomendez/Documents/Studio One/Multitracks/audiodownloader'

print("Title: ", yt.title)
print("Views: ", yt.views)

try:
    # Download the mp4 file
    mp4_file = yt.title + '.mp4'
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
except:
    print("Error: Unable to download the video.")
    exit()

try:
    # Convert mp4 to mp3
    mp3_file = yt.title + '.mp3'
    AudioSegment.from_file(mp4_file).export(mp3_file, format="mp3")

    # Delete the mp4 file
    os.remove(mp4_file)

    # Move the mp3 file to the desired folder
    if not os.path.exists(myDesiredFolder):
        os.makedirs(myDesiredFolder)
    shutil.move(mp3_file, myDesiredFolder)
except:
    print("Error: Unable to convert the video to mp3 or move the file to the desired folder.")
    exit()

print("Successfully converted the video to mp3 and moved it to the desired folder.")
