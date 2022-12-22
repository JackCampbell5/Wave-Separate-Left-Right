# This is for testing purposes to make sure the code does what I need
# This really just take a file splits it into left and right and puts it back together

# Import the necessary modules
import os
import wave

import numpy
import numpy as np

# Set the directory containing the wav files
directory = "C:\\Users\\jackp\\Documents\\Game Design\\SoundProject\\Audio\\Python Code\\TestFiles"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a wav file
    print(filename)
    if filename.endswith(".wav"):
        # Open the wav file
        wave_file = wave.open(os.path.join(directory, filename), "r")
        # print("The wave file is encoded incorrectly")

        original_params = wave_file.getparams()

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

        wave_data_right = np.array([left_channel, right_channel])
        print(len(wave_data_right[0]))
        wave_data_right = np.reshape(wave_data_right, len(wave_data)*2,order='F')
        print(len(wave_data))
        wave_data_right = np.reshape(wave_data_right, (len(wave_data),2))

        # Make the paths for writing left and right
        # path_left = os.path.join(directory, "left_" + filename)
        # path_right = os.path.join(directory, "right_" + filename)
        # outwav = wave.open(path_left, 'w')
        # outwav.setparams(original_params)
        # outwav.setnchannels(2)
        # outwav.writeframes(wave_data_right.tobytes())
        # outwav.close()

