# ganerate_template.py
#
# LAROCHE Tristan
# 31-01-2023
#==================================

from tkinter import filedialog
import tkinter as tk
import webbrowser

def generate_template(self):
    """Creates a window with some text and buttons then calls "template_creator"
    """
    self.generation_window = tk.Toplevel(self.root)
    self.generation_window.title("Generate Template")
    tk.Label(self.generation_window, text= "Please enter the number of states you want:").pack()
    entry = tk.Entry(self.generation_window)
    entry.pack()
    choice = tk.IntVar()
    tk.Radiobutton(self.generation_window, variable= choice, value= 0).pack()
    tk.Radiobutton(self.generation_window, variable= choice, value= 1).pack()
    tk.Button(self.generation_window, text= "Go!", command= lambda: [template_creator(entry.get(), choice.get())]).pack()
    tk.Button(self.generation_window, text= "Quit!", command= self.generation_window.destroy).pack()
def template_creator(size: int, choice:int):
    """Opens a file and creates and empty template

    Args:
        size (int): The "size" of the template (ex: 1 = 1:b 1:0 1:1)
        choice (int): 0 to open an existing file | 1 to save as a new file
    """
    steps = ("b", "0", "1")
    if choice == 0:
        file = open(filedialog.askopenfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]), "w")
    else:
        file = open(filedialog.asksaveasfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]), "w")
    for i in range(1, int(size)+1):
        for j in range(3):
            file.write(f"{i} : {steps[j]} : - : - : {i}\n")
    file.close()
    
def help(self):
    """Just an help window
    """
    self.help_window = tk.Toplevel(self.root)
    self.help_window.title("Help menu")
    text1 = tk.Label(self.help_window, text= "Welcome to the help menu")
    text1.pack()
    text1.config(font=('Helvetica bold', 18))
    text2 = tk.Label(self.help_window, text= "To use this, you need to understand how a Turing machine works in the first place")
    text2.pack()
    text2.config(font=('Helvetica bold', 18))
    tk.Button(self.help_window, text= "How it works?", command= lambda: webbrowser.open("https://www.futurelearn.com/info/courses/how-computers-work/0/steps/49259")).pack()
    text3 = tk.Label(self.help_window, text= "Now that you have the basis, let us introduce you... Programming!\nWell not really since we made it really easy to understand, there are 5 different instructions:\nThe current state, the value you read, the value you write, the direction you move, the next state.\nTo start, you can generate a template, by clicking on the 'Templates' menu, then 'Generate' and provide a size (the amound of states you want, ex: 3 states(b, 0, 1) = 3).")
    text3.pack()
    text3.config(font=('Helvetica bold', 12))
    text4 = tk.Label(self.help_window, text= "As you can see, the window is divided in two parts; you can't interract with the left one, it is only here as a preview to your program.\nHowever the right side is different since you can click buttons inside of it. We made the interface pretty simple too, ")
    text4.pack()
    text4.config(font=('Helvetica bold', 12))