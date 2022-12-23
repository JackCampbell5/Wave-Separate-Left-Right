# The goal of this file is to print out an array for debugging to a .txt file

# Import the os module, which provides functions for working with files and directories
import os

def array_to_text(array, directory):
    i = 1
    while os.path.isfile(os.path.join(directory, f"{i}array.txt")):
        i+=1
    # Create the "test_folder" directory in the custom location
    path = os.path.join(directory, "Debugging")
    try:
        os.mkdir(path)
    except:
        print("Folder already exists")
    # Change the current working directory to the "test_folder" directory
    os.chdir(path)
    with open(f"{i}array.txt", "w") as f:
        for i in range(100):
            f.write(str(array[i])+"\n")
            if i > 100:
                break
                print("Done printing Array")