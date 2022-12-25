# Import the necessary modules
import os
import wave
from helper_methods import array_to_text
from helper_methods import find_patterns
from helper_methods import print_to_scrach
import numpy as np

# Set the directory containing the wav files
directory = r"C:\Users\Jack Campbell\Documents\Sound project Help Files\Python Code\TestFiles\More"

# Get the wave file that
blank_file_name = "blank.wav"
blank_file = wave.open(os.path.join(directory, blank_file_name), "r")

# Read the wav file properties
blank_num_channels = blank_file.getnchannels()
blank_sample_width = blank_file.getsampwidth()
blank_sample_rate = blank_file.getframerate()
blank_num_frames = blank_file.getnframes()

# Read the entire wave file into a numpy array
blank_data = blank_file.readframes(blank_num_frames)
blank_data = np.frombuffer(blank_data, dtype=np.int16)
print(blank_file.getparams())

# Reshape the wave data into an array with one column per channel
blank_data = blank_data.reshape((blank_num_frames, blank_num_channels))

# Split the wave data into left and right channels
blank_left_channel = blank_data[:, 0]
blank_right_channel = blank_data[:, 1]

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a wav file
    if filename.endswith(".wav") and not (filename == blank_file_name):

        # Prints file name as record for what is used
        print(filename)

        # See if the wav file is encoded wrong and move on if it is
        try:
            # Open the wav file
            wave_file = wave.open(os.path.join(directory, filename), "r")
        except:
            print("The wave file is encoded incorrectly")
            break

        # Read the wav file properties
        num_channels = wave_file.getnchannels()
        sample_width = wave_file.getsampwidth()
        sample_rate = wave_file.getframerate()
        num_frames = wave_file.getnframes()

        # Read the entire wave file into a numpy array
        wave_data = wave_file.readframes(num_frames)
        wave_data = np.frombuffer(wave_data, dtype=np.int16)

        # Reshape the wave data into an array with one column per channel
        wave_data = wave_data.reshape((num_frames, num_channels))

        # Split the wave data into left and right channels
        left_channel = wave_data[:, 0]
        right_channel = wave_data[:, 1]

        blank_left_channel_final = blank_left_channel[:len(right_channel)]
        blank_right_channel_final = blank_left_channel[:len(left_channel)]

        # Need to be created in a 2*2 formation3
        wave_data_left = np.array([left_channel, blank_right_channel_final])
        wave_data_left = np.reshape(wave_data_left, len(wave_data) * 2, order='F')
        wave_data_left = np.reshape(wave_data_left, (len(wave_data), 2))

        wave_data_right = np.array([blank_left_channel_final, right_channel])
        wave_data_right = np.reshape(wave_data_right, len(wave_data) * 2, order='F')
        wave_data_right = np.reshape(wave_data_right, (len(wave_data), 2))

        # Make the paths for writing left and right
        path_left = os.path.join(directory, "left_" + filename)
        path_right = os.path.join(directory, "right_" + filename)

        # Create file for left
        outwav_left = wave.open(path_left, 'w')
        outwav_right = wave.open(path_right, 'w')

        # Set Parameters
        outwav_left.setparams(wave_file.getparams())
        outwav_right.setparams(wave_file.getparams())

        # Set stereo vs mono
        outwav_left.setnchannels(2)
        outwav_right.setnchannels(2)

        # Writes the output file
        outwav_left.writeframes(wave_data_left.tobytes())
        outwav_right.writeframes(wave_data_right.tobytes())

        # We are done
        outwav_left.close()
        outwav_right.close()
