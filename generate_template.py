# ganerate_template.py
#
# LAROCHE Tristan
# 31-01-2023
#==================================

from tkinter import filedialog
import tkinter as tk
import webbrowser
import i18n

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
    if file == "":
        return
    for i in range(1, int(size)+1):
        for j in range(3):
            file.write(f"{i} : {steps[j]} : - : - : {i}\n")
    file.close()
    
def help(self):
    """Just an help window
    """
    self.help_window = tk.Toplevel(self.root)
    self.help_window.title("Help menu")
    text1 = tk.Label(self.help_window, text=i18n.t("help_1"))
    text1.pack()
    text1.config(font=('Helvetica bold', 18))
    text2 = tk.Label(self.help_window, text=i18n.t("help_2"))
    text2.pack()
    text2.config(font=('Helvetica bold', 18))
    tk.Button(self.help_window, text=i18n.t("help_3"), command=lambda: webbrowser.open("https://www.futurelearn.com/info/courses/how-computers-work/0/steps/49259")).pack()
    text3 = tk.Label(self.help_window, text=i18n.t("help_4"))
    text3.pack()
    text3.config(font=('Helvetica bold', 12))
    text4 = tk.Label(self.help_window, text=i18n.t("help_5"))
    text4.pack()
    text4.config(font=('Helvetica bold', 12))