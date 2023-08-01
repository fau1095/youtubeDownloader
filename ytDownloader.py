#Coded by Fau, all rights reserved

from pytube import YouTube
from pydub import AudioSegment
from sys import argv
from pathlib import Path
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

# Prompt the user to enter a YouTube video URL as an input.
# 'argv[0]' represents the name of the script, and we concatenate it with the input message for clarity.
link = input((argv[0]) + "\n Enter the URL: ")

# Create a YouTube object 'yt' using the 'YouTube' class from the 'pytube' library.
# The 'YouTube' class is used to interact with YouTube videos and provides various methods for retrieving video details and streams.
yt = YouTube(link)

# Retrieve the value of the environment variable 'DESIRED_FOLDER_PATH' using the 'os.environ.get()' method.
# Environment variables are system-specific variables that store configuration settings or other useful information.
# 'os.environ' is a dictionary-like object representing the current process's environment variables.
myDesiredFolder = os.environ.get('DESIRED_FOLDER_PATH')

# Print the title and views of the YouTube video.
# 'yt.title' contains the title of the YouTube video, and 'yt.views' contains the number of views the video has.
# This information is fetched from the 'yt' YouTube object, which represents the video specified by the URL entered by the user.
print("Title: ", yt.title)
print("Views: ", yt.views)

# Get the progressive MP4 stream with the highest resolution available for download.
# 'yt' is the YouTube video object, and we use the 'streams' property to get a list of all available streams.
# We filter the list to include only progressive streams (i.e., streams that can be played as they download).
# We also specify that we only want streams with the 'mp4' file extension.
# The 'order_by' method arranges the streams in ascending order based on the specified attribute ('resolution' in this case).
# The 'desc' method reverses the order, so we get the highest resolution stream first.
# Finally, the 'first' method returns the first item from the filtered and sorted list, which corresponds to the highest resolution stream available.
# Yes, I let ChatGPT do these explanaitions because I'm too lazy
ya = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the selected progressive MP4 stream.
# Once we have the 'ya' stream object representing the highest resolution MP4 stream,
# we use the 'download' method to initiate the download of the video file to the current working directory.
ya.download()

def downloadedFile():
# used to rename file extension
# Convert mp4 to mp3
    file_name = yt.title + '.mp4'
# Specify the complete file path for the input MP4 file
    input_file_path = os.path.join(os.getcwd(),file_name)
    sound = AudioSegment.from_file(file_name, format="mp4")

# Set the mp3 file name
# Specify the complete file path for the output MP3 file
    #mp3_file = yt.title + '.mp3'
    mp3_file = os.path.join(os.getcwd(), yt.title + '.mp3')
# Export the mp3 file
    try:    
        sound.export(mp3_file, format="mp3")
    except Exception as e:
        print("Error during MP4 to MP3 conversion:",e)    

# Delete the mp4 file
    #os.remove(file_name)
    os.remove(input_file_path)

# Create the destination folder if it doesn't exist    
    folder_location = myDesiredFolder
    if not os.path.exists(folder_location):
        os.makedirs(folder_location)
# Move the MP3 file to the destination folder
    shutil.move(mp3_file, folder_location)

downloadedFile()