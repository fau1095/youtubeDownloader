#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
from pytube import YouTube
from sys import argv
from pathlib import Path
import os
import sys

link = argv[1]
yt = YouTube(link)

# Change this path to your desired folder 
folder = '/Users/fabriziomendez/Documents/Studio One/Multitracks/audiodownloader'

print ("Title: ", yt.title)
print ("Views: ", yt.views)

# If you only want the mp4 file, remove below commented lines:

# yd = yt.streams.get_highest_resolution()

# yd.download("/Users/fabriziomendez/Downloads")

ya = yt.streams.filter(only_audio=True)

ya[1].download(folder)

def downloadedFile():
# Used to rename file extension
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.mp4', '.mp3')
        output = os.rename(infilename, newname)
downloadedFile()
