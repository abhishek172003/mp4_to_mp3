import os
from moviepy.editor import *

def convert_mp4_to_mp3(input_file, output_file):
    """Converts an MP4 file to MP3 format.

    Args:
        input_file (str): Path to the input MP4 file.
        output_file (str): Path to the output MP3 file.
    """

    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    video.close()

# Get the current working directory
current_directory = os.getcwd()

# Convert all MP4 files in the current directory
for i in range(1, 254):  # Assuming files are named video1.mp4 to video253.mp4
    input_file = f"video{i}.mp4"
    output_file = f"audio{i}.mp3"
    if os.path.exists(os.path.join(current_directory, input_file)):
        convert_mp4_to_mp3(input_file, output_file)
        print(f"Converted {input_file} to {output_file}")
    else:
        print(f"File {input_file} not found.")