import os
from tkinter import *
from tkinter import filedialog
from wave_seperate_method import wave_seperate_method


# Methods List
def get_directory(row_num):
    my_dir = filedialog.askdirectory()  # select directory
    outputVar[row_num] = my_dir
    labels[row_num]["text"] = my_dir
    if not (row_num == 0 and checkbox_output.get()):
        if buttons[row_num + 1] != 0:
            buttons[row_num + 1]["state"] = "active"


def get_file(row_num):
    my_dir = filedialog.askopenfilename(initialdir=outputVar[0], title="Select a File",
                                        filetypes=(("Wave files", "*.wav*"), ("all files", "*.*")))  # select file
    outputVar[row_num] = my_dir
    labels[row_num]["text"] = my_dir
    if buttons[row_num + 1] != 0:
        buttons[row_num + 1]["state"] = "active"


def run_wave_seperate():
    labels[3]["text"] = "Running"
    return_value = wave_seperate_method(outputVar[0], outputVar[1], outputVar[2],outputVar[3])
    if return_value:
        labels[3]["text"]= "Complete"


def checkbox_output_fun(num, var):
    if var:
        var = True
        buttons[1]["state"] = "disabled"
        if outputVar[0] != 1:
            buttons[2]["state"] = "active"
    else:
        var = False
    outputVar[num] = var


# Define vars:
buttons = [0 for x in range(20)]
labels = [0 for x in range(20)]
outputVar = [0 for x in range(20)]
defult_padx = 10

# Create the Main window for all the info
window = Tk()

# Sets the resolution of the window
window.geometry('800x600')

# Set Title of window
window.title("Wave Program")

# Welcome text at top
l_title = Label(window, text="Welcome to Wave Separate", font=('', 35))
l_title.grid(row=0, column=0, columnspan=100, padx=defult_padx, pady=(20, 5))
# Into Label and directors
l_title_l = Label(window, text="Insert Director text here", font=('', 12))
l_title_l.grid(row=1, column=0, columnspan=100, padx=defult_padx, pady=(5, 20), sticky='W')

# Selection button 0 label 0
labels_button_zero = Label(window, text="Select target directory", font=('', 18))
labels_button_zero.grid(row=2, column=0, columnspan=4, padx=defult_padx, pady=(20, 1), sticky='W')
# Selection button 0
buttons[0] = Button(window, text='Select folder', font=('', 12), command=lambda: get_directory(0))
buttons[0].grid(row=3, column=0, padx=5, pady=(1, 10), sticky='W', ipadx=defult_padx, ipady=5)
# Selection label 0
labels[0] = Label(window, text=".", font=('', 10))
labels[0].grid(row=3, column=1, padx=defult_padx, sticky='W')

# Selection button 1 label 1
labels_button_one = Label(window, text="Select output directory", font=('', 18))
labels_button_one.grid(row=4, column=0, columnspan=4, padx=defult_padx, pady=(20, 1), sticky='W')
# Label of checkbox
labels_new = Label(window, text="Sub Folder?", font=('', 14))
labels_new.grid(row=5, column=0, padx=defult_padx, pady=(1, 1), sticky='W')
# # Checkbox creation
checkbox_output = IntVar()
outputVar[3] = False
checkbox = Checkbutton(window, variable=checkbox_output, command=lambda: checkbox_output_fun(3, checkbox_output.get()))
checkbox.grid(row=5, column=1, padx=defult_padx, pady=(20, 1), sticky='W')
# Selection button 1
buttons[1] = Button(window, text='Select folder', font=('', 12), command=lambda: get_directory(1),
                    state="disabled")
buttons[1].grid(row=6, column=0, padx=defult_padx, pady=(1, 10), sticky='W', ipadx=defult_padx, ipady=5)
# Selection label 1
labels[1] = Label(window, text=".", font=('', 10))
labels[1].grid(row=6, column=1, padx=defult_padx, sticky='W')

# Selection button 2 label 2
labels_button_two = Label(window, text="Select blank file directory", font=('', 18))
labels_button_two.grid(row=7, column=0, columnspan=4, padx=defult_padx, pady=(20, 1), sticky='W')
# Selection button 2
buttons[2] = Button(window, text='Select file', font=('', 12), command=lambda: get_file(2),
                    state="disabled")
buttons[2].grid(row=8, column=0, padx=defult_padx, pady=(1, 10), sticky='W', ipadx=defult_padx, ipady=5)
# Selection label 2
labels[2] = Label(window, text=".", font=('', 14))
labels[2].grid(row=8, column=1, padx=defult_padx, sticky='W')

# Run Button
buttons[3] = Button(window, text='Run', font=('', 10), command=lambda: run_wave_seperate(),
                    state="disabled")
buttons[3].grid(row=9, column=0, padx=defult_padx, pady=(20, 10), sticky='W', ipadx=defult_padx, ipady=5)

# Run text
labels[3] = Label(window, text="", font=('', 14))
labels[3].grid(row=8, column=1, padx=defult_padx, sticky='W')

# Says our method is ready to run
window.mainloop()
