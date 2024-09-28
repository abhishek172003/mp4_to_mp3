import os

def rename_mp4_files(directory):
    """Renames all MP4 files in a directory to video1, video2, etc.

    Args:
        directory (str): Path to the directory containing MP4 files.
    """

    mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]
    for i, filename in enumerate(mp4_files, start=1):
        new_filename = f"video{i}.mp4"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed {filename} to {new_filename}")

# Get the current working directory
current_directory = os.getcwd()

# Rename MP4 files in the current directory
rename_mp4_files(current_directory)