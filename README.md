# Wave Separate Left Right with GUI

## What it does(Overall):
+ This code is made to take a stereo wave file encoded with np.int16 type and create 2 stereo tracks from it.
+ The first stereo track has the left channel from the original track and a blank right chanel
+ Meaning that when played in a stereo system for example headphones it will only play out of the left earphone
+ The second stereo track has a blank left channel and the right channel from the gorgon track
+ This is an additive process meaning it just creates files and does not remove the original file
+ It will put the files in a sub folder called output files to make searching easier

### What it does(Specifically):

#### GUI.py
+ Takes 1 file as the directory to search for correctly formatted WAV files
+ If the checkbox is not clicked you select a directory where you want the files to be output
  + If the checkbox is clicked a sub directory will be made under your main directory called "Output Files" to hold the files
+ Finally select the blank file that is used for the other half 

#### wave_separate_method.py
+ A version of the main.py file found in the main branch in method form taking parameters to run
+ input_directory - Where the original wave files are
+ output_directory - Where the files should be output - or null if new_directory is true
+ blank_directory - the location for your blank.wav file
+ new_directory - boolean for whether a new directory was needed 

## How to run:
1. Install dependency's
2. Run the program
3. Locate your input directory 
4. Locate or create output directory
5. Find Blank.wav file
   + Or create one with [Create Blank Wave File](https://github.com/JackCampbell5/Create_Blank_Wav_File "Create Blank Wave File")
6. Click the run button

 
## Dependency's:
+ OS
+ Wave
+ Numpy 
+ Tkinter

## Sources used to create:
+ Chat GPT for the overall idea that I modified though
+ [Wave documentation](https://docs.python.org/3/library/wave.html "Wave Site")
+ [Numpy documentation](https://numpy.org/doc/stable/index.html "NumPy documentation")

## Other Notes
+ I suppose this program could be used to add together the left channel of one file and the right of another and the opposite if you wanted 

### Todo:
+ Bug Fixes
+ Add color?