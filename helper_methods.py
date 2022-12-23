# The goal of this file is to print out an array for debugging to a .txt file

# Import the os module, which provides functions for working with files and directories
import os


# This function takes the directory copied from file explorer and changes it into a directory the program can understand with excape charachers
# Depricated
def directory_type(directory):
    a = 0
    while a < len(directory):
        if directory[a] == "\\":
            directory = directory[:(a)] + "\\" + directory[a:]
            a += 2
        else:
            a += 1

    return directory


def array_to_text(array, directory, tag="", range_amount=100):
    # If tag exists put parentheses around it
    if not (tag == ""):
        tag = "(" + tag + ")"

    # If the range if over the length of the array set the range to arrray length
    if range_amount > len(array):
        range_amount = len(array)

    # Create the "test_folder" directory in the custom location
    path = os.path.join(directory, "Debugging")

    # Creates file path for txt file and makes sure it exists beforehand
    i = 0
    if os.path.isfile(os.path.join(path, f"{0}{tag}array.txt")):
        while os.path.isfile(os.path.join(path, f"{i}{tag}array.txt")):
            i += 1

    # Try to create the folder and if it exists ignore it
    if not (os.path.isdir(path)):
        os.mkdir(path)

    # Change the current working directory to the "test_folder" directory
    os.chdir(path)
    with open(f"{i}{tag}array.txt", "w") as f:
        for i in range(range_amount):
            f.write(str(array[i]) + "\n")


def find_patterns(data, pattern_length, directory):
    # Initialize a dictionary to store the patterns
    patterns = {}

    # Iterate over the data array with a sliding window of the desired pattern length
    for i in range(len(data) - pattern_length + 1):
        # Extract the pattern from the data array
        pattern = tuple(data[i:i + pattern_length])
        # Check if the pattern is already in the dictionary
        if pattern in patterns:
            # If it is, increment the count for that pattern
            patterns[pattern] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            patterns[pattern] = 1

    # Return the dictionary of patterns
    for a in patterns:
        print_to_scrach(directory, str(a) + ": "+str(patterns[a]), "pattern_scrach_output")
        if patterns[a]>300:
            print_to_scrach(directory, str(a) + ": " + str(patterns[a]), "pattern_scrach_output_big")
    print_to_scrach(directory,"\n \n","pattern_scrach_output")
    return patterns


def print_to_scrach(directory, what, file_name="scrach", reset=False):
    if reset:
        write_type = "w"
    else:
        write_type = "a"
    # Create the "test_folder" directory in the custom location
    path = os.path.join(directory, "Debugging")

    # Try to create the folder and if it exists ignore it
    if not (os.path.isdir(path)):
        os.mkdir(path)

    # Change the current working directory to the "test_folder" directory
    os.chdir(path)

    if not (type(what) == str):
        what = str(what)
    with open(f"{file_name}.txt", write_type) as f:
        f.write(what + "\n")
