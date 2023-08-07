"""

Ver 8.7.23
Coded by Fau, all rights reserved, but feel free to use the script on your own.

"""

# Import required libraries for YouTube video download and video/audio processing
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Prompt user to input the YouTube URL of the desired video
link = input("Enter the URL: ")

# Create a YouTube object 'yt' using the 'YouTube' class from the 'pytube' library.
# The 'YouTube' class is used to interact with YouTube videos and provides various methods for retrieving video details and streams.
yt = YouTube(link)

# Print the title and view count of the YouTube video
print("Title: ", yt.title)
print("Views: ", yt.views)

# Get the highest resolution progressive MP4 stream available for download
# 'yt' is the YouTube video object, and we use the 'streams' property to get a list of all available streams.
# We filter the list to include only progressive streams (i.e., streams that can be played as they download).
# We also specify that we only want streams with the 'mp4' file extension.
# The 'order_by' method arranges the streams in ascending order based on the specified attribute ('resolution' in this case).
# The 'desc' method reverses the order, so we get the highest resolution stream first.
# Finally, the 'first' method returns the first item from the filtered and sorted list, which corresponds to the highest resolution stream available.
ya = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Get the path of the folder where downloaded media will be stored from the environment variable
media_folder = os.environ.get('MEDIA_FOLDER')

# Create the media folder if it doesn't exist
if not os.path.exists(media_folder):
    os.makedirs(media_folder)

# Download the YouTube video's MP4 stream to the media folder
ya.download(output_path=media_folder)

# Function to convert the downloaded MP4 to MP3
def convert_mp4_to_mp3(input_path, output_folder):
    try:
        # Load the MP4 video using MoviePy's VideoFileClip
        video = VideoFileClip(input_path)
        # Extract the audio from the video
        audio = video.audio
        # Create the output MP3 file path based on the original MP4 filename
        output_file = os.path.splitext(os.path.basename(input_path))[0] + ".mp3"
        output_path = os.path.join(output_folder, output_file)
        # Write the audio to the output MP3 file
        audio.write_audiofile(output_path, codec='mp3')
        # Close the audio and video objects
        audio.close()
        video.close()
        print(f"Conversion completed, file can be found here: {output_path}")
    except Exception as e:
        print(f"Error converting: {e}")

# Main program execution
if __name__ == "__main__":
    # Get the desired output folder path from the environment variable
    desired_folder = os.environ.get('DESIRED_FOLDER_PATH')
    
    # List files in the MEDIA_FOLDER and find the first .mp4 file
    media_files = os.listdir(media_folder)
    mp4_files = [f for f in media_files if f.lower().endswith('.mp4')]
    if mp4_files:
        # Get the path of the first downloaded MP4 file
        input_file = os.path.join(media_folder, mp4_files[0])
        
        # Call the conversion function to convert MP4 to MP3
        convert_mp4_to_mp3(input_file, desired_folder)
        
        # Delete the original MP4 file
        os.remove(input_file)
        print(f"Original MP4 file: '{input_file}' was deleted.")
    else:
        print("No MP4 files found in the specified folder.")