# This is for testing purposes to make sure the code does what I need
# This really just take a file splits it into left and right and puts it back together

# Import the necessary modules
import os
import wave
import numpy as np

# Set the directory containing the wav files
directory = "C:\\Users\\Jack Campbell\\Documents\\Sound project Help Files\\Python Code"

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
        print(len(left_channel))
        print(len(right_channel))

        wave_data_right = np.array([left_channel, right_channel])
        wave_data_right = np.reshape(wave_data_right, len(wave_data) * 2, order='F')
        wave_data_right = np.reshape(wave_data_right, (len(wave_data), 2))

        # Make the paths for writing left and right
        # path_left = os.path.join(directory, "left_" + filename)
        # path_right = os.path.join(directory, "right_" + filename)
        # outwav = wave.open(path_left, 'w')
        # outwav.setparams(original_params)
        # outwav.setnchannels(2)
        # outwav.writeframes(wave_data_right.tobytes())
        # outwav.close()

# Deprecated code
#
# if len(left_channel) % 2 == 0:
#     left_zero_array = np.zeros(int(len(left_channel) / 2))
#     left_zero_array_one = np.full(int(len(left_channel) / 2), 1)
# else:
#     left_zero_array = np.zeros(int(((len(left_channel) / 2) - 0.5)))
#     left_zero_array_one = np.full(int(((len(left_channel) / 2) - 0.5)), 1)
# left_zero_array = np.array([left_zero_array_one, left_zero_array])
# left_zero_array = np.reshape(left_zero_array, len(left_zero_array[0]) * 2, order='F')
# if len(left_channel) % 2 == 1:
#     left_zero_array = np.append(left_zero_array, [1])
#
# if len(right_channel) % 2 == 0:
#     right_zero_array = np.zeros(int(len(right_channel) / 2))
#     right_zero_array_one = np.full(int(len(right_channel) / 2), 1)
# else:
#     right_zero_array = np.zeros(int(((len(right_channel) / 2) - 0.5)))
#     right_zero_array_one = np.full(int(((len(right_channel) / 2) - 0.5)), 1)
# right_zero_array = np.array([right_zero_array_one, right_zero_array])
# right_zero_array = np.reshape(right_zero_array, len(right_zero_array[0]) * 2, order='F')
# if len(right_channel) % 2 == 1:
#     right_zero_array = np.append(right_zero_array, [1])
