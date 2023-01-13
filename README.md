# Wave Separate Left Right

## What it does(Main.py):
+ This code is made to take a stereo wave file encoded with np.int16 type and create 2 stereo tracks from it.
+ The first stereo track has the left channel from the original track and a blank right chanel
+ Meaning that when played in a stereo system for example headphones it will only play out of the left earphone
+ The second stereo track has a blank left channel and the right channel from the gorgon track
+ This is an additive process meaning it just creates files and does not remove the original file
+ It will put the files in a sub folder called output files to make searching easier

### What it does(Other files):

#### Left Channel Test:
+ A file for testing purposes to make sure the code works
+ Takes a wave file and splits it into left and right and puts it back together to confirm process works

#### Helper Methods:
+ directory_type(Directory) - Take a directory from windows and make it the correct type
+ array_to_text(Array Name, Directory, Tag(Array Name), Range) - Prints the specified array to TXT in the specified length 
+ find_patterns(data, pattern_length) - finds patters of a certain length in a set of datat and return the amount of specified patters
+ print_to_scratch(directory, what_to_print, scratch_file_name="scratch", reset_file_during_write(Boolean)) - prints the specified data to scratch txt file in directory


## How to run:
1. Install dependency's
2. Set the directory for it to search
3. Put the Blank.wav file in the same directory
   + Or create one with [Create Blank Wave File](https://github.com/JackCampbell5/Create_Blank_Wav_File "Create Blank Wave File")
4. If name is not "Blank".wav then change it in line 13
5. Confirm that the wave files in directory are encoded with np.int16
   + Otherwise, the code will not run for that file
6. Config the files are not longer than the blank.wav inputted
   + Otherwise, code will not run for that file
7. Run the code

 
## Dependency's:
+ OS
+ Wave
+ Numpy 

## Sources used to create:
+ Chat GPT for the overall idea that I modified though
+ [Wave documentation](https://docs.python.org/3/library/wave.html "Wave Site")
+ [Numpy documentation](https://numpy.org/doc/stable/index.html "NumPy documentation")

### Todo:
+ BuG Fixes
+ Add color?
+ Update Read me for GUI