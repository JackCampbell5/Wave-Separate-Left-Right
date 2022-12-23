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
    if not (tag == ""):
        tag = "(" + tag + ")"
    # Create the "test_folder" directory in the custom location
    path = os.path.join(directory, "Debugging")

    i = 0
    if os.path.isfile(os.path.join(path, f"{0}{tag}array.txt")):
        while os.path.isfile(os.path.join(path, f"{i}{tag}array.txt")):
            i += 1
    print(i)

    try:
        os.mkdir(path)
    except:
        pass
    # Change the current working directory to the "test_folder" directory
    os.chdir(path)
    with open(f"{i}{tag}array.txt", "w") as f:
        for i in range(range_amount):
            f.write(str(array[i]) + "\n")
        else:
            print("Done printing Array")
