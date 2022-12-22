# Wave Separate Left Right

## What it does(Main.py):
+ This code is made to take a stereo wave file encoded with np.int16 type and create 2 stereo tracks from it.
+ The first stereo track has the left channel from the original track and a blank right chanel
+ Meaning that when played in a stereo system for example headphones it will only play out of the left earphone
+ The second stereo track has a blank left channel and the right channel from the gorgon track
+ This is an additive process meaning it just creates files and does not remove the original file

### What it does(Left Channel Test):
+ A file for testing purposes to make sure the code works
+ Takes a wave file and splits it into left and right and puts it back together to confim process works

## How to run
1. Install dependency's
2. Set the directory for it to search
3. Confirm that the wave files in directory are encoded with np.int16
4. Run the code

 
## Dependency's:
+ OS
+ Wave
+ Numpy 

## Sources used to create:
+ Chat GPT for the overall idea that i modified though
+ [Wave documentation](https://docs.python.org/3/library/wave.html "Wave Site")
+ [Numpy documentation](https://numpy.org/doc/stable/index.html "NumPy documentation")

### Todo
+ Make it put all the output files in a sub folder
+ Have it work
+ Make it not just crash when the wrong format wav is created
+ Make a method file that takes a normal directory and converts it correctly